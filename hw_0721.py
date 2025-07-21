import tkinter

piz = tkinter.Tk()
piz.title('조각 피자 주문 프로그램')
piz.geometry('400x300')
piz_label = tkinter.Label(piz,text='피자')
piz_label.pack()

piz_dic = {0:'치즈 피자(3200원)',1:'콤비네이션 피자(3500원)',2:'불고기 피자(3600원)'}
piz_price = {0:3200,1:3500,2:3600}
pizCk = {}
for i in range(len(piz_dic)) :
    pizCk[i]= tkinter.BooleanVar()
    piz_ck = tkinter.Checkbutton(piz,text=piz_dic[i],variable=pizCk[i]).pack(anchor='w')    

def buy():
    pizFistLabel = tkinter.Label(piz,text='주문내역').pack()
    t_sel_piz = []
    a=0
    for i in range(len(pizCk)) :
        if pizCk[i].get() == True :
            pizLabel = tkinter.Label(piz,text='-'+piz_dic[i]).pack()
            t_sel_piz.append(piz_price.get(i))
    for j in range(len(t_sel_piz)):
        a += t_sel_piz[j]
    pizFistLabel = tkinter.Label(piz,text='총 가격 :'+str(a)).pack()

pizBut = tkinter.Button(piz,text='주문',command=buy).pack()
piz.mainloop()