# 문자열 변수 선언

str_var = "This is my python code."
multi_line = """I', a developer, am learning Python.
It's fun and rewarding!
I hope to become proficient in it."""

print(str_var)
print(multi_line)

inum1 = 12
inum2 = 34
print(inum1 + inum2)  # 정수 덧셈


num1 = "12"
num2 = "34"
print(num1 + num2)  # 문자열 덧셈 (연결)
print(num1 * 3)  # 문자열 반복

# 인덱싱
print(str_var[11])
print(str_var[-1])
print(str_var[-5])

# 슬라이싱
print(str_var[11:17])
print(str_var[11:-6])
print(str_var[:10])

# 문자열 변수 선언
print(str_var.isalpha()
      )
num_var = "12"
print(num_var.isdecimal())

print(str_var.upper())
print(str_var.lower())
print(str_var.swapcase())
print(str_var.replace("my", "your"))

# Format String
weather = "흐림"
temp = 15.8

# % code
print("오늘의 날씨는 %s이고, 온도는 %.1f도입니다." % (weather, temp))

# .format() 
print("오늘의 날씨는 {}이고, 온도는 {}도입니다.".format(weather, temp))

# f""
print(f"오늘의 날씨는 {weather}이고, 온도는 {temp}도입니다.")

# 사용자로부터 문자열 입력받기
num = input("숫자를 입력하세요:")
print("입력한 숫자는:", num)
print("입력한 숫자 + 10:", int(num) + 10)