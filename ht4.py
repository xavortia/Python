food=dict.fromkeys([i for i in range(1,5)])
for i in range(1,5):
    food[i]=input('введите вашу любимую еду')
print(food)
del1=int(input('какой элемент вы хотите удалить?'))
food.pop(del1)
print(food) 