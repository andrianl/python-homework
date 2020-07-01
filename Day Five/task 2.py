
def ListsIntersection(first_list, second_list): 
    new_list = [value for value in first_list if value in second_list] 
    return new_list


def ListsIntersection2(first_list, second_list):
    return list(set(first_list) & set(second_list)) 
   



list1=[1,2,3,4,5,6,7,8,9,10]
list2=[5,6,7,8,9,10,11,12,13,15,15]
intersect_list=ListsIntersection(list1,list2)
intersect_list2=ListsIntersection2(list1,list2)
print(intersect_list)
print(intersect_list2)
