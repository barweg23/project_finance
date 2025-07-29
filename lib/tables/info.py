

class TableName:
    table_runs = "table_runs"
    stocks_metadata = "stocks_metadata"
    stocks_silver = "stocks_silver"
    stocks_gold_month = "stocks_gold_month"
    stocks_gold_week = "stocks_gold_week"
    stocks_gold_year = "stocks_gold_year"
class SchemaName:
    default = "default"

class UnityCatalogName:
    databricksformula1 = "databricksformula1"

class FullTableName: # UC.schema.table_name
    table_runs = f"{UnityCatalogName.databricksformula1}.{SchemaName.default}.{TableName.table_runs}"
    stocks_metadata = f"{UnityCatalogName.databricksformula1}.{SchemaName.default}.{TableName.stocks_metadata}"
    stocks_silver = f"{UnityCatalogName.databricksformula1}.{SchemaName.default}.{TableName.stocks_silver}"
    stocks_gold_month = f"{UnityCatalogName.databricksformula1}.{SchemaName.default}.{TableName.stocks_gold_month}"
    stocks_gold_week = f"{UnityCatalogName.databricksformula1}.{SchemaName.default}.{TableName.stocks_gold_week}"
    stocks_gold_year = f"{UnityCatalogName.databricksformula1}.{SchemaName.default}.{TableName.stocks_gold_year}"


class TableRuns:
    table_name = ""
    table_full_name =""
    pyspark_schema =  ""
    sql_create_query =""


if __name__ == "__main__":
    print(FullTableName.table_runs)
    print(UnityCatalogName.databricksformula1)
    print(TableRuns.table_full_name)
    print(TableRuns.sql_create_query)