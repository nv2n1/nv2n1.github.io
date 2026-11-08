---
title: "DDL vs DML: Key Differences in Database Commands"
date: 2018-03-24 11:44:30 +0000
modified: 2026-05-17 16:50:45 +0000
author: "Weiwei Jia"
layout: post
categories: [security-cryptography-2]
canonical: /what-are-the-differences-between-database-ddl-and-dml/
---

Database commands fall into distinct categories based on what they do. The two most fundamental are DDL (Data Definition Language) and DML (Data Manipulation Language). Understanding the difference is essential for anyone working with databases, from writing migrations to managing production systems.

## DDL: Data Definition Language

DDL statements define and modify the structure of your database schema itself. They create, alter, or remove the containers that hold data.

Common DDL commands:

- `CREATE TABLE` — defines a new table with columns and constraints
- `ALTER TABLE` — modifies table structure (add/drop columns, constraints, indexes)
- `DROP TABLE` — removes a table and its data
- `CREATE INDEX` — creates an index for query optimization
- `CREATE DATABASE` — creates a new database
- `TRUNCATE TABLE` — removes all rows from a table (faster than DELETE, non-recoverable in most systems)

DDL statements are **auto-committed** by default in most database systems — the changes take effect immediately and cannot be rolled back within a transaction. This is critical to understand when writing schema migration scripts.

Example:

``` sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE users ADD COLUMN last_login TIMESTAMP;

DROP TABLE users;
```

## DML: Data Manipulation Language

DML statements work with the data inside those structures. They insert, update, retrieve, or delete actual records.

Common DML commands:

- `SELECT` — retrieves data from one or more tables
- `INSERT` — adds new rows to a table
- `UPDATE` — modifies existing data
- `DELETE` — removes specific rows
- `MERGE` — combines INSERT and UPDATE operations (useful for upserts)

Unlike DDL, DML statements **are transactional** — you can wrap them in a transaction, make changes, and rollback if something goes wrong.

Example:

``` sql
INSERT INTO users (email) VALUES ('user@example.com');

UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE id = 1;

SELECT * FROM users WHERE created_at > NOW() - INTERVAL '7 days';

DELETE FROM users WHERE id = 42;
```

## Key Differences

| Aspect | DDL | DML |
|----|----|----|
| Purpose | Define/modify schema structure | Manipulate data within schema |
| Commits | Auto-committed, non-rollbackable | Transactional, can be rolled back |
| Examples | CREATE, ALTER, DROP | SELECT, INSERT, UPDATE, DELETE |
| Impact | Affects table definitions and metadata | Affects only the data |
| Lock behavior | May lock schema, blocking connections | Row/page locks depending on isolation level |

## Practical Considerations

When running DDL in production, be aware that some operations (like `ALTER TABLE ADD COLUMN` without a default) can lock tables on certain database engines. PostgreSQL handles this better than older MySQL versions, but it’s still worth testing on non-production first.

For DML, always use transactions when making related changes across multiple tables. A common pattern:

``` sql
BEGIN TRANSACTION;
INSERT INTO orders (user_id, total) VALUES (5, 99.99);
INSERT INTO order_items (order_id, product_id, qty) VALUES (LAST_INSERT_ID(), 42, 2);
COMMIT;
```

If either statement fails, both are rolled back, keeping your data consistent.

## Related: DCL and TCL

Two other command categories exist:

- **DCL (Data Control Language)** — controls permissions: `GRANT`, `REVOKE`
- **TCL (Transaction Control Language)** — manages transactions: `COMMIT`, `ROLLBACK`, `SAVEPOINT`

Understanding these distinctions helps you write safer, more predictable database code and makes troubleshooting schema and data issues much easier.
