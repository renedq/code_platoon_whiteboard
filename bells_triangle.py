number = 6

bell = []
bell.append([1])
print(bell[0])

for i in range(1, number+1):
	row = []
	row.append(bell[i-1][i-1])
	for j in range(1, i+1):
		row.append(row[j-1] + bell[i-1][j-1])
	
	bell.append(row)
	print(row)

