my_list = [10, 20, 30, 40, 50]
my_list.append(60)  # 리스트에 요소 추가

print(my_list)
print(len(my_list))  # 리스트의 길이
print(my_list[4])

sliced = my_list[3:]  # 리스트 슬라이싱
print(sliced)


fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("banana" in fruits)  # 요소 존재 여부 확인


numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # 리스트 정렬
print(numbers)
numbers.reverse()  # 리스트 뒤집기
print(numbers)

my_list.extend([70, 80])  # 리스트 확장
print(my_list)

print(my_list[-1])

multi_list = [0,1,3] * 3
print(multi_list)

del my_list[2]  # 리스트에서 요소 삭제
print(my_list)

max_value = max(my_list)  # 리스트에서 최대값 찾기
print(max_value)
min_value = min(my_list)  # 리스트에서 최소값 찾기
print(min_value)