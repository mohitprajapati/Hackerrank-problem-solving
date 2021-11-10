def jumpingOnClouds(c):
    # Write your code here
    count=0
    i=0
    if len(c)==1:
        return 0
    if len(c) == 2: return 0 if c[1]==1 else 1
    while(i<=len(c)-1):
        if c[i]!=1:
            
            
            if (i+2)<len(c):
                if c[i+1]!=1 and c[i+2]!=1:
                    count+=2
                    i+=3
                else:
                    i+=1
                    count+=1
            else:
                i+=1
                count+=1
        else :
            i+=1
        
    return count-1
