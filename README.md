# Distributed Banking and Financial Transaction Management System

![Project banner](assets/dashboard_overview.png)

**Team member:** Shakshi Nigam\
**Team ID:** TCA2573040\
**Database:** SQLite\
**Tools:** DB Browser for SQLite, SQL, Python

## Project Overview

The Distributed Banking and Financial Transaction Management System is
an academic database project that models core banking operations across
multiple branches. It manages customers, accounts, deposits,
withdrawals, transfers, loans, transaction history and audit records.

The SQLite edition demonstrates relational database design, integrity
constraints, transaction processing, rollback and recovery, indexing,
reporting, and a simulated multi-branch workflow.

> **Important:** This is an educational simulation, not a production
> banking platform. SQLite is an embedded database and does not provide
> Oracle-style stored procedures or a native multi-server distributed
> database deployment. Branch activity and distributed transaction
> scenarios are simulated within the project.

## Dashboard Previews

### 1. Banking overview

![Banking overview dashboard](assets/dashboard_overview.png)

### 2. Accounts dashboard

![Accounts dashboard](assets/dashboard_accounts.png)

### 3. Transactions dashboard

![Transactions dashboard](assets/dashboard_transactions.png)

*These are illustrative dashboard mockups for README documentation, not
screenshots captured from a running application. The figures shown are
sample/illustrative values.*

## Main Features

-   Customer registration and account management
-   Branch and employee records
-   Deposits and withdrawals
-   Inter-account fund transfers
-   Loan and loan-payment records
-   Automatic balance maintenance through SQLite triggers/application
    transactions
-   Transaction rollback when an operation fails
-   Audit logging of transaction activity
-   Account and transaction indexes
-   Account summaries and branch-wise financial reports
-   Test cases for successful and failed operations

## Database Design

The project uses the following core tables:

  Table                Purpose
  -------------------- ---------------------------------------------
  `CUSTOMER`           Stores customer details
  `ACCOUNT`            Stores bank account details and balances
  `BRANCH`             Stores branch information
  `BANK_TRANSACTION`   Records deposits, withdrawals and transfers
  `TRANSFER`           Stores transfer-specific information
  `LOAN`               Stores loan details
  `LOAN_PAYMENT`       Stores loan repayment records
  `EMPLOYEE`           Stores employee information
  `BENEFICIARY`        Stores beneficiary details
  `AUDIT_LOG`          Stores audit events

## Project Structure

``` text
Distributed-Banking-System/
├── banking_system.db
├── banking_app.py
├── README.md
├── PROJECT_REPORT.md
├── SQL/
│   ├── 01_schema.sql
│   ├── 02_seed_data.sql
│   ├── 03_views_reports.sql
│   ├── 04_demo_transfer.sql
│   ├── 05_test_cases.sql
│   └── 06_failed_transfer_demo.sql
└── assets/
    ├── dashboard_overview.png
    ├── dashboard_accounts.png
    └── dashboard_transactions.png
```

*Adjust the folder names above if your downloaded ZIP uses a different
structure.*

## Getting Started

### Option A --- Open the ready database

1.  Download and extract the project ZIP.
2.  Open **DB Browser for SQLite**.
3.  Choose **Open Database**.
4.  Select `banking_system.db`.
5.  Open the **Browse Data** tab to inspect the tables and records.
6.  Open **Execute SQL** to run queries and test operations.

### Option B --- Build the database from SQL scripts

1.  Open DB Browser for SQLite.
2.  Select **New Database** and save it as `banking_system.db`.
3.  Open the **Execute SQL** tab.
4.  Run the schema script first, followed by the seed-data script.
5.  Run the remaining scripts in their documented order.
6.  Click **Write Changes** to save changes to the database.

## Example SQL Queries

View all customers:

``` sql
SELECT * FROM CUSTOMER;
```

View all accounts with their customer names:

``` sql
SELECT
    a.account_id,
    c.customer_name,
    a.account_type,
    a.balance
FROM ACCOUNT AS a
JOIN CUSTOMER AS c
    ON c.customer_id = a.customer_id;
```

View transaction history:

``` sql
SELECT *
FROM BANK_TRANSACTION
ORDER BY transaction_date DESC;
```

View total balance by branch:

``` sql
SELECT
    branch_id,
    SUM(balance) AS total_balance
FROM ACCOUNT
GROUP BY branch_id;
```

*Column names can vary slightly depending on the exact schema script
included in your project. Use the schema file as the source of truth.*

## Transaction Safety and Recovery

A transfer must debit one account and credit another as a single logical
operation. If either part fails, the application should roll back the
complete transfer so that the database does not retain a one-sided
balance change.

The project includes a failed-transfer demonstration to explain this
recovery principle. In SQLite, transaction handling is performed with
SQL transaction statements and/or the Python `sqlite3` transaction API;
Oracle PL/SQL packages are not used.

## Concurrency and Distributed-Database Concepts

The project explains concurrency risks such as simultaneous withdrawals,
lost updates and inconsistent balances. SQLite serializes writes, so its
concurrency behavior differs from a multi-user Oracle or distributed
database environment. The project demonstrates the concepts through
controlled transaction examples and branch simulation rather than
claiming a true distributed deployment.

## Testing Checklist

-   Verify that customer and account records are created.
-   Confirm that deposits increase the account balance.
-   Confirm that withdrawals reduce the account balance only when
    sufficient funds exist.
-   Verify that a successful transfer updates both accounts.
-   Verify that a failed transfer leaves both balances unchanged.
-   Check that transaction and audit records are created as expected.
-   Run the report queries and validate their totals.

## Learning Outcomes

This project provides practical experience with:

-   Relational database design and ER modelling
-   Primary keys, foreign keys and integrity constraints
-   SQL joins, grouping, aggregation and views
-   SQLite triggers and indexes
-   ACID transaction concepts
-   COMMIT, ROLLBACK and recovery
-   Concurrency-control concepts
-   Audit trails and financial reporting

## Limitations and Future Enhancements

**Current limitations** - SQLite is used as a single-file database. -
Multiple branches are simulated rather than hosted on separate database
servers. - SQLite does not support Oracle PL/SQL stored procedures. -
Dashboard images in this README are illustrative mockups.

**Possible enhancements** - Build a web dashboard using Flask or
Django. - Add user authentication and role-based permissions. - Connect
separate branch databases through a distributed application layer. - Add
automated reconciliation and downloadable account statements. - Deploy
on a server-based database for realistic multi-user testing.

## Team

**Shakshi Nigam** --- `TCA2573040`

## License

This project is intended for academic learning and demonstration. Add or
update a license file if you plan to distribute it publicly.
<img width="2112" height="1200" alt="dashboard_transactions" src="https://github.com/user-attachments/assets/d7a90596-a549-44d2-b014-8ce5c5f49ec2" />
<img width="2112" height="1200" alt="dashboard_overview" src="https://github.com/user-attachments/assets/21205e66-f2cb-44a3-94e7-8cfabb0fdfc3" />
<img width="2112" height="1200" alt="dashboard_accounts" src="https://github.com/user-attachments/assets/ba4bc481-d17f-4144-b50a-8ae198476afe" />
