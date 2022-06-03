def sort(array,n):
    for i in range(n):
        for j in range(0,n-i-1):
            if(array[j]>array[j+1]):
                array[j],array[j+1] = array[j+1],array[j]

array = []
n = int(input('enter the size of array: '))
for i in range(n):
    value = int(input('input the element : '))
    array.append(value)
sort(array,n)
print('after sorting the list : ')
print(array)
print("Name - Vineet Kukreti,CSE(N),class Roll No - 81,StdID-20011316")
