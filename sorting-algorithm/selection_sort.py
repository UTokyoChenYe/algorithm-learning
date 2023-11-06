def selection_sort(alist):
    n = len(alist)

    for i in range(n-1):
        min_index = i

        #找到最小值的下表
        for j in range(i+1,n):
            if alist[j] < alist[min_index]:
                min_index = j
        
        #交换
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]

alist = [54,26,93,17,77,31,44,55,20]
selection_sort(alist)
print(alist)