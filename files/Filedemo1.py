file = open("myfile1.txt","a")
file.write("hello this is second line from file...")
file.close()

with open("files/myfile2.txt","a") as file1:
    file1.writelines(["Hi this is first line\n","hi this is second line\n"])
    print("data has been written successfully !!")

#file1.write(",,,,")     close..

name = "RAM"
with open("userData.txt","a") as file2:
    print(f"Hi i am user my name is {name}",file=file2)


#data = [{"name":"ram","age":23,"city":"ahmedabad","area":"bopal"},{"name":"ajay","age":23,"city":"ahmedabad","area":"bopal"}]
data = {"name":"ram","age":23,"city":"ahmedabad","area":"bopal"}
with open(data["name"]+".txt","a") as file3:
    for i ,j in data.items():
        file3.write(f"{i} --> {j}\n")
    print("user detail has been saved...")    
    