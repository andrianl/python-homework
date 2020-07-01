def func1(list,n):
    min = 0
    while n > 0:
        number = max(list)
        new_list.append(number)
        index_number = list.index(number)
        list[index_number] = min 
        n -= 1
    return new_list

list = [1,5,7,5,8,9,4,89,12,45,67,78,89,23]
new_list = []
n = int(input('How many numbers you need: '))
new_list = func1(list,n)
print(new_list)