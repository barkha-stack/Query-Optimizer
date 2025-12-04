from typing import List
from .utils import extract_where_columns

def suggest_indexes_for_query(query: str, table_name: str) -> List[str]:
    cols = extract_where_columns(query)
    suggestions = []
    for c in cols:
        suggestions.append(f"CREATE INDEX idx_{table_name}_{c} ON {table_name}({c});")
    return suggestions
