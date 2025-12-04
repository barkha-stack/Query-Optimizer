import sqlite3
import time

# ✅ Use relative imports within the package
from .plan_parser import has_table_scan, uses_index
from .index_optimizer import suggest_indexes_for_query
from .query_rewriter import rewrite_or_to_in, remove_select_star
from .utils import save_json_report


class Analyzer:
    def __init__(self, db_path="database.db"):
        self.db_path = db_path

    def explain_plan(self, query: str):
        """Return the SQLite query plan for a query."""
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        cur.execute(f"EXPLAIN QUERY PLAN {query}")
        plan = cur.fetchall()
        con.close()
        return plan

    def run_query_and_time(self, query: str, fetch_n=5):
        """Execute the query and return first N rows along with execution time."""
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        start = time.time()
        cur.execute(query)
        rows = cur.fetchmany(fetch_n)
        con.commit()
        con.close()
        elapsed = time.time() - start
        return rows, elapsed

    def analyze(self, query: str, table_name="employees", sample_columns=None):
        """Perform full analysis: explain plan, rewrite query, index suggestions, benchmarks."""
        if sample_columns is None:
            sample_columns = ["id", "name", "department", "salary", "city"]

        report = {
            "original_query": query,
            "suggestions": [],
            "plan": None,
            "optimized_query": None,
            "benchmarks": {},
            "index_suggestions": []
        }

        # 1️⃣ Explain plan
        try:
            plan = self.explain_plan(query)
            report["plan"] = plan
            if has_table_scan(plan):
                report["suggestions"].append(
                    "Full table scan detected; consider adding indexes on filter columns."
                )
            if not uses_index(plan):
                report["suggestions"].append("Query does not appear to use indexes.")
        except Exception as e:
            report["suggestions"].append(f"EXPLAIN failed: {e}")

        # 2️⃣ Query rewriting
        optimized_query = rewrite_or_to_in(query)
        optimized_query = remove_select_star(optimized_query, sample_columns)
        report["optimized_query"] = optimized_query
        if optimized_query != query:
            report["suggestions"].append("Query can be rewritten for better performance.")

        # 3️⃣ Index suggestions
        idx_sugs = suggest_indexes_for_query(query, table_name)
        if idx_sugs:
            report["suggestions"].append("Index suggestions available.")
            report["index_suggestions"] = idx_sugs

        # 4️⃣ Benchmark original vs optimized
        try:
            _, t1 = self.run_query_and_time(query)
            _, t2 = self.run_query_and_time(optimized_query)
            report["benchmarks"] = {"original_seconds": t1, "optimized_seconds": t2}
        except Exception as e:
            report["benchmarks"] = {"error": str(e)}

        # 5️⃣ Save report
        save_json_report(f"report_{int(time.time())}.json", report)

        return report


# ✅ Optional: run this module directly for testing
if __name__ == "__main__":
    # Use **absolute imports** here so you can run analyzer.py standalone
    from add_ery.plan_parser import has_table_scan, uses_index
    from add_ery.index_optimizer import suggest_indexes_for_query
    from add_ery.query_rewriter import rewrite_or_to_in, remove_select_star
    from add_ery.utils import save_json_report

    analyzer = Analyzer("database.db")
    test_query = "SELECT * FROM employees WHERE department='HR' OR salary>50000"
    report = analyzer.analyze(test_query)
    print(report)
