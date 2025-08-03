def pdfHandler(fileName):
    print(f"pdf handler function called...{fileName}")
    

def docHandler(fileName):
    print(f"doc handler function called...{fileName}")

def imageHandler(fileName):
    print(f"image handler function called...{fileName}")
        

#cb -- call back..
def fileHandler(cb,fileName):
    print("file handler called...")
    cb(fileName) 


fileName = "abc.jpg"
if fileName.endswith(".jpg") or fileName.endswith(".png"):
    fileHandler(imageHandler,fileName)
elif fileName.endswith(".pdf"):
    fileHandler(pdfHandler,fileName)
elif fileName.endswith(".doc"):
    fileHandler(docHandler,fileName)    
