# 변수의 선언
var = 42

print(var)  
print(var + 10)
print(var - 5)
print(var / 10)
print(var // 10)
print(var % 10)

var2 = var / 10

print(var > var2)  

var_float = 3.14

print(var_float * 6)  
print(var_float / 2)  

result = var * 10 + 5
print(result)
result = 5 + var * 10
print(result)
result = (5 + var) * 10
print(result)

is_true = True
is_false = False

print(is_true and is_true)
print(is_true and is_false)
print(is_false and is_false)

print(is_true or is_true)
print(is_true or is_false)
print(is_false or is_false)