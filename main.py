from add_ery.analyzer import Analyzer

if __name__ == "__main__":
    analyzer = Analyzer("database.db")
    query = "SELECT * FROM employees WHERE department='HR' OR salary>50000"
    report = analyzer.analyze(query)
    print(report)
