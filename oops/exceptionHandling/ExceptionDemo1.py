# no1 = int(input("enter no 1 :"))
# no2 = int(input("enter no 2 :"))

# try:
#     x = no1 / no2
#     print(x)
# except:
#     print("can not divide by zero")    

# print("...")    

# try:
#     no1 = int(input("enter no 1 :"))
#     no2 = int(input("enter no 2 :"))
#     x = no1 / no2
#     print(x)
# except:
#     print("can not divide by zero")    

# print("...")    

# try:
#     no1 = int(input("enter no 1 :"))
#     no2 = int(input("enter no 2 :"))
#     x = no1 / no2
#     print(x)
# except ZeroDivisionError:
#     print("can not divide by zero !")    
# except ValueError:
#     print("please enter digits only !")    

# print("...")    

# try:
#     no1 = int(input("enter no 1 :"))
#     no2 = int(input("enter no 2 :"))
#     x = no1 / no2
#     print(x)
# except ZeroDivisionError as e:
#     #print("can not divide by zero !")    
#     print(e)
# except ValueError as e:
#     #print("please enter digits only !")    
#     print(e)

# print("...")    



try:
    no1 = int(input("enter no 1 :"))
    no2 = int(input("enter no 2 :"))
    x = no1 / no2
    print(x)
    #50 files.... 41st -- path... exceptio..
    #41.... exception --- except...
    #file closing.. 50... no*
except ZeroDivisionError as e:
    #print("can not divide by zero !")    
    print(e)
except ValueError as e:
    #print("please enter digits only !")    
    print(e)
finally:
    print("finally bloack executeed...")   
    #if exception comes or not it will exceute.. 
    #trancation management...
    

