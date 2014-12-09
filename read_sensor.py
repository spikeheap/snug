#! /usr/bin/env python
import time
from RelaySensor import RelaySensor
while True:
	print(RelaySensor().read())
	time.sleep(5)
