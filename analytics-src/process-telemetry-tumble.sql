CREATE OR REPLACE PUMP "STREAM_PUMP" AS
  INSERT INTO "FAULTY_REEFERS"
  SELECT STREAM "container_id","measurement_time","product_id", "temperature","kilowatts","oxygen_level","carbon_dioxide_level","fan_1","latitude","longitude",
 TUMBLE_START(ts, INTERVAL '1' MINUTE) as window_start,
 TUMBLE_STOP(ts, INTERVAL '1' MINUTE) as window_stop,
COUNT(temperature)
FROM "SOURCE_SQL_STREAM_001"
GROUP BY TUMBLE(ts, INTERVAL '1' MINUTE), temperature
    WHERE "temperature" > 18; 