#!/usr/bin/env python

# initial statement in order to run as batch

import RPi.GPIO as GPIO # import GPIO library
import subprocess # import subprocess library to call bash

GPIO.setmode(GPIO.BOARD) # Use Physical Pin numbering scheme
shutdown = 5 # shutdown button is connected to pin 5 
GPIO.setup(shutdown, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Make shutdown input, Activate Pull UP Resistor

# There are several ways of inputs gpio into python. The first and simplest way is to check the input at a point in time. 
# This is know as "polling" and consists of a running loop which is stoped by the input
# The other way of responding to a GPIO input is using "interrupts" (edge detection).
# An edge is the name of a transition from HIGH to LOW (falling edge) or LOW to HIGH (rising edge)
# The wait_for_edge() function is designed to block execution of your program until an edge is detected. 

GPIO.wait_for_edge(shudown,GPIO.FALLING)
subprocess.call(['shutdown','-h','now'], shell = False) # execute bash command

GPIO.cleanup()
