from enum import Enum


class TableNameExample(Enum):
    KEY = 'VALUE'
    TABLE_RUNS = 'table_runs'


class TableNameClass:
    KEY = 'VALUE'


def calc(table_name: str):
    print(table_name)

def calc2(table_name: TableNameExample):
    if isinstance(table_name, TableName):
        print("table_name is TableName instance")
    if table_name == TableName.TABLE_RUNS:
        print("table_name is TableName TABLE_RUNS enum")
    print(table_name.value)
    print(table_name.name)


class TableName(Enum):
    TABLE_RUNS = "table_runs"
    STOCKS_METADATA = "stocks_metadata"
    STOCKS_SILVER = "stocks_silver"
    STOCKS_GOLD_MONTH = "stocks_gold_month"
    STOCKS_GOLD_WEEK = "stocks_gold_week"
    STOCKS_GOLD_YEAR = "stocks_gold_year"

class SchemaName(Enum):
    DEFAULT = "default"

class UnityCatalogName(Enum):
    DATABRICKSFORMULA1 = "databricksformula1"

class FullTableName(Enum): # UC.schema.table_name
    TABLE_RUNS = f"{UnityCatalogName.DATABRICKSFORMULA1.value}.{SchemaName.DEFAULT.value}.{TableName.TABLE_RUNS.value}"
    STOCKS_METADATA = f"{UnityCatalogName.DATABRICKSFORMULA1.value}.{SchemaName.DEFAULT.value}.{TableName.STOCKS_METADATA.value}"
    STOCKS_SILVER = f"{UnityCatalogName.DATABRICKSFORMULA1.value}.{SchemaName.DEFAULT.value}.{TableName.STOCKS_SILVER.value}"
    STOCKS_GOLD_MONTH = f"{UnityCatalogName.DATABRICKSFORMULA1.value}.{SchemaName.DEFAULT.value}.{TableName.STOCKS_GOLD_MONTH.value}"
    STOCKS_GOLD_WEEK = f"{UnityCatalogName.DATABRICKSFORMULA1.value}.{SchemaName.DEFAULT.value}.{TableName.STOCKS_GOLD_WEEK.value}"
    STOCKS_GOLD_YEAR = f"{UnityCatalogName.DATABRICKSFORMULA1.value}.{SchemaName.DEFAULT.value}.{TableName.STOCKS_GOLD_YEAR.value}"


if __name__ == "__main__":
    print(TableNameExample.KEY)
    print(TableNameClass.KEY)
    print(type(TableNameExample.KEY))
    print(type(TableNameClass.KEY))
    print(TableNameExample.KEY.name)
    print(TableNameExample.KEY.value)
    calc2(TableNameExample.KEY)
    calc2(TableNameExample.TABLE_RUNS)
    print("----")
    for x in TableNameExample:
        print(x)

