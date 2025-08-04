# def ex(item):
#     stack = []

#     for i in item:
#         if i in "({[":
#             stack.append(i)
        
#         elif i in ")}]" :
#             if not stack:
#                 return False
        
#             top = stack.pop()

#             if ( i==')' and top != '(') or \
#                 ( i=='}' and top != '{') or \
#                  ( i==']' and top != '[') :
#                 return False
    
#     return len(stack) == 0
# item = input('괄호 안에 문자를 입력하세요 ex : (abc)   = ')
# print(ex(item))
        
# from collections import deque

# def twin_queue(queue,range):
#     dq = deque(queue)
#     dq.rotate(range)

#     return list(dq)
# list1 = []
# i = 0
# num1 = 1800
# while i !=4 :
#     num = int(input())
#     if num >= 1 and num <=1800 :
#         num1 = num1 - num
#         i+=1

# if i==4 :
#     if num1 >=300:
#         print('Yes')
#     elif num1 < 300 :
#         print('NO')