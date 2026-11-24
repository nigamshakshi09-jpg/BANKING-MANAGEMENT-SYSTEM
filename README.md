# Distributed Banking and Financial Transaction Management System (SQLite)

**Team member:** Shakshi Nigam  
**Team ID:** TCA2573040  
**Database:** SQLite  
**Recommended GUI:** DB Browser for SQLite

## Project overview
A learning project that models customers, accounts, branches, employees, beneficiaries, loans, loan payments, transfers, transaction history and audit logs. It demonstrates integrity constraints, triggers, atomic transactions, rollback, concurrency behavior, indexes and financial reports.

## Files
- `banking_system.db` — ready-to-open SQLite database with sample data, triggers, indexes and views.
- `sql/01_schema.sql` — schema, constraints, indexes and triggers.
- `sql/02_seed_data.sql` — sample branches, customers, accounts and opening balances.
- `sql/03_views_reports.sql` — account, branch and loan report views.
- `sql/04_demo_transfer.sql` — atomic transfer demonstration.
- `sql/05_test_cases.sql` — verification queries and query-plan test.
- `sql/06_failed_transfer_demo.sql` — insufficient-funds recovery exercise.
- `docs/PROJECT_REPORT.md` — project report for submission.
- `banking_app.py` — small Python command-line interface for deposit, withdrawal and transfer.

## Open in DB Browser for SQLite
1. Install and open **DB Browser for SQLite**.
2. Select **Open Database** and choose `banking_system.db`.
3. Open **Browse Data** to inspect tables such as `CUSTOMER`, `ACCOUNT`, `BANK_TRANSACTION` and `AUDIT_LOG`.
4. Open **Execute SQL** to run queries from the `sql` folder.
5. To create a fresh database, choose **New Database**, then run `01_schema.sql`, `02_seed_data.sql`, and `03_views_reports.sql` in that order.

## Demonstrate a transfer
Open `sql/04_demo_transfer.sql` and run the statements as a single transaction. If the demo reference already exists, the unique constraint prevents a duplicate; create a new reference or reset the database before repeating. Verify both account balances and the `TRANSFER` table after commit.

## Important SQLite vs Oracle distinction
SQLite does **not** support Oracle PL/SQL packages, stored procedures, database links, or Oracle's server-style Two-Phase Locking implementation. This version uses SQLite triggers for automatic balance updates and Python transaction functions for reusable banking operations. `BEGIN IMMEDIATE` obtains a write reservation before the transaction, helping serialize writers; SQLite uses database-level locking rather than row-level 2PL. Branches are represented in one database using `BRANCH` records, so this is a distributed-branch simulation, not a physically distributed database. A real distributed deployment would require multiple database servers and a distributed transaction protocol.

## Run the Python demo
Python 3 is required; no third-party packages are needed:
```bash
python banking_app.py
```
The app connects to `banking_system.db` in the same folder and offers deposit, withdrawal, transfer and balance display.

## Safety note
This is an academic demonstration with fictional sample data. Do not use it for real banking or store real customer information.
