from add_ery.index_optimizer import suggest_indexes_for_query

def test_suggest_index():
    q = "SELECT * FROM employees WHERE city = 'Mumbai' AND salary > 50000"
    s = suggest_indexes_for_query(q, "employees")
    assert any("city" in x or "salary" in x for x in s)
