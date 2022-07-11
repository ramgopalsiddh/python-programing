class computer:

    def __init__(self):
        self.name = "ram gopal"
        self.age = 18

    def update(self):
        self.age = 30 

    def compare(self,other):
         if self.age == other.age:
            return True
         else:
            return False           


c1  = computer()
c1.age = 30
c2  = computer()

if c1 == c2:
    print("they are same")
else:
    print("they are defferent")    

c1.update()

print(c1.name,c1.age)
print(c2.name,c2.age)