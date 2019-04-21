import BlynkLib
import time
import os
from time import sleep
valuelatlong=""

BLYNK_AUTH = 'c30255f26f8446308f8b114723fd1e13'
# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)
# Register Virtual Pins
i=0
j=0
@blynk.VIRTUAL_WRITE(1)
def my_write_handler(param):
	global i
	global j
	print(param)
	if (i<=1):
		src=open("sample.txt","r")
		fline=param
		oline=src.readlines()
		#Here, we prepend the string we want to on first line
		oline.insert(0,fline)
		src.close()
		#We again open the file in WRITE mode 
		src=open("sample.txt","w")
		src.writelines(oline)
		i=i+1
		print("insideif")
		print(i)
		print(j)
		src.close()
	
	j=j+1
	
	if (j==4):
		j=0
		i=0
		
	
	'''
	print(param)
	#aluelatlong = param
	#ime.sleep(5)
	f=open("sample.txt","a")
	src=open("sample.txt","r")
	fline=param
	oline=src.readlines()
	#Here, we prepend the string we want to on first line
	oline.insert(0,fline)
	#f.write(param)
	
	f0= open("sample.txt", "r+")
	for i in f0:
		lat = i[0:10]
		#lang = i[10:20]
		print(lat)
		#print(lang)
	f.close()
	src.close()'''
	
	#os.system('sudo rm -rf sample.txt')
	
	
# Start Blynk (this call should never return)
blynk.run()



