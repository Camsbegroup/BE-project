import BlynkLib
import time
BLYNK_AUTH = 'd072284fac3645ee849394454a33336d'
# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)
# Register Virtual Pins
@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):
    print('Current V1 value: {}'.format(value))

@blynk.VIRTUAL_READ(6)
def my_read_handler():
    # this widget will show some time in seconds..
    blynk.virtual_write(V6,point,String(latitude,1),String(longitude,1),MapPointName);

# Start Blynk (this call should never return)
blynk.run()
