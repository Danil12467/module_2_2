print('Введите первое число')
name1 = input()
print('Введите второе число')
name2 = input()
print('Введите третье число')
name3 = input()
if name1 == name2 == name3:
    print(3)
elif name1==name2 or name1==name3 or name2==name3:
    print(2)
else:
    print(0)
