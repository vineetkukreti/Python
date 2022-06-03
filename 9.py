def insert(dict,n ):
    for i in range(n):
            key = input('enter the key: ')
            value= input('enter the value to insert in dicitonary: ')
            dict[key] = value
    #print('elements in dictionary are: ', dict)
    return dict

def access(dict,n):
    print('printing all the keys in the dictionary: ')
    for i in dict:
        print(i)
        print('printing all the vlaues of dictionary: ')
    for i in dict.values():
        print(i)
        print('accessing keys and value in the dictionary : ')
    for i,j in dict.items():
        print(i,j)

def update(dict,n):
    dict.update({n+1 : "hello" })
    print("after updating dictionary : ",dict)

def remove(dict,n):
    print('deleting key and value is: ',dict.popitem())
    print('after deleting the keys form the dictionary: ')
    print(dict)

dict = {}
print('1.Creating Dictionarty \n2.access dictionary \n3.update dictionary \n4.remove element \n5.iterating dictonary\n')
while(1):
    choice = int(input('enter your choice: '))
    if(choice == 1):
        n = int(input('enter the number of keys in the dictionary: '))
        insert(dict,n)
        print('elements in dictionary are: ', dict)
    elif(choice == 2):
            access(dict,n)
    elif(choice == 3):
            update(dict,n)
    elif(choice == 4):
            remove(dict,n)
    elif(choice == 5):
            print('You want to EXIT from the program.')
            print("Name - Vineet Kukreti,CSE(N),class Roll No - 81,StdID-20011316")
            exit(0)
    else:
            print('invalid choice')
