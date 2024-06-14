n = 1260
count = 0

coin_list = [500, 100, 50, 10]
for coint in coin_list:
	count += n//coint
	n %= coint

print(count)