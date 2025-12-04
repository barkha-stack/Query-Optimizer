import re
import json
from typing import List

def extract_where_columns(query: str) -> List[str]:
    cols = re.findall(r"WHERE\s+(.*)", query, flags=re.IGNORECASE)
    if not cols:
        return []
    where = cols[0]
    columns = re.findall(r"([a-zA-Z_][a-zA-Z0-9_]*)\s*(?:=|LIKE|IN)\s*", where, flags=re.IGNORECASE)
    return list(dict.fromkeys(columns))

def save_json_report(path: str, data: dict):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
