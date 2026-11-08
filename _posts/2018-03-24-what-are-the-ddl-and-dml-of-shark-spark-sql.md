---
title: "Spark SQL: DDL and DML Operations Explained"
date: 2018-03-24 11:44:30 +0000
author: "Eric Ma"
layout: post
categories: [development-best-practices]
canonical: /what-are-the-ddl-and-dml-of-shark-spark-sql/
---

Spark SQL doesn’t have a separate DDL/DML specification distinct from Hive QL — it inherits its SQL dialect directly from Hive. If you’re designing a SQL engine or looking to understand Spark SQL’s data definition and manipulation capabilities, you need to reference Hive’s DDL and DML documentation.

## Why Spark SQL Uses Hive QL

Spark SQL was built on top of Hive’s query execution layer, so it adopted HiveQL as its primary SQL dialect. This decision meant developers could leverage existing Hive metadata, tables, and ecosystem tools. While Spark SQL has since evolved with its own optimizer and execution engine, the SQL syntax remains fundamentally compatible with HiveQL.

## DDL Operations in Spark SQL

Data Definition Language (DDL) covers schema and metadata operations. Common DDL statements in Spark SQL include:

- **CREATE TABLE** — Define new tables with column types and constraints
- **ALTER TABLE** — Modify table structure, add/drop columns, rename tables
- **DROP TABLE** — Remove tables from the catalog
- **CREATE DATABASE** — Create schema namespaces
- **CREATE VIEW** — Define logical views over existing tables
- **TRUNCATE TABLE** — Remove all rows while preserving structure

Example:

``` sql
CREATE TABLE users (
  id INT,
  name STRING,
  email STRING,
  created_at TIMESTAMP
)
USING PARQUET
PARTITIONED BY (year INT);

ALTER TABLE users ADD COLUMN last_login TIMESTAMP;
DROP TABLE users;
```

Spark SQL also supports external tables, temporary views, and managed tables with different storage formats (Parquet, ORC, Delta Lake, CSV).

## DML Operations in Spark SQL

Data Manipulation Language (DML) covers data access and modification. Standard DML operations include:

- **SELECT** — Query data with filtering, aggregation, and joins
- **INSERT INTO** — Add rows to existing tables
- **INSERT OVERWRITE** — Replace table data
- **UPDATE** — Modify existing rows (available in Delta Lake)
- **DELETE** — Remove rows (available in Delta Lake)
- **WITH** — Common table expressions (CTEs) for complex queries

Example:

``` sql
INSERT INTO users (id, name, email, created_at)
VALUES (1, 'Alice', 'alice@example.com', CURRENT_TIMESTAMP);

SELECT name, COUNT(*) as login_count
FROM users
WHERE year = 2026
GROUP BY name
HAVING login_count > 5;

UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE id = 1;
```

## Key Differences from Standard SQL

Spark SQL’s HiveQL dialect has some quirks worth knowing:

- **String concatenation** uses `CONCAT()` function rather than `||` operator
- **LIMIT clause** is required for certain operations when running on distributed data
- **Subqueries** in FROM clauses work, but some correlated subqueries have limitations
- **Window functions** are well-supported (ROW_NUMBER, RANK, LAG, LEAD)
- **CASE expressions** follow standard SQL but have edge cases with NULL handling

## Modern Alternatives and Extensions

If you’re implementing a new SQL engine, consider that Spark SQL has evolved significantly. Modern Spark (3.x+) supports:

- **Delta Lake syntax** for ACID transactions (UPDATE, DELETE, MERGE)
- **Apache Iceberg** and **Apache Hudi** table formats with richer semantics
- **Structured Streaming** with incremental processing
- **Python/Scala/SQL unified APIs** via DataFrame operations

For current reference material, check the official <a href="https://spark.apache.org/docs/latest/sql-ref.html" rel="nofollow noopener" target="_blank">Apache Spark SQL documentation</a> rather than the older Shark paper. The Spark SQL reference has been maintained and updated far beyond Shark’s original design.

If you’re building a SQL language implementation, study both Spark SQL’s execution model and the broader SQL standardization efforts. Spark’s approach prioritizes distributed execution over strict SQL compliance, which is a deliberate trade-off worth understanding for your own design decisions.
