def insert_sort(alist):
    n = len(alist)

    '''
    for i in range(1,n):
        for j in range(i,0,-1): #这里其实不太对，应该是遇到换不动了就要停下来
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
    '''

    for i in range(1,n):

        j = i - 1 #这个实现更好，因为一旦遇到换不动了就停下来了
        while j >= 0 and alist[j] > alist[j+1]:
            alist[j], alist[j+1] = alist[j+1], alist[j]
            j -= 1

alist = [54,26,93,17,77,31,44,55,20]
insert_sort(alist)
print(alist)