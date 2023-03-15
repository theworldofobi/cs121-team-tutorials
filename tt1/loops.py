"""
Module #1 Simple Practice: Lists and Loops
from: https://classes.cs.uchicago.edu/archive/2021/fall/12100-1/tutorials/tt1/index.html
"""

### Lists
lst0 = []
lst1 = [1, "abc", 5.7, [1, 3, 5]]
lst2 = [10, 11, 12, 13, 14, 15, 16]
lst3 = [7, -5, 6, 27, -3, 0, 14]
lst4 = [0, 1, 1, 3, 2, 4, 6, 1, 7, 8]

# Task 1 
lst5 = [7, "xyz", 2.7]

# Task 2 - predicted result = 4
len(lst1)

# Task 3 - retrieving 5.7 from lst1
lst1[2]

# Task 4 - predicted result = IndexError (out of range)
# lst1[4]

# Task 5 - predicted result = 16
lst2[-1]

# Task 6 - retrieving 5 from list in lst1
lst1[3][2]
lst1[-1][-1]

# Task 7 - change list values
lst1[3][1] = 15.0

# Task 8 - slice items 1-5 in lst2
lst2[1:6]

# Task 9 - slice items 0-2 in lst2
lst2[:3]

# Task 10 - slice items 1-end in lst2
lst2[1:]

# Task 11
lst0.extend([3, 5, 7, 2])
lst0[3]
lst0[-2]

# Task 12
nl = lst2 + lst3
nl[4] = 12

### Loops

# Task 13
all_pos = True

for val in lst3:
    if val < 0:
        all_pos = False
        break

# Task 14
pos_only = []

for val in lst3:
    if val > 0:
        pos_only.append(val)

# Task 15
is_pos = []

for val in lst3:
    if val > 0:
        is_pos.append(True)
    else:
        is_pos.append(False)
        
# Task 16
# lst4 = [0, 1, 1, 3, 2, 4, 6, 1, 7, 8]
max_num = max(lst4)
counts = [0] * max_num

for v in lst4:
    counts[v] += 1