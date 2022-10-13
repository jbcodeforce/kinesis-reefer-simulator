import datetime
import json
import random
import boto3
import time
import os

'''
Simulator of refrigerator container, called Reefer, to send
temperature values.

This is to connect to Kinesis
'''


base_temp = -5. # in celcius
MAX_TEMP = 50. # in celcius
POWER_LEVEL = 2.7  # in kW
O2_LEVEL = 21  # in percent  - below 12 is bad
CO2_LEVEL = 7  # in percent - above 12 is bad

def buildTelemetryRecord():
    global base_temp
    temp = -5
    fan = True
    cid = random.choice(['C01', 'C02', 'C03', 'C10'])
    if cid == 'C02' or cid == 'C01' and base_temp < MAX_TEMP:
        base_temp =  base_temp + 2
        temp = base_temp
        fan = False
    return {
        'measurement_time': datetime.datetime.now().isoformat(),
        'container_id': cid,
        'temperature': temp + random.randint(-1,1),
        'kilowatts': POWER_LEVEL + random.randint(-2,2),
        'oxygen_level': O2_LEVEL + random.uniform(-20,20),
        'product_id': 'P01',
        'fan_1': fan,
        'carbon_dioxide_level': CO2_LEVEL + random.uniform(-5,15),
        'latitude': '',
        'longitude': ''
    }

class ReeferSimulator:

    def generate(self,stream_name, kinesis_client = None):
        while True:
            data = buildTelemetryRecord()
            print(data)
            if kinesis_client != None:
                kinesis_client.put_record(StreamName=stream_name, Data = json.dumps(data), PartitionKey="partitionKey")
            time.sleep(2)

    