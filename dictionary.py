my_dict = {}
my_dict["key"] = "value"  # 딕셔너리에 키-값 쌍 추가

person = {
  "name": "홍길동",
  "age": 30,
  "city": "서울"
}
name = person["name"]  # 딕셔너리에서 값 가져오기
print(name)

print(f"이름은 {person['name']}이고, 나이는 {person['age']}세이며, 도시는 {person['city']}입니다.")

country = person.get("country", "정보 없음")  # 키가 없을 때 기본값 반환
print(country)

person["age"] = 35  # 딕셔너리에서 값 수정
print(person)

person["country"] = "대한민국"  # 딕셔너리에 새로운 키-값 쌍 추가
print(person)

print(person.keys())  # 딕셔너리의 모든 키
print(person.values())  # 딕셔너리의 모든 값
print(person.items())  # 딕셔너리의 모든 키-값 쌍