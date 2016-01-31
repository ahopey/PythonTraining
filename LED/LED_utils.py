import RPi.GPIO as GPIO

pins = [5,6,13,19,26]
pwms = []

#turn all on/off
def turnAllLeds(on):
    for led in enumerate(pins):    
        GPIO.output(led, on)

def setupLeds():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    for led in enumerate(pins):
        GPIO.setup(led, GPIO.OUT)

def turnOneLed(index, on):
     GPIO.output(pins[index], on)


#PWM stuff comming

def setupPWMs(init):
    for index in range(0, len(pins)):
        p = GPIO.PWM(pins[index], 50);
        p.start(init)
        pwms.append(p)

def setAllDutyCycles(dc):
    for index in range(0, len(pins)):
        pwms[index].ChangeDutyCycle(dc)
