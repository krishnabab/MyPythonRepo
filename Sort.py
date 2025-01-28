print("Testing a sorting function")
#code for bubble sort
Array = [64, 34, 25, 12, 22, 11, 90]
print("Original Array: ", Array)
for i in range(len(Array)):
    for j in range(len(Array)-i-1):
        if Array[j] > Array[j+1]:
            Array[j], Array[j+1] = Array[j+1], Array[j]
print("Sorted Array: ", Array)