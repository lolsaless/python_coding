# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일때 + 음수일때 -
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

print("왼쪽 정렬하고, 빈칸으로 _로 채움")
print("{0:_<+10}".format(-500))
print("{0:_<+10}".format(500))
print("{0:_<10}".format(+500))

print("3자리 마다 콤마를 찍어주기")
print("{0:,}".format(1000000000000000))

print("3자리 마다 콤마를 찍어주기, +- 부호도 붙이기")
print("{0:+,}".format(-1000000000))
print("{0:+,}".format(+1000000000))

print("3자리 마다 콤마를 찍어주기, +- 부호도 붙이고, 자리수도 확보하기")
print("돈이 많으면 행복하니까 빈자리는 ^ 로 표시하기")
print("{0:^<+30,}".format(10000000000000))

print("소수점 출력")
print("{0:f}".format(5/3))
print("소수점을 트겅 자리수 까지만 출력")
print("{0:.2f}".format(5/3))