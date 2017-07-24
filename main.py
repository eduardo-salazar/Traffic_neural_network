import tensorflow as ts

#Create contants
x1 = ts.constant([1,2,3,4])
x2 = ts.constant([5,6,7,8])

# Multiply
result = ts.multiply(x1,x2)

print(result)
