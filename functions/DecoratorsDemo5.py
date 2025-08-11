
def logs(func):
    
    def inner(*args,**kwargs):
        print("function called ..",func.__name__)
        func(*args,**kwargs)
    
    return inner    



@logs
def paynow(amount):
    print("paying amount rs",amount)


@logs
def sendmail(to,subject):
    print(f"sendning mail to {to} with subject {subject}")    


@logs
def accessData(user,role):
    print(f"accessing data by {user} having  role {role}")    


paynow(1200)
sendmail("samir@gmail.com","test")
accessData("ram","admin")