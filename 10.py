# def Bsearch(list,l,r,key):
# 	if(r>=l):
# 		mid = l+(r-l)//2
# 		if(list[mid] == key):
# 			return mid
# 		elif(list[mid] > key):
# 			return Bsearch(list,l,mid-1,key)
# 		else:
# 			return Bsearch(list,mid+1,r,key)

# list = []
# n = int(input('enter the size of list: '))
# for i in range(n):
#     value = int(input('enter the number in list: '))
#     list.append(value)
# key = int(input('enter the key to find in list: '))
# search = Bsearch(list,0,n-1,key)
# if(search!=-1):
#     print("element is found in the list at : ",search+1)
# else:
#     print('element is not found in the list')
# print("Name - Vineet Kukreti,CSE(N),class Roll No - 81,StdID-20011316")
def Lsearch(list,n,key):
	for i in range(n):
		if(key == list[i]):
			return i+1
	return 0

list =[]
n = int(input("enter the size of list: "))
for i in range(n):
    value = int(input("enter the element: "))
    list.append(value)
key = int(input("enter the key to search in the list: "))
search = Lsearch(list,n,key)
if(search):
    print("key is found in the list at : ",search)
else:
    print("key is not found in the list.")

print("Name – Vineet Kukreti ,CSE3(N),class Roll NO.-81,StdID-20011316")
