class Bank:
    
    def __init__(self):
        self.name = "ICICI" #2 copy -- b1.name= "ICICI", b2.name="ICICI"
        print("default const of Bank class called !!")

    def getDetail(self):
        print("Bank Name = ",self.name)

b1 = Bank()        
b2 = Bank()
    