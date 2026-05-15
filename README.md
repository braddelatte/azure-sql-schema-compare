# Azure SQL Schema Compare

A Python and Jupyter Notebook toolkit for comparing Azure SQL database schemas across multiple databases and generating recommended consolidated target DDL for migration projects.

---

# Features

## Schema Comparison

Compare database schemas across multiple Azure SQL databases, including:

- Missing columns
- Data type mismatches
- Nullable differences
- Identity differences
- Precision and scale differences
- Primary key differences

## Automatic Table Discovery

Supports two modes:

- Manual table list from JSON
- Automatic table discovery from SQL

## Consolidation DDL Generation

Generate recommended SQL Server `CREATE TABLE` scripts that:

- Include all discovered columns
- Select safer/wider compatible data types
- Reduce migration failures caused by:
  - Missing columns
  - Data type conflicts
  - Length mismatches

## Output Reports

Exports results to Excel and SQL files for analysis and migration planning.

---

# Repository Structure

```text
azure-sql-schema-compare/
│
├── notebooks/
│   ├── schema_compare.ipynb
│   └── generate_recommended_ddl.ipynb
│
├── src/
│   └── connections.py
│
├── sql/
│   └── get_base_tables.sql
│
├── config/
│   ├── databases.json
│   ├── tables_to_compare.json
│   ├── databases.example.json
│   └── tables_to_compare.example.json
│
├── output/                 # ignored by Git
│
├── output.example/
│   ├── .gitkeep
│   └── README.md
│
├── .env                    # ignored by Git
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Requirements

- Python 3.12+
- Azure SQL access
- Microsoft ODBC Driver 18 for SQL Server
- VS Code with Jupyter extension recommended

---

# Installation

## Clone Repository

```bash
git clone <repo-url>
cd azure-sql-schema-compare
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

## Install Requirements

```bash
pip install -r requirements.txt
```

---

# Configuration

## Create `.env`

Create a `.env` file in the repository root.

Example:

```env
SQL_SERVER=yourserver.database.windows.net
SQL_USERNAME=yourlogin@company.com
AUTH_MODE=ActiveDirectoryInteractive
```

---

# Database Configuration

## `config/databases.json`

```json
[
    "database_1",
    "database_2",
    "database_3"
]
```

---

# Manual Table Configuration

## `config/tables_to_compare.json`

```json
[
    {
        "schema": "dbo",
        "table": "basetbl_MEL_MRI_Hdr"
    }
]
```

---

# SQL Discovery Mode

The notebook can automatically discover tables using:

```text
sql/get_base_tables.sql
```

This allows:

- table exclusions
- schema filtering
- custom discovery logic

---

# Running the Schema Compare Notebook

Open:

```text
notebooks/schema_compare.ipynb
```

Run all cells.

The notebook will:

1. Load database configuration
2. Discover or load tables
3. Compare schemas
4. Detect:
   - missing columns
   - datatype mismatches
   - PK differences
5. Export Excel comparison reports

---

# Running the DDL Generator Notebook

Open:

```text
notebooks/generate_recommended_ddl.ipynb
```

Run all cells.

The notebook will:

1. Read schema comparison results
2. Determine recommended target data types
3. Generate consolidated `CREATE TABLE` statements
4. Export recommended DDL to SQL files

---

# Output Files

Generated outputs are written to:

```text
output/
```

Typical outputs include:

- `schema_compare_results.xlsx`
- `recommended_column_decisions.xlsx`
- `recommended_target_ddl.sql`

---

# Authentication

Current implementation supports:

- Azure AD Interactive Authentication

Connection handling is managed in:

```text
src/connections.py
```

---

# Notes

- `.env`
- `/output`
- private config files

are excluded from Git for security and privacy.

---

# Future Enhancements

Potential future additions:

- Parallel schema collection
- Automated migration script generation
- Data profiling
- Row count comparison
- Constraint comparison
- Index comparison
- Foreign key comparison
- Automated ETL staging generation
- Data quality scanning
- Delta Lake compatibility analysis

---

# Author

Brad Delatte

Initial development created for Azure SQL schema consolidation and migration analysis workflows.