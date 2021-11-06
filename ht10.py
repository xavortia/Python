nums=[]
for i in range (0,3):
    num=int(input('vvedite chislo'))
    nums.append(num)
    print(nums) 
qw=input('вы хотите добавить последнее введенное число?')
if qw=='no':
    nums.remove(num)
    print(nums)
else:
    print(nums)