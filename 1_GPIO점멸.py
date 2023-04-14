import RPi.GPIO as GPIO
import time 

print(">>> Setup LED pins")

GPIO.setmode(GPIO.BCM)
LED_P = 25
GPIO.setup(LED_P, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_P, True)
        time.sleep(0.5)
        GPIO.output(LED_P, False)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
