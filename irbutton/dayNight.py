from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
selButton = 16
led1=22
irControl=18

# Make selButton an input, Activate Pull UP Resistor
GPIO.setup(selButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Make led1 and irControl as an Output
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(irControl,GPIO.OUT)

# Sets led initially as off & ir initially as night
BSled = False
BSir = False

while(1):                  # Create an infinite Loop
        if GPIO.input(selButton)==0:            # Look for button 1 press
                print "selButton Was Pressed:"
                if BSled==False & BSir==False:                # If the LED is off
                        GPIO.output(led1,True) # turn it on
                        GPIO.output(irControl,True) # changes ir filter
                        BSled=True              # Set Flag to show LED1 is now On
                        BSir=True
                        sleep(.5)             # Delay
                else:                         # If the LED is on
                        GPIO.output(led1,False) # Turn LED off
                        GPIO.output(irControl,False) # filter to night
                        BSled=False               # Set Flag to show LED1 is now Off
                        BSir=False
                        sleep(.5)