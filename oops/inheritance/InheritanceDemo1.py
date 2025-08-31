class Car:
    
    
    def __init__(self):
        print("parent class const called...")
        self.type = "sedan"
        self.seat = 5
    
    def engine(self):
        print("engine...")    


class BMW(Car):
    
    def __init__(self):
        print("child class default const called... !!")
        super().__init__()
    
    
    def getDetail(self):
        self.engine()
        print("cart type = ",self.type)    
        print("car seat = ",self.seat)



b = BMW()        
b.getDetail()