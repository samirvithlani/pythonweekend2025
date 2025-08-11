# def test():
#     return 1
#     return 2
#     return 3

# x = test()
# print(x)

def test():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


# x = test()
# print(x)  
# for i in x:
#     print(i)
# print(next(x))  
# print(next(x))  
# print(next(x))  
# print(next(x))  
# print(next(x))  

for i in test():
    print(i)