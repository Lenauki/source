'''
def add(a,b):
    return a+b


a = 1
b = 6
c = add (a,b)
print(c)
'''
'''
def say():
    return 'hi'


print(say())


def addd(a,b):
    print('%d, %d의 합은 %d입니다.' % (a, b, a+b))


addd(3,4)

'''

'''
def add_many(choice, *args):  #args는 튜플의 형태로 저장함
    if choice == 'add':    
        result = 0
        for i in args:
            result += i

    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
    else:
        print('add 또는 mul을 선택하세요')
        result = 0       
    return result


a = add_many('mul',1,2,3,4,5)
'''

'''
def add_and_mul(a,b):
    return a+b, a*b


result = add_and_mul(3,5)

print(result)
'''
'''
def say_myself(name, old, man=True):
    print('나의 이름은 %s 입니다.' % name)
    print('나이는 %d 살입니다' % old)
    if man:
        print('남자입니다')
    else:
        print('여자입니다')

say_myself('바바라', 18,0)
'''

'''
a = 1
def vartest(a):
    a += 1
    return a

a =vartest(a)
print(a)
'''
'''
add = lambda a, b: a+b
result = add(5,11)
print(result)
'''

a = input()


