

class time:
  

        def __init__(self,h,m,s):
            self.hour = h
            self.minuts = m 
            self.second = s

    
        def show(self):
            print( self.hour , ':' , self.minuts , ':' , self.second) 

        def Standard_time(self):
    
            if self.second ==60 :
                self.minuts += 1
            if self.second > 60 :
                b = int(self.second/ 60)
                a = self.second% 60
                self.minuts = self.minuts+b
                self.second = a
            if self.minuts==60 :
                self.hour = self.hour+1
            if self.minuts > 60 :
                b = int(self.minuts/ 60)
                a = self.minuts% 60
                self.hour = self.hour+b
                self.minuts = a
                #print( self.hour , ':' , self.minuts , ':' , self.second)
            #if mehman.second==60 :
            #    mehman.minuts = mehman.minuts+1
            #if mehman.second > 60 :
            #    b = int(mehman.second/ 60)
            #    a = mehman.second% 60
            #    mehman.minuts = mehman.minuts+b
            #    mehman.second = a
            #if mehman.minuts==60 :
            #    mehman.hour = mehman.hour+1
            #if mehman.minuts > 60 :
            #    b = int(mehman.hour/ 60)
            #    a = mehman.minuts% 60
            #    mehman.hour = mehman.hour+b
            #    mehman.minuts = a
            #    print(mehman) 
            # 
        def total_time(self,mehman):
            result = time(None,None,None)
            #Standard_time(t1,t2) 
            result.second = self.second + mehman.second
            result.minuts = self.minuts + mehman.minuts
            result.hour = self.hour + mehman.hour
            if result.second==60 :
                result.minuts = result.minuts+1
                result.second= 0
            if result.second > 60 :
                b = int(result.second/ 60)
                a = result.second% 60
                result.minuts = result.minuts+b
                result.second = a
            if result.minuts==60 :
                result.hour = result['h']+1
                result.minuts= 0
            if result.minuts > 60 :
                b = int(result.minuts/ 60)
                a = result.minuts% 60
                result.hour = result.hour+b
                result.minuts = a

            return result

        def subtraction_time(self,mehman):
            result = time(None,None,None)
    #Standard_time(t1,t2)
     
            if mehman.second< self.second:
                mehman.minuts = mehman.minuts - 1
                mehman.second = mehman.second + 60
            if mehman.minuts< self.minuts:
                mehman.hour = mehman.hour - 1
                mehman.minuts = mehman.minuts + 60

            result.second = mehman.second - self.second
            result.minuts = mehman.minuts - self.minuts
            result.hour = mehman.hour - self.hour
            return result    
     
        def time_second(self):
            #self.hour = int(input('saat zaman aval:  '))
            #self.minuts = int(input('daghigheh zaman aval:  '))
            #self.second = int(input('sanieh zaman aval:  '))
            if self.second==60 :
                self.minuts = self.minuts+1
            if self.second > 60 :
                b = (self.second/ 60)
                a = self.second% 60
                self.minuts = self.minuts+b
                self.second = a
            if self.minuts==60 :
                self.hour = self.hour+1
            if self.minuts > 60 :
                b = (self.hour/ 60)
                a = self.minuts% 60
                self.hour = self.hour+b
                self.minuts = a
            #print(t1)
            
            second_time = self.hour*3600+self.minuts*60+self.second
            #print("ثانیه",second_time)
            return(second_time)
       

a = time(3,25,89)
b = time(16,67,45)   

a.Standard_time()
b.Standard_time()
a.show()
b.show()
print("-----jameh do zaman")
c = a.total_time(b)
c.Standard_time()
c.show()
print("-----tafrigh do zaman")
d = a.subtraction_time(b)
d.Standard_time()
d.show()
print("--------time to second")
e=a.time_second()
e.show()
f=b.time_second()
f.show()