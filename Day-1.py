x = 10
y = x

# to see the memory given to the object in heap memory
# example for x = 2304127009296, y = 2304127009296
print(id(x))
print(id(y))

# writing a string multiple times
string = "hey!!" * 5
print(string)

# working with strings
# string are immutable in python
x = "Hello"
print(len(x))  # 5

y = x[0]
print(y)  # H


# substrings in python

n = "0123456789"
# it'll remove last argument -1
# therefore 8-1 = 7,  so it'll print numbers till 7
p = n[3:8]  # "34567"
print(p)

q = n[3:9:1]  # third argument here is step value.
print(q)  # 345678
r = n[3:9:2]  # step value is of 2, so  it'll skip 1 number
print(r)  # 357
# we can also use negative numbers for step value

s = n[5:1:-1]
print(s)  # 5432
# negative step values will return string in opposite direction

# more examples for strings

n1 = n[1::2]
print(n1)  # 13579
# this might run for infinity, it'll just skip 1 number till there's nothing
# much left to print

m1 = n[9::-1]
print(m1)  # 9876543210
# it'll just print numbers in opposite direction

# other way to execute upper example
m2 = n[::-1]
print(m2)  # 9876543210
# here it will start rom the last possible value available

# Escape characters, will look into it later.
# \n
# sep = " "
# used to separate values

# type casting (converting one type of data into other type)
x = 10;
y = "05"
print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
# x1 = 1.52 # float
# never convert large data type to weaker one, it causes data loss
# Example, never convert int to float
num = int(float("2.64"))
print(num) # 2
# to convert a string to float we should, convert it into integer first,
# then we can convert it into float

# c = "hey!"
# float(c)
# print(c)
# also we can't convert a string to a number (int or float)
