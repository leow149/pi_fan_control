"""pi_fan_control.py by leow149"""

import time
import RPi.GPIO as GPIO
from gpiozero import CPUTemperature

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

MAXTEMP = int(70)
MINTEMP = int(35)
P = GPIO.PWM(12, 25000)
P.start(0)

try:
    while True:
        CPU = CPUTemperature()
        TEMP = int(CPU.temperature)
        if TEMP >= MAXTEMP:
            P.ChangeDutyCycle(100)
            print(TEMP)
            time.sleep(1)
        elif TEMP <= MINTEMP:
            P.ChangeDutyCycle(1)
            print(TEMP)
            time.sleep(0)
        else:
            SPEED = float(TEMP * 1.43)
            GESCH = round(SPEED)
            P.ChangeDutyCycle(GESCH)
            print(TEMP)
            time.sleep(1)
except KeyboardInterrupt:
    time.sleep(2)
finally:
    P.stop()
    GPIO.cleanup()
