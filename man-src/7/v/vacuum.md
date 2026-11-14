---
title: "vacuum(7)"
name: "vacuum"
section: "7"
letter: "v"
url: "/docs/linux/man/7-vacuum/"
description: "VACUUM – garbage-collect and optionally analyze a database"
---

<p>VACUUM &#8211; garbage-collect and optionally analyze a database </p>
<h2>Synopsis</h2>
<pre>VACUUM [ FULL ] [ FREEZE ] [ VERBOSE ] [ <i>table</i> ]
VACUUM [ FULL ] [ FREEZE ] [ VERBOSE ] ANALYZE [ <i>table</i> [ (<i>column</i> [, ...] ) ] ]</pre>
<h2>Description</h2>
<p><code>VACUUM</code> reclaims storage occupied by dead tuples. In normal PostgreSQL operation, tuples that are deleted or obsoleted by an update are not physically removed from their table; they remain present until a <code>VACUUM</code> is done. Therefore it&#8217;s necessary to do <code>VACUUM</code> periodically, especially on frequently-updated tables. </p>
<p> With no parameter, <code>VACUUM</code> processes every table in the current database that the current user has permission to vacuum. With a parameter, <code>VACUUM</code> processes only that table. </p>
<p> <code>VACUUM ANALYZE</code> performs a <code>VACUUM</code> and then an <code>ANALYZE</code> for each selected table. This is a handy combination form for routine maintenance scripts. See ANALYZE [<code><a href="/docs/linux/man/7-analyze/">analyze</a></code>(7)] for more details about its processing. </p>
<p> Plain <code>VACUUM</code> (without FULL) simply reclaims space and makes it available for re-use. This form of the command can operate in parallel with normal reading and writing of the table, as an exclusive lock is not obtained. <code>VACUUM FULL</code> does more extensive processing, including moving of tuples across blocks to try to compact the table to the minimum number of disk blocks. This form is much slower and requires an exclusive lock on each table while it is being processed.</p>
<h2>Parameters</h2>
<dl>
<dt><code>FULL</code></p>
<dd>Selects &#8220;full&#8221; vacuum, which can reclaim more space, but takes much longer and exclusively locks the table.</p>
<dt><code>FREEZE</code></p>
<dd>Selects aggressive &#8220;freezing&#8221; of tuples. Specifying FREEZE is equivalent to performing <code>VACUUM</code> with the vacuum_freeze_min_age parameter set to zero. The FREEZE option is deprecated and will be removed in a future release; set the parameter instead.</p>
<dt><code>VERBOSE</code></p>
<dd>Prints a detailed vacuum activity report for each table.</p>
<dt><code>ANALYZE</code></p>
<dd>Updates statistics used by the planner to determine the most efficient way to execute a query.</p>
<dt><i>table</i></p>
<dd>The name (optionally schema-qualified) of a specific table to vacuum. Defaults to all tables in the current database.</p>
<dt><i>column</i></p>
<dd>The name of a specific column to analyze. Defaults to all columns.</dl>
<h2>Outputs</h2>
<p>When VERBOSE is specified, <code>VACUUM</code> emits progress messages to indicate which table is currently being processed. Various statistics about the tables are printed as well.</p>
<h2>Notes</h2>
<p>To vacuum a table, one must ordinarily be the table&#8217;s owner or a superuser. However, database owners are allowed to vacuum all tables in their databases, except shared catalogs. (The restriction for shared catalogs means that a true database-wide <code>VACUUM</code> can only be performed by a superuser.) <code>VACUUM</code> will skip over any tables that the calling user does not have permission to vacuum. </p>
<p> <code>VACUUM</code> cannot be executed inside a transaction block. </p>
<p> For tables with GIN indexes, <code>VACUUM</code> (in any form) also completes any pending index insertions, by moving pending index entries to the appropriate places in the main GIN index structure. See in the documentation for details. </p>
<p> We recommend that active production databases be vacuumed frequently (at least nightly), in order to remove dead rows. After adding or deleting a large number of rows, it might be a good idea to issue a <code>VACUUM ANALYZE</code> command for the affected table. This will update the system catalogs with the results of all recent changes, and allow the PostgreSQL query planner to make better choices in planning queries. </p>
<p> The <code>FULL</code> option is not recommended for routine use, but might be useful in special cases. An example is when you have deleted or updated most of the rows in a table and would like the table to physically shrink to occupy less disk space and allow faster table scans. <code>VACUUM FULL</code> will usually shrink the table more than a plain <code>VACUUM</code> would. The <code>FULL</code> option does not shrink indexes; a periodic <code>REINDEX</code> is still recommended. In fact, it is often faster to drop all indexes, <code>VACUUM FULL</code>, and recreate the indexes. </p>
<p> <code>VACUUM</code> causes a substantial increase in I/O traffic, which might cause poor performance for other active sessions. Therefore, it is sometimes advisable to use the cost-based vacuum delay feature. See in the documentation for details. </p>
<p> PostgreSQL includes an &#8220;autovacuum&#8221; facility which can automate routine vacuum maintenance. For more information about automatic and manual vacuuming, see in the documentation.</p>
<h2>Examples</h2>
<p>The following is an example from running <code>VACUUM</code> on a table in the regression database: </p>
<pre>regression=# VACUUM VERBOSE ANALYZE onek;
INFO: vacuuming &quot;public.onek&quot;
INFO: index &quot;onek_unique1&quot; now contains 1000 tuples in 14 pages
DETAIL: 3000 index tuples were removed.
0 index pages have been deleted, 0 are currently reusable.
CPU 0.01s/0.08u sec elapsed 0.18 sec.
INFO: index &quot;onek_unique2&quot; now contains 1000 tuples in 16 pages
DETAIL: 3000 index tuples were removed.
0 index pages have been deleted, 0 are currently reusable.
CPU 0.00s/0.07u sec elapsed 0.23 sec.
INFO: index &quot;onek_hundred&quot; now contains 1000 tuples in 13 pages
DETAIL: 3000 index tuples were removed.
0 index pages have been deleted, 0 are currently reusable.
CPU 0.01s/0.08u sec elapsed 0.17 sec.
INFO: index &quot;onek_stringu1&quot; now contains 1000 tuples in 48 pages
DETAIL: 3000 index tuples were removed.
0 index pages have been deleted, 0 are currently reusable.
CPU 0.01s/0.09u sec elapsed 0.59 sec.
INFO: &quot;onek&quot;: removed 3000 tuples in 108 pages
DETAIL: CPU 0.01s/0.06u sec elapsed 0.07 sec.
INFO: &quot;onek&quot;: found 3000 removable, 1000 nonremovable tuples in 143 pages
DETAIL: 0 dead tuples cannot be removed yet.
There were 0 unused item pointers.
0 pages are entirely empty.
CPU 0.07s/0.39u sec elapsed 1.56 sec.
INFO: analyzing &quot;public.onek&quot;
INFO: &quot;onek&quot;: 36 pages, 1000 rows sampled, 1000 estimated total rows
VACUUM</pre>
<h2>Compatibility</h2>
<p>There is no <code>VACUUM</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>vacuumdb [<code><a href="/docs/linux/man/1-vacuumdb/">vacuumdb</a></code>(1)], in the documentation, in the documentation </p>
