class User:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
    def getUserData(self):
        print(f"name  ={self.name}")    
        print(f"age ={self.age}")    

naman = User("naman",22)        
naman.getUserData()