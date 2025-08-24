#read data from file


# with open("th.txt","r") as file:
#     x = file.read()
#     x = file.read(10)
#     print(x)


# with open("userData.txt") as file2:
#     for i in file2:
#         print(i,end="")    


# with open("userData.txt","r") as file3:
#     # x = file3.readline()
#     # print(x)
    
#     while True:
#         x = file3.readline()
#         print(x,end="")
#         if not x:
#             break

with open("task.txt","r") as file4:
    # x = file4.readlines()
    # for i in x:
    #     print(i,end="")
    
    for i in file4.readlines():
        print(i,end="")