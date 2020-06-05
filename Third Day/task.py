first_list= []
second_list=[]

stop= False

while stop is not True:
    n=input("Enter number:")
    if n=="stop":
        first_list.extend(second_list)
        print(first_list)
        stop=True
        pass
    if int(n)>=0:
        first_list.append(n)
        pass
    elif int(n)<0:
        second_list.append(n)
        pass
    else:
        break
        pass
