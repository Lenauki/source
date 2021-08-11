'''
for i in range(2,10):
    for j in range(1,10):
        print(i, '*', j, '=', i*j, end= ' ')
    print('')
'''
'''
for i in range(1,10):
    for j in range(2,10):
        print('%d * %d =' %(j,i),(j*i), end= '  ')
    print('')
'''

'''
a = ['one', 'two', 'hi', '^^']
result = []

for num in a:
    result.append(num)

print(result)

'''
'''
a = [1, 2, 3, 4]
result = []
for num in a:
    if num % 2 ==0:
        result.append(num * 3)
print(result)
'''

'''
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

'''

