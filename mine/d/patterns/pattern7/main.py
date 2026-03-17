class mergeIntervals:
    def merge_intervals(intervals):
        intervals.sort(key=lambda i:i[0])

        output = [intervals[0]]

        for start , end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd,start)
            else:
                output.append([start,end])
        return output

def min_diff(arr):
    arr.sort()
    n = len(arr)
    r = n-1
    l = 0
    min_num = 1000
    while l < r:
        left_diff = abs(arr[l+1]-arr[l])
        right_diff = abs(arr[r]-arr[r-1])
        
        if left_diff<right_diff:
            min_num = min(min_num,left_diff)
            r -= 1
        else:
            min_num = min(min_num,right_diff)
            l+= 1

    return min_num

def closestToK(arr,k):
    arr.sort()
    l = 0
    n = len(arr)
    r = n -1
    min_diff = float('inf')
    res = []
    while l<r:
        curr_sum = arr[l] + arr[r]
        if abs(k-curr_sum) < min_diff:
            res = [arr[l],arr[r]]
            min_diff = abs(curr_sum-k)
        if curr_sum<k:
            l += 1
        if curr_sum>=k:
            r -= 1
    return res

def assign_cookies(g,s):
    s.sort()
    g.sort()
    n = len(s)
    m = len(g)
    sPointer = 0
    gPointer = 0
    count = 0
    while sPointer<n and gPointer < m:
        if gPointer >= sPointer:
            gPointer += 1
            count += 1
        sPointer += 1
    return count

def overlap_interval(intervals):
    intervals.sort(key=lambda i:i[0])
    output = [intervals[0]]
    count = 0
    for start ,end in intervals[1:]:
        lastEnd = output[-1][1]
        if lastEnd >= start:
            count += 1
            output[-1][1] = max(lastEnd,end)
        else:
            output.append([start,end])
    return output,count

def can_attend(intervals):
    intervals.sort(key=lambda i:i[0])
    output = [intervals[0]]
    for start ,end in intervals[1:]:
        lastEnd = output[-1][1]
        if start < lastEnd:
            output[-1][1] = end
            return False
        else:
            output.append([start,end])
    return output

def findPlatform(arr, dep):
    arr.sort()
    dep.sort()

    platforms_needed = 0
    max_platforms = 0
    i = 0   
    j = 0  
    n = len(arr)

    while i < n:
        if arr[i] <= dep[j]:
            platforms_needed += 1
            i += 1
        else:
            platforms_needed -= 1
            j += 1
        
      
        max_platforms = max(max_platforms, platforms_needed)

    return max_platforms



if __name__ == '__main__':
    # print(findPlatform(arr=[900,905],dep=[920,930]))
    # print(mergeIntervals.merge_intervals([[1,3],[2,6],[8,10]]))
    # print(min_diff([1,1,1]))
    # print(closestToK([1,2,3,8],5))
    # print(assign_cookies([1,2,3,5],[1,2,4,3]))
    # print(overlap_interval([[1,5],[2,3]]))
    #print(can_attend( [[0,30],[5,10]]))
    