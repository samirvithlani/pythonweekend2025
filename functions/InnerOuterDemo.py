# def outer():
#     print("outer function caled")
#     def inner():
#         print("inner function called !!")

#     inner()

# outer()
        

# def outer(ono1):
#     print("outer function caled")
#     def inner():
#         x=100
#         print("inner function called !!")
#         print("outer var",ono1)
#         print("x = ",x)

#     inner()
#     print("x = ",x)

# outer(100)


# def outer(ono1):
#     print("outer function caled")
#     def inner():
#         x=100
#         print("inner function called !!")
#         print("outer var",ono1)
#         print("x = ",x)
#         return "i am inner"

#     inr = inner()
#     print("inner return",inr)

# outer(100)                

def outer():
    def inner():
       print("hi this is inner function !!")
   
    return inner     
x =outer()
print(x)
x()