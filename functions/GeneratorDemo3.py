# def getStudents():
#     yield [f"student {i}" for i in range(1,11)]
#     yield [f"student {i}" for i in range(11,21)]
#     yield [f"student {i}" for i in range(21,31)]

# for i in getStudents():
#     print(i)    
    
    
#1000 100    
def getStudents(total,batchsize):
    yield [f"student {i}" for i in range(1,11)]
    yield [f"student {i}" for i in range(11,21)]
    yield [f"student {i}" for i in range(21,31)]

for i in getStudents():
    print(i)    
    
        