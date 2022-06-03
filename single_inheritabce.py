class call:
    def add(self,a=None,b=None):
        print("Sum is :",a+b)
class cal2(call):
    def sub(self,a=None,b=None):
        print("difference is: ",a-b)
class cal3(cal2):
    def multiply(self,a=None,b=None):
        print("Multiply is: ",a*b)
class cal4(cal3):
    def div(self,a=None,b=None):
        print("Division is: ",a//b)
a=cal4()
a.sub(8,2)
a.add(2,4)
a.multiply(5,5)
a.div(5,2)