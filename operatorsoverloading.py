

class student:
    def __init__(self,m1,m2):
       self.m1 = m1
       self.m2 = m2

    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2) 

        return s3  

    def __gt__(self,other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        if s1>s2:
            return True
        else:
            False        

    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)

s1 = student(30,50) 
s2 = student(20,30)

s3 = s1+s2

if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")    

a = 9
print(a)    

print(s1)
print(s2)