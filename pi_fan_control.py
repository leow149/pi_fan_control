"""pi_fan_control.py by leow149"""

import time
import RPi.GPIO as GPIO
from gpiozero import CPUTemperature

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

maxtemp = int(70)
mintemp = int(35)
p = GPIO.PWM(12, 25000)
p.start(0)

try:
    while True:
        cpu = CPUTemperature()
        temp = int(cpu.temperature)
        if temp >= maxtemp:
            p.ChangeDutyCycle(100)
            print(temp)
            time.sleep(1)
        elif temp <= mintemp:
            p.ChangeDutyCycle(1)
            print(temp)
            time.sleep(0)
        else:
            speed = float(temp * 1.43)
            gesch = round(speed)
            p.ChangeDutyCycle(gesch)
            print(temp)
            time.sleep(1)
except KeyboardInterrupt:
    time.sleep(2)
finally:
    p.stop()
    GPIO.cleanup()
