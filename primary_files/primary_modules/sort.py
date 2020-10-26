def GETsmallest_number(list):
    smallest_number = 0


 # getting the smallest number in the list
    for num in list:
        if num == list[0]:
            smallest_number = num
        elif num < smallest_number:
            smallest_number = num 
        else:
            continue
    
    return smallest_number


def GETsorted_list(list):
    passed_list = list
    sorted_list= []
    for i in range(0,len(passed_list)):
        num = GETsmallest_number(passed_list)
        sorted_list.append(num)
        passed_list.remove(num)
        
    return sorted_list