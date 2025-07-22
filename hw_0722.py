path = r'C:\rokey\python\ch12\pizza_file1.txt'
mode = 'r'

with open(path,mode,encoding='utf-8') as pizza :
    piz_text = pizza.readlines()
    list = []
    for i in piz_text :
        piz_list = i.split(' ')
        list.append(piz_list[0].strip())

print(list)