class Parent:
    
    def home(self):
        print("this is home function from parent class")


class Child(Parent):        
    
    def home(self):
        print("this is home funciton from child class ...")


c = Child()
c.home()        