import os
def write():
    f = open('sample.txt','w')
    string = input('enter the sentence you want to put in file: ')
    f.write(string)
    f.close()

def read():
    f = open('sample.txt','r')
    print(f.read())
    f.close()

def append():
    f = open('sample.txt','a')
    str = input('enter the string to append in the file: ')
    f.write(str)
    f.close()

def delete():
    os.remove('sample.txt')

print('1.write \n2.read \n3.append \n4.delete \n5.EXIT\n')

while(1):
    choice = int(input('enter your choice: '))
    if(choice == 1):
        write()
    elif(choice == 2):
        read()
    elif(choice == 3):
        append()
    elif(choice == 4):
        delete()
    elif(choice == 5):
        print('you want to EXIT from the program.')
        print("Name - Vineet Kukreti,CSE(N),class Roll No - 81,StdID-20011316")
        exit(0)
    else:
        print('!!Invalid Choice!!')
