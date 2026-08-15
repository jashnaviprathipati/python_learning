# ==============================
# DATATYPES
# ==============================

# 1. int
a = 10
print(a, type(a))

# 2. float
b = 10.5
print(b, type(b))

# 3. complex
c = 2 + 3j
print(c, type(c))

# 4. bool
d = True
print(d, type(d))

# 5. NoneType
e = None
print(e, type(e))

# 6. string
f = "Jashnavi"
print(f, type(f))

# 7. range
g = range(1, 6)
print(g, type(g))

# 8. list
h = [10, 20, 30]
print(h, type(h))

# 9. tuple
i = (10, 20, 30)
print(i, type(i))

# 10. set
j = {10, 20, 30}
print(j, type(j))

# 11. dict
k = {"name": "Jashnavi", "age": 25}
print(k, type(k))


# ==============================
# TYPE CONVERSION
# ==============================

# int to float
x = 10
y = float(x)
print(y, type(y))

# float to int
x = 10.5
y = int(x)
print(y, type(y))

# int to string
x = 100
y = str(x)
print(y, type(y))

# string to int
x = "50"
y = int(x)
print(y, type(y))

# list to tuple
x = [1, 2, 3]
y = tuple(x)
print(y, type(y))

# tuple to list
x = (1, 2, 3)
y = list(x)
print(y, type(y))

# list to set
x = [1, 2, 2, 3]
y = set(x)
print(y, type(y))

# range to list
x = range(1, 6)
y = list(x)
print(y, type(y))