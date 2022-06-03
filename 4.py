'''
    4 Design, Develop and Implement a menu driven Program in Python to perform the following
    tasks
    a. To check if an entered year is leap year or not?
    b. To calculate a GCD of two numbers
    c. To check if an entered number is prime or not
     Support the program with appropriate functions for each of the above tasks

'''
def  find_leap_year():
      n = int(input("Enter the year = "))
      if(n%400==0 or n%4==0 and n%100!=0):
            print(n," is leap year.\n")
      else:
            print(n," is not leap year")
def GCD():
      a = int(input("Enter first number : "))
      b = int(input("Enter second number : "))
      print(f"GCD of {a} and {b}")
      n = min(a,b)
      hcf = 1
      for x in range(1,n+1):
            if(a%x==0 and b%x==0):
                  hcf = x
      print(hcf)
def find_prime_no():
    n = int(input("Enter the no : "))
    for i in range(2,n):
        if(n%i==0):
            print(n," is not a prime no")
            return
    print(n," is prime no")
print("1.To check if an entered year is leap year or not\n2.To calculate a GCD of two numbers\n3."
      "To check if an entered number is prime or not\n")
while True:
    choice = int(input("Enter your choice = "))
    if choice == 1:
        find_leap_year()
    elif choice == 2:
        GCD()
    elif choice == 3:
        find_prime_no()
    else:
        print("invalid")