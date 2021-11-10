def squares(a, b):
    # Write your code here
    lst=[]
    cnt=0
    
    sqrtA = math.ceil(math.sqrt(a))
    sqrtB = math.floor(math.sqrt(b))
    
    return sqrtB - sqrtA + 1
