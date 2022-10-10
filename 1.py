
A = input('Введите имя студента: ')
B = input('Введите фамилию студента: ')
C = int(input('Введите год рождения: '))
print(A, B, C, sep='_')
A, B  = B, A
C += 60
print(A, B, C, sep='_')