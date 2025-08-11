# def getStudents():
#     yield [f"student {i}" for i in range(1,11)]
#     yield [f"student {i}" for i in range(11,21)]
#     yield [f"student {i}" for i in range(21,31)]

# for i in getStudents():
#     print(i)    
    
    
#1000 100    
def getStudents(total,batchsize):
    #1 -->101 ,5
    for i in range(1,total+1,batchsize):
        #end 1 + 5 =6
        end = i + batchsize
        yield [f"student {s}" for  s in range(i,end) if s <= total]

for i in getStudents(100,5):
    print(i)    
    
        