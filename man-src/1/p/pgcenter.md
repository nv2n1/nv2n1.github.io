---
title: "pgcenter(1)"
name: "pgcenter"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgcenter/"
description: "pgcenter – is the PostgreSQL administration console with top-like monitoring."
---

<h2>NAME</h2>
<p> pgcenter &#8211; is the PostgreSQL administration console with top-like monitoring.</p>
<h2>SYNOPSIS</h2>
<p> <code>pgcenter</code> [OPTION]&#8230; [DBNAME [USERNAME]] </p>
<h2>DESCRIPTION</h2>
<p> <code>PostgreSQL</code> provides various statistics which includes information about tables, indexes, functions and other database objects and their usage. Moreover, statistics has information about connections, current queries and database operations (INSERT/DELETE/UPDATE). But most of this statistics are provided as permanently incremented counters. The <code>pgcenter</code> provides convenient interface to this statistics and allow viewing statistics changes in time interval, eg. per second. The <code>pgcenter</code> provides fast access for database management task, such as editing configuration files, reloading services, viewing log files and canceling or terminating database backends (by pid or using state mask). However if need execute some specific operations, pgcenter can start psql session for this purposes. </p>
<p> The <code>pgcenter</code> uses <i>screens</i> and <i>contexts</i>. Screen is a special area for displaying statistics. Number of screen limited by eight. Context is the type of displayed statistics: table statistics, index statistics, functions statistics, replication statistics, etc. </p>
<p> All operations in pgcenter realized through hotkeys. </p>
<p> When <code>pgcenter</code> starts it using the connection parameters transmitted directly through the arguments, or use a connection file that describes the connections options. For each connection is allocated a separate screen. When the arguments and connections file used together, connect options from arguments always starts in the firts screen. If the arguments or connections file is not specified, <code>pgcenter</code> use default connection settings. </p>
<p> The <code>pgcenter</code> main window divided into 3 window: <i>SUMMARY</i>, <i>CMDLINE</i>, <i>DBRESULT</i> and optional <i>LOGTAIL</i> window which hidden by default and appears only by user command. </p>
<h2>COMMAND-LINE OPTIONS</h2>
<p> The command-line syntax for pgcenter consists of:</p>
<dl>
<dt>-h, &#8211;host=HOSTNAME</p>
<dd> PostgreSQL server host or socket directory (default: &quot;/tmp&quot;).</p>
<dt>-p, &#8211;port=PORT</p>
<dd> PostgreSQL server port (default: &quot;5432&quot;).</p>
<dt>-U, &#8211;username=USERNAME</p>
<dd> PostgerSQL user name (default: &quot;current logged user&quot;).</p>
<dt>-d, &#8211;dbname=DBNAME</p>
<dd> PostgreSQL administrative database name (default: &quot;pgbouncer&quot;).</p>
<dt>-f, &#8211;file=FILENAME</p>
<dd> Use connections information from file. By default, pgcenter when starting, trying read <i>~/.pgcenterrc</i> connections file. This behaviour can be overriden with this option.</p>
<dt>-w, &#8211;no-password</p>
<dd> Never prompt for password.</p>
<dt>-W, &#8211;password</p>
<dd> Force password prompt (should happen automatically).</p>
<dt>-?, &#8211;help</p>
<dd> Show this help, then exit.</p>
<dt>-V, &#8211;version</p>
<dd> Print version, then exit. </p>
</dl>
<h2>SUMMARY WINDOW</h2>
<p> Summary window always displayed and provides various information about system load and current connected PostgreSQL. </p>
<dl>
<dt><code>Current Time and Load Average</code></p>
<dd> Line 1-1 shows program name, current time, system load avg over the last 1, 5 and 15 minutes. </p>
<dt><code>CPU Usage</code></p>
<dd> Line 1-2 shows CPU usage percentages based on the interval since the last refresh. </p>
<p> <code>us, user</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Percentage of CPU utilization that occurred while executing at the user level (application).</dl>
<p> <code>sy, system</code></p>
<dl>
<dt>
<dd> Percentage of CPU utilization that occurred while executing at the system level (kernel).</dl>
<p> <code>ni, nice</code></p>
<dl>
<dt>
<dd> Percentage of CPU utilization that occurred while executing at the user level with nice priority.</dl>
<p> <code>id, idle</code></p>
<dl>
<dt>
<dd> Percentage of time that the CPU or CPUs were idle and the system did not have an outstanding disk I/O request.</dl>
<p> <code>wa, iowait</code></p>
<dl>
<dt>
<dd> Percentage of time that the CPU or CPUs were idle during which the system had an outstanding disk I/O request.</dl>
<p> <code>hi, hardirq</code></p>
<dl>
<dt>
<dd> Percentage of time that the CPU or CPUS spent servicing hardware interrupts.</dl>
<p> <code>si, softirq</code></p>
<dl>
<dt>
<dd> Percentage of time thatthe CPU or CPUS spent servicing software interrupts.</dl>
<p> <code>st, steal</code></p>
<dl>
<dt>
<dd> Percentage of time spent in involuntary wait by the virtual CPU or CPUs while the hypervisor was servicing another virtual processor.</dl>
</dl>
<dt><code>CPU Usage</code></p>
<dd> Line 1-3 shows memory and line 1-4 shows swap usage based on the interval since the last refresh. </p>
<p> <code>total</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Total amount of RAM or swap in MiB (mebibyte = 1024 KiB = 1,048,576 bytes).</dl>
<p> <code>free</code></p>
<dl>
<dt>
<dd> Total amount of free RAM or swap in MiB (mebibyte = 1024 KiB = 1,048,576 bytes).</dl>
<p> <code>used</code></p>
<dl>
<dt>
<dd> Total amount of used RAM or swap in MiB (mebibyte = 1024 KiB = 1,048,576 bytes).</dl>
<p> <code>buff/cached</code></p>
<dl>
<dt>
<dd> Total amount of cached and buffered RAM in MiB (mebibyte = 1024 KiB = 1,048,576 bytes).</dl>
<p> <code>dirty/writeback</code></p>
<dl>
<dt>
<dd> Total ammount of dirty memory which is waiting to be written back to the disk. And total amount of memory actively being written back to the disk. Values are in MiB (mebibyte = 1024 KiB = 1,048,576 bytes).</dl>
</dl>
<dt><code>Connection information</code></p>
<dd> Line 2-1 shows connection information to the current PostgreSQL: </p>
<p> <code>conn</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Current screen number (from 1 to 8) and connection status.</dl>
<p> <code>conninfo</code></p>
<dl>
<dt>
<dd> Current connection information with following format: <code>host:port</code> <code>username [at] dbname</code>.</dl>
<p> <code>postgresql version</code></p>
<dl>
<dt>
<dd> Version of the PostgreSQL.</dl>
<p> <code>uptime</code></p>
<dl>
<dt>
<dd> Uptime of PostgreSQL service.</dl>
<dl>
<dt>
<dd> Used query: SELECT now() &#8211; pg_postmaster_start_time();</dl>
</dl>
<dt><code>Summary activity</code></p>
<dd> Line 2-2 shows current PostgreSQL connections grouped by their states. </p>
<p> <code>total</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Total connections number.</dl>
<dl>
<dt>
<dd> Used query: SELECT count(*) FROM pg_stat_activity;</dl>
<p> <code>idle</code></p>
<dl>
<dt>
<dd> Number of backends in <code>idle</code> state which is waiting for a new client command.</dl>
<dl>
<dt>
<dd>
<pre>
Used query: SELECT count(*) FROM pg_stat_activity 
            WHERE state = 'idle';
</pre>
</dl>
<p> <code>idle_in_xact</code></p>
<dl>
<dt>
<dd> Number of backends in <code>idle in transaction</code> means the backend is in a transaction, but is not currently executing a query, and <code>idle in transaction (aborted)</code> which is similar to idle in transaction, except one of the statements in the transaction caused an error.</dl>
<dl>
<dt>
<dd>
<pre>
Used query: SELECT count(*) FROM pg_stat_activity 
            WHERE state IN ('idle in transaction', 'idle in transaction (aborted)');
</pre>
</dl>
<p> <code>active</code></p>
<dl>
<dt>
<dd> Number of backends in <code>active</code> state when backends is executing a queries.</dl>
<dl>
<dt>
<dd>
<pre>
Used query: SELECT count(*) FROM pg_stat_activity 
            WHERE state = 'active';
</pre>
</dl>
<p> <code>waiting</code></p>
<dl>
<dt>
<dd> Number of backends which is currently waiting on a lock.</dl>
<dl>
<dt>
<dd>
<pre>
Used query: SELECT count(*) FROM pg_stat_activity 
            WHERE waiting;
</pre>
</dl>
<p> <code>others</code></p>
<dl>
<dt>
<dd> Number of backends with <code>fastpath function call</code> state which executes fast-path functions and <code>disabled</code> state which is reported only if <i>track_activities</i> is disabled in backend.</dl>
<dl>
<dt>
<dd>
<pre>
Used query: SELECT count(*) FROM pg_stat_activity 
            WHERE state IN ('fastpath function call','disabled');
