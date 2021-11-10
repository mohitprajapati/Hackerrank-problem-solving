# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    day=0
    if year>1917: # Gregorian calender 
        if (year%4==0 and year%100!=0) or year%400==0 :
            day=256-244 
            month='09'
        else:
            day=256-243
            month='09'
    else:
        if year%4==0:
            day=256-244 
            month='09'
        else:
            day=256-243
            month='09'
            
    return str(day)+'.'+month+'.'+str(year)
