#Erfan Nouhi
#W3schools

def bubble_sort_one(arr):
    length = len(arr)

    for i in range(length):
        for j in range(length-1):#avoid index out of range error
            if arr[j] > arr[j+1]:
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp


def bubble_sort_two(arr):
    length = len(arr)

    for i in range(length-1):#enough to sort array with this length 
        for j in range(length-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp



def bubble_sort_three(arr):
    length = len(arr)
    for i in range(length-1):#enough to sort array with this length
        for j in range(length-1-i):#each time the the largest at traversing bubbles up so less cycles
            if arr[j] > arr[j+1]:
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp

arr = [12,34,354,25,3235,6,5,34]
print(arr)
bubble_sort_three(arr)
print(arr)
