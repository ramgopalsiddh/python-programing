

def person( name,**data):

    print(name)

    for i,j in data.items():
        print(i,j)



person(name="ram",age=24,city="churu",mob=8209870707,village="bhanuda")   