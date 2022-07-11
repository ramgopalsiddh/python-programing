
def update(lst):
    
    print(id(lst))

    lst[1] = 25
    print(" x ",lst)

lst = [10,20,30]
update(lst)  
print(id(lst))  
print(" lst ",lst)