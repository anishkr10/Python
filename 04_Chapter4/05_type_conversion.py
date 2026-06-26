# Type Conversion : Type conversion is the process of changing one data type into another data type.

a = "12"
b = int (a)

print(type(a))
print(type(b))


# you can convert strings if its holds valid integer

# c = "12.5"
# c = int(c)

# print(c)

# convert sting to float

d = "12.4"
d = float(d)

print(d)

# convert int into float

e = 15
e = float(e)

print(e)


f = 12
g = 0
h = 12.4
i = 0.0
j = ""
k = "hello"

print(bool(f))
print(bool(g))
print(bool(h))
print(bool(i))
print(bool(j))
print(bool(k))

# 7 Value → False

# 1. False
# 2. 0
# 3. 0.0
# 4. “”
# 5. []
# 6. ()
# 7. {}

# Implicit Conversion : Implicit type conversion is the process of converting one data type into another data type without any user involvement. It is also known as type casting.

a = 10
b = (a/2)

print(b) 