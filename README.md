# Query Optimizer
A Python-based SQL Query Optimization tool for SQLite databases.  
It analyzes queries, rewrites inefficient patterns, suggests indexes, and benchmarks performance.
## Features
- Query analysis: EXPLAIN plans, detect full table scans, detect queries not using indexes
- Query rewriting: OR → IN, SELECT * → explicit columns
- Index suggestions: Recommends indexes for WHERE filter columns
- Benchmarking: Compare execution time of original vs optimized query
- JSON reports: Saves suggestions, optimized query, and benchmarks
## Project Structure
Query_Optimizer/
├── add_ery/
│   ├── analyzer.py
│   ├── index_optimizer.py
│   ├── plan_parser.py
│   ├── query_rewriter.py
│   └── utils.py
├── tests/
├── examples/
├── setup_database.py
├── run.py
├── requirements.txt
└── README.md
## Installation
1. Clone the repository:
   git clone https://github.com/barkha-stack/Query-Optimizer.git
2. Create a virtual environment:
   python -m venv venv
   venv\Scripts\activate  # Windows
3. Install dependencies:
   pip install -r requirements.txt
4. Setup database:
   python setup_database.py
## Usage
Run a single query:
python run.py --query "SELECT * FROM employees WHERE department='HR' OR department='Tech';"

Run queries from a file:
python run.py --file examples/sample_queries.sql
## Running Tests
pytest -q
## Continuous Integration
GitHub Actions workflow (.github/workflows/ci.yml) runs automatically on push or pull request:
- Installs dependencies
- Sets up database
- Runs tests
## License
MIT License


