---
title: "Updating String Values in MySQL with REPLACE()"
date: 2018-03-24 11:53:27 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-write-a-sql-to-replace-strings-in-a-column-in-a-mysql-database-table/
---

The `REPLACE()` function is your primary tool for modifying string values within a column. It scans for a substring and replaces all occurrences with a new value.

### Basic syntax

``` sql
UPDATE table_name
SET column_name = REPLACE(column_name, 'old_string', 'new_string')
WHERE condition;
```

### Simple example

Replace all instances of “old_domain” with “new_domain” in the `email` column:

``` sql
UPDATE users
SET email = REPLACE(email, 'old_domain.com', 'new_domain.com');
```

This updates every row. If you need to target specific records, add a WHERE clause:

``` sql
UPDATE users
SET email = REPLACE(email, 'old_domain.com', 'new_domain.com')
WHERE email LIKE '%old_domain.com%';
```

### Case-sensitive replacements

By default, `REPLACE()` is case-insensitive in MySQL. If you need case-sensitive matching, use `BINARY`:

``` sql
UPDATE users
SET email = REPLACE(BINARY email, 'OldValue', 'NewValue');
```

### Multiple replacements in one query

Chain multiple `REPLACE()` calls:

``` sql
UPDATE products
SET description = REPLACE(
  REPLACE(description, 'old_color', 'new_color'),
  'old_size', 'new_size'
);
```

### Using REGEXP for pattern-based replacement

For more complex patterns, use `REGEXP_REPLACE()` (available in MySQL 8.0+):

``` sql
UPDATE logs
SET message = REGEXP_REPLACE(message, '[0-9]{3}-[0-9]{4}', 'XXX-XXXX');
```

This masks phone numbers in a message column.

### Preview changes before updating

Always preview the changes first. Use a SELECT statement with the replacement logic:

``` sql
SELECT id, email, REPLACE(email, 'old_domain.com', 'new_domain.com') AS new_email
FROM users
WHERE email LIKE '%old_domain.com%';
```

Review the output before running the UPDATE.

### Performance considerations

On large tables, updates can lock resources. Consider:

- Adding a WHERE clause to limit the scope
- Running during low-traffic periods
- Using `LIMIT` for batch processing:

``` sql
UPDATE users
SET email = REPLACE(email, 'old_domain.com', 'new_domain.com')
WHERE email LIKE '%old_domain.com%'
LIMIT 1000;
```

Then repeat until all rows are updated.

### Replacing with NULL

To remove a substring by replacing it with nothing:

``` sql
UPDATE articles
SET title = REPLACE(title, 'deprecated_keyword', '');
```

To replace with NULL:

``` sql
UPDATE articles
SET title = REPLACE(title, 'deprecated_keyword', NULL);
```

### Working with multiple columns

Update several columns at once:

``` sql
UPDATE employees
SET first_name = REPLACE(first_name, 'John', 'Jon'),
    last_name = REPLACE(last_name, 'Smith', 'Smythe')
WHERE department_id = 5;
```

### Safe practices

1.  **Back up before bulk updates** — Always maintain a recent database backup.
2.  **Test on a development instance** — Verify the replacement logic doesn’t produce unexpected results.
3.  **Use transactions for safety** — Wrap large updates in a transaction so you can roll back if needed:

``` sql
START TRANSACTION;
UPDATE users
SET email = REPLACE(email, 'old_domain.com', 'new_domain.com')
WHERE email LIKE '%old_domain.com%';
-- Review the result, then:
COMMIT;
-- Or ROLLBACK; if something looks wrong
```

4.  **Log your changes** — Document what was replaced, when, and why for audit trails.
5.  **Verify after the update** — Run a SELECT query to confirm the replacements worked correctly:

``` sql
SELECT COUNT(*)
FROM users
WHERE email LIKE '%old_domain.com%';
```

This count should be zero after a successful replacement.

## 2026 Best Practices and Advanced Techniques

For Updating String Values in MySQL with REPLACE(), understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
