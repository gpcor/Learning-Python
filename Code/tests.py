import re

file1 = open("Learning-Python/Code/resume.txt","r")
phoneRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')

mo = phoneRegex.search(file1)
print(mo.group())