import os 

spam = open('/Users/gcorsini/Desktop/Delicious/spam.txt', 'w')
weird = open('/Users/gcorsini/Desktop/Delicious/weird.txt', 'w')

love = open('/Users/gcorsini/Desktop/Delicious/foo/love.txt', 'w')
eggs = open('/Users/gcorsini/Desktop/Delicious/walnut/eggs.txt', 'w')

bacon = open('/Users/gcorsini/Desktop/Delicious/walnut/waffles/bacon.txt', 'w')

spam.close()
weird.close()
love.close()
eggs.close()
bacon.close()