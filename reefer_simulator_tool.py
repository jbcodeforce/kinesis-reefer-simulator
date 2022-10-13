import os,sys
import boto3
from app.domain.reefer_simulator import ReeferSimulator

STREAM_NAME = os.getenv("STREAM_NAME")

def parseArguments():
    mode = 'local'
    if len(sys.argv) == 1:
        print("Usage reefer_simulator_tool [local|aws]")
        exit(1)
    else:
        
        for idx in range(1, len(sys.argv)):
            arg=sys.argv[idx]
            if arg == "aws":
                mode = 'aws'
    return mode

if __name__ == '__main__':
    mode=parseArguments()
    simulator = ReeferSimulator()
    if mode == 'aws':
        simulator.generate(STREAM_NAME, boto3.client('kinesis'))
    else:
        simulator.generate(STREAM_NAME)
    