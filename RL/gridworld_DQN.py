# gridworld_DQN.py
import random
import torch
import torch.nn as nn
import torch.optim as optim
from collections import deque
from gridworld_ui import GridWorldUI, START, GOAL, TRAPS, GRID_SIZE

# Qnet 정의(입력으로 상태s 가 들어가면 출력으로 각 행동a에 대한 Q값을 출력)
# 단순 hidden_size 64인 linear layer 와 ReLU, 그리고 출력층인 linear layer로 구성
class QNet(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(state_dim, 64), 
            nn.ReLU(),
            nn.Linear(64, action_dim)
        )
    def forward(self, x): return self.fc(x)

# state encoding -> 좌표값(pos)를 넣으면 이를 일자로 폈을 때의 인덱스의 값만 1로 하고 나머지 0인 tensor배열로 반환
# 예를 들어, (1,2) 좌표이면 idx = 1*5+2 = 7 이고, s = tensor([0,0,0,0,0,0,0,1,0,0,.....]) 으로 agent의 위치값을 상태로써 인코딩
def encode_state(pos):
    i, j = pos
    idx = i*GRID_SIZE + j
    s = torch.zeros(GRID_SIZE*GRID_SIZE)
    s[idx] = 1.0
    return s

# 상태전이(=agent 이동) 함수 정의(입력으로 상태s와 행동a를 받아와, 출력으로 다음 상태s'와 즉시보상(이동패널티) -0.1, 에피소드 종료여부 반환(에피소드 종료이면 True))
def step(pos, action):
    moves = [(-1,0),(1,0),(0,-1),(0,1)] #up, down, left, right -> i,j 가 row,col 기준 좌표이므로
    i, j = pos  #현재 상태s(agent의 좌표 pos)를 가져옴
    di, dj = moves[action]  #action에 따른 이동 정의
    ni, nj = i+di, j+dj #이동으로 얻어진 새로운 좌표
    if not (0 <= ni < GRID_SIZE and 0 <= nj < GRID_SIZE):
        ni, nj = i, j   #만약 주어진 grid 범위 밖으로 넘어갔다면 제자리
    new_pos = (ni, nj)  #다음 상태 s'(agent의 새로운 좌표 new_pos)
    if new_pos == GOAL: return new_pos, 20, True    #Goal에 도달하면 보상 20주고 에피소드 종료(True)
    if new_pos in TRAPS: return new_pos, -10, True  #Trap에 도달하면 패널티 -10 주고 에피소드 종료(True)
    return new_pos, -0.1, False #Goal이나 Trap이 아닌 상태로 전이하면 -0.1 이동패널티 주고 에피소드 진행(False)

