def bubble_sort(array):
    n = len(array)
    print('Starting Bubble Sort')
    for ps in range(n):
        swapped = False
        for i in range(n-1):
            for num in array:
                [print('#',end='') for _ in range(1,num+1)]
                print()
            if array[i]>array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]  
                swapped = True
        if not swapped:
            break
    return array


ml1 = [0,1,4,2,9,7,-1,0,-9,0,100,-5,-6]
print(bubble_sort(ml1))


if __name__=='__main__':
    print('Hi')