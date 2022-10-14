CREATE OR REPLACE PUMP "STREAM_PUMP" AS
  INSERT INTO "FAULTY_REEFERS"
  SELECT STREAM "container_id","measurement_time","product_id", "temperature","kilowatts","oxygen_level","carbon_dioxide_level","fan_1","latitude","longitude",
FROM "SOURCE_SQL_STREAM_001"

    WHERE "temperature" > 18; 