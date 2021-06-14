data = []
with open(file = 'data.csv', mode = 'r', encoding = 'utf-8') as f:
	line = next(f)
	for line in f:
		line = line.strip().split(',')
		line[2] = int(line[2])
		line[3] = int(line[3])
		data.append(line)

output_data = []
for i in range(len(data)):
	if data[i][3] == 0:
		pass
	else:
		for a in range(data[i][2]):
			for b in range(data[i][3]):
				output_data.append([data[i][0], data[i][1],  data[i][4 + a], data[i + 1][4 + b]])
for i in range(len(output_data)):
	print(output_data[i][0], end = ',')
	print(output_data[i][1], end = ',')
	print(output_data[i][2], end = ',')
	print(output_data[i][3])
