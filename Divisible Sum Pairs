def divisibleSumPairs(n, k, ar):
    # Write your code here
    
    count=0
    stat=0
    summ=0
    while count<=n:
        for j in range(n-count-1):
            summ=ar[count]+ar[j+count+1]
            if summ%k==0:
                stat+=1
        count+=1
    return stat
