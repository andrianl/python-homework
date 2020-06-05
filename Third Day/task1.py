first_list=[-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
second_list=[]


for i in first_list:
    if i%2==0:
        i=0
        second_list.append(i)
    else:
        i*=i
        second_list.append(i)

print(first_list)
print(second_list)



# first_list=[]
# second_list=[]
# stop=False

# while stop is not True:
#     n=input("Enter number:")
#     if n=="stop":
#         print(first_list)
#         print(second_list)
#         stop=True
#         pass
#     elif int(n)%2==0:
#        first_list.append(int(n))
#        n=0
#        second_list.append(n)
#        pass
#     elif int(n)%2==1:
#         first_list.append(int(n))
#         n=int(n)**2
#         second_list.append(n)
#         pass
#     else:
#         print("wrong")
#         pass

