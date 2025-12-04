import re

class QueryOptimizer:

    def optimize(self, query):
        suggestions = []

        # Rule 1: SELECT * is inefficient
        if "select *" in query.lower():
            suggestions.append("Avoid SELECT *. Specify only required columns.")

        # Rule 2: Missing WHERE = full table scan
        if "where" not in query.lower():
            suggestions.append("Query has no WHERE clause → may cause full table scan.")

        # Rule 3: Detect unnecessary ORDER BY
        if "order by" in query.lower() and "limit" not in query.lower():
            suggestions.append("ORDER BY without LIMIT can be slow on large tables.")

        # Rule 4: LIKE '%text' pattern
        like_pattern = re.search(r"like '\%.*?'", query.lower())
        if like_pattern:
            suggestions.append("LIKE '%text' prevents index use. Try full-text search instead.")

        # Rule 5: Detect OR conditions
        if " or " in query.lower():
            suggestions.append("Multiple OR conditions found. Consider using IN() instead.")

        return suggestions
