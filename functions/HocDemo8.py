#args and kwargs


def add(*args):
    total = 0
    for i in args:
        total+=i
    #print(f"sum = {total}")    
    return total

def sub(*args):
    total = 0
    for i in args:
        total-=i
    #print(f"sum = {total}")
    return total

def mul(*args):
    total = 1
    for i in args:
        total*=i
    #print(f"sum = {total}")
    return total

def div(*args):
    total = 1
    for i in args:
        total/=i
    #print(f"sum = {total}")
    return total
   
   

def calc(op,*args):
    print("calc opned...")
    # ans = op(*args) 
    # #print(f"ans = {ans}")
    # return ans
    return op(*args)

#calc(add,10,20,30,40,50)    
ans=None

choice = input("Enter choice :")
if choice =="add":
    ans = calc(add,10,20,30,40,50)

elif choice =="sub":
    ans = calc(sub,200,20,30,40,50)

print(f"ans = {ans}")                    