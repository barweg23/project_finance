from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType, TimestampType, LongType

from lib.tables.info import FullTableName


class SchemaTableInfo:
    table_runs = StructType([
    StructField("run_id", LongType(), True),
    StructField("job_id", LongType(), True),
    StructField("type_of_run", StringType(), True),
    StructField("created_timestamp", TimestampType(), True)
])
    stocks_schema = StructType([
    StructField("ingestion_date", StringType(), True),
    StructField("created_timestamp", TimestampType(), True),
    StructField("run_id", LongType(), True),
    StructField("job_id", LongType(), True),
    StructField("ticker", StringType(), True),
    StructField("extraction_from", DateType(), True),
    StructField("extraction_to", DateType(), True),
    StructField("status", StringType(), True)

])


class CreateTableQuery:
    table_runs = f"""CREATE table if not exists {FullTableName.table_runs} (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    run_id BIGINT,
    job_id BIGINT,
    type_of_run VARCHAR(255),
    created_timestamp TIMESTAMP
);"""


if __name__ == "__main__":
    print(CreateTableQuery.table_runs)
