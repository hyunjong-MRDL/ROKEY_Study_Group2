# gridworld_ui.py
import tkinter as tk

GRID_SIZE = 5
CELL_SIZE = 160
GOAL = (4, 4)
START = (0, 0)
TRAPS = [(1, 3), (4, 1)]
STEP_REWARD = -0.1
GOAL_REWARD = 20
TRAP_REWARD = -10


class GridWorldUI:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(
            self.root, width=GRID_SIZE*CELL_SIZE, height=GRID_SIZE*CELL_SIZE
        )
        self.canvas.pack()

        self.agent_pos = list(START)
        self.agent = None

        self.q_values = {}
        self.q_text_items = {}

        self.trajectory = []
        self.step_idx = 0
        self.on_episode_end = None  # callback for end of episode

        self.draw_grid()
        self.draw_agent()

        self._after_id = None
        self.episode_running = False  # 명시 초기화

        # spacebar → 다음 episode 시작
        self.root.bind("<space>", self.start_episode)

    def draw_grid(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                x1, y1 = j*CELL_SIZE, i*CELL_SIZE
                x2, y2 = x1+CELL_SIZE, y1+CELL_SIZE
                if (i, j) == START:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue")
                    self.canvas.create_text((x1+x2)//2, (y1+y2)//2, text="Start", font=("Arial", 14))
                elif (i, j) == GOAL:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="yellow")
                    self.canvas.create_text((x1+x2)//2, (y1+y2)//2,
                                            text=f"Goal\nR={GOAL_REWARD}", font=("Arial", 14))
                elif (i, j) in TRAPS:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="red")
                    self.canvas.create_text((x1+x2)//2, (y1+y2)//2,
                                            text=f"X\nR={TRAP_REWARD}", font=("Arial", 14))
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                    self.canvas.create_text((x1+x2)//2, (y1+y2)//2,
                                            text=f"R={STEP_REWARD}", font=("Arial", 10))

    def draw_agent(self):
        i, j = self.agent_pos
        x1, y1 = j*CELL_SIZE, i*CELL_SIZE
        x2, y2 = x1+CELL_SIZE, y1+CELL_SIZE
        margin = CELL_SIZE * 0.3
        self.agent = self.canvas.create_polygon(
            (x1+CELL_SIZE//2, y1+margin,
             x1+margin, y2-margin,
             x2-margin, y2-margin),
            fill="blue"
        )

    def move_agent(self, new_pos):
        i, j = new_pos
        if not (0 <= i < GRID_SIZE and 0 <= j < GRID_SIZE):
            new_pos = self.agent_pos
        self.agent_pos = new_pos
        self.canvas.delete(self.agent)
        self.draw_agent()

        # 도달 시: 다음 예약을 더 이상 진행하지 않게 플래그 내리고, 리셋만 지연
        if tuple(new_pos) in TRAPS or tuple(new_pos) == GOAL:
            self.episode_running = False
            # 예약 취소
            if self._after_id is not None:
                try: self.root.after_cancel(self._after_id)
                except: pass
                self._after_id = None
            self._after_id = self.root.after(500, self.end_episode)

        # trap/goal 도달 시 episode 종료 예약
        if tuple(new_pos) in TRAPS or tuple(new_pos) == GOAL:
            self.episode_running = False  # 애니메이션 중단
            # 0.5초 뒤에 episode 종료 처리 → agent가 도달한 칸 보이게
            self.root.after(500, self.end_episode)

    def update_q_values(self, state, q_list):
        i, j = state
        x1, y1 = j*CELL_SIZE, i*CELL_SIZE
        cx, cy = (x1+CELL_SIZE//2, y1+CELL_SIZE//2)

        if state in self.q_text_items:
            for item_id in self.q_text_items[state]:
                self.canvas.delete(item_id)

        up_id = self.canvas.create_text(cx, y1+20, text=f"U:{q_list[0]:.2f}", font=("Arial", 10))
        down_id = self.canvas.create_text(cx, y1+CELL_SIZE-20, text=f"D:{q_list[1]:.2f}", font=("Arial", 10))
        left_id = self.canvas.create_text(x1+25, cy, text=f"L:{q_list[2]:.2f}", font=("Arial", 10))
        right_id = self.canvas.create_text(x1+CELL_SIZE-25, cy, text=f"R:{q_list[3]:.2f}", font=("Arial", 10))

        self.q_text_items[state] = [up_id, down_id, left_id, right_id]

    def start_episode(self, event=None):
        # 이전 예약 있으면 취소
        if self._after_id is not None:
            try: self.root.after_cancel(self._after_id)
            except: pass
            self._after_id = None
        self.step_idx = 0
        self.episode_running = True
        self.animate_episode()

    def end_episode(self):
        if self.on_episode_end:
            self.on_episode_end()   # 여기서 reset_agent 호출

    def animate_episode(self):
        if not self.episode_running:
            return
        if self.step_idx < len(self.trajectory):
            self.move_agent(self.trajectory[self.step_idx])
            self.step_idx += 1
            # move_agent에서 도중에 episode_running이 False가 될 수도 있으므로, 여기서 한 번 더 체크
            if self.episode_running:
                self._after_id = self.root.after(400, self.animate_episode)
        else:
            self.episode_running = False
            self._after_id = None
            print("Episode trajectory done.")

    def reset_agent(self):
        """에피소드 끝났을 때 호출 → 시작 위치로 리셋"""
        self.agent_pos = list(START)
        self.canvas.delete(self.agent)
        self.draw_agent()

    def render(self):
        self.root.update()


if __name__ == "__main__":
    ui = GridWorldUI()
    ui.trajectory = [START, (0,1), (1,1), (2,1), (3,1), (4,1), (4,2), (4,3), GOAL]
    ui.on_episode_end = ui.reset_agent
    ui.root.mainloop()