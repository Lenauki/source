#1
print('')
print('#'*5, 'Q1','#'*5)
a = 'life is too short, you need python'

if 'wife' in a: print('wife')
elif 'python' in a and 'you' not in a: print(python)
elif 'shirt' not in a: print('shirt')
elif 'need' in a: print('need')
else: print('none')

#2
print('')
print('#'*5, 'Q2','#'*5)
result = 0
a = 1
while a <= 1000:
    if a %3 == 0:
        result += a
    a += 1 
print(result)

#3
print('')
print('#'*5, 'Q3','#'*5)
a = 0
while True:
    a += 1
    if a > 5: break
    print('*'*a)

b = 5
while True:
    b -= 1
    if b <=0: break
    print('*'*b)
    
#4
print('')
print('#'*5, 'Q4','#'*5)
for a in range(1,101):
    print(a, end = ' ')
print(' ')

#5
print('')
print('#'*5, 'Q5','#'*5)
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for score in A:
    total+= score
avg = total/len(A)
print(avg)


numbers = [1, 2, 3, 4, 5]
result =[n*2 for n in numbers if n % 2 == 1]
print(result)
