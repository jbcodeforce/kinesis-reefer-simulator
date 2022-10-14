import boto3
import os
import json




kinesis_client = boto3.client('kinesis')
shard_id='shardId-000000000000'
stream_name=os.getenv("STREAM_NAME")
print(stream_name)
shards= kinesis_client.list_shards(StreamName=stream_name)
print(shards)
shardId=shards["Shards"][0]["ShardId"]
shard_it = kinesis_client.get_shard_iterator(StreamName=stream_name, ShardId=shardId,ShardIteratorType="LATEST")["ShardIterator"]

out=kinesis_client.get_records( ShardIterator=shard_it, Limit=10)
if len(out["Records"])>0:
    	print(out["Records"][0]["Data"])
print(out)