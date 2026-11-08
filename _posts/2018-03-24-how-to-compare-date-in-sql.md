---
title: "Comparing Dates in SQL: A Practical Guide"
date: 2018-03-24 11:53:09 +0000
layout: post
canonical: https://www.systutorials.com/how-to-compare-date-in-sql/
---

Date comparison is one of the most common operations in SQL queries, whether you’re filtering orders, analyzing logs, or generating reports. The approach varies slightly across database systems, but the underlying principles remain consistent.

## Basic Date Comparison

The simplest form uses standard comparison operators against a date string in `YYYY-MM-DD` format:

``` sql
SELECT * FROM orders WHERE order_date > '2025-01-01';
```

This works across most SQL databases, but there’s an important performance caveat: comparing directly against a string allows the database query planner to use indexes on the `order_date` column. However, if you need to extract or manipulate the date component, wrapping the column in a function can prevent index usage.

## Database-Specific Approaches

### PostgreSQL

PostgreSQL handles dates flexibly. Cast strings explicitly to avoid ambiguity:

``` sql
-- Direct comparison (recommended, uses index)
SELECT * FROM orders WHERE order_date > '2025-01-01'::date;

-- Extract date component from timestamp
SELECT * FROM orders WHERE order_date::date = '2025-01-01';

-- Using DATE function
SELECT * FROM orders WHERE DATE(order_date) = '2025-01-01';
```

When comparing `timestamp` columns against dates, the cast approach is cleanest and preserves index efficiency.

### MySQL / MariaDB

``` sql
-- Direct string comparison (uses index)
SELECT * FROM orders WHERE order_date > '2025-01-01';

-- Extract date from datetime column
SELECT * FROM orders WHERE DATE(order_date) = '2025-01-01';

-- Time-aware comparison
SELECT * FROM orders WHERE order_date >= '2025-01-01 00:00:00';
```

With MySQL, wrapping a column in `DATE()` creates a function call that may prevent index usage. If you’re filtering by a full date range, use explicit timestamp boundaries instead.

### SQLite

``` sql
-- Date string comparison
SELECT * FROM orders WHERE order_date > '2025-01-01';

-- Using date() function
SELECT * FROM orders WHERE date(order_date) = '2025-01-01';

-- ISO 8601 format (recommended)
SELECT * FROM orders WHERE order_date >= '2025-01-01' 
  AND order_date < '2025-01-02';
```

SQLite stores dates as strings or Julian day numbers depending on your schema. The ISO 8601 format (`YYYY-MM-DD`) is most portable.

## Range Comparisons

For date ranges, use explicit boundaries instead of functions:

``` sql
-- Efficient: allows index usage
SELECT * FROM orders 
WHERE order_date >= '2025-01-01' 
  AND order_date < '2025-02-01';

-- Less efficient: function prevents index optimization
SELECT * FROM orders 
WHERE MONTH(order_date) = 1 
  AND YEAR(order_date) = 2025;
```

The first approach lets the database use indexes; the second forces a full table scan.

## Relative Date Comparisons

### PostgreSQL

``` sql
SELECT * FROM orders 
WHERE order_date > NOW() - INTERVAL '30 days';

SELECT * FROM orders 
WHERE order_date::date = CURRENT_DATE;
```

### MySQL

``` sql
SELECT * FROM orders 
WHERE order_date > DATE_SUB(NOW(), INTERVAL 30 DAY);

SELECT * FROM orders 
WHERE DATE(order_date) = CURDATE();
```

### SQLite

``` sql
SELECT * FROM orders 
WHERE order_date > date('now', '-30 days');

SELECT * FROM orders 
WHERE date(order_date) = date('now');
```

## NULL Handling

Dates can be NULL, and comparisons with NULL always return unknown:

``` sql
-- This won't include NULL dates
SELECT * FROM orders WHERE order_date > '2025-01-01';

-- Explicitly handle NULLs if needed
SELECT * FROM orders 
WHERE order_date > '2025-01-01' 
   OR order_date IS NULL;

-- Coalesce to a default date
SELECT * FROM orders 
WHERE COALESCE(order_date, '1900-01-01') > '2025-01-01';
```

## Performance Best Practices

- **Avoid functions on columns**: `DATE(column) = value` prevents index usage. Use range comparisons instead.
- **Use indexes**: Ensure date columns have indexes for frequent comparisons.
- **Store consistently**: Use `DATE` for date-only values and `TIMESTAMP` or `DATETIME` for date+time to avoid unnecessary conversions.
- **Test your queries**: Use `EXPLAIN` or `EXPLAIN PLAN` to verify index usage on your specific database.

``` sql
-- PostgreSQL: check index usage
EXPLAIN SELECT * FROM orders WHERE order_date > '2025-01-01';

-- MySQL: check index usage
EXPLAIN SELECT * FROM orders WHERE order_date > '2025-01-01'\G
```
