#decorators are pure python function which will take function as argument and return new function object
#use of decorators are to change behaviour of funciton without changing code
#decorators are denoted by @


def order_food(func): #3  func == throw_party -- address == func
    
    def inner(persons): #6
      if(persons>0):
          print("ordering food..")
          func(persons)
      else:
          print("no party...")    
    
    return inner #4   



@order_food #2 #5
def throw_party(no_pers): #9
    print("throw party",no_pers) #10

throw_party(10)    #1