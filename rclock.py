import RPi.GPIO as GPIO
import time
import datetime
from gui import Wavescreen

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
control_pins = [6,13,19,26]
control_pins.reverse()

for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]]

def tick():
  for i in range(32): # 1 minute
      for halfstep in range(8):
        for pin in range(4):
          GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
          time.sleep(0.001)
      for pin in range(4):
        GPIO.output(control_pins[pin], 0)  

setup = False
def press():
  if True:
    return True
    
eStop = True
hour, chigm = datetime.datetime.now().hour, datetime.datetime.now().minute
prev_min = datetime.datetime.now().minute

yeet = Wavescreen("BLACK")
yeet.show("BLACK", 100, 50, f"{hour:02d}:{chigm:02d}", "WHITE", yeet.Font3, 0)
while eStop is True:
  if setup:
    tick()
  hour, chigm = datetime.datetime.now().hour, datetime.datetime.now().minute
  if prev_min != chigm:
    yeet.show("BLACK", 100, 50, f"{hour:02d}:{chigm:02d}", "WHITE", yeet.Font3, 0)
    if setup is not True:
      tick()
    prev_min = chigm
  time.sleep(0.001)
      
GPIO.cleanup()
yeet.fin()
