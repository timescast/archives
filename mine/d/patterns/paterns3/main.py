
from re import M
from sys import prefix


def prefix_lr(arr,l,r):
    prefix = []
    curr_sum = 0
    for x in arr:
        curr_sum += x
        prefix.append(curr_sum)
    if l == 0:
        return prefix[r]
    return prefix[r] - prefix[l-1]

def cumul_summ_arr(arr):
    prefix = [0]*len(arr)
    prefix[0] = arr[0]
    for i in range(1,len(arr)):
        prefix[i] = prefix[i-1]+arr[i]
    return prefix

def sumfirstn(arr,n):
    prefix = [0]*len(arr)
    prefix[0] = arr[0]
    for i in range(1,len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    if n == 0:
        return prefix[0]
    return prefix[n-1]

def maximumprefixsum(arr):
    prefix = [0]*len(arr)
    prefix[0] = arr[0]
    for i in range(1,len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    return max(prefix)

def bal_indx_check(arr):
    prefix = [0]*len(arr)
    prefix[0]=arr[0]
    for i in range(1,len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    for i in range(len(prefix)):
        if prefix[i] == sum(arr)-arr[i]:
            return True
    return False

class MulSubSum:
    def __init__(self,arr):
        self.prefix = [0]*len(arr)
        self.prefix[0] = arr[0]
        for i in range(1,len(arr)):
            self.prefix[i] = self.prefix[i-1] + arr[i]
    def query(self,tple):
        print(tple)
        rarr = []
        for t in tple:

            l,r = t[0],t[1]
            if l == 0:
                rarr.append(self.prefix[r])
                continue
            rarr.append(self.prefix[r]-self.prefix[l-1])
        return rarr

def equilibrium(arr):
    n = len(arr)
    for i in range(n):
        leftsum = sum(arr[i:])
        rightsum = sum(arr[i+1:])
        if leftsum == rightsum:
            return i
    return -1

def equlasplit(arr):
    n = len(arr)
    prefix = [0]*n
    prefix[0] = arr[0]
    for i in range(1,n):
        prefix[i] = arr[i] + prefix[i-1]
    total_sum = prefix[-1]
    for i in range(n-1):
        if prefix[i] == total_sum - prefix[i]:
            return i
    return -1 

def prefixsumdiff(arr,L,R):
    n = len(arr)
    prefix = [0]*n 
    prefix[0] = arr[0]
    for i in range(1,n):
        prefix[i] = arr[i] + prefix[i-1]
    return prefix[R] - prefix[L]

def validlong(arr,K):
    n = len(arr)
    prefix = [0]*n
    prefix[0] = arr[0]
    for i in range(1,n):
        prefix[i] = prefix[i-1]+arr[i]
    for i in range(n):
        if prefix[i] > K:
            return i
def cumlvl(arr):
    n = len(arr)
    prefix = [0]*n
    prefix[0] = arr[0]
    s = set()
    for i in range(1,n):
        prefix[i] = arr[i] + prefix[i-1]
        s.add(prefix[i])
    print(prefix,s)
    return n - len(s)

class meanofquery:
    def __init__(self,arr):
        n = len(arr)
        self.prefix = [0]*n
        self.prefix[0] = arr[0]
        for i in range(1,n):
            self.prefix[i] = arr[i] + self.prefix[i-1]
    def query(self,query):
        cul = 0
        rarr = []
        for q in query:
            l,r = q[0],q[1]
            if l-1 == 0:
                rarr.append(self.prefix[r-1]//r)
                continue
            cul = self.prefix[r-1]-self.prefix[l-1-1]
            print(cul)
            no = r-l + 1
            rarr.append(cul//no)
        return rarr

def presum(arr):
    n= len(arr)
    presum = [0]*n
    presum[0] = arr[0]
    for i in range(1,n):
        presum[i] = arr[i] - arr[i-1]
        print(presum)
    return presum

def productarray(arr):
    n = len(arr)
    res = [0]*n
    prefix_product = [1]*n
    sufix_product = [1]*n
    for i in range(1,n):
        prefix_product[i] = arr[i-1]*prefix_product[i-1]
    for j in range(n-2,-1,-1):
        print(j)
        sufix_product[j] = arr[j+1]*sufix_product[j+1]
    print(prefix_product,sufix_product)
    for k in range(n):
        res[k] = prefix_product[k]*sufix_product[k]
    return res

def maxsubarray(arr,k):
    maxsubarr = []
    sum = 0
    l = []
    for i in range(len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum += arr[j]
            if sum == k:
                maxsubarr.append(arr[i:j+1])
                l.append(len(arr[i:j+1]))
    return maxsubarr,max(l)


if __name__ == "__main__":
    #print(prefix_lr([3,5,7,9], 0,2))
    #print(cumul_summ_arr([3,1,4]))
    #print(sumfirstn([1,2,3,4,5],4))
    #print(maximumprefixsum([1,2,-5,4]))
    #print(bal_indx_check([1,2,3]))
    #pf_arr = MulSubSum([2,4,6,8])
    #print(pf_arr.query(((1,3),(0,1))))
    #print(equilibrium([1,1,1,1]))
    # print(equlasplit([1, 2, 3, 4, 5, 5]))
    # print(prefixsumdiff([3,1,4,2],1,3))
    #print(validlong([2,3,5,4],7))
    # print(cumlvl([1,-1,1,-1]))
    # prefix=meanofquery([3, 7, 2, 8, 5])
    # print(prefix.prefix)
    # print(prefix.query([[1,3],[2,5]]))
    # print(presum([5, 7, 10, 11, 18]))
    # print(productarray([1,2,3,1,2,3]))
    # print(productarray([10,3,5,6,2]))
    print(maxsubarray([10, 5, 2, 7, 1, -10],15))
