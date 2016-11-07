#!/usr/bin/env python
import RPi.GPIO as GPIO
import os
import smbus
from time import sleep

b = smbus.SMBus(1)
address = 0x20
GPIOA = 0x12
GPIOB = 0x13
b.write_byte_data(address,0x0C,0xFF)
b.write_byte_data(address,0x0D,0xFF)

if os.path.exists('ranking.txt'):
	os.remove('ranking.txt')
if os.path.exists('stop-script'):
	os.remove('stop-script')
text_file = open('ranking.txt', 'w')
#text_file.write('Ranking:\n')
text_file.close()
i = 1
team = [
'01',
'02', 
'03',
'04',
'05',
'06',
'07',
'08',
'09',
'10',
'11',
'12',
'13',
'14',
'15',
'16',
]

def checkseat(seat, i):
	flag = False
	with open('ranking.txt', 'r') as file_read:
		for line in file_read:
			if line[:2] == seat:
				flag = True
	if flag != True:
		with open('ranking.txt', 'a') as file_w:
			if int(seat) < 10:
				id = int(seat[1:2])-1
			else:
				id = int(seat)-1
			file_w.write("%s %s: Team %s - Button pressed \n" % (seat, i, team[id]))
		return i+1
	else:
		return i

while True:
	if os.path.exists('stop-script'):
		break;
	else:
		buzzer_a = b.read_byte_data(address,GPIOA)
		buzzer_b = b.read_byte_data(address,GPIOB)
		result_a = '{0:08b}'.format(buzzer_a)
		result_b = '{0:08b}'.format(buzzer_b)
		if result_b[7:8] == "0":
			i = checkseat("01", i)
			print "Button 1 pressed"
		if result_b[6:7] == "0":
			i = checkseat("02", i)
			print "Button 2 pressed"
		if result_b[5:6] == "0":
			i = checkseat("03", i)
			print "Button 3 pressed"
		if result_b[4:5] == "0":
			i = checkseat("04", i)
			print "Button 4 pressed"
		if result_b[3:4] == "0":
			i = checkseat("05", i)
			print "Button 5 pressed"
		if result_b[2:3] == "0":
			i = checkseat("06", i)
			print "Button 6 pressed"
		if result_b[1:2] == "0":
			i = checkseat("07", i)
			print "Button 7 pressed"
		if result_b[0:1] == "0":
			i = checkseat("08", i)
			print "Button 8 pressed"
		if result_a[7:8] == "0":
			i = checkseat("09", i)
			print "Button 9 pressed"
		if result_a[6:7] == "0":
			i = checkseat("10", i)
			print "Button 10 pressed"
		if result_a[5:6] == "0":
			i = checkseat("11", i)
			print "Button 11 pressed"
		if result_a[4:5] == "0":
			i = checkseat("12", i)
			print "Button 12 pressed"
		if result_a[3:4] == "0":
			i = checkseat("13", i)
			print "Button 13 pressed"
		if result_a[2:3] == "0":
			i = checkseat("14", i)
			print "Button 14 pressed"
		if result_a[1:2] == "0":
			i = checkseat("15", i)
			print "Button 15 pressed"
		if result_a[0:1] == "0":
			i = checkseat("16", i)
			print "Button 16 pressed"
