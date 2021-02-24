# 짝수 합 구하기
num = int(input())
data = [i for i in range(1, num + 1) if i % 2 == 0]
print(data)
print(sum(data))
