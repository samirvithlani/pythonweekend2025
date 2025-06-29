numbers = [1,2,-11,90,-78,55]
#numlab = ["pos","pos"]
numlab =["POS" if i>0 else " NEG" for i in numbers]

# for i in numbers:
#     if i>0:
#         numlab.append("POS")
#     else:
#         numlab.append("NEG")    

print(numlab)        

numbers = [1,2,11,90,78,55]
evenodd = ["EVEN" if i %2==0 else "ODD" for i in numbers]
print(evenodd)

numbers = [1,2,-11,90,-78,55]

cleanNo = [0 if i<0 else i for i in numbers]

# for i in numbers:
#     if i<0:
#         i=0
#         cleanNo.append(i)
#     else:
#         cleanNo.append(i)    

print(cleanNo)    