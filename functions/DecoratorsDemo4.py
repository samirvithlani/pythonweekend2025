
def safeDiv(func):
    def inner(no1,no2):
        if no2 ==0:
            print("can not divide by zero")
        else:
            func(no1,no2)    
    
    return inner        

@safeDiv
def div(no1,no2):
    print(f"div = {no1/no2}")

div(10,2)    