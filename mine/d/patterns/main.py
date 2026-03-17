 
def findp(lst):
    if lst[0] >= lst[1]:
        large = lst[0]
        slarge = lst[1]
    else:
        large = lst[1]
        slarge = lst[0]
    for i in range(2,len(lst)):
        if lst[i] > large:
            slarge = large
            large = lst[i]
        elif lst[i] > slarge and lst[i] != large:
            slarge = lst[i]
    return slarge


def findmissing(arr):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(i)
    for i in range(len(arr)):
        if new_arr[i] not in arr:
            return new_arr[i]
        
def count_even(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            count += 1
    return count

def remove_n(arr,k):
    c = 0
    i = 0
    n = len(arr)
    new_arr = []
    for i in range(n):
        if arr[i] != k:
            new_arr.append(arr[i])
    return len(new_arr)

def max_subarr(arr):
    c_arr = []
    for i in range(len(arr)):
        c = arr[i]
        for j in range(i+1,len(arr)):
            c += arr[j]
        c_arr.append(c) 
    return max(c_arr)

def maj_elem(arr):
    count = []
    for i in range(len(arr)):
        c = 1
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                c += 1
        count.append(c)
    for c in range(len(count)):
        if count[c] > len(arr)/2:
            return arr[c]
    return None

def plusone(arr):
    new_arr = []
    st = ""
    for i in range(len(arr)):
        st+=f"{arr[i]}"
    i = int(st)
    i += 1
    st = str(i)
    for i in range(len(st)):
        new_arr.append(int(st[i]))
    return new_arr

def disap(arr):
    d = []
    for i in range(len(arr)):
        if i not in arr and i !=0:
            d.append(i)
    return d

def findcount(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count


def repeatelem(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1
    for i in arr:
        if count[i]>1:
            return i
    return count

def checkanagram(str1,str2):
    count1 = {}
    count2 = {}
    for s in str1:
        if s in count1:
            count1[s] +=1
        else:
            count1[s] = 1
    for s in str2:
        if s in count2:
            count2[s] += 1
        else:
            count2[s] = 1
    if count1 == count2:
        return True 
    else:
        return False
def maxfreq(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    big  = count[arr[0]]
    for c in count:
        if count[c] > big:
            big = count[c]  
    for c in count:
        if count[c] == big:
            return c

def finddups(arr):
    count = {}
    arr2= []
    for i in arr:
        if i in count:
            count[i] += 1
            arr2.append(i)
        else:
            count[i] = 1
    return arr2  

def oddappr(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    arr = []
    for c in count:
        if count[c] % 2 != 0:
            arr.append(c)
    return arr

def checksub(arr1,arr2):
    count1 = {}
    count2 = {}
    for i in arr1:
        if i in count1:
            count1[i] +=1
        else:
            count1[i] = 1
    for i in arr2:
        if i in count2:
            count2[i] += 1
        else:
            count2[i] = 1
    for i in range(len(count2)):
        for c in count2:
            if count2[c] != count1.get(c,None):
                return False
    return True
def nonrepeat(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1
    for c in count:
        if count[c] == 1:
            return c
if __name__ == "__main__":
    #print(findp([10,3,4,5]))
    #print(findmissing([0,1,2,4]))
    #print(count_even([1,2,4,46]))
    #print(remove_n([0,1,2,2,3,0,4,2],2))
    #print(max_subarr([5,4,-1,7,8]))
    #print(maj_elem([2,2,1,1,1,2,2]))
    #print(plusone([9,9,9]))
    #print(disap([4,3,2,7,8,2,3,1]))
    #print(findcount([1,2,2,3,1]))
    #print(repeatelem([10,5,3,4,3,5,6]))
    #print(checkanagram("anagram","nagaram"))
    #print(maxfreq([1,2,2,3,5,5,5]))
    #print(finddups([1,1,2]))
    #print(oddappr([4,4,5]))
    #print(checksub([1,2,3,4],[2,4]))
    #print(nonrepeat([1,2,2,1,3]))