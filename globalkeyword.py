'''global variable'''
a = 10

def something():
    '''change in global variable by local'''
    global a
    '''local variable'''
    a = 25

    print("in fun" ,a)


something()





print("out side",a)