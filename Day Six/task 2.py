def Arguments(func):
    def inner(*args, **kwargs):
        print(args,kwargs)
    return inner

@Arguments
def BiggestNumber(list,n):
    min = 0
    while n > 0:
        number = max(list)
        new_list.append(number)
        index_number = list.index(number)
        list[index_number] = min 
        n -= 1
    return new_list


list = [1,3,5,7,8,9,11,13,12,10,8,6,4,2]
new_list = []
n = int(input('How many numbers you need: '))
new_list = BiggestNumber(list,n)
print(new_list)

    