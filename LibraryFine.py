def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    fine=0
    if d1<=d2 and m1<=m2 and y1<=y2:
        fine=0
    if d1>d2 and m2==m1 and y2==y1:
        fine=15*(d1-d2)
    if m1>m2 and y1==y2:
        fine = 500*(m1-m2)
    if y1>y2:
        fine =10000
    return fine
