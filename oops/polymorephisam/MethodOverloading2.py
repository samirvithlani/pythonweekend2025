from multipledispatch import dispatch

class Shape:
    
    @dispatch()
    def area(self):
        print("function without param called.. area")
    
    @dispatch(float)
    def area(self,r):
        print("function with param called Area",r)    

    @dispatch(int,int)        
    def area(self,h,w):
        print("function with param called Area",h,w)    



s = Shape()
s.area(10,20)
s.area()
s.area(100.0)        



#print(10==10)
#print(10 is 10)

a = 10
b = 20
print(a==b)
print(a is b)

a = [10,20,30]
b = [10,20,30]

print(a==b)
print(a is b)