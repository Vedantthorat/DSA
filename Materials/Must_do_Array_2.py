1. Array in waveform

def waveArray(arr):
    if not arr:
        return
    n = len(arr)
    for i in range(0, n - 1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
        
    return arr

arr = [1,2,3,4,5]
print(waveArray(arr))

# first ele >= second 
# second ele <= thord
# thord ele >= fourth and so on
# o/p = [2, 1, 4, 3, 5]


2. Max consecutive zero-one


def max_consecutive_01(arr):
    if not arr:
        return
    
    cnt = 1
    max_cnt = 0
    
    for i in range(1, len(arr)):
        
        if arr[i] == arr[i-1]:
            cnt += 1
            
        else:
            max_cnt = max(max_cnt, cnt)
            
            cnt = 1
            
    return max_cnt

arr = [1,2,4,1,1,1,3]
print(max_consecutive_01(arr))

# using bit manipulation

def max_consecitive_using_bit(arr):
    if not arr:
        return
    
    prev, max_cnt, cnt = arr[0],0,0
    
    for num in arr[1:]:
        if prev ^ num == 0:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
            
            prev = num
    return max_cnt
            
arr = [1,2,4,1,1,1,3]
print(max_consecitive_using_bit(arr))


3. Maximum product triplet
def maxProductTriplet(arr):
    if len(arr) < 3:
        return
    
    arr.sort()
    n = len(arr)
    return max(arr[0] * arr[1] * arr[n - 1], arr[n-1]* arr[n-2]* arr[n-3])

arr = [-10,-3,-5,-6,-20]
print(maxProductTriplet(arr))

# after sort
'''
arr = [-20,-10,-6,-5,-3]


'''

4. Move zero to end

def moveZeroEnd(arr):
    
    #if not arr:
       # return
    
    cnt = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[cnt] = arr[cnt], arr[i]
            cnt += 1
            
    return arr

#arr = [2,4,5,1,0,5,0,6]
arr = []

print(moveZeroEnd(arr))


5. 










