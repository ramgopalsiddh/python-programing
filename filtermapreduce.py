
nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda n : n%2==0, nums))

print("even",evens)


nums = [3,2,6,8,4,6,2,9]

odd = list(filter(lambda n : n%2!=0, nums))

print("odd",odd)