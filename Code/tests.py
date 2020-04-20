import re

prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
dotStar = re.compile(r'.*', re.DOTALL)
mo = dotStar.search(prime)

print(mo) 