import RPi.GPIO as GPIO
import time
import LED_utils

LED_utils.setupLeds()
LED_utils.turnAllLeds(1)
LED_utils.setupPWMs(100)

led_index = 0
try:
    while True:
        for dc in range(100, -1, -5):
            LED_utils.pwms[led_index].ChangeDutyCycle(dc)
            time.sleep(0.1)

        for dc in range(0, 101, 5):
            LED_utils.pwms[led_index].ChangeDutyCycle(dc)            
            time.sleep(0.1)        
        
        LED_utils.pwms[led_index].ChangeDutyCycle(100)
        led_index += 1        
        LED_utils.turnAllLeds(1)
        
        if led_index == 5:
            led_index = 0
except KeyboardInterrupt:
    pass

GPIO.cleanup()
    
