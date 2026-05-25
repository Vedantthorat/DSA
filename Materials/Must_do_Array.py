1. Array Reverse

'''
def reverse_array(arr):
    if not arr:
        return None
    
    left, right = 0, len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        
        left += 1
        right -= 1
        
    return arr



arr = [1,2,4,5,6]

print(reverse_array(arr))
'''
def revArray(arr):
    if not arr:
        return None
    
    temp = len(arr) * [0]
    
    for i in range(len(arr)):
        
        temp[i] = arr[len(arr) - i - 1]
        
    for i in range(len(arr)):
        arr[i] = temp[i]
        
    return arr

arr = [1,2,4,5,6]

print(revArray(arr))





2. Reverse array by group K

def reverseGroup(arr, k):
    if not arr:
        return
    
    i = 0
    n = len(arr)
    
    while i < n:
        left = i
        right = min(i + k-1,n - 1)
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            i += k
            
    return arr

arr = [1,2,3,4,5,7]
k = 3

print(reverseGroup(arr,k))


3. Reverse array by d

def revArray_by_d(arr, d):
    if not arr:
        return
    n = len(arr)
    d %= n
    def reverse(left, right):
        #left, right = 0, len(arr) - 1
        while left < right:
            
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
    reverse(0, d-1)
        
    reverse(d, n-1)
        
    reverse(0, n-1)
        
    return arr
    
    
arr = [1,2,3,4,6]
d = 2

print(revArray_by_d(arr,d))


4. third largest

def find_third_large(arr):
    if len(arr) < 3:
        return arr
    
    first = second = third = float('-inf')
    
    for i in arr:
        if i > first:
            third = second
            second = first
            first = i
            
        elif i > second:
            third = second
            second = i
        elif i > third:
            third = i
            
    return third

arr = [34,544,23,66,11,656]

print(find_third_large(arr))


5. second largest

def find_second_large(arr):
    if len(arr) < 2:
        return arr
    
    first = seconf = float('-inf')
    
    for i in arr:
        if i > first:
            second = first
            first = i
            
        elif i > second:
            second = i
            
    return second

arr = [34,544,23,66,11,656]

print(find_second_large(arr))

6. 
