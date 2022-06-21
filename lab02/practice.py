#numbers = [-3,-2,-1,0,1,2,3]

def kth_smallest(numbers, k):
        
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
    
print(kth_smallest([-3, -2, -1, 0, 1, 2, 3], 5))
     
#print(new_list)
#print(sorted_list)

