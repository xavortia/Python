num=[123,423,897,270]
print(num[0], num[1], num[2], num[3], sep='\n')
num1=int(input())
try:
    num.index(num1)
except ValueError:
    print('that is not in list')
print(num)
