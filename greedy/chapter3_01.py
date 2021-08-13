n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

"""" my code
def first_num(arr):
	first = 0
	for num in arr:
		if first < num:
			first = num
	return first

def second_num(arr, first):
	second = 0
	for num in arr:
		if second < num and num != first:
			second = num
	return second

first = first_num(arr)
second = second_num(arr, first)
count = 0
sum = 0

for i in range(m):
	if count == k:
		count = 0
		sum += second
	else:
		sum += first
	count += 1

print(sum)
"""

# answer 1
arr.sort() # 입력받은 수를 정렬
first = arr[n - 1] # 가장 큰 수
second = arr[n - 2] # 두 번째로 큰 수

result = 0

while True:
	for i in range(k): # 가장 큰 수를 k번 더하기
		if m == 0: # m 이 0 이라면 탈출
			break
		result += first
		m -= 1 # 더할 때마다 1씩 빼기
	if m == 0: # m 이 0 이라면 반복문 탈출
		break
	result += second # 두 번째로 큰 수를 한 번 더하기
	m -= 1 # 더할 때마다 1씩 빼기

print(result)

# answer 2
arr.sort() # 입력받은 수를 정렬
first = arr[n - 1] # 가장 큰 수
second = arr[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수
count = int(n / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second