</pre>
</dl>
</dl>
<dt><code>Autovacuum activity</code></p>
<dd> Line 2-3 shows current PostgreSQL autovacuum activity. </p>
<p> <code>workers</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Total number of autovacuum workers currently running.</dl>
<p> <code>max</code></p>
<dl>
<dt>
<dd> Max number of allowed autovacuum workers.</dl>
<p> <code>manual</code></p>
<dl>
<dt>
<dd> Total number of vacuum workers started by user.</dl>
<p> <code>wraparound</code></p>
<dl>
<dt>
<dd> Total number of workers currently running and perform anti wraparound vacuum.</dl>
<p> <code>avw_maxtime</code></p>
<dl>
<dt>
<dd> Execution time of the oldest autovacuum or user-started worker.</dl>
</dl>
<dt><code>Statements activity</code></p>
<dd> Line 2-4 shows statements activity. Some information provided by <i>pg_stat_statements</i> contrib module which not installed by default. For proper work, <i>pg_stat_statements</i> must be installed into database. For more information see URLS sections below. </p>
<p> <code>stmt/s</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Number of statements per second. This value calculated as difference between two values within 1 second interval.</dl>
<dl>
<dt>
<dd>
<pre>
Used query: SELECT sum(calls) FROM pg_stat_statements;
</pre>
</dl>
<p> <code>stmt_avgtime</code></p>
<dl>
<dt>
<dd> Average queries duration in milisecond. Result defines here present the average time since the start of statistics collection. Therefore, to obtain a result that corresponds to the current time, pg_stat_statements statistics should be periodically reset (once a day, for example).</dl>
<dl>
<dt>
<dd>
<pre>
Used query: SELECT (sum(total_time) / sum(calls))::numeric(6,3) AS avg_query 
            FROM pg_stat_statements;
</pre>
</dl>
<p> <code>xact_maxtime</code></p>
<dl>
<dt>
<dd> Execution time of the oldest transaction (not a query or session).</dl>
<dl>
<dt>
<dd>
<pre>
Used query: SELECT coalesce(date_trunc('seconds', max(now() - xact_start)), '00:00:00')
            FROM pg_stat_activity;
</pre>
</dl>
</dl>
</dl>
<h2>CMDLINE WINDOW</h2>
<p> Cmdline window used for displaying diagnostic messages or when need additional input from user. </p>
<h2>DBRESULT WINDOW</h2>
<p> Dbresult window used for displaying statistics from PostgreSQL. Here <i>pgcenter</i> uses statistics contexts, which determines what type of statistics will be shown. </p>
<dl>
<dt><code>pg_stat_database context</code></p>
<dd> Statistics from <i>pg_stat_database</i> system view which show database-wide statistics. Note, when new database created or existing database dropped, <i>pgcenter</i> resets it&#8217;s own counters (not postgresql statistics counters) to zero. </p>
<pre>
Used query: SELECT 
                datname, 
                xact_commit AS commit, xact_rollback AS rollback, 
                blks_read AS reads, blks_hit AS hits,
                tup_returned AS returned, tup_fetched AS fetched, 
                tup_inserted AS inserts, tup_updated AS updates, tup_deleted AS deletes, 
                conflicts, deadlocks, 
                temp_files AS tmp_files, temp_bytes AS tmp_bytes, 
                blk_read_time AS read_t, blk_write_time AS write_t 
            FROM pg_stat_database ORDER BY datname;
