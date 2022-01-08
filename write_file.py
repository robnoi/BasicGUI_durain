
from datetime import datetime



def writetext(quantity,total):
	stamp = datetime.now()
	stamp =stamp.replace(year = stamp.year+543)
	stamp = stamp.strftime('%Y-%m-%d  %H:%M:%S')
	filename = 'data.txt'
	with open(filename,'a',encoding = 'utf-8') as file:
		file.write('\n'+'วัน-เวลา = {} ทุเรียน {} กิโลกรัม ราคา {:,.2f} บาท'.format(stamp,quantity,total))

writetext(90,9000)
writetext(2,200)