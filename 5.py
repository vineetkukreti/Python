def  push(stack,max):
    n = len(stack)
    if(n==max):
        print("\nstack is full\n")
        return 
    else:
        stack.append(input("Enter the element = "))
def display(stack,top):
    top = len(stack) - 1
    if (top < 0):
        print("Stack is empty")
    print(*stack[::-1])

def Pop(stack,top):
    top = len(stack)-1
    if(top<0):
        print("Stack is empty")
    else:
        print("Deleted element = ",stack.pop())

stack = []
top = 0
max = int(input("Enter the size of stack = "))
print("1.Push\n2.Pop\n3.Display\n4.Exit")
while True:
    choice = int(input("Enter your choice = "))
    if choice == 1:
        push(stack,max)
    elif choice == 2:
        Pop(stack,top)
    elif choice == 3:
        display(stack,top)
    elif choice == 4:
        exit()
    else:
        print("\nWrong Choice")
