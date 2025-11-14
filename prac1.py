
l = [1,10,12,14,15,19,21,24,26,42]

def linear_search(l, id):
    for i in range(len(l)):
        if l[i]==id:
            return True, i 

    return False, -1


def binary_search(l, id):
    high = len(l)-1
    low  = 0
    while low < high:
        mid = int((low+high)/2)
        if l[mid]==id:
            return True, mid 
        elif l[mid] > id:
            high = mid - 1
        else:
            low = mid + 1


    return False, -1


# Start Execution

print(linear_search(l, 26))
print(binary_search(l, 34))


    
