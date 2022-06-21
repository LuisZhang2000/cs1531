
def find_reverse(numbers):
    #TODO: find the reverse of the list
    return list(reversed(numbers))
    pass

def find_max(numbers):
    #TODO: find the maximum of the list
    return max(numbers)
    pass

def find_min(numbers):
    #TODO: find the minimum of the list
    return min(numbers)
    pass

def find_sum(numbers):
    #TODO: find the sum of all the numbers in the list
    return sum(numbers)
    pass

def find_average(numbers):
    #TODO: find the average of all the numbers in the list
    return (sum(numbers)/len(numbers))
    pass

def find_descending(numbers):
    #TODO: numbers sorted in descending order
    return sorted(numbers, reverse=True)
    pass

def second_smallest(numbers):   
    #TODO: find the second smallest
    second_smallest = 0
    sorted_nums = sorted(numbers)
    for x in range(len(sorted_nums)):
        if sorted_nums[x] < sorted_nums[x + 1]:
            second_smallest = sorted_nums[x + 1]
            break
        x += 1        
    return second_smallest
    pass

def kth_smallest(numbers, k):
    #TODO: find the kth smallest number in the list
    # make new list without any duplicate numbers
    # then sort the new list by ascending order
    # then return kth smallest
    
    new_list = []
    kth = 0
    for i in numbers:
        if i not in new_list:
            new_list.append(i)
        i += 1      
    sorted_list = sorted(new_list)
    for j in range(len(sorted_list)):
        if j == k - 1:
            kth = sorted_list[j]
        j += 1
    return kth
    pass

if __name__ == '__main__':
    # If you are testing, place your print statements here
    pass
