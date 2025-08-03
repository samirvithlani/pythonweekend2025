def pdfHandler(fileName):
    print(f"pdf handler function called...{fileName}")
    

def docHandler(fileName):
    print(f"doc handler function called...{fileName}")

def imageHandler(fileName):
    print(f"image handler function called...{fileName}")
        

#cb -- call back..
def fileHandler(cb):
    print("file handler called...")
    cb("xyz") 


fileName = "abc.pdf"
if fileName.endswith(".jpg"):
    fileHandler(imageHandler)
elif fileName.endswith(".pdf"):
    fileHandler(pdfHandler)
elif fileName.endswith(".doc"):
    fileHandler(docHandler)    