# --- Trainer ---
class DQNTrainer:
    def __init__(self, ui):
        self.ui = ui
        self.state_dim, self.action_dim = GRID_SIZE*GRID_SIZE, 4    #State space와 Action space 크기 -> 격자점 개수 25와 상/하/좌/우 4
        self.qnet = QNet(self.state_dim, self.action_dim)   #Qnet
        self.target_qnet = QNet(self.state_dim, self.action_dim)    #Target-Qnet
        self.target_qnet.load_state_dict(self.qnet.state_dict())    #Target-Qnet은 주기적으로 Qnet을 복사한 네트워크임. 맨 처음에 복사하며 초기화
        self.optimizer = optim.Adam(self.qnet.parameters(), lr=0.001)   #Qnet 학습시킬 optimizer 정의
        self.buffer = deque(maxlen=10000)   #replay buffer 생성
        self.gamma, self.batch_size = 0.99, 32  #discount factor인 gamma와 batch_size
        self.epsilon, self.eps_min, self.eps_decay = 1.0, 0.05, 0.995   #self.epsilon 은 초기 epsilon 값, self.eps_decay는 선형 감소계수, self.eps_min는 epsilon 최소값(최종값)
        self.episode = 0    #에피소드 카운터
        self.last_traj = []    #애니메이션 재생에 사용할 마지막 trajectory(이동경로) 저장

    # 에피소드 한번 학습
    def run_one_episode(self):
        pos = START
        traj = [pos]    #경로를 저장할 traj 배열
        done = False    #에피소드 종료여부(False면 에피소드 진행, True면 종료)
        while not done:
            s = encode_state(pos).unsqueeze(0)  #state encoding 및 배치차원 추가
            if random.random() < self.epsilon:
                a = random.randint(0, self.action_dim-1)    #epsilon의 확률만큼은 random한 action 선택
            else:
                a = self.qnet(s).argmax().item()    #1-epsilon 확률만큼 greedy한 Q가 가장 큰 action 선택
            new_pos, r, done = step(pos, a) # 상태전이(s,a로 s',r,done을 얻음)
            traj.append(new_pos)    #경로에 new_pos(s'를 의미) 추가
            self.buffer.append((pos,a,r,new_pos,done))  #replay buffer에 (s,a,r,s',done) 튜플 저장.
            pos = new_pos   #새로운 좌표를 현재 좌표로

            #만약 replay buffer에 쌓인 버퍼 수가 배치 수(16) 이상이 되면 그때부터 Qnet를 업데이트함(Qnet을 replay buffer에서 배치단위로 샘플링하여 update 할것이기에 최소 배치단위 개수만큼은 필요)
            if len(self.buffer) >= self.batch_size:
                self.update_network()
        
        self.epsilon = max(self.eps_min, self.epsilon*self.eps_decay)   #epsilon 값은 초기값에서 시작하여 선형감소계수에 의해 선형적으로 감소. 최소값에 도달하면 더이상 감소하지 않고 고정
        if self.episode % 5 == 0:
            self.target_qnet.load_state_dict(self.qnet.state_dict())    #5에피소드마다 Target-Qnet을 업데이트(Qnet을 복사해옴)
        self.episode += 1   #에피소드 카운터 증가
        self.last_traj = traj   #경로를 마지막 에피소드 경로로써 저장

    # Qnet 학습
    def update_network(self):
        import random
        batch = random.sample(self.buffer, self.batch_size) #Replay buffer에서 random sampling(batch_size 만큼)
        
        ## replay buffer에서 뽑은 배치단위 (s,a,r,s',done)을 학습에 쓰기 위해 tensor로 묶어줌
        s_batch = torch.stack([encode_state(b[0]) for b in batch])  #배치 내 모든 현재 상태 s를 encoding하고 (batch, state_dim) 텐서로
        a_batch = torch.tensor([b[1] for b in batch])   #배치 내 모든 행동 a를 (batch,)인 정수 텐서(벡터)로
        r_batch = torch.tensor([b[2] for b in batch])   #배치 내 모든 보상 r을 (batch,)인 실수 텐서(벡터)로
        s2_batch = torch.stack([encode_state(b[3]) for b in batch]) #배치 내 모든 다음 상태 s'를 encoding하고 (batch, state_dim) 텐서로
        d_batch = torch.tensor([b[4] for b in batch], dtype=torch.float32)  #종료여부(done)을 실수 텐서(0. or 1.)로(타겟 계산에 사용됨)

        ## Q-value 업데이트 식
        '''gather(dim,index)는 주어진 dim 축에서 index가 가리키는 위치의 값들을 모아오는 연산이다.
        self.qnet(s_batch)는 (batch, action_dim) 모양의 텐서로 모든 행동 A에 대한 Q값이 들어있는데,
        우리가 필요한 Q는 샘플들에서 선택한 행동들의 Q만 알면 된다. 따라서 a_batch.unsqueeze(1) 의
        (batch, 1) 모양인 각 샘플이 실제로 한 행동의 인덱스를 담고있는 텐서를 이용하여 그 샘플이 취한 행동의
        Q만 뽑아준다.'''
        q_values = self.qnet(s_batch).gather(1, a_batch.unsqueeze(1)).squeeze()

        ## Target의 Q값은 Target-Qnet에서 뽑아야 하며, Target은 고정시켜 놔야 하기 때문에 no_grad()상태(학습안함)으로 Q(s',a')가져옴
        '''qnet을 거치면 (batch,state_dim)의 텐서가 (batch,action_dim)의 텐서가 된다. 따라서 이 중에서 Q가 가장
        큰 값을 뽑으려면 dim=1 에 대해 max값을 구하면 (각 샘플별 max Q값, 그때의 argmax 행동 인덱스)가 출력 되므로
        [0]으로 인덱싱하여 max Q값만 가져오면 된다.'''
        with torch.no_grad():
            max_next = self.target_qnet(s2_batch).max(1)[0]
            target = r_batch + self.gamma*(1-d_batch)*max_next  #(gamma 뒤에 (1-done)을 곱해줌으로써 done = 1 이면 학습 종료를 의미하며 보상 r만 Q값으로 가져감)
        
        
        loss = ((q_values - target)**2).mean()
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

    ## 학습으로 구한 Q값을 ui에 업데이트(시각화)
    def update_ui(self):
        # Q값 업데이트
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                s = encode_state((i,j)).unsqueeze(0)
                qvals = self.qnet(s).detach().numpy().flatten()
                self.ui.update_q_values((i,j), qvals.tolist())
        # 마지막 trajectory 전달
        self.ui.trajectory = self.last_traj


# ui를 띄우고 학습 후 마지막 trajectory 관찰(space를 눌러 진행 가능)
# on_space 함수 내 for 문의 range 내 값을 조절하여 몇 에피소드 학습마다 애니메이션으로
# 관찰할 지 정해줄 수 있음.
def main():
    ui = GridWorldUI()
    ui.root.unbind("<space>")     # UI의 기본 스페이스 바인딩 제거
    
    trainer = DQNTrainer(ui)

    def on_space(event=None):
        # --- 스페이스바 = 100 에피소드 학습 ---
        for _ in range(100):
            trainer.run_one_episode()   #1 에피소드 학습
        trainer.update_ui() #계산한 Q값 업데이트하여 ui에 반영
        print(f"== {trainer.episode} episodes 학습 완료 ==")
        # trajectory 애니메이션 재생
        ui.start_episode()

    ui.root.bind("<space>", on_space)  # DQN 핸들러만 사용
    ui.root.mainloop()


if __name__ == "__main__":
    main()

