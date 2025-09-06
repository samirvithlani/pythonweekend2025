class Student:
    
    def __init__(self,marks):
        self.marks = marks
    
    
    #other --> Student class object
    #self == ram -- left side oprand
    #other == shyam right side oprand
    def __add__(self,other):
        print("self...",self.marks)
        print("other...",other.marks)
        return self.marks + other.marks

ram = Student(23)
shyam = Student(24)

total = ram + shyam #+ --> __add__ function
print(total)
            