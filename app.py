#! /usr/bin/env python3 
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
import numpy as np

from TempSensor import TempSensor
from RelaySensor import RelaySensor
from RelayController import RelayController

from MockTempSensor import MockTempSensor

class Job:
    """A simple scheduled job"""
    days_active = [False, True, False, False, True, False, False] # Starts on Sunday
    start_time = '08:30'
    duration = 60 # minutes
    enabled = True

    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    def __init__(self, days_active, start_time, duration):
        self.days_active = days_active
        self.start_time = start_time
        self.duration = duration

    def days_active_as_str(self):
    
    	if self.days_active.count(True) == 7:
    		return 'Every day'
    	elif self.days_active.count(True) == 5 and self.days_active[0] == False and self.days_active[6] == False:
    		return 'Weekdays'
    	elif self.days_active.count(True) == 2 and self.days_active[0] == True and self.days_active[6] == True:
    		return 'Weekends'
    	else:
    		 pretty_days = np.ma.masked_where( np.array(self.days_active), np.array(self.days) ).compressed() 
    		 return ', '.join( pretty_days )


app = Flask(__name__)

sensors = [
#  MockTempSensor(),
    TempSensor(),
    RelaySensor(),
]

controllers = [
    RelayController(),
]

@app.route('/', methods=['POST', 'GET'])
def index():
	# Handle form
	error = None	

	# Response
	heating_status = False
	jobs = [ Job([False, True, True, True, True, True, False], '15:30', 35), Job([True, True, True, True, True, True, True], '06:30', 30), Job([False, True, False, False, True, False, False], '08:30', 35), Job([True, False, False, False, False, False, True], '20:30', 180) ]
	return render_template( 'index.html', heating_status=heating_status, jobs=jobs, error=error )

@app.route('/api/switch', methods=['GET'])
def switch():
    if 'state' in request.args:
        if request.args['state'] == 'on':
            if 'duration' in request.args:
                duration = request.args['duration']
                print(duration)
            # TODO wire into heating on
            controllers[0].set(1)
            print('switching on')
        else:
            # TODO wire into heating off
            controllers[0].set(0)
            print('switching off')
        response = jsonify({'success': True})
        response.status_code = 200
    else:
        response = jsonify({'success': False, 'errors': ["No state provided"]})
        response.status_code = 500
    return response

if __name__ == "__main__":
    app.debug = True # Auto-reload & messaging
    app.run(host='0.0.0.0')
