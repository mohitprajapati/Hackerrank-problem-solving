# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    # k==jump distance 
    i=k
    energy=100
     
    while(1):
        if c[i]==0:
            energy=energy-1
        if c[i]==1:
            energy=energy-1-2
        if i==0:
            return energy
        i+=k
        if i>=len(c):
            i=i-len(c)
