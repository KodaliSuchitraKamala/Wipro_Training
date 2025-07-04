''' program to print the next 10 day dates continuously '''
from datetime import *
d = date.today()
print(d)
for x in range(1, 10):
    nextdate = d + timedelta(days = x)
    print(nextdate)
