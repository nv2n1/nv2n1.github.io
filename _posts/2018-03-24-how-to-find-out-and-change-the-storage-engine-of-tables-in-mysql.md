---
title: "Checking and Changing MySQL Table Storage Engines"
date: 2018-03-24 08:17:32 +0000
layout: post
canonical: https://www.systutorials.com/how-to-find-out-and-change-the-storage-engine-of-tables-in-mysql/
---

To check which storage engine a table uses, query the `information_schema` database:

``` sql
SELECT ENGINE
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'database_name'
AND TABLE_NAME = 'table_name';
```

Replace `database_name` and `table_name` with your actual values.

You can also use the `SHOW TABLE STATUS` command for a quicker view:

``` sql
SHOW TABLE STATUS FROM database_name WHERE Name = 'table_name'\G
```

The `\G` formats output vertically, making the `Engine` field easier to read. To see all tables in a database and their engines at once:

``` sql
SHOW TABLE STATUS FROM database_name;
```

## Changing a Table’s Storage Engine

To convert a single table to a different engine:

``` sql
ALTER TABLE table_name ENGINE = InnoDB;
```

Common storage engines include `InnoDB` (default in modern MySQL/MariaDB), `MyISAM`, and `Archive`.

For large tables, this operation locks the table and can take significant time. To minimize impact on production systems, consider using online DDL if available:

``` sql
ALTER TABLE table_name ENGINE = InnoDB, ALGORITHM=INPLACE, LOCK=NONE;
```

Note: `ALGORITHM=INPLACE` requires sufficient free space and may not work for all engine conversions or table structures.

## Converting Multiple Tables

If you need to change the engine for many tables, generate the SQL statements dynamically:

``` sql
SELECT CONCAT('ALTER TABLE `', TABLE_NAME, '` ENGINE=InnoDB;')
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'database_name'
AND ENGINE != 'InnoDB';
```

Copy the output and execute it as a batch, or pipe it directly:

``` bash
mysql -u user -p database_name -e "SELECT CONCAT('ALTER TABLE \`', TABLE_NAME, '\` ENGINE=InnoDB;') FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'database_name' AND ENGINE != 'InnoDB';" | mysql -u user -p database_name
```

## Setting the Default Storage Engine

Configure the default engine in `/etc/mysql/mysql.conf.d/mysqld.cnf` (or `/etc/my.cnf` on some systems):

``` ini
[mysqld]
default-storage-engine = InnoDB
```

For MariaDB, use:

``` ini
[mysqld]
default-storage-engine = InnoDB
```

Restart MySQL/MariaDB after modifying the configuration:

``` bash
sudo systemctl restart mysql
```

You can also set it temporarily for the current session:

``` sql
SET DEFAULT_STORAGE_ENGINE = InnoDB;
```

## Considerations When Changing Engines

**InnoDB** is the modern standard for most workloads:

- ACID compliance and crash recovery
- Row-level locking for better concurrency
- Foreign key support
- Better for transactional workloads

**MyISAM** is legacy and rarely recommended:

- No transaction support
- Table-level locking
- Useful only for read-heavy, non-critical data

**Archive** is suitable for compressed historical data that’s rarely accessed.

When converting from MyISAM to InnoDB on a production system, plan for:

- Increased memory usage (InnoDB maintains a buffer pool)
- Longer conversion time for large tables
- Potential performance differences in queries

Verify the conversion succeeded by checking the engine again with `SHOW TABLE STATUS` before considering the migration complete.

## 2026 Best Practices

This article extends “Checking and Changing MySQL Table Storage Engines” with practical guidance. Modern development practices emphasize security, performance, and maintainability. Follow these guidelines to build robust, production-ready systems.

## 2026 Comprehensive Guide for MySQL

This article extends “Checking and Changing MySQL Table Storage Engines” with advanced techniques and best practices for 2026. Following modern guidelines ensures reliable, maintainable, and secure systems.

### Advanced Implementation Strategies

For complex deployments involving mysql, consider Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment.

### Security and Hardening

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data, and follow the principle of least privilege for access controls.

### Performance Optimization

- Monitor system resources continuously with htop, vmstat, iotop
- Use caching strategies to optimize performance
- Profile application performance before and after optimizations
- Optimize database queries with proper indexing

### Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce issues, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found.

### Best Practices

- Write clean, self-documenting code with clear comments
- Use version control effectively with meaningful commit messages
- Implement proper testing before deployment
- Monitor production systems and set up alerts

### Resources and Further Reading

For more information on mysql, consult official documentation and community resources. Stay updated with the latest tools and frameworks.
