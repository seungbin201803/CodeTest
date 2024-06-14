n, m, k = map(int, input().split())
data = list(map(int, input().split()))

max_val = max(data)
max_val_2 = max([x for x in data if x != max_val])

count_m = 0
count_k = 0
result = 0
while count_m < m:
	if count_k < k:
		result += max_val
		count_k += 1
	else:
		result += max_val_2
		count_k = 0
	count_m += 1

print(result)
