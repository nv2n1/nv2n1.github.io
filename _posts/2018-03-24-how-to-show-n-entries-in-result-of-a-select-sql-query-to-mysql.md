---
title: "Limit SQL Query Results to N Rows in MySQL"
date: 2018-03-24 11:53:09 +0000
author: "David Yang"
layout: post
canonical: https://www.systutorials.com/how-to-show-n-entries-in-result-of-a-select-sql-query-to-mysql/
---

The `LIMIT` clause in MySQL lets you control how many rows a `SELECT` query returns. This is essential for pagination, performance tuning, and working with large datasets.

### Basic LIMIT Syntax

To return only the first N rows from a table:

``` sql
SELECT * FROM qa_users LIMIT 10;
```

This returns the first 10 rows from the `qa_users` table. Simple and straightforward.

### LIMIT with OFFSET

When you need to skip rows (for pagination), combine `LIMIT` with `OFFSET`:

``` sql
SELECT * FROM qa_users LIMIT 10 OFFSET 20;
```

This skips the first 20 rows and returns the next 10 rows (rows 21-30). This is commonly written as:

``` sql
SELECT * FROM qa_users LIMIT 20, 10;
```

Both syntaxes are equivalent — `LIMIT offset, count` is just older notation. The explicit `OFFSET` keyword is clearer and recommended.

### Practical Example: Pagination

If you’re building a paginated API returning 50 results per page:

``` sql
-- Page 1 (rows 1-50)
SELECT id, username, email FROM qa_users LIMIT 50 OFFSET 0;

-- Page 2 (rows 51-100)
SELECT id, username, email FROM qa_users LIMIT 50 OFFSET 50;

-- Page 3 (rows 101-150)
SELECT id, username, email FROM qa_users LIMIT 50 OFFSET 100;
```

With filtering and ordering:

``` sql
SELECT id, username, email, created_at 
FROM qa_users 
WHERE status = 'active' 
ORDER BY created_at DESC 
LIMIT 25 OFFSET 0;
```

### Performance Considerations

- Use `LIMIT` with indexed columns in your `WHERE` and `ORDER BY` clauses for best performance
- For large offsets (e.g., `OFFSET 1000000`), queries slow down significantly because MySQL still scans and discards all preceding rows. Use keyset pagination for better performance:

``` sql
SELECT id, username, email FROM qa_users 
WHERE id > :last_id 
ORDER BY id 
LIMIT 50;
```

This approach uses the last row’s ID instead of an offset, which is much faster on large tables.

### Database-Specific Alternatives

Different databases use different syntax:

- **PostgreSQL**: `LIMIT 10 OFFSET 20` (same as MySQL, but also supports `FETCH NEXT 10 ROWS ONLY`)
- **SQL Server**: `OFFSET 20 ROWS FETCH NEXT 10 ROWS ONLY` (or older `TOP 10` for just limiting without offset)
- **SQLite**: `LIMIT 10 OFFSET 20`
- **Oracle Database**: `OFFSET 20 ROWS FETCH NEXT 10 ROWS ONLY` (modern versions; older versions required subqueries with ROWNUM)

### LIMIT with ORDER BY

Always combine `LIMIT` with `ORDER BY` when order matters:

``` sql
SELECT * FROM qa_users ORDER BY username ASC LIMIT 5;
```

Without `ORDER BY`, the database returns 5 rows in whatever order is fastest internally — usually insertion order, but not guaranteed.

### Getting the Total Count

When paginating, you typically need the total row count for UI purposes:

``` sql
SELECT COUNT(*) as total FROM qa_users WHERE status = 'active';
SELECT id, username FROM qa_users WHERE status = 'active' LIMIT 50 OFFSET 0;
```

Run both queries: the first tells you how many pages exist, the second returns your paginated data.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Limit SQL Query Results to N Rows in MySQL with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for Limit SQL Query Results to N Rows in MySQL. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
