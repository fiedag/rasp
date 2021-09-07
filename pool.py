#!/usr/bin/env python3
#
# pool.py
#
# Author: Alex Fiedler
# Date: 04-SEP-2021
#
#


# never run anything for >2 hours = 7200 seconds
_MAXTIME=7200


# library for sleeping
import time
# library for processing the input parameters
import argparse

# datetime calculations
from datetime import datetime

# file operations
from pathlib import Path

# a way to skip days
from skipper import run_this_time

# get all input paramaters
parser = argparse.ArgumentParser(prog='pool')
parser.add_argument('-pump', required=True, type=int, help='runtime (in seconds) for the poolpump')
args = parser.parse_args()


# library for General Purpose IO
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# set up some constants
_PUMP_PIN=4
_RELAY_OFF=GPIO.LOW
_RELAY_ON=GPIO.HIGH


GPIO.setup(_PUMP_PIN, GPIO.OUT)

try:
	t1 = datetime.now()
	GPIO.output(_PUMP_PIN, GPIO.LOW)
	time.sleep(min(args.pump,_MAXTIME))  # do not leave relay on for more than the max time
	GPIO.output(_PUMP_PIN, GPIO.HIGH)
	t2 = datetime.now()
	msg="Device controlled by pin {} was on for {}".format(_PUMP_PIN, t2 - t1)
	print(msg)
except:
	print("unexpected exception")
	pass
finally:
	GPIO.output(_PUMP_PIN, GPIO.HIGH)


