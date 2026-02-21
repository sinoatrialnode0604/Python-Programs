import pandas as pd

a = pd.Series([20,30,40])

print(a)

#accessing elements

print(a[2])

#using positional and locational index.

b = pd.Series([23,24,25,26],index= ['a','b','c','d'])
print(b['d'])

#methods

#head(n)

print(a.head(1))

#count(n)

print(a.count())

#tail(n)

print(a.tail(2))