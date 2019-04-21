#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.

"""

import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint
import time
import threading


start = 0

PERIOD_OF_TIME = 20

count = 0

scancheck="global"
def fingerprintdemo():
	global start
	start = time.time()
	print (start)
	## Search for a finger
	##

	## Tries to initialize the sensor
	try:
		f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

		if ( f.verifyPassword() == False ):
			raise ValueError('The given fingerprint sensor password is wrong!')

	except Exception as e:
		print('The fingerprint sensor could not be initialized!')
		print('Exception message: ' + str(e))
		exit(1)

	## Gets some sensor information
	print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

	## Tries to search the finger and calculate hash
	try:
		print('Waiting for finger...')
		
		## Wait that finger is read
		 
		while ( f.readImage() == False ):
			if (time.time() > start + PERIOD_OF_TIME):
				morewaiting()
				start = time.time()
				print (start)				
			else:
				pass
		
		## Converts read image to characteristics and stores it in charbuffer 1
		f.convertImage(0x01)

		## Searchs template
		result = f.searchTemplate()

		positionNumber = result[0]
		accuracyScore = result[1]
		global repeataccess
		if ( positionNumber == -1 ):
			print('No match found!')
			exit(0)
			repeataccess = 0
		else:
			print('Found template at position #' + str(positionNumber))
			print('The accuracy score is: ' + str(accuracyScore))
			repeataccess = 1
			
			

		## OPTIONAL stuff
		##

		## Loads the found template to charbuffer 1
		f.loadTemplate(positionNumber, 0x01)

		## Downloads the characteristics of template loaded in charbuffer 1
		characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')

		## Hashes characteristics of template
		print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())
		
	except Exception as e:
		print('Operation failed!')
		print('Exception message: ' + str(e))
		exit(1)


def morewaiting():
	print("insde function")
	return
def every(delay, task):
  next_time = time.time() + delay
  while True:
    time.sleep(max(0, next_time - time.time()))
    try:
		task()
		
    except Exception:
      traceback.print_exc()
      # in production code you might want to have this instead of course:
      # logger.exception("Problem while executing repetitive task.")
    # skip tasks if we are behind schedule:
    next_time += (time.time() - next_time) // delay * delay + delay



if __name__ == '__main__':
	fingerprintdemo()
	t1= threading.Thread(target=lambda: every(5, fingerprintdemo))
	t1.start()

		
	
		





	



