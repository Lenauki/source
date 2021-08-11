'''
f = open("c:/source/Newfile.txt","r")
while True:
    line = f.readline()
    if not line: break
    print(line, end = '')
f.close()

'''

'''
f = open("c:/source/Newfile.txt","r")
lines = f.readlines()
print(type(lines))
print(lines)
for line in lines:
    print(line, end = '')
f.close()

'''

'''
f = open("c:/source/Newfile.txt","r")
data = f.read()
print(data)
f.close()
'''
'''
f = open("c:/source/Newfile.txt","a")
for i in range(11,20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
'''

with open('foo.txt',"w") as f:
    f.write("Life is too short, you need python")
