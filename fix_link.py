import os
import re

file_path = "d:/수학교과캠프/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace any occurrence of the incorrect link pointing directly to the root
content = content.replace('href=\\"개념 설명.dc.html\\"', 'href=\\"uploads/개념 설명.dc.html\\"')
content = content.replace('href="개념 설명.dc.html"', 'href="uploads/개념 설명.dc.html"')
content = content.replace('href=\\"%EA%B0%9C%EB%85%90%20%EC%84%A4%EB%AA%85.dc.html\\"', 'href=\\"uploads/%EA%B0%9C%EB%85%90%20%EC%84%A4%EB%AA%85.dc.html\\"')
content = content.replace('href="%EA%B0%9C%EB%85%90%20%EC%84%A4%EB%AA%85.dc.html"', 'href="uploads/%EA%B0%9C%EB%85%90%20%EC%84%A4%EB%AA%85.dc.html"')
content = content.replace('href=\\"/%EA%B0%9C%EB%85%90%20%EC%84%A4%EB%AA%85.dc.html\\"', 'href=\\"uploads/%EA%B0%9C%EB%85%90%20%EC%84%A4%EB%AA%85.dc.html\\"')
content = content.replace('href="/%EA%B0%9C%EB%85%90%20%EC%84%A4%EB%AA%85.dc.html"', 'href="uploads/%EA%B0%9C%EB%85%90%20%EC%84%A4%EB%AA%85.dc.html"')

# We can also do a regex just in case:
content = re.sub(r'href=\\?"/?(?:%EA%B0%9C%EB%85%90(?:%20| )%EC%84%A4%EB%AA%85|개념(?:%20| )설명)\.dc\.html\\?"', r'href=\"uploads/개념 설명.dc.html\"', content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Link fixed in index.html (if found).")
