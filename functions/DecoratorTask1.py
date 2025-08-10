
def check_dt(func):
    def inner(*args):
        flag = True
        for i in args:
            if type(i)!= int:
                print("heree",i)
                flag = False
                break
        
        if flag == True:
            func(*args)
        else:
            print("all data must be number kind !!")        
    return inner        
            



@check_dt
def add(*args):
    sum =0
    for i in args:
        sum+=i
    
    print("sum = ",sum)        

add(10,20,30,"ok")    
        