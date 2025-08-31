class Bank:
    
    def __init__(self,name):
        #self.name = "ICICI" #2 copy -- b1.name= "ICICI", b2.name="SBI"
        self.name = name
        print("param const of Bank class called !!")

    def getDetail(self): #b1 b2
        print("Bank Name = ",self.name)

b1 = Bank("ICICI")        
b2 = Bank("SBI")

b1.getDetail()
b2.getDetail()
    