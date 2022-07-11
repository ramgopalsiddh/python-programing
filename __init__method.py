class computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
        
    def config(self):
        print ("config is",self.cpu, self.ram)    
    


con1 = computer('i5',16)
con2 = computer('ryzen 3',8)


con1.config()
con2.config()