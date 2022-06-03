def ZeroDivisionError():
    try:
        a =int(input('enter the number: '))
        b = int(input('enter the number: '))
        c = a/b
        print(c)
    except:
        print('divide by zero error.')

def Nameerror():
    try:
        name = "hello world"
        print(Name)
    except NameError:
        print("name error occured.")

def Indentationerror():
    i=0
    try:
        while(i<4):
            i+=1
    except IndentationError as e:
            print (e)
def ioerror():
    try:
        f = open('sa.txt','r')
        print(f.read())
    except IOError as e:
        print('IO error occured')

print('1.Zero Division Error \n2.Name Error \n3.Indentation Error \n4.IOError \n5.EXIT')
while(1):
    choice = int(input('enter your choice: '))
    if(choice == 1):
            ZeroDivisionError()
    elif(choice == 2):
            Nameerror()
    elif(choice == 3):
            Indentationerror()
    elif(choice == 4):
            ioerror()
    elif(choice == 5):
            print('You want to EXIT from the program.')
            print("Name - Vineet Kukreti,CSE(N),class Roll No - 81,StdID-20011316")
            exit(0)
    else:
            print('Invalid Choice')
