numbers = [7, 2, 1, 6, 3, 4, 50]
sorted_list = []
smallest_number = numbers[0]

for i in range(0,len(numbers)):
    for num in numbers: # getting the smallest number in the list
        if num == numbers[0]:
            smallest_number = num
        elif num < smallest_number:
            smallest_number = num 
        else:
            continue
    
    # putting the smallest number from the passed list in a new var
    sorted_list.append(smallest_number)
    numbers.remove(smallest_number)



for num in sorted_list: print(num)