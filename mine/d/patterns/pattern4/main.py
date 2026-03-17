def check_palindorome(string):
    l = 0
    n = len(string)
    r = n-1
    while l<r:
        if string[l] != string[r]:
            return False
        l += 1
        r -=1
    return True   

def reverse_arr(arr):
    l = 0
    n = len(arr)
    r = n-1
    while l<=r:
        # temp = arr[l]
        # arr[l] = arr[r]
        # arr[r] = temp
        arr[l],arr[r] = arr[r],arr[l]
        l += 1
        r -= 1
        temp = 0
    return arr


def remove_dups(arr):
    s = 0
    f = 0
    n = len(arr)
    rarr = [arr[s]]
    while f<n:
        if arr[s] != arr[f]:
            s = f
            print(arr[s])
            print(arr[f])
            rarr.append(arr[s])
        f += 1
    return rarr


def movezeros(arr):
    n = len(arr)
    rarr = []
    for i in range(n):
        if arr[i] != 0:
            rarr.append(arr[i])
    p = n - len(rarr)
    print(p)
    for j in range(p):
        print(j)
        rarr.append(0)
    return rarr

def slowfast(arr):
    slow = 0
    fast = 0
    n = len(arr)
    while fast<n:
        fast += 2
        slow += 1
    return slow

def twosum(arr,k):
    left = 0
    n = len(arr)
    right = n -1
    while left<=right:
        if arr[left] + arr[right] == k:
            return arr[left],arr[right]
        elif arr[left] + arr[right] > k:
            right -=1
        else:
            left +=1
    return "Not found"


def contwater(arr):
    left = 0
    n = len(arr)
    r = n-1
    res = 0
    while left<r:
        area = min(arr[left],arr[r])*(r-left)
        res = max(res, area)
        if arr[left]<arr[r]:
            left += 1
        else:
            r -= 1
    return res

def sort_nums(arr):
    lo,mid = 0,0
    n = len(arr)
    hi = n-1
    while mid <= hi:
        if arr[mid] == 0:
            arr[lo],arr[mid] = arr[mid],arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[hi],arr[mid] = arr[mid],arr[hi]
            hi -= 1
            mid -= 1        
    return arr

def sorted_sqrs(arr):
    n = len(arr)
    left = 0
    right = n-1
    rarr = []
    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            rarr.append(arr[left]**2)
            left += 1
        else:
            rarr.append(arr[right]**2)
            right -= 1
    return rarr

def remove_dup(arr):
    slow = 0
    for fast in range(1,len(arr)):
        if arr[fast]!=arr[slow]:
            slow+=1
            arr[slow]=arr[fast]
    print(slow)
    return arr[:slow+1]


def remove_elem(arr,k):
    pointer = 0
    for i in range(len(arr)):
        if arr[i] != k:
            arr[pointer] = arr[i]
            pointer += 1
    return arr[:pointer]


def countpairs_hm(arr,k):
    freq = {}
    cnt = 0
    for i in range(len(arr)):
        freq[arr[i]] = freq.get(arr[i],0) + 1
        if arr[i]+k in freq:
            cnt += freq[arr[i]+k]
        elif arr[i] - k in freq:
            cnt += freq[arr[i]-k]
    return freq,cnt

def triplet_sum(arr,k):
    arr.sort()
    n = len(arr) 
    r = n -1
    rarr = []
    for i in range(n-2):
        trip = k - arr[i]
        l = i + 1
        r = n -1
        print(trip)
        while l < r:
            summ = arr[l] + arr[r]
            if trip == summ:
                rarr.append([arr[i],arr[l],arr[r]])
                r -= 1
                l += 1
            elif arr[l] + arr[r] > trip:
                r -= 1
            else:
                l += 1
        return rarr 

def triplet_sum2(arr):
    arr.sort()
    n = len(arr)
    r = n -1
    for i in range(n):
        l = i + 1
        r = n -1
        while l<r:
            if arr[r] - arr[l] == arr[i]:
                print(arr[r],arr[l])
                return True
            elif arr[r] - arr[l] > arr[i]:
                r -= 1
            else:
                l += 1
        return False

if __name__ == '__main__':
    # print(check_palindorome("hello"))
    # print(reverse_arr([0,1,2,3,4]))
    # print(remove_dups([1,1,2,2,3,3,5]))
    # print(movezeros([0,1,2,0,3,4,0]))
    # print(slowfast([10,20,30,40,50]))
    # print(twosum([1,2,3,4],6))
    # print(contwater([2, 1, 8, 6, 4, 6, 5, 5]))
    # print(sort_nums([0,1,0,1,2,1]))
    # print(sorted_sqrs([-4,-3,0,1,2]))
    # print(remove_dup([0,1,2,2,3]))
    # print(remove_elem([0,1,2,2,3],2))
    # print(countpairs([1, 4, 1, 4, 5],3))
    # print(countpairs_hm([1, 4, 1, 4, 5],3))
    # print(triplet_sum([40, 20, 10, 3, 6, 7], k = 24))
    # print(triplet_sum2([3, 4, 5]))
    # print(contwater_2([2, 1, 8, 6, 4, 6, 5, 5]))