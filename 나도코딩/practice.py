station1 = '사당'
station2 = '신도림'
station3 = '인천공항'

print(station1 + '행 열차가 들어오고 있습니다.')

print(3-2)
print(5*3)

print(1 != 3) #True
print(not(1 != 3)) #False

print((3>0) and (3 < 5)) #True
print((3 > 0 ) & (3 < 5))
print((3>0) or (3>5)) #둘중 하나라도 만족하면 True

print(16%5)


#숫자처리함수
print(abs(-5)) #5
print(pow(4,2)) #4^2 = 4*4 = 16
print(max(5,12))
print(min(5,12))
print(round(3.14))

from math import *
print(floor(4.99)) #내림
print(ceil(3.14)) #올림
print(sqrt(16)) #제곱근 4

#랜덤 라이브러리

from random import *

print(random()) #0.0 이상 1.0미만의 값 생성
