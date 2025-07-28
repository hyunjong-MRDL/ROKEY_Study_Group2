import tkinter as tkk

root = tkk.Tk()
root.geometry("400x300")
root.title("조각 피자 주문 프로그램")

olabel = tkk.Label(root, text="피자").pack(side="top")

menu_names = {0: "치즈 피자",
              1: "콤비네이션 피자",
              2: "불고기 피자"}

menu_prices = {0: 3200,
               1: 3500,
               2: 3600}

check_log = {}
for i in range(len(menu_names)):
    check_log[i] = tkk.BooleanVar()
    check_btn = tkk.Checkbutton(root, variable=check_log[i],
                                text=f"{menu_names[i]} ({menu_prices[i]}원)")
    check_btn.pack(anchor="w")

def print_order():
    total = 0
    order_text = "\n주문내역:\n"
    for i in range(len(check_log)):
        if check_log[i].get(): # 주문한 메뉴만 실행
            order_text += f"- {menu_names[i]} ({menu_prices[i]}원)\n"
            total += menu_prices[i]
    if total == 0:
        order_text = "\n*** 경고 ***\n아직 메뉴를 선택하지 않았습니다.\n메뉴를 선택해 주십시오."
    else:
        order_text += f"\n총 가격: {total}원"
    
    order_label.config(text=order_text) # 주문 내역 Label 내용 갱신

button = tkk.Button(root, text="주문", command=print_order).pack()

order_label = tkk.Label(root, text="")
order_label.pack()

root.mainloop()