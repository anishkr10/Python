a = "COLLEGE"

print(a[3:6:1]) # Output: LEG

# C O L L E G E
# 0 1 2 3 4 5 6 

# [3:6:1]
# 3 -> Starting index
# 6 -> Ending index
# 1 -> Step value

b = "COLLEGE"

# OUTPUT: C L E E
print(b[0:7:2])

print(b[::2]) # it is also same as b[0:7:2] because by default starting index is 0 and ending index is length of string and step value is 1
# Input 

# C O L L E G E
# 0 1 2 3 4 5 6

#[0:7:2]

# 0 -> Starting index
# 7 -> Ending index because we want to include the last character
# 2 -> Step value
