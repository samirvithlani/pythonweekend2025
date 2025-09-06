class Student:
    
    def __init__(self,*marks):
        self.marks = marks
     
     
     #==
    def __eq__(self, other):
        return self.marks == other.marks



amit = Student(20,30,40)    
sumit = Student(21,29,40)
        
if amit == sumit:
    print("both has same marks within subject also")            
else:
    print("no same marks,...")    