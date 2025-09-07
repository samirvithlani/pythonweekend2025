from  abc import ABC,abstractmethod
#abstract base class

#upi -->abstract class...
class UPI(ABC):

    @abstractmethod    
    def transfer(self):
        #print("upi transfer called..")
        pass
    
    @abstractmethod
    def checkbal(self,x):
        pass
    
    
    def rules(self):
        print("ok...")



class SBI(UPI):
    
    def transfer(self):
        print("sbi ka apna logic !!")
    
    def checkbal(self, x):
        print("sbi check bal")    


#u = UPI() #error... abstract..
s = SBI()
s.transfer()
            