import os
import random
import time
import logging
from flask import Flask
from flask_restful import Api

wait = int(os.getenv('START_WAIT_SECS', '0'))
crash_factor = int(os.getenv('CRASH_FACTOR', '0'))
print(f'waiting {str(wait)}')
time.sleep(wait)
print('starting app')

if crash_factor > 0:
    crash_random = random.randint(0,99)
    print(f'crash factor was {str(crash_factor)}, crash random int is {str(crash_random)}')
    if crash_factor > crash_random:

        raise ValueError('U told me to crash')

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
api = Api(app)

from k8sprobetester.healthz import HealthEndpoint
