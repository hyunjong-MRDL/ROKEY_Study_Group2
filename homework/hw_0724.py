import re

# text = '이메일 목록:test@example.com, hello@world.net, user@domain.urg'
# p = re.compile(r'\w+@\w+[.]\w+',re.DOTALL)
# print(p.findall(text))


# text = '연락처:010-1234-5678, 02-987-6543, 031-456-7890'
# p = re.compile(r'010-\d+-\d+')
# print(p.findall(text))

text = 'I Iove Python. Java is also popular. Python is great for AI.'
p = re.compile(r'[^.]*\bPython\b[^.]*\.')
print(p.findall(text))

# text = '상품 코드: A123, B456, C789, 가격: 12000 원'
# p = re.compile('\d{1,}')
# print(p.findall(text))

# text = 'NASA is working on AI projects with IBM and Google.'
# p = re.compile('[A-Z]+')
# print(p.findall(text))