
from re import S


class kasr:

        def __init__(self,s,m):
            self.soorat = s
            self.makhraj = m

        def sum(self , mehman):
            result = kasr(None,None)
            if self.makhraj % mehman.makhraj == 0 or mehman.makhraj % self.makhraj == 0:
                if self.makhraj > mehman.makhraj:
                    q = self.makhraj / mehman.makhraj
                    result.soorat = self.soorat + mehman.soorat*q
                    result.makhraj = self.makhraj
                else:
                    p = mehman.makhraj / self.makhraj
                    result.soorat = p*self.soorat + mehman.soorat
                    result.makhraj = mehman.makhraj 
            else:
                result.soorat = self.soorat* mehman.makhraj+ self.makhraj * mehman.soorat
                result.makhraj = self.makhraj * mehman.makhraj           
            return result

        def mul(self , mehman):
            result = kasr(None,None)
            result.soorat = self.soorat * mehman.soorat
            result.makhraj = self.makhraj * mehman.makhraj
            return result
            
        def sub(self , mehman):

            result = kasr(None,None)
            if self.makhraj % mehman.makhraj == 0 or mehman.makhraj % self.makhraj == 0:
                if self.makhraj > mehman.makhraj:
                    q = self.makhraj / mehman.makhraj
                    result.soorat = self.soorat - mehman.soorat*q
                    result.makhraj = self.makhraj
                else:
                    p = mehman.makhraj / self.makhraj
                    result.soorat = p*self.soorat - mehman.soorat
                    result.makhraj = mehman.makhraj 
            else:
                result.soorat = self.soorat* mehman.makhraj- self.makhraj * mehman.soorat
                result.makhraj = self.makhraj * mehman.makhraj           
            return result

        def div(self , mehman):
            result = kasr(None,None)
            result.soorat = self.soorat * mehman.makhraj
            result.makhraj = self.makhraj * mehman.soorat
            return result

        def show(self):
            print( self.soorat , '/' , self.makhraj) 

           
            
    

a = kasr(3,5)
b = kasr(4,3)
print("hello, welcome toSimple Math")
a.show()
b.show()

c = a.mul(b)
print("mul = ",c.show())
d = a.sum(b)
print("sum= ",d.show())
e = a.sub(b)
print("sum = ",e.show())
f = a.div(b)
print("div = ",f.show())




        

                     
