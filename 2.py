'''
2 String
a. Write a program to read string and display “Total number of Uppercase and
Lowercase letters”
b. Write a function Reverse_Word(word) which returns the words in reverse
c. Write a function getVowels(word) which takes a word as an argument and returns
the vowels(‘a’,’e’,’i’,’o’,’u’) in that word

'''
def evaluate(str):
    a = len(str)
    upper = 0
    lower = 0
    for i in range(a):
        if(str[i]>='A' and str[i]<='Z'):upper = upper+1
        elif(str[i]>='a' and str[i]<='z'):lower = lower+1
    print(f"No of lower character = {lower}\nNo of upper character = {upper}")

def reverse(str):
    s = str[::-1]
    return s

def getvowels(str):
    vowels = "AEIOUaeiou"
    result = []
    for i in str:
        if(i in vowels):
            result = i
    return result
                
str = input("Enter the string = ")
evaluate(str)
print("Reversed word  = ",reverse(str))
x = getvowels(str)
print("get vowels = ",x)
