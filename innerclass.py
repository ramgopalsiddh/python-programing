

class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()
    
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop:

        def __init__(self):
            self.brand = 'hp' 
            self.cpu = 'i5'
            self.ram = 8   

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = student('shyam',2)
s2 = student('rahul',4) 

s1.show()    
