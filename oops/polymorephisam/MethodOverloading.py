class Shape:
    
    def area(self):
        print("function without param called.. area")
    
    def area(self,r):
        print("function with param called Area",r)    
        
    def area(self,h,w):
        print("function with param called Area",h,w)    



s = Shape()
s.area(10,20)        