def cutTheSticks(arr):
    # Write your code here
    lst=[]
    while(len(arr)>0):
        arr.sort()
        smallest=arr[0]
        #print(len(arr1))
        lst.append(len(arr))
        i=0
        arr = [i for i in arr if i != smallest]
        for i in range(len(arr)):
            arr[i]-=smallest
