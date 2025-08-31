#class name must starts with cap if joining ltr then it will cap
#User UserDetail

class Demo:
    
    #self is an current object class
    x =100 #class level variable / sttaic vaiable in python 
    #you can use anywhere in calss
    #it will create only one copy. -- 1000 obeject 1 copy
    def test(self): #self == d
        t = 1000 #local variable 
        #it can use only in scope
        self.a = 999 #instance variable...
        #it will create no of object copy
        #it can be use with same object within class
        print("test function called..")
    
    def display(self):
        print("a = ",self.a) 
        print("x = ",self.x)  
        #print("t = ",t) #error..
        



#if you want to access any prop of class we need ref of class
#what is ref --> object of your class

#d is an object of Demo class
#we can create n no of object class
d = Demo()   
d.test()      
print("x outside class ",d.x)
print("a outside class",d.a)
#d.test(d) -- >class current object      
    