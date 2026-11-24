import sqlite3
from pathlib import Path

DB = Path(__file__).with_name("banking_system.db")

def connect():
    con = sqlite3.connect(DB, timeout=10)
    con.execute("PRAGMA foreign_keys = ON")
    return con

def post(con, account_id, kind, amount, description, related=None):
    con.execute("""INSERT INTO BANK_TRANSACTION
        (account_id, transaction_type, amount, description, related_account_id)
        VALUES (?, ?, ?, ?, ?)""", (account_id, kind, amount, description, related))

def deposit(account_id, amount):
    with connect() as con:
        post(con, account_id, "DEPOSIT", amount, "Cash deposit")

def withdraw(account_id, amount):
    with connect() as con:
        post(con, account_id, "WITHDRAWAL", amount, "Cash withdrawal")

def transfer(source, destination, amount):
    if source == destination:
        raise ValueError("Source and destination accounts must be different")
    # BEGIN IMMEDIATE serializes writers before either side of the transfer is posted.
    con = connect()
    try:
        con.execute("BEGIN IMMEDIATE")
        post(con, source, "TRANSFER_OUT", amount, "Fund transfer", destination)
        post(con, destination, "TRANSFER_IN", amount, "Fund transfer", source)
        ref = f"APP-{source}-{destination}-{int(__import__('time').time()*1000)}"
        con.execute("""INSERT INTO TRANSFER
            (from_account_id,to_account_id,amount,status,reference)
            VALUES(?,?,?,'COMPLETED',?)""", (source,destination,amount,ref))
        con.commit()
        print("Transfer completed. Reference:", ref)
    except Exception:
        con.rollback()
        raise
    finally:
        con.close()

def show_balances():
    with connect() as con:
        for row in con.execute("SELECT account_id, balance, status FROM ACCOUNT ORDER BY account_id"):
            print(row)

def main():
    while True:
        print("\nDISTRIBUTED BANKING SYSTEM (SQLite)")
        print("1. Deposit  2. Withdraw  3. Transfer  4. Show balances  0. Exit")
        choice = input("Choose: ").strip()
        try:
            if choice == "1": deposit(int(input("Account ID: ")), float(input("Amount: ")))
            elif choice == "2": withdraw(int(input("Account ID: ")), float(input("Amount: ")))
            elif choice == "3": transfer(int(input("From account: ")), int(input("To account: ")), float(input("Amount: ")))
            elif choice == "4": show_balances()
            elif choice == "0": break
            else: print("Invalid choice")
        except Exception as exc:
            print("Operation failed:", exc)

if __name__ == "__main__":
    main()
