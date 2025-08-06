from dataclasses import dataclass
from datetime import datetime



@dataclass
class TableRuns:
    run_id: int
    job_id: int
    type_of_run: str
    created_timestamp: datetime

if __name__ == "__main__":
    data = TableRuns(int(1), int(2), 'run_type', datetime.now())
    print(data)
