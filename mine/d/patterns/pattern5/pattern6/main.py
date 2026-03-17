##### naive approach
 


import stat

from annotated_types import MaxLen


def maxsubstr(st):
    n = len(st)
    max_len= 0
    for i in range(n):
        for j in range(i,n):
            if st[j] in st[i:j]:
                break
        max_len = max(max_len,len(st[i:j]))
    return max_len


def maxsubstr_opt(st):
    n = len(st)
    max_len = 0
    sett = set()
    l = 0
    for r in range(n):
        while st[r] in sett:
            sett.remove(st[l])
            l += 1
        w = (r-l)+1
        max_len = max(w,max_len)
        sett.add(st[r])
    return max_len


def arraysum(arr,k):
    max_len = 0
    left = 0
    current_sum = 0
    for right in range(len(arr)):
        current_sum += arr[right]
     
    while current_sum > k and right >= left:
        current_sum -= arr[left]
        left += 1
    max_len = max(max_len, right - left + 1)
    return max_len

def atmost_kzeros(arr,k):
    n = len(arr)
    l = 0
    num_zeros = 0
    max_len = 0
    for r in range(n):
        if arr[r] == 0:
            num_zeros += 1
        while num_zeros > k:
            print(l)
            if arr[l] == 0:
                num_zeros -= 1
            l += 1
        max_len = max(max_len,(r-1)+1)
    return max_len

def min_len(arr,k):
    l = 0
    curr_sum = 0
    max_len = 0
    for r in range(len(arr)):
        curr_sum += arr[r]
        while curr_sum >= k:
            if curr_sum == k:
                max_len = (r-l)+1
            curr_sum -= arr[l]
            l += 1
        
    return max_len


def dist_ele(st,k):
    sett = set()
    l = 0
    max_len = 0
    for r in range(len(st)):
        sett.add(st[r])
        while len(sett)>k:
            sett.remove(st[l])
            l += 1
        w = (r-l)+1
        max_len = max(max_len,w)
        
    return max_len


def count_sub_k_odd(arr,k):
    start = 0
    total_subarr = 0
    odd_count = 0
    for end in range(len(arr)):
        if arr[end]%2 != 0:
            odd_count += 1
        while odd_count > k :
            if arr[start]%2 !=0:
                odd_count -= 1
            start += 1
        print(total_subarr)
        total_subarr += (end-start+1)
    return total_subarr


def long_increse_subarr(arr):
    start = 0
    max_len = 0
    curr_max = -1
    for end in range(len(arr)):
        while curr_max >= arr[end] and end >= start:
            curr_max = max(curr_max,arr[start])
            start += 1
        max_len = max(max_len,(end-start)+1)
        curr_max = max(curr_max,arr[end])
    return max_len


def max_flip(arr,k):
    start = 0
    max_len = 0
    zero_count = 0
    for end in range(len(arr)):
        if arr[end] == 0:
            zero_count += 1
        while zero_count > k:
            if arr[start] == 0:
                zero_count -= 1
            start += 1
        max_len = max(max_len,(end-start)+1)
    return max_len



if __name__ == '__main__':
    #print(maxsubstr('abcabcbbcabcdefgh'))
    # print(maxsubstr_opt('abcabcbbcabc'))
    # print(arraysum([1,2,1,1],2))
    #print(atmost_kzeros([1,0,1,1,0],1))
    # print(min_len([1,1,1],k=3))
    # print(dist_ele('aa',2))
    # print(count_sub_k_odd([2,4,6],1))
    # print(long_increse_subarr([5,4,3]))
    print(max_flip([0,1,1,0],1))
