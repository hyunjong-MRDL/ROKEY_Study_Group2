import re

pattern = r"[a-zA-Z0-9]+@[a-z]+\.(?:com|net|org)" # "?:" non-capture
text = "이메일 목록: test@example.com, hello@world.net, user123@domain.org"
matches = re.findall(pattern, text)
print(matches)