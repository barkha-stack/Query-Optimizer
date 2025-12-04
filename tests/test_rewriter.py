from add_ery.query_rewriter import rewrite_or_to_in

def test_or_to_in():
    q = "SELECT * FROM employees WHERE department = 'Tech' OR department = 'HR';"
    out = rewrite_or_to_in(q)
    assert "IN" in out and "OR" not in out
