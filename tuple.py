my_tuple = (1,)

# 과일 바구니
fruit_basket = ("apple", "banana", "cherry", "date", "elderberry")
print(fruit_basket)
print(fruit_basket[1])  # 인덱싱
print(fruit_basket[-1])  # 음수 인덱싱
print(fruit_basket[1:4])  # 슬라이싱

# 패킹과 언패킹
tp = 1, 2, 3  # 패킹
print(tp)
v1, v2, v3 = tp  # 언패킹
print(v1, v2, v3)

a = 10
b = 20

temp = a
a = b
b = temp

a, b = b, a  # 파이썬의 스왑 기능
print(a, b)

tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
val1, val2, val3, *rest = tp  # 언패킹과 나머지 요소를 리스트로 받기
print(val1, val2, val3)
print(rest)

