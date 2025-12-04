import re

def rewrite_or_to_in(query: str) -> str:
    pattern = re.compile(r"(\b[a-zA-Z_][a-zA-Z0-9_]*\b)\s*=\s*'([^']*)'\s+OR\s+\1\s*=\s*'([^']*)'", flags=re.IGNORECASE)
    new = pattern.sub(r"\1 IN ('\2','\3')", query)
    return new

def remove_select_star(query: str, sample_columns: list) -> str:
    if re.search(r"select\s+\*\s+from", query, flags=re.IGNORECASE):
        cols = ", ".join(sample_columns)
        return re.sub(r"select\s+\*\s+from", f"select {cols} from", query, flags=re.IGNORECASE)
    return query
