def has_table_scan(plan_rows):
    for row in plan_rows:
        detail = str(row).upper()
        if "SCAN" in detail and "TABLE" in detail:
            return True
    return False

def uses_index(plan_rows):
    for row in plan_rows:
        detail = str(row).upper()
        if "USING INDEX" in detail or "USING COVERING INDEX" in detail:
            return True
    return False
