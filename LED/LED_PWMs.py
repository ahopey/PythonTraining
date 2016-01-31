import RPi.GPIO as GPIO
import time
import LED_utils

LED_utils.setupLeds()
LED_utils.turnAllLeds(1)
LED_utils.setupPWMs(100)

LED_utils.turnAllLeds(1)
time.sleep(1)

for led_index in range(0, len(LED_utils.pins)):
    dc = 100 - led_index * (100 / (len(LED_utils.pins) - 1))
    LED_utils.pwms[led_index].start(dc)
    time.sleep(1)

input('press enter to continue')

GPIO.cleanup()


