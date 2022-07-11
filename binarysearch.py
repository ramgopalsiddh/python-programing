pos = -1

def search(list,n):

    l = 0
    u = len(list)-1

    while l <=u:
        mid = (l+u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid
            else:
                u = mid  

list = [4,7,8,12,45,99,100,300,390,399]
n = 300

if search (list, n):
    print("found at",pos)

else:
    print("not found")    
