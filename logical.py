logicalValueOne = bool(input("1빈문자열은 False 아니면 True"))
#logicalValueOne = True
#bool 함수가 이런식으로 인식함
One = logicalValueOne
logicalValueTwo = bool(input("2빈문자열은 False 아니면 True "))
#logicalValueTwo = False
Two = logicalValueTwo

print("{}  {}".format(One,Two))
print("One = {} not One = {}".format(One,(not One )) )
print("{} and {} ={}".format(One, Two, (One and Two)))
print("{} or {} ={}".format(One, Two, (One or Two)))

#논리 연산자는 논리값과 논리값을 연산해서 논리값을 리턴하는 연산자
