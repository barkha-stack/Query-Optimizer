import argparse
from add_ery.analyzer import Analyzer

def main():
    parser = argparse.ArgumentParser(description="ADD-ERY Query Optimizer CLI")
    parser.add_argument("--query", "-q", help="SQL query to analyze")
    parser.add_argument("--file", "-f", help="Path to .sql file containing query")
    parser.add_argument("--db", default="database.db", help="SQLite DB path")
    args = parser.parse_args()

    if not args.query and not args.file:
        print("Provide --query or --file")
        return

    q = args.query
    if args.file:
        with open(args.file, "r", encoding="utf-8") as fh:
            q = fh.read()

    a = Analyzer(db_path=args.db)
    report = a.analyze(q)
    print("=== Suggestions ===")
    for s in report.get("suggestions", []):
        print("-", s)
    print("\nOptimized query:\n", report.get("optimized_query"))
    print("\nBenchmarks:\n", report.get("benchmarks"))

if __name__ == "__main__":
    main()
