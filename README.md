# Reefer simulator to Kinesis Streams

## What this is about

The code is the Reefer simulator to sent telemetries events to Kinesis Data Streams (the top left component on the left of the figure below)

![](./docs/images/archi-aws-mapping.png)


## Run it in Cloud9

* Copy paste the reefer_simulator.py

* Set STREAM_NAME environment variable in Terminal

```sh
export STREAM_NAME=telemetries
```

* Create a Kinesis Data Streams service named `telemetries` with 1 shard
* Start

```sh
python reefer_simulator.py
```

* Stop it with Control-C

## Build docker image

```sh
docker build -t jbcodeforce/reefer-simulator .
dokcer push jbcodeforce/reefer-simulator
```

