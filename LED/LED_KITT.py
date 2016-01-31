import RPi.GPIO as GPIO
import time
import LED_utils

LED_utils.setupLeds()
LED_utils.turnAllLeds(1)
LED_utils.setupPWMs(100)

#constants
width = 1
sleep = 0.1

#calculated params
pwm_step = 100 / (width + 1)
    
index = 0
inc = 1
try:
    while True:
        LED_utils.setAllDutyCycles(100);

        for pwm_index in range(index - width, index + width + 1):
            if (pwm_index > -1) and (pwm_index < 5):
                dc = abs(index - pwm_index) * pwm_step
                LED_utils.pwms[pwm_index].ChangeDutyCycle(dc)
                #print('set ' + str(pwm_index) + ' to ' + str(dc))

        #print()
        time.sleep(sleep)
        index += inc   

        if index == 5:
            index = 3
            inc = -1

        if index == -1:
            index = 1
            inc = 1            
except KeyboardInterrupt:
    GPIO.cleanup()
