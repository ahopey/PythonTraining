import RPi.GPIO as GPIO
import time
import LED_utils

LED_utils.setupLeds()

led_index = 0
try:
    while True:
        LED_utils.turnAllLeds(1)
        LED_utils.turnOneLed(led_index, 0)        
        led_index += 1
        if led_index == 5:
            led_index = 0
        time.sleep(1)
except KeyboardInterrupt:
    LED_utils.turnAllLeds(1)
    GPIO.cleanup()



