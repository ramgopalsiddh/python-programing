

def fib(n):
    
    

     a = 0
     b = 1
     

     if n == 0:
        print(a)

     else:
        print(a)
        print(b)

        for n in range(2,n):
            c = a+b
            a = b
            b = c
            
            print(c)

fib(12)            