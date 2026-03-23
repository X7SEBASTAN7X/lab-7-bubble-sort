def bubble_sort(array):
    n = len(array)
    for _ in range(n):
        for i in range(n-1):
            swap = False
            if array[i]>array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
                swap = True
            # if swap == False: 
        #     print('Ended early')
        #     break
    return array


ml1 = [0,1,4,2,9,7,-1]
print(bubble_sort(ml1))


if __name__=='__main__':
    print('Hi')