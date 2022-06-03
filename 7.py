#7.Design, Develop and Implement a menu driven Program in Python for the following set
#operations
#a. Union()
#b. Intersection()
#. Difference()
#. Symmetric_Difference()
#upport the program with appropriate functions for each of the above operation

# Creating Sets 
s1 = {1,4,3,7,9}
s2 = {2,5,0,9,1}

#UNION
def union():
    print("Union is : ", s1|s2)

#INTERSECTION
def intersection():
    print("Intersection is : ", s1&s2)

#DIFFERENCE
def difference():
    print("Difference is : ", s1-s2)

#SYMMETRIC DIFFERENCE
def Symmetric_Difference():
    print("Symmetric Difference is : ", s1^s2)

# MENU
print("\n------MENU------\n1-Union \n2-Intersection \n3-Difference \n4-Symmetric_Difference\n5-Exit")
def menu():
    c = int(input("\nEnter Your Choice : "))
    
    if(c == 1):
        union()
    elif(c == 2):
        intersection()
    elif(c == 3):
        difference()
    elif(c == 4):
        Symmetric_Difference()
    else:
        exit()
    menu()

menu()
