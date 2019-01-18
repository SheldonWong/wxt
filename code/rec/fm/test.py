


with open('./small_train.txt') as f:
	lines = f.readlines()
data = []
for line in lines:
	for a in line.split(" ")[1:-1]:
		data.append(int(a.split(":")[1]))
print(data)
print(max(data))
