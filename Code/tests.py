import random

stringA = 'AJKMLNFDBKSTRUBJQAZWSQWERTYUIOPFUNASDFGHJKLXLKHJGFDSANUFPOIUYTREWQSWZAQJBURTSKBDFNLMKJA'
stringB = reversed(stringA)

print(type(stringB))
print(stringB)

if stringB == stringA:
    print('This is a palindrome')
else:
    print('This is not a palindrome')
