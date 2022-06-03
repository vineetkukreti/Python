'''
8 Design, Develop and Implement a menu driven Program in Python for the following
operations on Tuple
    a. Create a tuple of 5 numbers
    b. Write a user defined function maximum(number) to find the maximum number in
    the tuple
    c. Write a user defined function minimum(number) to find the minimum number in
    the tuple
    d. Exit
'''
def MAX(t):
    n = len(t)
    max = t[0]
    for i in range(n):
        if max < t[i]:
            max = t[i]
    return max
def MIN(t):
    n = len(t)
    min = t[0]
    for i in range(n):
        if min > t[i]:
            min = t[i]
    return min
print("------------------------------------------------------")
print("\t\t  ::: MAIN MENU :::")
print("\t\t\t1.create tuple\n\t\t\t2.Find Max in tuple\n\t\t\t3.Find Min in tuple\n\t\t\t4.exit")
print("------------------------------------------------------")
while True:
    choice = int(input("Enter your choice = "))
    if choice == 1:
        a = []
        n = int(input("No of element : "))
        for i in range(n):
            a.append(int(input("Enter the element  : ")))
        t = tuple(a)
        print(t)
    elif choice == 2:
        print("Max  : ",MAX(t))
    elif choice == 3:
        print("Min  : ",min(t))
    elif choice == 4:
        exit(0)
    else:
        print("Invalid choice")
