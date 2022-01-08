#BasicGUI.py

from tkinter import  ttk, messagebox
import tkinter as tk 
from datetime import datetime
import csv


def read_CSV():
	with open('data.csv',newline = '',encoding = 'utf-8') as file:
		fr = csv.reader(file) # list
		# print(list(fr))
		data = list(fr)
	return data

def writetext(quantity,cal):
	stamp = timestamp()
	filename = 'data.txt'
	with open(filename,'a',encoding = 'utf-8') as file:
		file.write('\n'+'วัน-เวลา = {} ทุเรียน {} กิโลกรัม ราคา {:,.2f} บาท'.format(stamp,quantity,cal))


def write_CSV(data):
	# data = ['time',10,500]
	with open('data.csv','a',newline = '',encoding = 'utf-8') as file:
		fw = csv.writer(file)
		fw.writerow(data)


def timestamp(thai = True):
	if thai == True:
		# time Thai
		stamp = datetime.now()
		stamp =stamp.replace(year = stamp.year+543)
		stamp = stamp.strftime('%Y-%m-%d  %H:%M:%S')
	else:
		# time Eng
		stamp = datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
	return stamp

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
	

GUI = tk.Tk() 
GUI.geometry('700x700')
GUI.title('Program cal')

file = tk.PhotoImage(file = 'ทุเรียน.png')
IMG = tk.Label(GUI,image = file,text = '')
IMG.pack()

L1 = tk.Label(GUI,text = 'โปรแกรมคำนวณทุเรียน',font = ('Angsana New',30,'bold'),fg = 'green')
L1.pack()

L2 = tk.Label(GUI,text= 'กรุณากรอกจำนวน',font = ('Angsana new',20 ))
L2.pack()

v_quatity = tk.StringVar()

E1 = ttk.Entry(GUI,textvariable = v_quatity,font = ('impact',30))
E1.pack()


def Calculate(event = None):
	quantity = v_quatity.get()
	price = 100
	print('ราคา', float(quantity)*price)
	cal = float(quantity)*price

	# pop up
	
	title = 'โปรแกรมคำนวนค่าทุเรียน'
	text = 'จำนวนทุเรียน {} กิโลกรัม ราคา {:,.2f} บาท '

	messagebox.showinfo(title,text.format(quantity,cal))

	# CLEAR
	v_quatity.set('')
	E1.focus()
	
	# write text
	writetext(quantity,cal)

	# write csv
	data = [timestamp(),quantity,cal]
	write_CSV(data)

	
	

B1 = ttk.Button(GUI,text = 'คำนวณ',command = Calculate)
B1.pack(ipadx = 30, ipady =20,pady = 20)

E1.bind('<Return>',Calculate)

def summaryData(event):
	sm = sumdata()
	title = 'ยอดสรุปรวม'
	text = 'จำนวนทั้งหมด {} กิโลกรัม ราคารวม {} บาท'
	messagebox.showinfo(title,text.format(sm[0],sm[1]))
	

GUI.bind('<F1>',summaryData)



GUI.mainloop()
