nums = 17;

output = ''
count = 0
first = 0
second = 1

while count < nums:
	output += "{}, ".format(first)
	next_num = first + second
	first = second
	second = next_num
	count += 1

print(output[:-2])
