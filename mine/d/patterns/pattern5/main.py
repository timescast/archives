from numpy import mean
from sympy import product


def maxsubarr(arr,k):
    rarr = {}
    res = 0
    for i in range(len(arr)-k+1):
        val = sum(arr[i:i+k])
        res = max(val,res)
        rarr[val]= arr[i:i+k]
    return rarr[res],res



def avg(arr,k):
    summ = 0
    for i in range(len(arr)):
        summ += arr[i]
    return summ/k
def avgsubarr(arr,k):
    rarr = []
    for i in range(len(arr)-k+1):
        # val =mean(arr[i:i+k])
        avg_val = avg(arr[i:i+k],k)
        rarr.append(avg_val)
    return rarr

def grtsum(arr,k,x):
    count = 0
    for i in range(len(arr)-k+1):
        if x < sum(arr[i:i+k]):
            count += 1
    return count

def max_vowels(string,k):
    vowels = ["a","e","i","o","u"]
    count = 0
    
    for i in range(len(string)-k+1):
        wcount = 0
        for j in string[i:i+k] :
            if j in vowels:
                wcount += 1
        count = max(wcount,count)
    return count 


def negval(arr,k):
    n = len(arr)
    rarr = [0]*n
    for i in range(len(arr)-k+1):
        for j in arr[i:i+k]:
            if j < 0:
                rarr[i] = j
    return rarr

def small_sum(arr,k):
    res = 1000000
    rarr = {}
    for i in range(len(arr)-k+1):
        val = sum(arr[i:i+k])
        rarr[val] = arr[i:i+k]
        res = min(res,val)
    return rarr[res]

def count_even(arr,k):
    rarr = {}
    count = 0
    max_count = 0
    for i in range(len(arr)-k+1):
        count = 0
        for j in arr[i:i+k]:
            if j % 2 == 0:
                count += 1
                rarr[count] = arr[i:i+k]
                max_count = max(count,max_count)
                print(count,max_count)
    return rarr[max_count]


def max_product(arr,k):
    rarr = {}
    max_prod = 0
    for i in range(len(arr)+k-1):
        prod = 1
        for j in arr[i:i+k]:
            prod *= j
            rarr[prod] = arr[i:i+k]
        max_prod = max(prod,max_prod)
    return rarr[max_prod],max_prod


###############################################################################################



def max_sum_fixed(arr,k):
    curr_sum = sum(arr[:k])
    max_sum = curr_sum
    for i in range(len(arr)-k):
        curr_sum = curr_sum - arr[i] + arr[i+k]
        max_sum = max(curr_sum,max_sum)
    return max_sum


def avg_sum_fixed(arr,k):
    curr_sum = sum(arr[:k])
    avg_sum = curr_sum/k
    rarr = []
    rarr.append(avg_sum)
    for i in range(len(arr)-k):
        curr_sum = curr_sum - arr[i] + arr[i+k]
        rarr.append(curr_sum/k)
    return rarr

def num_big_fixed(arr,k,x):
    curr_sum = sum(arr[:k])
    count = 0
    if curr_sum > x:
        count += 1
    for i in range(len(arr)-k):
        curr_sum = curr_sum - arr[i] + arr[i+k]
        if curr_sum > x:
            count += 1
    return count 

def max_vowels_2(st,k):
    vowels = set('aeiou')
    count = sum(c in vowels for c in st[:k])
    max_count = count
    for i in range(k,len(st)):
        print(st[i])
        print(st[i-k])
        if st[i] in vowels:
            count += 1
        if st[i-k] in vowels:
            count -= 1
        max_count = max(count,max_count)
    return max_count


def first_negative(arr,k):
    fn_idx = 0
    res = []
    n = len(arr)
    for i in range(k-1,n):
        while fn_idx < i and (fn_idx <= i-k or arr[fn_idx]>=0):
            
            fn_idx += 1
            if fn_idx < n and arr[fn_idx]< 0:
                print(fn_idx)
                res.append(arr[fn_idx])
            else:
                res.append(0)
    return res

def min_size(arr,k):
    curr_sum = sum(arr[:k])
    rarr = []
    rarr.append(curr_sum)
    for i in range(len(arr)-k):
        
        val  = curr_sum - arr[i] + arr[k+i]
        curr_sum = min(val,curr_sum)
    return curr_sum

def max_even(arr,k):
    count = 0
    for num in arr[:k]:
        if num%2 == 0:
            count += 1  
    max_count = 0
    for i in range(len(arr)-k):
        print(f'count--{count} i ---{i}')
        if arr[i+k] % 2 == 0:
            count += 1
        if arr[i] % 2 == 0:
            count -=1
        max_count = max(count,max_count)
    return max_count

def max_prod(arr,k):
    prod = 1
    for p in range(len(arr[:k])):
        prod *= arr[p]
    max_prod = prod
    for i in range(len(arr)-k):
        prod = prod * arr[i+k]
        prod = prod // arr[i]
        max_prod = max(prod,max_prod)
    return max_prod
    

if __name__ == '__main__':
    # print(first_negative([2,-1,3,-4,5],2))
    # print(min_size([3,3,3],2))
    # print(max_even([2,4,6],2))
    # print(max_prod([2,2,2],2))
    # print(longest_sub('abc'))
    # print(max_vowels_2('leetcode',2))
    # print(maxsubarr([2,1,5,1,3], 2))
    # print(avgsubarr([5,5],2))
    # print(grtsum([4,4,4],2,7))
    # print(max_vowels('aeiou',2))
    # print(negval([2,-1,3,-4,5],k=2))
    # print(small_sum([3,3,3],2))
    # print(count_even([1,2,4,5,6],3))
    # print(max_product([1,2,3,4],2))
    # print(max_sum_fixed([2, 1, 5, 1, 3, 2], 3))
    # print(avg_sum_fixed([1,2,3,4],2))
    # print(num_big_fixed([1,3,2,6],2,4))

