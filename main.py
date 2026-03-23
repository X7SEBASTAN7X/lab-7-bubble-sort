def bubble_sort(array):
    n = len(array)
    for _ in range(n):
        for i in range(n-1):
            if array[i]>array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]        

    return array


ml1 = [0,1,4,2,9,7,-1,0,-9,0,100,-5,-6]
print(bubble_sort(ml1))


if __name__=='__main__':
    print('Hi')