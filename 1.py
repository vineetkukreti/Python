def sum(a,b):
    sum = a+b
    return sum
def difference(a,b):
    diff = a-b
    return diff
def multiplication(a,b) :
    mul = a*b
    return mul
def division(a,b):
    div = a/b
    return div
def modulus(a,b):
    mod = a%b
    return mod
def flooring(a,b):
    flo = a//b
    return flo

print('1.sum \n2.difference \n3.multiplication \n4.division \n5.modulus \n6.flooring \n7.exit');
while(1):
    choice = int(input('enter your choice: '))
    if(choice == 1):
            a =int(input('enter the number: '))
            b = int(input('enter the number : '))
            print('sum of',a,'&',b,' is : ',sum(a,b))
    elif(choice == 2):
            a = int(input('enter the number: '))
            b = int(input('enter the number: '))
            print('difference of',a,'&',b,' is : ',difference(a,b))
    elif(choice ==3):
            a=int(input('enter the number: '));
            b = int(input('enter the number: '));
            print('multiplication of',a,'&',b,' is : ',multiplication(a,b))
    elif(choice == 4):
            a = int(input('enter the number : ' ))
            b= int(input('enter the number: '))
            print('division of',a,'&',b,' is : ',division(a,b))
    elif(choice == 5):
            a= int(input('enter the number: '))
            b = int(input('enter the number: '))
            print('modulus of',a,'&',b,' is : ',modulus(a,b))
    elif(choice == 6):
            a = int(input('enter the number: '))
            b= int(input('enter the number: '))
            print('flooring of',a,'&',b,' is : ',flooring(a,b))
    elif(choice == 7):
            print("you want to exit from the program .")
            print("Name - Vineet Kukreti,CSR3(N),class Roll No - 81,StdID-20011316")
            exit(0)
    else:
            print('invalid choice')


