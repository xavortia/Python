name=[]
for i in range(0,3):
    a=input()
    name.append(a)
f=input('вы хотите добавить кого то?')
while True:
    if f=='no':
        break
    else:
        a=input()
        name.append(a)
        f=input('вы хотите добавить кого то?')
print(name)
r=input('vvedite imia iz spiska')
print(name.index(r))
s=input('этот чел будет на тусе?')
if s=='no':
    name.remove(r)
    print(name)
print(name)