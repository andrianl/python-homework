first_list=["Hello", "World", 2000, 2020, 5, 25,8,10]
second_list=["World", "World", 2020, 2020, 25, 25,5, 0,1]
result=[]

for i in first_list:
    for j in second_list:
        if i==j:
            result.append(i)
            break

print(first_list)
print(second_list)
print(result)


# first_list=["Hello", "World", 2000, 2020, 5, 25,8,10]
# second_list=["World", "World", 2020, 2020, 25, 25,5, 0,1]
# result = list(set(first_list) & set(second_list))
# print(first_list)
# print(second_list)
# print(result)