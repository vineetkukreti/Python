# 6.develop and implement a menu driven pogram in python for the operation on queue
# a. add element on to queue(enqueue)
# b. delete an element from queue(dqueue)
# c. demonstrate overflow and underflow situation on queue
# d.display the status of queue
# e. exit

def isFull(queue,size):
    if(len(queue)==size):
        print('OVREFLOW !')
        menu()
        
def isEmpty(queue,top):
    top = len(queue)-1
    if(top == 0):
        print('UNDERFLOW !')
        menu()

def enqueue(queue,size):
    isFull(queue,size)
    data = int(input('enter the value : '))
    queue.append(data)
        
def display(queue,top):
    top = len(queue)-1
    if(top == 0):
        print('UNDERFLOW !')
    else:
        print(queue)

def status(queue, top, size):
    isFull(queue,size)
    isEmpty(queue,top)
    
def dqueue(queue,top):
    isEmpty(queue,top)
    print('deleted element is : ',queue.pop(0))

def menu():
    queue=[]
    top = 0
    size = int(input('enter the size of queue: '))
    print(' Press 1.Push \n Press 2.Pop\n Press 3. Display\n Press 4. Status\n Press 0.exit')
    while True:
        choice = int (input('\nenter your choice: '))
        if(choice==1):
            enqueue(queue,size)
        elif(choice == 2):
            dqueue(queue,top)
        elif(choice ==3):
            print("\nOutput : \n")
            display(queue,top)
        elif(choice == 4):
            status(queue, top, size)
        elif(choice == 0):
            exit()
        else:
            print('invalid choice')
menu()    
