def find_maximum_subarray(A,low,high):
    if high==low:
        return (low,high,A[low])

    else:
        mid = int((low+high)/2)
        left_low,left_high,left_sum = find_maximum_subarray(A,low,mid)
        right_low,right_high,right_sum = find_maximum_subarray(A,mid+1,high)
        cross_low,cross_high,cross_sum = find_max_crossing_subarray(A,low,mid,high)
        if left_sum>=right_sum and left_sum>=cross_sum:
            return (left_low,left_high,left_sum)
        if right_sum>=left_sum and right_sum>=cross_sum:
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)


def find_max_crossing_subarray(A,low,mid,high):
    left_sum=0
    max_left=-1
    sum=0
    i=mid
    for i in reversed(range(low,i+1)):
        sum = sum+A[i]     
        if sum>left_sum:
            left_sum=sum
            max_left = i

    right_sum=0
    max_right=-1
    sum=0
    j=mid+1
    for j in range(j,high+1):
        sum = sum+A[j]
        if sum>right_sum:
            right_sum = sum
            max_right=j

    return (max_left,max_right,left_sum+right_sum)

A = [1,2,3,-4,-5,-6,7,8,9]
t = find_maximum_subarray(A,0,len(A)-1)
print(t)