</pre>
<p> <code>datname</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Name of this database.</dl>
<p> <code>commit</code></p>
<dl>
<dt>
<dd> Number of transactions per second in this database that have been committed.</dl>
<p> <code>rollback</code></p>
<dl>
<dt>
<dd> Number of transactions per second in this database that have been rolled back.</dl>
<p> <code>reads</code></p>
<dl>
<dt>
<dd> Number of disk blocks read per second in this database.</dl>
<p> <code>hits</code></p>
<dl>
<dt>
<dd> Number of times per second when disk blocks were found already in the buffer cache, so that a read was not necessary (this only includes hits in the PostgreSQL buffer cache, not the operating system&#8217;s file system cache).</dl>
<p> <code>returned</code></p>
<dl>
<dt>
<dd> Number of rows returned by queries in this database (per second).</dl>
<p> <code>fetched</code></p>
<dl>
<dt>
<dd> Number of rows fetched by queries in this database (per second).</dl>
<p> <code>inserts</code></p>
<dl>
<dt>
<dd> Number of rows inserted by queries in this database (per second).</dl>
<p> <code>updates</code></p>
<dl>
<dt>
<dd> Number of rows updated by queries in this database (per second).</dl>
<p> <code>deletes</code></p>
<dl>
<dt>
<dd> Number of rows deleted by queries in this database (per second).</dl>
<p> <code>conflicts</code></p>
<dl>
<dt>
<dd> Number of queries per second canceled due to conflicts with recovery in this database. Conflicts occur only on standby servers.</dl>
<p> <code>deadlocks</code></p>
<dl>
<dt>
<dd> Number of deadlocks detected in this database (per second).</dl>
<p> <code>tmp_files</code></p>
<dl>
<dt>
<dd> Number of temporary files created by queries in this database (pre second). All temporary files are counted, regardless of why the temporary file was created (e.g., sorting or hashing), and regardless of the <i>log_temp_files</i> setting.</dl>
<p> <code>tmp_bytes</code></p>
<dl>
<dt>
<dd> Total amount of data written to temporary files by queries in this database (per second). All temporary files are counted, regardless of why the temporary file was created, and regardless of the <i>log_temp_files</i> setting.</dl>
<p> <code>read_t</code></p>
<dl>
<dt>
<dd> Time spent reading data file blocks by backends in this database, in milliseconds.</dl>
<p> <code>write_t</code></p>
<dl>
<dt>
<dd> Time spent writing data file blocks by backends in this database, in milliseconds.</dl>
</dl>
<dt><code>pg_stat_replication context</code></p>
<dd> Statistics from <i>pg_stat_replication</i> system view which will contain one row per WAL sender process, showing statistics about replication to that sender&#8217;s connected standby server. Only directly connected standbys are listed; no information is available about downstream standby servers. </p>
<pre><code>
Used query : SELECT
                 client_addr AS client,
             usename AS user,
             application_name AS name,
             state,
             sync_state AS mode,
             (pg_xlog_location_diff(pg_current_xlog_location(), sent_location) / 1024)::int as pending,
             (pg_xlog_location_diff(sent_location, write_location) / 1024)::int as write,
             (pg_xlog_location_diff(write_location, flush_location) / 1024)::int as flush,
             (pg_xlog_location_diff(flush_location, replay_location) / 1024)::int as replay,
             (pg_xlog_location_diff(pg_current_xlog_location(), replay_location))::int / 1024 as total_lag
                 FROM pg_stat_replication "
</code></pre>
<p> <code>client</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> IP address of the client connected to this WAL sender. If this field is null, it indicates that the client is connected via a Unix socket on the server machine.</dl>
<p> <code>user</code></p>
<dl>
<dt>
<dd> Name of the user logged into this WAL sender process.</dl>
<p> <code>name</code></p>
<dl>
<dt>
<dd> Name of the application that is connected to this WAL sender.</dl>
<p> <code>state</code></p>
<dl>
<dt>
<dd> Current WAL sender state.</dl>
<p> <code>mode</code></p>
<dl>
<dt>
<dd> Synchronous state of this standby server.</dl>
<p> <code>pending</code></p>
<dl>
<dt>
<dd> Difference between XLOG current position and XLOG sent position, shows amount of XLOG in kilobytes which should be sent over network.</dl>
<p> <code>write</code></p>
<dl>
<dt>
<dd> Difference between XLOG sent position and XLOG write position, shows amount of XLOG in kilobytes which sent over network, but not written yet on remote host.</dl>
<p> <code>flush</code></p>
<dl>
<dt>
<dd> Difference between XLOG write position and XLOG flush position, shows amount of XLOG in kilobytes which written, but not flushed yet on remote host.</dl>
<p> <code>replay</code></p>
<dl>
<dt>
<dd> Difference between XLOG flush position and XLOG replay position, shows amount of XLOG in kilobytes which flushed, but not replayed yet on remote host.</dl>
<p> <code>total_lag</code></p>
<dl>
<dt>
<dd> Difference between XLOG current position on the master server and XLOG replay position onremote host, shows the total amount of XLOG in kilobytes, the standby is behind.</dl>
</dl>
<dt><code>pg_stat_tables context</code></p>
<dd> Statistics from <i>pg_stat_user_tables</i> or <i>pg_stat_all_tables</i> views which will contain one row for each table in the current database (including TOAST tables), showing statistics about accesses to that specific table. <i>pg_stat_user_tables</i> used by default, and <i>pgcenter </i> can be switched to <i>pg_stat_all_tables</i> using <code>,</code> hotkey. </p>
<pre>
Used query: SELECT
                schemaname || '.' || relname AS relation,
                seq_scan, seq_tup_read AS seq_read,
                idx_scan, idx_tup_fetch AS idx_fetch,
                n_tup_ins AS inserts, n_tup_upd AS updates,
                n_tup_del AS deletes, n_tup_hot_upd AS hot_updates,
                n_live_tup AS live, n_dead_tup AS dead
            FROM pg_stat_user_tables ORDER BY 1;
</pre>
<p> <code>relation</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Name of this table including schemaname.</dl>
<p> <code>seq_scan</code></p>
<dl>
<dt>
<dd> Number of sequential scans initiated on this table (per second).</dl>
<p> <code>seq_read</code></p>
<dl>
<dt>
<dd> Number of live rows fetched by sequential scans (per second).</dl>
<p> <code>idx_scan</code></p>
<dl>
<dt>
<dd> Number of index scans initiated on this table (per second).</dl>
<p> <code>idx_fetch</code></p>
<dl>
<dt>
<dd> Number of live rows fetched by index scans (per second).</dl>
<p> <code>inserts</code></p>
<dl>
<dt>
<dd> Number of rows inserted (per second).</dl>
<p> <code>updates</code></p>
<dl>
<dt>
<dd> Number of rows updated (per second).</dl>
<p> <code>deletes</code></p>
<dl>
<dt>
<dd> Number of rows deleted (per second).</dl>
<p> <code>hot_updates</code></p>
<dl>
<dt>
<dd> Number of rows HOT updated means with no separate index update required (per second).</dl>
<p> <code>live</code></p>
<dl>
<dt>
<dd> Estimated number of live rows (per second).</dl>
<p> <code>dead</code></p>
<dl>
<dt>
<dd> Estimated number of dead rows (per second).</dl>
</dl>
<dt><code>pg_statio_tables context</code></p>
<dd> Show statistics from <i>pg_statio_user_tables</i> or <i>pg_statio_all_tables </i> views which showing statistics about I/O on that specific table in the current database. <i>pg_statio_user_tables</i> used by default, and <i>pgcenter</i> can be switched to <i>pg_statio_all_tables</i> using <code>, </code> hotkey.<br />
Used query : SELECT<br />
                 schemaname ||<br />
             &#8216;.&#8217; || relname AS relation,<br />
    heap_blks_read *(SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) AS heap_read,<br />
    heap_blks_hit *(SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) AS heap_hit,<br />
    idx_blks_read *(SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) AS idx_read,<br />
    idx_blks_hit *(SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) AS idx_hit,<br />
    toast_blks_read *(SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) AS toast_read,<br />
    toast_blks_hit *(SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) AS toast_hit,<br />
    tidx_blks_read *(SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) AS tidx_read,<br />
    tidx_blks_hit *(SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) AS tidx_hit<br />
    FROM pg_statio_user_tables ORDER BY 1;</p>
<p> <code>relation</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Name of this table including schemaname.</dl>
<p> <code>heap_read</code></p>
<dl>
<dt>
<dd> Number of data read from disk related to this table in kilobytes per second.</dl>
<p> <code>heap_hit</code></p>
<dl>
<dt>
<dd> Number of buffer hits in this table in kilobytes per second.</dl>
<p> <code>idx_read</code></p>
<dl>
<dt>
<dd> Number of data read from disk in kilobytes per second related to all indexes on this table.</dl>
<p> <code>idx_hit</code></p>
<dl>
<dt>
<dd> Number of buffer hits in all indexes on this table in kilobytes per second.</dl>
<p> <code>toast_read</code></p>
<dl>
<dt>
<dd> Number of data read from disk in kilobytes per second from this table&#8217;s TOAST table (if any).</dl>
<p> <code>toast_hit</code></p>
<dl>
<dt>
<dd> Number of buffer hits in this table&#8217;s TOAST table (if any) in kilobytes per second.</dl>
<p> <code>tidx_read</code></p>
<dl>
<dt>
<dd> Number of data read from disk in kilobytes per second from this table&#8217;s TOAST table indexes (if any).</dl>
<p> <code>tidx_hit</code></p>
<dl>
<dt>
<dd> Number of buffer hits in this table&#8217;s TOAST table indexes (if any) in kilobytes per second.</dl>
</dl>
<dt><code>pg_stat_indexes context</code></p>
<dd> Show statistics from <i>pg_stat_user_indexes</i> and <i>pg_statio_user_indexes</i> (or <i>pg_stat_all_indexes</i> and <i>pg_statio_all_indexes</i>). The <i>pg_stat_user_indexes</i> view will contain one row for each index in the current database, showing statistics about accesses to that specific index. <i>pg_statio_user_indexes</i> view will contain one row for each index in the current database, showing statistics about I/O on that specific index. </p>
<p> Note: Indexes can be used via either simple index scans or &quot;bitmap&quot; index scans. In a bitmap scan the output of several indexes can be combined via AND or OR rules, so it is difficult to associate individual heap row fetches with specific indexes when a bitmap scan is used. Therefore, a bitmap scan increments the <i>pg_stat_all_indexes.idx_tup_read </i> count(s) for the index(es) it uses, and it increments the <i>pg_stat_all_tables.idx_tup_fetch </i> count for the table, but it does not affect <i>pg_stat_all_indexes.idx_tup_fetch</i>. The <i>idx_tup_read </i> and <i>idx_tup_fetch </i> counts can be different even without any use of bitmap scans, because <i>idx_tup_read </i> counts index entries retrieved from the index while <i>idx_tup_fetch </i> counts live rows fetched from the table. The latter will be less if any dead or not-yet-committed rows are fetched using the index, or if any heap fetches are avoided by means of an index-only scan.<br />
Used query : SELECT<br />
                 s.schemaname ||<br />
    &#8216;.&#8217; || s.relname as relation,<br />
    s.indexrelname AS index,<br />
    s.idx_scan, s.idx_tup_read, s.idx_tup_fetch,<br />
    i.idx_blks_read *(SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) AS idx_read,<br />
    i.idx_blks_hit *(SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) AS idx_hit<br />
    FROM<br />
    pg_stat_user_indexes s,<br />
    pg_statio_user_indexes i<br />
    WHERE s.indexrelid = i.indexrelid ORDER BY 1;</p>
<p> <code>relation</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Name of the table for this index including schemaname.</dl>
<p> <code>index</code></p>
<dl>
<dt>
<dd> Name of this index.</dl>
<p> <code>idx_scan</code></p>
<dl>
<dt>
<dd> Number of index scans per second initiated on this index.</dl>
<p> <code>idx_tup_read</code></p>
<dl>
<dt>
<dd> Number of index entries returned per second by scans on this index.</dl>
<p> <code>idx_tup_fetch</code></p>
<dl>
<dt>
<dd> Number of live table rows fetched per second by simple index scans using this index.</dl>
<p> <code>idx_read</code></p>
<dl>
<dt>
<dd> Number of disk blocks read per second from this index.</dl>
<p> <code>idx_hit</code></p>
<dl>
<dt>
<dd> Number of buffer hits per second in this index.</dl>
</dl>
<dt><code>pg_tables_size context</code></p>
<dd> Show statistics about tables sizes. For taking information about size of relations use <i>pg_stat_user_tables</i> (or <i>pg_stat_all_tables</i>) view, <i>pg_class</i> system catalog and <i>pg_relation_size()</i>, <i>pg_total_relation_size()</i> functions.<br />
Used query : SELECT<br />
                 s.schemaname ||<br />
    &#8216;.&#8217; || s.relname AS relation,<br />
    pg_total_relation_size((s.schemaname || &#8216;.&#8217; || s.relname)::regclass) / 1024 AS total_size,<br />
    pg_relation_size((s.schemaname || &#8216;.&#8217; || s.relname)::regclass) / 1024 AS rel_size,<br />
    (pg_total_relation_size((s.schemaname || &#8216;.&#8217; || s.relname)::regclass) / 1024) &#8211;<br />
        (pg_relation_size((s.schemaname || &#8216;.&#8217; || s.relname)::regclass) / 1024) AS idx_size,<br />
    pg_total_relation_size((s.schemaname || &#8216;.&#8217; || s.relname)::regclass) / 1024 AS total_change,<br />
    pg_relation_size((s.schemaname || &#8216;.&#8217; || s.relname)::regclass) / 1024 AS rel_change,<br />
    (pg_total_relation_size((s.schemaname || &#8216;.&#8217; || s.relname)::regclass) / 1024) &#8211;<br />
        (pg_relation_size((s.schemaname || &#8216;.&#8217; || s.relname)::regclass) / 1024) AS idx_change<br />
        FROM pg_stat_user_tables s,<br />
    pg_class c WHERE s.relid = c.oid ORDER BY 1;</p>
<p> <code>relation</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Name of this table including schema name.</dl>
<p> <code>total_size</code></p>
<dl>
<dt>
<dd> Total size of relation including indexes, in kilobytes.</dl>
<p> <code>rel_size</code></p>
<dl>
<dt>
<dd> Size of relation without indexes, in kilobytes.</dl>
<p> <code>idx_size</code></p>
<dl>
<dt>
<dd> Size of all indexes of relation, in kilobytes.</dl>
<p> <code>total_change</code></p>
<dl>
<dt>
<dd> Relation and indexes size changes in kilobytes per second.</dl>
<p> <code>rel_change</code></p>
<dl>
<dt>
<dd> Only relation size changes in kilobytes per second.</dl>
<p> <code>idx_change</code></p>
<dl>
<dt>
<dd> Only indexes size changes in kilobytes per second.</dl>
</dl>
<dt><code>pg_stat_activity context</code></p>
<dd> Show process activity from <i>pg_stat_activity</i> which have one row per server process, showing information related to the current activity of that process. Show process which runs too long. Default threshold is 10 seconds, and can be changed with <code>A</code> hotkey. Idle process not displaying. Note: The <i>waiting</i> and <i>state</i> columns are independent. If a backend is in the active state, it may or may not be waiting. If the state is active and waiting is true, it means that a query is being executed, but is being blocked by a lock somewhere in the system. </p>
<pre>
Used query: SELECT
                pid, client_addr AS cl_addr, client_port AS cl_port,
                datname, usename, state, waiting,
                date_trunc('seconds', clock_timestamp() - xact_start) AS xact_age,
                date_trunc('seconds', clock_timestamp() - query_start) AS query_age,
                date_trunc('seconds', clock_timestamp() - state_change) AS change_age,
                query
            FROM pg_stat_activity
            WHERE ((clock_timestamp() - xact_start) &gt; '00:00:10'::interval
                   OR (clock_timestamp() - query_start) &gt; '00:00:10'::interval) 
            AND state &lt;&gt; 'idle' AND pid &lt;&gt; pg_backend_pid()
            ORDER BY COALESCE(xact_start, query_start);
</pre>
<p> <code>pid</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Process ID of this backend.</dl>
<p> <code>cl_addr</code></p>
<dl>
<dt>
<dd> IP address of the client connected to this backend. If this field is null, it indicates either that the client is connected via a Unix socket on the server machine or that this is an internal process such as autovacuum.</dl>
<p> <code>cl_port</code></p>
<dl>
<dt>
<dd> TCP port number that the client is using for communication with this backend, or -1 if a Unix socket is used.</dl>
<p> <code>datname</code></p>
<dl>
<dt>
<dd> Name of the database this backend is connected to.</dl>
<p> <code>usename</code></p>
<dl>
<dt>
<dd> Name of the user logged into this backend.</dl>
<p> <code>state</code></p>
<dl>
<dt>
<dd> Current overall state of this backend. Possible values are:</p>
<dl>
<dt>
<dd></dl>
<p> <code>active</code></p>
<dl>
<dt>
<dd> The backend is executing a query.</dl>
<p> <code>idle</code></p>
<dl>
<dt>
<dd> The backend is waiting for a new client command.</dl>
<p> <code>idle in transaction</code></p>
<dl>
<dt>
<dd> The backend is in a transaction, but is not currently executing a query.</dl>
<p> <code>idle in transaction (aborted)</code></p>
<dl>
<dt>
<dd> This state is similar to idle in transaction, except one of the statements in the transaction caused an error.</dl>
<p> <code>fastpath function call</code></p>
<dl>
<dt>
<dd> The backend is executing a fast-path function.</dl>
<p> <code>disabled</code></p>
<dl>
<dt>
<dd> This state is reported if <i>track_activities</i> is disabled in this backend.</dl>
</dl>
<p> <code>waiting</code></p>
<dl>
<dt>
<dd> True if this backend is currently waiting on a lock.</dl>
<p> <code>xact_age</code></p>
<dl>
<dt>
<dd> Age of transaction started within current process, or null if no transaction is active. If the current query is the first of its transaction, this column is equal to the query_age column.</dl>
<p> <code>query_age</code></p>
<dl>
<dt>
<dd> Age of currently active query, or if state is not active, when the last query was started.</dl>
<p> <code>change_age</code></p>
<dl>
<dt>
<dd> Age since when the <i>state</i> was last changed.</dl>
<p> <code>query</code></p>
<dl>
<dt>
<dd> Text of this backend&#8217;s most recent query. If <i>state</i> is active this field shows the currently executing query. In all other states, it shows the last query that was executed.</dl>
</dl>
<dt><code>pg_stat_functions context</code></p>
<dd> Show statistics from <i>pg_stat_user_function</i> view which contain one row for each tracked function, showing statistics about executions of that function. The <i>track_functions</i> parameter in <i>postgresql.conf</i> controls exactly which functions are tracked. </p>
<pre>
Used query: SELECT
                funcid, schemaname ||'.'||funcname AS function,
                calls AS total_calls, calls AS calls,
                date_trunc('seconds', total_time / 1000 * '1 second'::interval) AS total_t,
                date_trunc('seconds', self_time / 1000 * '1 second'::interval) AS self_t,
                round((total_time / calls)::numeric, 4) AS avg_t,
                round((self_time / calls)::numeric, 4) AS avg_self_t
            FROM pg_stat_user_functions ORDER BY x DESC;
</pre>
<p> <code>funcid</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Unique OID of a function.</dl>
<p> <code>function</code></p>
<dl>
<dt>
<dd> Name of this function, including schema name.</dl>
<p> <code>total_calls</code></p>
<dl>
<dt>
<dd> Number of times this function has been called.</dl>
<p> <code>calls</code></p>
<dl>
<dt>
<dd> Number of times this function has been called per second.</dl>
<p> <code>total_t</code></p>
<dl>
<dt>
<dd> Total time spent in this function and all other functions called by it.</dl>
<p> <code>self_t</code></p>
<dl>
<dt>
<dd> Total time spent in this function itself, not including other functions called by it.</dl>
<p> <code>avg_t</code></p>
<dl>
<dt>
<dd> Average time spent in this function and all other functions called by it, in milliseconds.</dl>
<p> <code>avg_self_t</code></p>
<dl>
<dt>
<dd> Average time spent in this function itself, not including other functions called by it, in milliseconds.</dl>
</dl>
<dt><code>pg_stat_statements_timing context</code></p>
<dd> Show timing statistics from pg_stat_statements module which tracking execution statistics of all SQL statements executed by a server. The module must be loaded by adding <i>pg_stat_statements</i> to <i>shared_preload_libraries </i> in <i>postgresql.conf</i>. This means that a server restart is needed to add or remove the module. When module loaded, <i>pg_stat_statement</i> extension must be installed in target database. For more information see <a rel="nofollow" href="http://www.postgresql.org/docs/9.4/static/pgstatstatements.html.">http://www.postgresql.org/docs/9.4/static/pgstatstatements.html.</a> Additionally used <i>pg_authid</i> and <i>pg_database</i> views. Different versions of the PostgreSQL may have different number of fields.<br />
Used query : SELECT<br />
                 a.rolname AS user,<br />
    d.datname AS database,<br />
    date_trunc(&#8216;seconds&#8217;, round(sum(p.total_time)) / 1000 * &#8216;1 second&#8217; ::interval) AS t_all_t,<br />
    date_trunc(&#8216;seconds&#8217;, round(sum(p.blk_read_time)) / 1000 * &#8216;1 second&#8217; ::interval) AS t_read_t,<br />
    date_trunc(&#8216;seconds&#8217;, round(sum(p.blk_write_time)) / 1000 * &#8216;1 second&#8217; ::interval) AS t_write_t,<br />
    date_trunc(&#8216;seconds&#8217;, round((sum(p.total_time) &#8211; (sum(p.blk_read_time) + sum(p.blk_write_time)))) / 1000 * &#8216;1 second&#8217; ::interval) AS tot_cpu_t,<br />
    round(sum(p.total_time)) AS all_t,<br />
    round(sum(p.blk_read_time)) AS read_t,<br />
    round(sum(p.blk_write_time)) AS write_t,<br />
    round((sum(p.total_time) &#8211; (sum(p.blk_read_time) + sum(p.blk_write_time)))) AS cpu_t,<br />
    sum(p.calls) AS calls,<br />
    left(md5(d.datname || a.rolname || p.query), 10) AS queryid,<br />
    regexp_replace(<br />
        regexp_replace(<br />
            regexp_replace(<br />
                regexp_replace(<br />
                    regexp_replace(p.query,<br />
                                   E &#8216;\?(::[a-zA-Z_]+)?( *, *\?(::[a-zA-Z_]+)?)+&#8217;, &#8216;?&#8217;, &#8216;g&#8217;),<br />
                    E &#8216;\$[0-9]+(::[a-zA-Z_]+)?( *, *\$[0-9]+(::[a-zA-Z_]+)?)*&#8217;, &#8216;$N&#8217;, &#8216;g&#8217;),<br />
                E &#8216;&#8211;.*$&#8217;, &#8221;, &#8216;ng&#8217;),<br />
            E &#8216;/\*.*?\*\/&#8217;, &#8221;, &#8216;g&#8217;),<br />
        E &#8216;\s+&#8217;, &#8216; &#8216;, &#8216;g&#8217;) AS query<br />
    FROM pg_stat_statements p<br />
    JOIN pg_authid a ON a.oid = p.userid<br />
                                JOIN pg_database d ON d.oid = p.dbid<br />
                                                              WHERE d.datname<br />
                                                              != &#8216;postgres&#8217; AND calls &gt; 50 GROUP BY a.rolname,<br />
                        d.datname, query;</p>
<p> <code>user</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> User who executed the statement.</dl>
<p> <code>database</code></p>
<dl>
<dt>
<dd> Database in which the statement was executed.</dl>
<p> <code>t_all_t</code></p>
<dl>
<dt>
<dd> Total time spent in the statement since last stats reset.</dl>
<p> <code>t_read_t</code></p>
<dl>
<dt>
<dd> Total time the statement spent reading blocks (if <i>track_io_timing</i> is enabled, otherwise zero) since last stats reset.</dl>
<p> <code>t_write_t</code></p>
<dl>
<dt>
<dd> Total time the statement spent writing blocks (if <i>track_io_timing</i> is enabled, otherwise zero) since last stats reset.</dl>
<p> <code>t_cpu_t</code></p>
<dl>
<dt>
<dd> Total time the statement spent in CPU cycling (if <i>track_io_timing</i> is enabled, otherwise equals <code>total_t</code>) since last stats reset.</dl>
<p> <code>all_t</code></p>
<dl>
<dt>
<dd> Current time spent in the statement in ms.</dl>
<p> <code>read_t</code></p>
<dl>
<dt>
<dd> Current time the statement spent reading blocks (if <i>track_io_timing</i> is enabled, otherwise zero) in ms.</dl>
<p> <code>write_t</code></p>
<dl>
<dt>
<dd> Total time the statement spent writing blocks (if <i>track_io_timing</i> is enabled, otherwise zero) in ms.</dl>
<p> <code>cpu_t</code></p>
<dl>
<dt>
<dd> Total time the statement spent in CPU cycling, (if <i>track_io_timing</i> is enabled, otherwise equals <code>total_t</code>) in ms.</dl>
<p> <code>calls</code></p>
<dl>
<dt>
<dd> Current number of query calls.</dl>
<p> <code>queryid</code></p>
<dl>
<dt>
<dd> Query ID generated with MD5 hash function and truncated to 10 symbols. Hash based on username, dbname and query text.</dl>
<p> <code>query</code></p>
<dl>
<dt>
<dd> Text of a representative statement.</dl>
</dl>
<dt><code>pg_stat_statements_general context</code></p>
<dd> Show general statistics about rows and calls from pg_stat_statements module which tracking execution statistics of all SQL statements executed by a server. The module must be loaded by adding <i>pg_stat_statements</i> to <i>shared_preload_libraries </i> in <i>postgresql.conf</i>. This means that a server restart is needed to add or remove the module. When module loaded, <i>pg_stat_statement</i> extension must be installed in target database. For more information see <a rel="nofollow" href="http://www.postgresql.org/docs/9.4/static/pgstatstatements.html.">http://www.postgresql.org/docs/9.4/static/pgstatstatements.html.</a> Additionally used <i>pg_authid</i> and <i>pg_database</i> views.<br />
Used query : SELECT<br />
                 a.rolname AS user,<br />
    d.datname AS database,<br />
    sum(p.calls) AS t_calls, sum(p.rows) as t_rows,<br />
    sum(p.calls) AS calls, sum(p.rows) as rows,<br />
    left(md5(d.datname || a.rolname || p.query), 10) AS queryid,<br />
    regexp_replace(<br />
        regexp_replace(<br />
            regexp_replace(<br />
                regexp_replace(<br />
                    regexp_replace(p.query,<br />
                                   E &#8216;\?(::[a-zA-Z_]+)?( *, *\?(::[a-zA-Z_]+)?)+&#8217;, &#8216;?&#8217;, &#8216;g&#8217;),<br />
                    E &#8216;\$[0-9]+(::[a-zA-Z_]+)?( *, *\$[0-9]+(::[a-zA-Z_]+)?)*&#8217;, &#8216;$N&#8217;, &#8216;g&#8217;),<br />
                E &#8216;&#8211;.*$&#8217;, &#8221;, &#8216;ng&#8217;),<br />
            E &#8216;/\*.*?\*\/&#8217;, &#8221;, &#8216;g&#8217;),<br />
        E &#8216;\s+&#8217;, &#8216; &#8216;, &#8216;g&#8217;) AS query<br />
    FROM pg_stat_statements p<br />
    JOIN pg_authid a ON a.oid = p.userid<br />
                                JOIN pg_database d ON d.oid = p.dbid<br />
                                                              WHERE d.datname<br />
                                                              != &#8216;postgres&#8217; AND calls &gt; 50 GROUP BY a.rolname,<br />
                        d.datname, query;</p>
<p> <code>user</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> User who executed the statement.</dl>
<p> <code>database</code></p>
<dl>
<dt>
<dd> Database in which the statement was executed.</dl>
<p> <code>t_calls</code></p>
<dl>
<dt>
<dd> Total number of times the statement was executed.</dl>
<p> <code>t_rows</code></p>
<dl>
<dt>
<dd> Total number of rows retrieved or affected by the statement.</dl>
<p> <code>calls</code></p>
<dl>
<dt>
<dd> Number of times the statement was executed per second.</dl>
<p> <code>rows</code></p>
<dl>
<dt>
<dd> Number of rows retrieved or affected by the statement per second.</dl>
<p> <code>queryid</code></p>
<dl>
<dt>
<dd> Query ID generated with MD5 hash function and truncated to 10 symbols. Hash based on username, dbname and query text.</dl>
<p> <code>query</code></p>
<dl>
<dt>
<dd> Text of a representative statement</dl>
</dl>
<dt><code>pg_stat_statements_io context</code></p>
<dd> Show statistics about buffer input/output from pg_stat_statements module which tracking execution statistics of all SQL statements executed by a server. The module must be loaded by adding <i>pg_stat_statements</i> to <i>shared_preload_libraries </i> in <i>postgresql.conf</i>. This means that a server restart is needed to add or remove the module. When module loaded, <i>pg_stat_statement</i> extension must be installed in target database. For more information see <a rel="nofollow" href="http://www.postgresql.org/docs/9.4/static/pgstatstatements.html.">http://www.postgresql.org/docs/9.4/static/pgstatstatements.html.</a> Additionally used <i>pg_authid</i> and <i>pg_database</i> views.<br />
Used query : SELECT<br />
                 a.rolname AS user,<br />
    d.datname AS database,<br />
    (sum(p.shared_blks_hit) + sum(p.local_blks_hit)) * (SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) as t_hits,<br />
    (sum(p.shared_blks_read) + sum(p.local_blks_read)) * (SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) as t_reads,<br />
    (sum(p.shared_blks_dirtied) + sum(p.local_blks_dirtied)) * (SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) as t_dirtied,<br />
    (sum(p.shared_blks_written) + sum(p.local_blks_written)) * (SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) as t_written,<br />
    (sum(p.shared_blks_hit) + sum(p.local_blks_hit)) * (SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) as hits,<br />
    (sum(p.shared_blks_read) + sum(p.local_blks_read)) * (SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) as reads,<br />
    (sum(p.shared_blks_dirtied) + sum(p.local_blks_dirtied)) * (SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) as dirtied,<br />
    (sum(p.shared_blks_written) + sum(p.local_blks_written)) * (SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) as written,<br />
    sum(p.calls) AS calls,<br />
    left(md5(d.datname || a.rolname || p.query), 10) AS queryid,<br />
    regexp_replace(<br />
        regexp_replace(<br />
            regexp_replace(<br />
                regexp_replace(<br />
                    regexp_replace(p.query,<br />
                                   E &#8216;\?(::[a-zA-Z_]+)?( *, *\?(::[a-zA-Z_]+)?)+&#8217;, &#8216;?&#8217;, &#8216;g&#8217;),<br />
                    E &#8216;\$[0-9]+(::[a-zA-Z_]+)?( *, *\$[0-9]+(::[a-zA-Z_]+)?)*&#8217;, &#8216;$N&#8217;, &#8216;g&#8217;),<br />
                E &#8216;&#8211;.*$&#8217;, &#8221;, &#8216;ng&#8217;),<br />
            E &#8216;/\*.*?\*\/&#8217;, &#8221;, &#8216;g&#8217;),<br />
        E &#8216;\s+&#8217;, &#8216; &#8216;, &#8216;g&#8217;) AS query<br />
    FROM pg_stat_statements p<br />
    JOIN pg_authid a ON a.oid = p.userid<br />
                                JOIN pg_database d ON d.oid = p.dbid<br />
                                                              WHERE d.datname<br />
                                                              != &#8216;postgres&#8217; AND calls &gt; 50 GROUP BY a.rolname,<br />
                        d.datname, query;</p>
<p> <code>user</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> User who executed the statement.</dl>
<p> <code>database</code></p>
<dl>
<dt>
<dd> Database in which the statement was executed.</dl>
<p> <code>t_hits</code></p>
<dl>
<dt>
<dd> Total amount of shared and local data hits from cache by the statement since stats reset, in Kbytes.</dl>
<p> <code>t_reads</code></p>
<dl>
<dt>
<dd> Total amount of shared and local data read by the statement since stats reset, in Kbytes.</dl>
<p> <code>t_dirtied</code></p>
<dl>
<dt>
<dd> Total amount of shared and local data dirtied by the statement since stats reset, in Kbytes.</dl>
<p> <code>t_written</code></p>
<dl>
<dt>
<dd> Total amount of shared and local data written by the statement since stats reset, in Kbytes.</dl>
<p> <code>hits</code></p>
<dl>
<dt>
<dd> Amount of shared and local data hits from cache by the statement per interval (default 1 second), in Kbytes.</dl>
<p> <code>reads</code></p>
<dl>
<dt>
<dd> Amount of shared and local data read by the statement per interval (default 1 second), in Kbytes.</dl>
<p> <code>dirtied</code></p>
<dl>
<dt>
<dd> Amount of shared and local data dirtied by the statement per interval (default 1 second), in Kbytes.</dl>
<p> <code>written</code></p>
<dl>
<dt>
<dd> Amount of shared and local data written by the statement per interval (default 1 second), in Kbytes.</dl>
<p> <code>calls</code></p>
<dl>
<dt>
<dd> Number of rows retrieved or affected by the statement per interval.</dl>
<p> <code>queryid</code></p>
<dl>
<dt>
<dd> Query ID generated with MD5 hash function and truncated to 10 symbols. Hash based on username, dbname and query text.</dl>
<p> <code>query</code></p>
<dl>
<dt>
<dd> Text of a representative statement</dl>
</dl>
<dt><code>pg_stat_statements_temp context</code></p>
<dd> Show statistics about buffers input/output related with temporary buffers. Stats read from pg_stat_statements module which tracking execution statistics of all SQL statements executed by a server. The module must be loaded by adding <i>pg_stat_statements</i> to <i>shared_preload_libraries </i> in <i>postgresql.conf</i>. This means that a server restart is needed to add or remove the module. When module loaded, <i>pg_stat_statement</i> extension must be installed in target database. For more information see <a rel="nofollow" href="http://www.postgresql.org/docs/9.4/static/pgstatstatements.html.">http://www.postgresql.org/docs/9.4/static/pgstatstatements.html.</a> Additionally used <i>pg_authid</i> and <i>pg_database</i> views.<br />
Used query : SELECT<br />
                 a.rolname AS user,<br />
    d.datname AS database,<br />
    sum(p.temp_blks_read) * (SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) as t_tmp_read,<br />
    sum(p.temp_blks_written) * (SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) as t_tmp_write,<br />
    sum(p.temp_blks_read) * (SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) as tmp_read,<br />
    sum(p.temp_blks_written) * (SELECT current_setting(&#8216;block_size&#8217;)::int / 1024) as tmp_write,<br />
    sum(p.calls) AS calls,<br />
    left(md5(d.datname || a.rolname || p.query), 10) AS queryid,<br />
    regexp_replace(<br />
        regexp_replace(<br />
            regexp_replace(<br />
                regexp_replace(<br />
                    regexp_replace(p.query,<br />
                                   E &#8216;\?(::[a-zA-Z_]+)?( *, *\?(::[a-zA-Z_]+)?)+&#8217;, &#8216;?&#8217;, &#8216;g&#8217;),<br />
                    E &#8216;\$[0-9]+(::[a-zA-Z_]+)?( *, *\$[0-9]+(::[a-zA-Z_]+)?)*&#8217;, &#8216;$N&#8217;, &#8216;g&#8217;),<br />
                E &#8216;&#8211;.*$&#8217;, &#8221;, &#8216;ng&#8217;),<br />
            E &#8216;/\*.*?\*\/&#8217;, &#8221;, &#8216;g&#8217;),<br />
        E &#8216;\s+&#8217;, &#8216; &#8216;, &#8216;g&#8217;) AS query<br />
    FROM pg_stat_statements p<br />
    JOIN pg_authid a ON a.oid = p.userid<br />
                                JOIN pg_database d ON d.oid = p.dbid<br />
                                                              WHERE d.datname<br />
                                                              != &#8216;postgres&#8217; AND calls &gt; 50 GROUP BY a.rolname,<br />
                        d.datname, query;</p>
<p> <code>user</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> User who executed the statement.</dl>
<p> <code>database</code></p>
<dl>
<dt>
<dd> Database in which the statement was executed.</dl>
<p> <code>t_tmp_read</code></p>
<dl>
<dt>
<dd> Total amount of temp data read by the statement since last stats reset, in Kbytes.</dl>
<p> <code>t_tmp_write</code></p>
<dl>
<dt>
<dd> Total amount of temp data written by the statement sice last stats reset, in Kbytes.</dl>
<p> <code>tmp_read</code></p>
<dl>
<dt>
<dd> Amount of temp data read by the statement per interval, in Kbytes.</dl>
<p> <code>tmp_write</code></p>
<dl>
<dt>
<dd> Amount of temp data written by the statement per interval, in Kbytes.</dl>
<p> <code>calls</code></p>
<dl>
<dt>
<dd> Number of times the statement was executed per second.</dl>
<p> <code>queryid</code></p>
<dl>
<dt>
<dd> Query ID generated with MD5 hash function and truncated to 10 symbols. Hash based on username, dbname and query text.</dl>
<p> <code>query</code></p>
<dl>
<dt>
<dd> Text of a representative statement</dl>
</dl>
<dt><code>pg_stat_statements_local context</code></p>
<dd> Show statistics about local input/output (backends that use local memory and not shared buffers) from pg_stat_statements module which tracking execution statistics of all SQL statements executed by a server. The module must be loaded by adding <i>pg_stat_statements</i> to <i>shared_preload_libraries </i> in <i>postgresql.conf</i>. This means that a server restart is needed to add or remove the module. When module loaded, <i>pg_stat_statement</i> extension must be installed in target database. For more information see <a rel="nofollow" href="http://www.postgresql.org/docs/9.4/static/pgstatstatements.html.">http://www.postgresql.org/docs/9.4/static/pgstatstatements.html.</a> Additionally used <i>pg_authid</i> and <i>pg_database</i> views. </p>
<pre><code>
Used query : SELECT
                 a.rolname AS user,
    d.datname AS database,
    (sum(p.local_blks_hit)) * (SELECT current_setting('block_size')::int / 1024) as t_lo_hits,
    (sum(p.local_blks_read)) * (SELECT current_setting('block_size')::int / 1024) as t_lo_reads,
    (sum(p.local_blks_dirtied)) * (SELECT current_setting('block_size')::int / 1024) as t_lo_dirtied,
    (sum(p.local_blks_written)) * (SELECT current_setting('block_size')::int / 1024) as t_lo_written,
    (sum(p.local_blks_hit)) * (SELECT current_setting('block_size')::int / 1024) as lo_hits,
    (sum(p.local_blks_read)) * (SELECT current_setting('block_size')::int / 1024) as lo_reads,
    (sum(p.local_blks_dirtied)) * (SELECT current_setting('block_size')::int / 1024) as lo_dirtied,
    (sum(p.local_blks_written)) * (SELECT current_setting('block_size')::int / 1024) as lo_written,
    sum(p.calls) AS calls,
    left(md5(d.datname || a.rolname || p.query), 10) AS queryid,
    regexp_replace(
        regexp_replace(
            regexp_replace(
                regexp_replace(
                    regexp_replace(p.query,
                                   E '\?(::[a-zA-Z_]+)?( *, *\?(::[a-zA-Z_]+)?)+', '?', 'g'),
                    E '\$[0-9]+(::[a-zA-Z_]+)?( *, *\$[0-9]+(::[a-zA-Z_]+)?)*', '$N', 'g'),
                E '--.*$', '', 'ng'),
            E '/\*.*?\*\/', '', 'g'),
        E '\s+', ' ', 'g') AS query
    FROM pg_stat_statements p
    JOIN pg_authid a ON a.oid = p.userid
                                JOIN pg_database d ON d.oid = p.dbid
                                                              WHERE d.datname
                                                              != 'postgres' AND calls &gt; 50 GROUP BY a.rolname,
                        d.datname, query;
</code></pre>
<p> <code>user</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> User who executed the statement.</dl>
<p> <code>database</code></p>
<dl>
<dt>
<dd> Database in which the statement was executed.</dl>
<p> <code>t_lo_hits</code></p>
<dl>
<dt>
<dd> Total amount of data hits from backends local memory by the statement since stats reset, in Kbytes.</dl>
<p> <code>t_lo_reads</code></p>
<dl>
<dt>
<dd> Total amount of data read from backends local memory by the statement since stats reset, in Kbytes.</dl>
<p> <code>t_lo_dirtied</code></p>
<dl>
<dt>
<dd> Total amount of data dirtied in backends local memory by the statement since stats reset, in Kbytes.</dl>
<p> <code>t_lo_written</code></p>
<dl>
<dt>
<dd> Total amount of data written to backends local memory by the statement since stats reset, in Kbytes.</dl>
<p> <code>lo_hits</code></p>
<dl>
<dt>
<dd> Amount of data hits from backends local memory by the statement per interval (default 1 second), in Kbytes.</dl>
<p> <code>lo_reads</code></p>
<dl>
<dt>
<dd> Amount of data read from backends local memory by the statement per interval (default 1 second), in Kbytes.</dl>
<p> <code>lo_dirtied</code></p>
<dl>
<dt>
<dd> Amount of data dirtied in backends local memory by the statement per interval (default 1 second), in Kbytes.</dl>
<p> <code>lo_written</code></p>
<dl>
<dt>
<dd> Amount of data written to backends local memory by the statement per interval (default 1 second), in Kbytes.</dl>
<p> <code>calls</code></p>
<dl>
<dt>
<dd> Number of rows retrieved or affected by the statement per interval.</dl>
<p> <code>queryid</code></p>
<dl>
<dt>
<dd> Query ID generated with MD5 hash function and truncated to 10 symbols. Hash based on username, dbname and query text.</dl>
<p> <code>query</code></p>
<dl>
<dt>
<dd> Text of a representative statement</dl>
</dl>
<dt><code>pg_stat_progress_vacuum context</code></p>
<dd> Whenever VACUUM is running, the pg_stat_progress_vacuum view will contain one row for each backend (including autovacuum worker processes) that is currently vacuuming. The tables below describe the information that will be reported and provide information about how to interpret it. Progress reporting is not currently supported for VACUUM FULL and backends running VACUUM FULL will not be listed in this view. This statistics are available since PostgreSQL 9.6, for more information see <a rel="nofollow" href="https://www.postgresql.org/docs/9.6/static/progress-reporting.html.">https://www.postgresql.org/docs/9.6/static/progress-reporting.html.</a> Additionally used <i>pg_stat_activity</i> view. </p>
<pre>
Used query:
    SELECT
        a.pid,
        date_trunc('seconds', clock_timestamp() - xact_start) AS xact_age,
        v.datname, v.relid::regclass AS relation,
        a.state, v.phase,
        v.heap_blks_total * (SELECT current_setting('block_size')::int / 1024) AS total,
        v.heap_blks_scanned * (SELECT current_setting('block_size')::int / 1024) AS scanned,
        v.heap_blks_vacuumed * (SELECT current_setting('block_size')::int / 1024) AS vacuumed,
        a.wait_event_type AS wait_etype, a.wait_event,
        a.query
    FROM pg_stat_progress_vacuum v
    JOIN pg_stat_activity a ON v.pid = a.pid
    ORDER BY COALESCE(a.xact_start, a.query_start)
</pre>
<p> <code>pid</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Process ID of vacuum.</dl>
<p> <code>xact_age</code></p>
<dl>
<dt>
<dd> Age of vacuum task.</dl>
<p> <code>datname</code></p>
<dl>
<dt>
<dd> Database name where vacuum worker is connected.</dl>
<p> <code>state</code></p>
<dl>
<dt>
<dd> Postgres backend state (see pg_stat_activity backends states).</dl>
<p> <code>phase</code></p>
<dl>
<dt>
<dd> Current processing phase of vacuum. See VACUUM phases &#8211; <a rel="nofollow" href="https://www.postgresql.org/docs/9.6/static/progress-reporting.html#VACUUM-PHASES.">https://www.postgresql.org/docs/9.6/static/progress-reporting.html#VACUUM-PHASES.</a></dl>
<p> <code>total</code></p>
<dl>
<dt>
<dd> Total size of the table in Kbytes. This number is reported as of the beginning of the scan; size increased during vacuum will not be (and need not be) shown and this space will not be visited by this VACUUM.</dl>
<p> <code>scanned</code></p>
<dl>
<dt>
<dd> Size of table in Kbytes that is scanned. Because the visibility map is used to optimize scans, some blocks will be skipped without inspection; skipped blocks are included in this total, so that this number will eventually become equal to total when the vacuum is complete. This counter only advances when the phase is scanning heap.</dl>
<p> <code>vacuumed</code></p>
<dl>
<dt>
<dd> Size of table in Kbytes that is vacuumed. Unless the table has no indexes, this counter only advances when the phase is vacuuming heap. Blocks that contain no dead tuples are skipped, so the counter may sometimes skip forward in large increments.</dl>
<p> <code>wait_etype</code></p>
<dl>
<dt>
<dd> The type of event for which the backend is waiting, if any; otherwise NULL.</dl>
<p> <code>wait_event</code></p>
<dl>
<dt>
<dd> Wait event name if backend is currently waiting, otherwise NULL.</dl>
<p> <code>query</code></p>
<dl>
<dt>
<dd> Text of a representative statement.</dl>
</dl>
</dl>
<h2>SUBSCREENS</h2>
<p> Subscreens it&#8217;s a additional screens which presents auxilary data which not directly related with the PostgreSQL but may be useful in troubleshoot. </p>
<dl>
<dt><code>Logtail subscreen</code></p>
<dd> Opens logfile in subscreen and tail this log. Used only if <code>pgcenter</code> and <code>PostgreSQL</code> running on the same host. All multiline log entries truncates to end of line. Requires database superuser privileges. </p>
<dt><code>iostat subscreen</code></p>
<dd> Report input/output statistics for devices and partitions. The iostat subscreen is used for monitoring system input/output device loading by observing the time the devices are active in relation to their average transfer rates. The first report generated by the iostat subscreen provides statistics concerning the time since the system was booted. Each subsequent report covers the time since the previous report. Iostat subscreen similar to <code>iostat</code> utility from <code>sysstat</code> package and /proc/diskstats interface. For the proper iostat work /proc filesystem must be mounted for iostat to work. Kernels older than 2.6.x are not supported. </p>
<p> <code>Device</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Block device registered in a system.</dl>
<p> <code>rrqm/s</code></p>
<dl>
<dt>
<dd> The number of read requests merged per second that were queued to the device.</dl>
<p> <code>wrqm/s</code></p>
<dl>
<dt>
<dd> The number of write requests merged per second that were queued to the device.</dl>
<p> <code>r/s</code></p>
<dl>
<dt>
<dd> The number (after merges) of read requests completed per second for the device.</dl>
<p> <code>w/s</code></p>
<dl>
<dt>
<dd> The number (after merges) of write requests completed per second for the device.</dl>
<p> <code>rMB/s</code></p>
<dl>
<dt>
<dd> The number of megabytes read from the device per second.</dl>
<p> <code>wMB/s</code></p>
<dl>
<dt>
<dd> The number of megabytes written to the device per second.</dl>
<p> <code>avgrq-sz</code></p>
<dl>
<dt>
<dd> The average size (in sectors) of the requests that were issued to the device.</dl>
<p> <code>avgqu-sz</code></p>
<dl>
<dt>
<dd> The average queue length of the requests that were issued to the device.</dl>
<p> <code>await</code></p>
<dl>
<dt>
<dd> The average time (in milliseconds) for I/O requests issued to the device to be served. This includes the time spent by the requests in queue and the time spent servicing them.</dl>
<p> <code>r_await</code></p>
<dl>
<dt>
<dd> The average time (in milliseconds) for read requests issued to the device to be served. This includes the time spent by the requests in queue and the time spent servicing them.</dl>
<p> <code>w_await</code></p>
<dl>
<dt>
<dd> The average time (in milliseconds) for write requests issued to the device to be served. This includes the time spent by the requests in queue and the time spent servicing them.</dl>
<p> <code>%util</code></p>
<dl>
<dt>
<dd> Percentage of elapsed time during which I/O requests were issued to the device (bandwidth utilization for the device). Device saturation occurs when this value is close to 100% for devices serving requests serially. But for devices serving requests in parallel, such as RAID arrays and modern SSDs, this number does not reflect their performance limits.</dl>
</dl>
<dt><code>nicstat subscreen</code></p>
<dd> Print network traffic statistics for all network cards (NICs), including packets, kilobytes per second, average packet sizes and more. Nicstat subscreen similar to nicstat utility and use /proc/net/dev interface. </p>
<p> <code>Interface</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Network interface registered in a system.</dl>
<p> <code>rMbps</code></p>
<dl>
<dt>
<dd> Megabits per interval read (received).</dl>
<p> <code>wMbps</code></p>
<dl>
<dt>
<dd> Megabits per interval written (transmitted).</dl>
<p> <code>rPk/s</code></p>
<dl>
<dt>
<dd> Packets per interval read (received).</dl>
<p> <code>wPk/s</code></p>
<dl>
<dt>
<dd> Packets per interval written (transmitted).</dl>
<p> <code>rAvs</code></p>
<dl>
<dt>
<dd> Average size of packets read (received).</dl>
<p> <code>wAvs</code></p>
<dl>
<dt>
<dd> Average size of packets written (transmitted).</dl>
<p> <code>IErr</code></p>
<dl>
<dt>
<dd> Packets received that could not be processed because they contained errors.</dl>
<p> <code>OErr</code></p>
<dl>
<dt>
<dd> Packets that were not successfully transmitted because of errors.</dl>
<p> <code>Coll</code></p>
<dl>
<dt>
<dd> Ethernet collisions during transmit.</dl>
<p> <code>Sat</code></p>
<dl>
<dt>
<dd> Saturation. This the number of errors/second seen for the interface &#8211; an indicator the interface may be approaching saturation. This statistic is combined from a number of kernel statistics.</dl>
<p> <code>%rUtil</code> <code>%wUtil</code></p>
<dl>
<dt>
<dd> Percentage utilization for bytes read and written, respectively.</dl>
<p> <code>%Util</code></p>
<dl>
<dt>
<dd> Percentage utilization of the interface. For full-duplex interfaces, this is the greater of rMB/s or wMB/s as a percentage of the interface speed. For half-duplex interfaces, rMB/s and wMB/s are summed.</dl>
</dl>
</dl>
<h2>INTERACTIVE COMMANDS</h2>
<p> The global interactive commands are always available main program mode</p>
<dl>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>1..8</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Switch screen</code> toggle</p>
<dd> Switch between already opened screens. Number of screens limited by eight.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>d</code>&nbsp;<wbr>&nbsp;<wbr>:<code>pg_stat_database</code> toggle</p>
<dd> Show statistics from <code>pg_stat_database</code> view. This statistics includes per database info about commits/rollbacks, returned and fetched tuples, write operations such as inserts/deletes/updates, abnormal situations like conflicts and deadlocks, info about temporary files usage and read/write timings.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>r</code>&nbsp;<wbr>&nbsp;<wbr>:<code>pg_stat_replication</code> toggle</p>
<dd> Show statistics from <i>pg_stat_replication</i> view. Statistics about streaming replication connections, includes information about connected standbys and amount of data which is sent, written, flushed or replayed on standby servers. Also available info about replication lag.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>t</code>&nbsp;<wbr>&nbsp;<wbr>:<code>pg_stat_tables</code> toggle</p>
<dd> Show statistics from <i>pg_stat_user_tables</i> (or <i>pg_stat_all_tables</i>) view about accesses to that specific tables. Includes sequential/index scans, number of inserted/updated/deleted tuples, number of live/dead tuples. Useful for determine current tables workload. By default, displayed only user tables, displaying system tables can be enabled by pressing <code>V</code>.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>T</code>&nbsp;<wbr>&nbsp;<wbr>:<code>pg_statio_tables</code> toggle</p>
<dd> Show statistics from <i>pg_statio_user_tables</i> (or <i>pg_statio_all_tables</i>) view about I/O on tables in the current database. Includes info about reads from disk and shared buffers related to tables, their indexes or TOAST. Useful for determine current tables workload. By default, displayed only user tables, displaying system tables can be enabled by pressing <code>V</code>.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>i</code>&nbsp;<wbr>&nbsp;<wbr>:<code>pg_stat_indexes</code> toggle</p>
<dd> Show statistics from <i>pg_stat_user_indexes</i> and <i>pg_statio_user_indexes</i> (or <i>pg_stat_all_indexes</i> and <i>pg_statio_all_indexes</i>) views which showing statistics about accesses to that specific indexes and their I/O. Includes info about number of index scans, number of readen and fetched tuples, data read from disk or shared buffers. By default, displayed only user indexes, displaying system indexes can be enabled by pressing <code>V</code>. Useful for determine index usage.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>s</code>&nbsp;<wbr>&nbsp;<wbr>:<code>pg_tables_size</code> toggle</p>
<dd> Show statistics about tables and their indexes sizes. For taking information about size of relations use <i>pg_stat_user_tables</i> (or <i>pg_stat_all_tables</i>) view, <i>pg_class</i> system catalog and <i>pg_relation_size()</i>, <i>pg_total_relation_size()</i> functions.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>a</code>&nbsp;<wbr>&nbsp;<wbr>:<code>pg_stat_activity</code> toggle</p>
<dd> Show statistics about long queries from <i>pg_stat_activity</i> view. Show information about client (address, port, name, database), text of query and his state and age. Default age threshold is 10 seconds, and can be changed with <code>A</code> hotkey.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>f</code>&nbsp;<wbr>&nbsp;<wbr>:<code>pg_stat_functions</code> toggle</p>
<dd> Show statistics from <i>pg_stat_user_functions</i> view about tracked functions and their executions, such as number of calls and execution time. The <i>track_functions</i> parameter in <i>postgresql.conf</i> controls exactly which functions are tracked.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>v</code>&nbsp;<wbr>&nbsp;<wbr>:<code>pg_stat_progress_vacuum</code> toggle</p>
<dd> Show statistics from <i>pg_stat_progress_vacuum</i> view about vacuum execution progress. Available since PostgreSQL 9.6.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>x</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Switch to next pg_stat_statements screen</code> toggle</p>
<dd> Switches between <code>pg_stat_statements</code> screens: timings, general, input/output, temporary input/output, local input/output.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>X</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Show pg_stat_statements menu</code> toggle</p>
<dd> Open pg_stat_statements menu and allow to choose pg_stat_statements screen without switching.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>E</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Edit configuration files menu</code> toggle</p>
<dd> Open configuration files menu and edit specific config. Supported editing of postgresql.conf, pg_hba.conf, pg_ident.conf and recovery.conf. Used only if <code>pgcenter</code> and <code>PostgreSQL</code> running on the same host. Use $EDITOR environment variable or <code>vi</code> by default. Requires database superuser privileges.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>C</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Show current configuration</code> toggle</p>
<dd> Show current <code>PostgreSQL</code> configuration from <i>pg_settings</i> view. For viewing all parameters requires database superuser privileges.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>R</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Reload</code> toggle</p>
<dd> Reload <code>PostgreSQL</code> service for apply configuration changes. The <code>pgcenter</code> used <i>pg_reload_conf()</i> function for reloading. Requires database superuser privileges.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>p</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Start psql session</code> toggle</p>
<dd> Start <code>psql</code> session with current connection settings.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>B</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Open iostat subscreen</code> toggle</p>
<dd> Open subscreen with iostat which reporting input/output statistics for devices and partitions. Show statistics from current host.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>I</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Open nicstat subscreen</code> toggle</p>
<dd> Open subscreen with nicstat which reporting network statistics for all network cards (NICs), including packets, kilobytes per second, average packet sizes and more.. Show statistics from current host.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>L</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Open logtail subscreen</code> toggle</p>
<dd> Open subscreen and tail postgresql log. Used only if <code>pgcenter</code> and <code>PostgreSQL</code> running on the same host. Requires database superuser privileges.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>l</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Open log file</code> toggle</p>
<dd> Open logfile with pager. Use $PAGER environment variable or <code>less</code> by default. Used only if <code>pgcenter</code> and <code>PostgreSQL</code> running on the same host. Requires database superuser privileges.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>N</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Open new connection</code> toggle</p>
<dd> Open new screen with new connection to <code>PostgreSQL</code>. Specify host, port, user, dbname options and open new connection.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>Ctrl+D</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Close current connection</code> toggle</p>
<dd> Close current screen and connection.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>W</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Write connection options</code> toggle</p>
<dd> Write connection settings into config file. By default is <i>~/.pgcenterrc</i> is used. If <code>&#8211;file=FILENAME</code> argument was used at <code>pgcenter</code> start, connection settings will be written at specified file.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>Left, Right</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Change sort</code> toggle</p>
<dd> Change column which is used for sort.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>/</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Change sort order</code> toggle</p>
<dd> Change sort order, descent or ascent. Descent order used by default.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>F</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Set filtration</code> toggle</p>
<dd> Set filter pattern for a column, or reset filtration with empty value. Note, filter patterns are remebered between tab and context switches. Filtered column marked with <code>*</code> symbol. No filtration by default.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Cancel backend</code> toggle</p>
<dd> Cancel query execution using backend pid with <i>pg_cancel_backend()</i> function. This function allowed only when <code>pg_stat_activity</code> screen enabled by <code>a</code> hotkey. Requires database superuser privileges.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>_</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Terminate backend</code> toggle</p>
<dd> Terminate process using backend pid with <code>pg_terminate_backend()</code> function. This function allowed only when <code>pg_stat_activity</code> screen enabled by <code>a</code> hotkey. Requires database superuser privileges.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>Del</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Cancel group of backends</code> toggle</p>
<dd> Cancel queries execution in group of backends with <code>pg_cancel_backend()</code> function. Group of backends determined using mask which specified by <code>n</code> toggle. Note, queries are canceled without confirmation. This function allowed only when <code>pg_stat_activity</code> screen enabled by <code>a</code> hotkey. Unprivileged users can cancel their own queries. Superusers can cancel any queries. Backend pids which queries will be canceled are selected from <code>pg_stat_activity</code> view, select condition determined by mask which can be defined with <code>n</code> hotkey.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>Shift+Del</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Terminate group of backends</code> toggle</p>
<dd> Terminate queries execution in group of backends with <code>pg_terminate_backend()</code> function. Group of backends determined using mask which specified by <code>n</code> toggle. Note, backends are terminated without confirmation. This function allowed only when <code>pg_stat_activity</code> screen enabled by <code>a</code> hotkey. Unprivileged users can terminate their own backends. Superusers can terminate any backends. Backend pids which will be terminated are selected from <code>pg_stat_activity</code> view, select condition determined by mask which can be defined with <code>n</code> hotkey.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>n</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Set new mask</code> toggle</p>
<dd> Set new mask for group cancel/terminate. Type of backends associated with their states: </p>
<p> <code>active</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Backend which are executing a queries. </p>
<pre>
Used condition: WHERE state = 'active' AND (
                    (clock_timestamp() - xact_start) &gt; '00:00:10.0'::interval 
                     OR 
                    (clock_timestamp() - query_start) &gt; '00:00:10.0'::interval
                ) AND pid &lt;&gt; pg_backend_pid();
</pre>
</dl>
<p> <code>idle</code></p>
<dl>
<dt>
<dd> Backends which are do nothing and waiting for a new client command. </p>
<pre>
Used confition: WHERE state = 'idle' AND (
                    (clock_timestamp() - xact_start) &gt; '00:00:10.0'::interval 
                     OR 
                    (clock_timestamp() - query_start) &gt; '00:00:10.0'::interval
                ) AND pid &lt;&gt; pg_backend_pid();
</pre>
</dl>
<p> <code>idle_in_xact</code></p>
<dl>
<dt>
<dd> Includes <code>idle in transaction</code> and <code>idle in transaction: (aborted)</code> states. Always a bad state. </p>
<pre>
Used condition: WHERE state IN ('idle in transaction (aborted)', 'idle in transaction') AND (
                    (clock_timestamp() - xact_start) &gt; '00:00:10.0'::interval
                     OR
                    (clock_timestamp() - query_start) &gt; '00:00:10.0'::interval)
                AND pid &lt;&gt; pg_backend_pid();
</pre>
</dl>
<p> <code>waiting</code></p>
<dl>
<dt>
<dd> Backends which are currently waiting on a lock. Long waiting transactions or statements are bad. </p>
<pre>
Used condition: WHERE waiting AND (
                    (clock_timestamp() - xact_start) &gt; '00:00:10.0'::interval
                     OR (clock_timestamp() - query_start) &gt; '00:00:10.0'::interval
                ) AND pid &lt;&gt; pg_backend_pid();
</pre>
</dl>
<p> <code>other</code></p>
<dl>
<dt>
<dd> backends which are executing a <code>fast-path function call</code> or with <code>disabled</code> state &#8211; when <i>track_activities</i> are disabled in those backends. </p>
<pre>
Used condition: WHERE state IN ('fastpath function call', 'disabled') AND (
                    (clock_timestamp() - xact_start) &gt; '00:00:10.0'::interval
                     OR (clock_timestamp() - query_start) &gt; '00:00:10.0'::interval
                ) AND pid &lt;&gt; pg_backend_pid();
</pre>
</dl>
<p> A ten seconds interval used in condition determines query or transaction age and can be overriden with <code>A</code> hotkey. </p>
<p> Note, <code>waiting</code> is not a backend state. If a backend is in the active state, it may or may not be waiting. If the state is active and waiting is true, it means that a query is being executed, but is being blocked by a lock somewhere in the system. Therefore, if <code>waiting</code> added to the mask, all waiting queries will be canceled ot terminated independently of his backends states.</dl>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>m</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Display current mask</code> toggle</p>
<dd> Show current mask which will used for group cancel/terminate.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>A</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Change age threshold</code> toggle</p>
<dd> Change age threshold for long running queries. Queries which age is never then threshold not displayed. Default threshold 10 seconds. This function allowed only when <code>pg_stat_activity</code> screen enabled by <code>a</code> hotkey.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>V</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Show system tables</code> toggle</p>
<dd> Toggle on/off system tables and indexes. By default, the pgcenter shows table/index statistics for user tables from <i>pg_stat_user_*</i> views.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>K</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Reset postgresql stats</code> toggle</p>
<dd> Reset <code>PostgreSQL</code> stats counters for the current database to zero. The <i>pg_stat_statements</i> counters also reseted. Requires database superuser privileges.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>G</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Get query report</code> toggle</p>
<dd> Show query report with various information about specified query. This function work only in <code>pg_stat_statements_timing</code> and <code>pg_stat_statements_general</code> screens. For specifying query use id values from <code>queryid</code> column.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>z</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Change refresh interval</code> toggle</p>
<dd> You will be prompted to enter the delay time, in seconds, between display updates. Can not be less that 1 second.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>Z</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Change Color Mapping</code> toggle</p>
<dd> This key will take you to a separate screen where you can change the colors for the windows.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>space</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Pause program execution</code> toggle</p>
<dd>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>F1</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Help</code> toggle</p>
<dd> Show help screen.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>q</code>&nbsp;<wbr>&nbsp;<wbr>:<code>Quit</code></p>
<dd>
</dl>
<h2>URLS</h2>
<dl>
<dt>pg_stat_statements module</p>
<dd> <a rel="nofollow" href="http://www.postgresql.org/docs/9.4/static/pgstatstatements.html">http://www.postgresql.org/docs/9.4/static/pgstatstatements.html</a></p>
<dt>PostgreSQL statistics collector</p>
<dd> <a rel="nofollow" href="http://www.postgresql.org/docs/9.4/static/monitoring-stats.html">http://www.postgresql.org/docs/9.4/static/monitoring-stats.html</a> </p>
</dl>
<h2>BUGS</h2>
<p> To report bugs, use <a rel="nofollow" href="http://github.com/lesovsky/pgbconsole/issues">http://github.com/lesovsky/pgbconsole/issues</a> page </p>
<h2>AUTHOR</h2>
<p> Alexey Lesovsky, &lt;lesovsky [at] gmail.com&gt; </p>
<h2>SEE ALSO</h2>
<h2>Index</h2>
