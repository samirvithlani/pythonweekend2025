class Father:
    
    def __init__(self):
        self.amount =1000
        self.p = 2000
    
    def car(self):
        print("Father class car called..")    

class Mother:
    
    def __init__(self):
        self.amount=2000
        self.q=199
    
    def bike(self):
        print("Mother class bike called..")    


class Child(Mother,Father):
    
    def __init__(self):
        super().__init__() #parent const..
    
    
    def getData(self):
        print(f"amount = ",self.amount)    
        print(f"amount = ",self.q)
        print(f"amount = ",self.p)    
                    
        self.car()
        self.bike()


c = Child() #const..
c.getData()        