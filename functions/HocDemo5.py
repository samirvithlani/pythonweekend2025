#args and kwargs


def add(*args):
    total = 0
    for i in args:
        total+=i
    print(f"sum = {total}")    

def sub(*args):
    total = 0
    for i in args:
        total-=i
    print(f"sum = {total}")

def mul(*args):
    total = 1
    for i in args:
        total*=i
    print(f"sum = {total}")

def div(*args):
    total = 1
    for i in args:
        total/=i
    print(f"sum = {total}")
   
   

def calc(op,*args):
    print("calc opned...")
    op(*args) 

#calc(add,10,20,30,40,50)    
choice = input("Enter choice :")
if choice =="add":
    calc(add,10,20,30,40,50)

elif choice =="sub":
    calc(sub,200,20,30,40,50)
                    