'''
f = open("C:/source/Newfile.txt","r")
while True:
    line = f.readline()
    if not line :break
    print(line)
f.close()
'''
'''
#1#
def is_odd(num):
    if num %2 ==1:
     return True
    else:
     return False


is_odd(5)
is_odd(6)
#2#


def avgs(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)




avgs(1,3,2,1,2,3,1,3,2)


#3#


input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)


#4#
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python","이거만 띄워져서 나옴")
print("".join(["you", "need", "python"]))


#5#

f1 = open("C:/source/test.txt","w")
f1.write('Life is too short')
f1.close()
f2 = open("C:/source/test.txt","r")
print(f2.read())
f1.close()

#6#
f3 =  open("C:/source/test.txt","a")
while True:
    useri = input("저장할 내용 입력 : ")
    if useri == '999': break
    f3.write("\n")
    f3.write(useri)
    f3.write("\n")
f3.close()

f4 = open("C:/source/test.txt","r")
print(f4.read())
f4.close()
'''

#7#
f5 = open("C:/source/test1.txt","w")
f5.write("Life is too short \nyou need java")
f5.close()

f5 = open("C:/source/test1.txt","r")
reple = f5.read()
f5.close()

reple = reple.replace("java","python")

f6 = open("C:/source/test1.txt","w")
f6.write(reple)
f6.close()
f5 = open("C:/source/test1.txt","r")
print(f5.read())
f5.close()



