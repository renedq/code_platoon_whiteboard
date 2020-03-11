input = [1,3,2,5,6,7,11,300,25,88]

count = 0

for i in input: 
	if i % 2 == 0:
	  count+=1

print("Total even numbers {}".format(count))
