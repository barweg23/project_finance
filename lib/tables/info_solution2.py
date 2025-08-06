from dataclasses import dataclass
from datetime import datetime

from lib.tables.info import UnityCatalogName, SchemaName
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType, TimestampType, LongType


class TableRuns:
    table_name = "table_runs"
    table_full_name = f"{UnityCatalogName.databricksformula1}.{SchemaName.default}.{table_name}"
    pyspark_schema = StructType([
    StructField("run_id", LongType(), True),
    StructField("job_id", LongType(), True),
    StructField("type_of_run", StringType(), True),
    StructField("created_timestamp", TimestampType(), True)
])
    sql_create_query = f"""CREATE table if not exists {table_full_name} (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    run_id BIGINT,
    job_id BIGINT,
    type_of_run VARCHAR(255),
    created_timestamp TIMESTAMP
);"""

    @dataclass
    class RowDataclass:
        run_id: int
        job_id: int
        type_of_run: str
        created_timestamp: datetime


if __name__ == "__main__":
    print(TableRuns.table_full_name)
    print(TableRuns.sql_create_query)
    print(TableRuns.table_name)
    print(TableRuns.pyspark_schema)
    data = TableRuns.RowDataclass(int(1), int(2), 'run_type', datetime.now())
    print(data)