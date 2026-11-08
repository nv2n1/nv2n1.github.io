---
title: "How to Set Up MySQL Replication"
date: 2018-03-24 08:18:01 +0000
layout: post
canonical: https://www.systutorials.com/how-to-set-up-mysql-replication/
---

MySQL replication lets you maintain synchronized copies of your database across multiple servers. This is essential for high availability, read scaling, and backups. Here’s how to configure it properly.

## Prerequisites

You need at least two MySQL instances: a primary (source) and one or more replicas. Both should run the same or compatible MySQL versions. MySQL 5.7+ and 8.0 are standard in 2026; if you’re stuck on older versions, plan an upgrade.

## Primary server configuration

On your primary MySQL instance, enable binary logging by editing `/etc/mysql/mysql.conf.d/mysqld.cnf`:

``` ini
[mysqld]
server-id = 1
log_bin = /var/log/mysql/mysql-bin.log
binlog_format = ROW
binlog_expire_logs_seconds = 604800
```

The `server-id` must be unique across all instances. Use `ROW` format for safer replication with triggers and functions. The `binlog_expire_logs_seconds` setting (here, 7 days) prevents disk space issues from old binary logs.

Restart MySQL:

``` bash
sudo systemctl restart mysql
```

Create a replication user on the primary:

``` sql
CREATE USER 'repl'@'replica_ip' IDENTIFIED BY 'strong_password';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'replica_ip';
FLUSH PRIVILEGES;
```

Check the current binary log position:

``` sql
SHOW MASTER STATUS;
```

Note the `File` and `Position` values — you’ll need these when setting up replicas.

## Replica server configuration

Edit the replica’s `/etc/mysql/mysql.conf.d/mysqld.cnf`:

``` ini
[mysqld]
server-id = 2
log_bin = /var/log/mysql/mysql-bin.log
relay-log = /var/log/mysql/mysql-relay-bin
relay-log-index = /var/log/mysql/mysql-relay-bin.index
read_only = ON
super_read_only = ON
```

Use `read_only` to prevent accidental writes. The `super_read_only` prevents even privileged users from writing.

Restart MySQL and configure replication:

``` sql
CHANGE REPLICATION SOURCE TO
  SOURCE_HOST = 'primary_ip',
  SOURCE_USER = 'repl',
  SOURCE_PASSWORD = 'strong_password',
  SOURCE_LOG_FILE = 'mysql-bin.000001',
  SOURCE_LOG_POS = 1234;

START REPLICA;
```

Replace the log file and position with values from `SHOW MASTER STATUS` on the primary. Verify replication is working:

``` sql
SHOW REPLICA STATUS\G
```

Look for `Replica_IO_Running: Yes` and `Replica_SQL_Running: Yes`. Any value in `Last_Error` indicates a problem.

## Running multiple instances on a single host

For testing or development, you can run multiple MySQL instances on the same server. Create separate data directories and socket files:

``` bash
sudo mkdir -p /var/lib/mysql_instance2
sudo chown mysql:mysql /var/lib/mysql_instance2
sudo chmod 750 /var/lib/mysql_instance2
```

Initialize the instance:

``` bash
sudo mysqld --initialize --datadir=/var/lib/mysql_instance2 --user=mysql
```

Create a separate systemd service file at `/etc/systemd/system/mysql@instance2.service`:

``` ini
[Unit]
Description=MySQL Instance %i
After=network.target

[Service]
Type=notify
User=mysql
Group=mysql
ExecStart=/usr/sbin/mysqld --defaults-file=/etc/mysql/instance2.cnf
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Create `/etc/mysql/instance2.cnf` with its own configuration:

``` ini
[mysqld]
server-id = 2
port = 3307
socket = /var/run/mysqld/mysqld_instance2.sock
datadir = /var/lib/mysql_instance2
pid-file = /var/run/mysqld/mysqld_instance2.pid
log_bin = /var/log/mysql/mysql-bin-instance2
relay-log = /var/log/mysql/mysql-relay-bin-instance2
```

Each instance needs a unique `port`, `server-id`, `socket`, and `datadir`.

Enable and start the second instance:

``` bash
sudo systemctl daemon-reload
sudo systemctl enable mysql@instance2
sudo systemctl start mysql@instance2
```

Connect using:

``` bash
mysql -u root -p -S /var/run/mysqld/mysqld_instance2.sock
```

Or specify the port:

``` bash
mysql -u root -p -h 127.0.0.1 -P 3307
```

## Monitoring replication

Check replica lag periodically:

``` sql
SHOW REPLICA STATUS\G
```

Monitor `Seconds_Behind_Master` — if it’s consistently high, investigate slow queries or network latency. Use `Performance_Schema` tables for deeper analysis:

``` sql
SELECT * FROM performance_schema.replication_applier_status_by_worker;
```

## Common issues

**Replication stops after a duplicate key error**: Set `slave_skip_errors` (MySQL 5.7) or handle via application logic. Better: fix the underlying issue and resync.

**Binary logs filling disk**: Adjust `binlog_expire_logs_seconds` based on your recovery window and disk space.

**High Seconds_Behind_Master**: Enable parallel replication with `replica_parallel_workers`:

``` sql
SET GLOBAL replica_parallel_workers = 4;
```

Run regular backups on replicas using `mysqldump` or `Percona XtraBackup` — replication is not a backup strategy.
