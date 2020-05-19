import RPi.GPIO as GPIO  
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

## Define our pins ##
LED = 4
TRIG = 18
ECHO = 17

## setup our LED and our PWM
GPIO.setup(LED, GPIO.OUT) 
pwm = GPIO.PWM(LED, 100)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

## init our duty cycle ##
pwm.start(100)

## max distance, this is when the LED start to shine ##
dc = 0
MAX = 22
step = 100/(MAX-2)
## this sensor HC-SRO4 range from 2cm - 4m

try:
    while True:
        GPIO.output(TRIG, True)
        time.sleep (0.0001)
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO) == False:
            start_t = time.time()
            
        while GPIO.input(ECHO) == True:
            end_t = time.time()
        
        return_t = end_t - start_t
        
        distance = return_t/0.000058
        print(round(distance, 2))
        
        if (distance < MAX):
            dc = (MAX - distance)*step
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.002)
        else:
            pass
except KeyboardInterrupt:
    print("Stop requested")
    
pwm.stop()
GPIO.cleanup()
    

