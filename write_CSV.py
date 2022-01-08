import csv


def write_CSV(data):
	# data = ['time',10,500]
	with open('data.csv','a',newline = '',encoding = 'utf-8') as file:
		fw = csv.writer(file)
		fw.writerow(data)


def read_CSV():
	with open('data.csv',newline = '',encoding = 'utf-8') as file:
		fr = csv.reader(file) # list
		# print(list(fr))
		data = list(fr)
	return data

def sumdata():
	result = read_CSV()
	sumlist_quan = []
	sumlist_total = []
	for d in result:
		sumlist_quan.append(float(d[1]))
		sumlist_total.append(float(d[2]))
	sumquan = sum(sumlist_quan)
	sumtotal = sum(sumlist_total)

	return (sumquan,sumtotal)

result = sumdata()
print(result)