original_list = ["Hello", "World", "Hello", "Friend",  5, 25, 25, 50, 5]

new_list = list(set(original_list)) 

print(original_list)
print(new_list)

# original_list=[]
# new_list=[]

# stop =  False

# while stop is not True:
#     element=(input("Enter list element:"))
#     if element=="stop":
#         new_list=list(set(original_list))
#         print(original_list)
#         print(new_list)
#         stop = True
#         pass
#     else:
#         original_list.append(element)
#         pass
