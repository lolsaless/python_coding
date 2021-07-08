weather = "rain"
if weather == "rain":
    print("우산을 챙기세요.")
elif weather == "pm2.0":
    print("마스크 챙기세요")

temp = int(input("기온을 입력하세요 :"))
if 30 <= temp:
    print("나가지 마세요")
elif 10 <= temp:
    print("괜찮은 날씨입니다.")
elif 0 <= temp:
    print("외투를 챙기세요")
else:
    print("나가지마세요.")