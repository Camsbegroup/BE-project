import BlynkLib
import time
from time import sleep
time.sleep(3)
BLYNK_AUTH = 'ff59465d4bc74d80b68dbd1810dcc38d'
blynk = BlynkLib.Blynk(BLYNK_AUTH)
lat=0


@blynk.VIRTUAL_READ(10)
def my_read_handler():
	f0= open("sample.txt", "r+")
	for i in f0:
		global lat
		lat = i[0:10]
		print(lat)
		
	blynk.virtual_write(10,lat)
	f0.close()
	
@blynk.VIRTUAL_READ(11)
def my_read_handler():
	f= open("sample.txt", "r+")
	for i in f:
		global lang
		lang = i[10:20]
		print(lang)
	blynk.virtual_write(11,lang)
	f.close()
	
blynk.run()
