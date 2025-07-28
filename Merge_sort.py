def merge_sort(arr,left,right):
    if len(arr)<=1:
        return arr
    mid=(left+right)//2
    left_half=merge_sort(arr[:mid])
    right_half=merge_sort(arr[mid:])
    return merge
def merge(left,right):
    merged=[]
    i=0
    j=0
    while i <len(left) and j<len(right):
        if left[i]<=right[j]:
            merged.append(left[i])
            i+=1
        else:
           merged.append(right[j])
           j+=1
    
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged