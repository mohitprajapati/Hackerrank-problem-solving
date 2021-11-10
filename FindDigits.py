# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    num=n
    cnt=0
    while(num>0):
        digit=num%10
        if digit!=0:
            if n%digit==0:
                cnt+=1
        num//=10
    return cnt
