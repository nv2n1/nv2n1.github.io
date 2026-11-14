---
title: "analyze(7)"
name: "analyze"
section: "7"
letter: "a"
url: "/docs/linux/man/7-analyze/"
description: "ANALYZE – collect statistics about a database"
---

<p>ANALYZE &#8211; collect statistics about a database </p>
<h2>Synopsis</h2>
<pre>ANALYZE [ VERBOSE ] [ <i>table</i> [ ( <i>column</i> [, ...] ) ] ]</pre>
<h2>Description</h2>
<p><code>ANALYZE</code> collects statistics about the contents of tables in the database, and stores the results in the <code>pg_statistic</code> system catalog. Subsequently, the query planner uses these statistics to help determine the most efficient execution plans for queries. </p>
<p> With no parameter, <code>ANALYZE</code> examines every table in the current database. With a parameter, <code>ANALYZE</code> examines only that table. It is further possible to give a list of column names, in which case only the statistics for those columns are collected.</p>
<h2>Parameters</h2>
<dl>
<dt><code>VERBOSE</code></p>
<dd>Enables display of progress messages.</p>
<dt><i>table</i></p>
<dd>The name (possibly schema-qualified) of a specific table to analyze. Defaults to all tables in the current database.</p>
<dt><i>column</i></p>
<dd>The name of a specific column to analyze. Defaults to all columns.</dl>
<h2>Outputs</h2>
<p>When VERBOSE is specified, <code>ANALYZE</code> emits progress messages to indicate which table is currently being processed. Various statistics about the tables are printed as well.</p>
<h2>Notes</h2>
<p>In the default PostgreSQL configuration, in the documentation takes care of automatic analyzing of tables when they are first loaded with data, and as they change throughout regular operation. When autovacuum is disabled, it is a good idea to run <code>ANALYZE</code> periodically, or just after making major changes in the contents of a table. Accurate statistics will help the planner to choose the most appropriate query plan, and thereby improve the speed of query processing. A common strategy is to run VACUUM [<code><a href="/docs/linux/man/7-vacuum/">vacuum</a></code>(7)] and <code>ANALYZE</code> once a day during a low-usage time of day. </p>
<p> <code>ANALYZE</code> requires only a read lock on the target table, so it can run in parallel with other activity on the table. </p>
<p> The statistics collected by <code>ANALYZE</code> usually include a list of some of the most common values in each column and a histogram showing the approximate data distribution in each column. One or both of these can be omitted if <code>ANALYZE</code> deems them uninteresting (for example, in a unique-key column, there are no common values) or if the column data type does not support the appropriate operators. There is more information about the statistics in in the documentation. </p>
<p> For large tables, <code>ANALYZE</code> takes a random sample of the table contents, rather than examining every row. This allows even very large tables to be analyzed in a small amount of time. Note, however, that the statistics are only approximate, and will change slightly each time <code>ANALYZE</code> is run, even if the actual table contents did not change. This might result in small changes in the planner&#8217;s estimated costs shown by EXPLAIN [<code><a href="/docs/linux/man/7-explain/">explain</a></code>(7)]. In rare situations, this non-determinism will cause the planner&#8217;s choices of query plans to change after <code>ANALYZE</code> is run. To avoid this, raise the amount of statistics collected by <code>ANALYZE</code>, as described below. </p>
<p> The extent of analysis can be controlled by adjusting the default_statistics_target configuration variable, or on a column-by-column basis by setting the per-column statistics target with <code>ALTER TABLE &#8230; ALTER COLUMN &#8230; SET STATISTICS</code> (see ALTER TABLE [<code><a href="/docs/linux/man/7-alter_table/">alter_table</a></code>(7)]). The target value sets the maximum number of entries in the most-common-value list and the maximum number of bins in the histogram. The default target value is 100, but this can be adjusted up or down to trade off accuracy of planner estimates against the time taken for <code>ANALYZE</code> and the amount of space occupied in pg_statistic. In particular, setting the statistics target to zero disables collection of statistics for that column. It might be useful to do that for columns that are never used as part of the WHERE, GROUP BY, or ORDER BY clauses of queries, since the planner will have no use for statistics on such columns. </p>
<p> The largest statistics target among the columns being analyzed determines the number of table rows sampled to prepare the statistics. Increasing the target causes a proportional increase in the time and space needed to do <code>ANALYZE</code>.</p>
<h2>Compatibility</h2>
<p>There is no <code>ANALYZE</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>VACUUM [<code><a href="/docs/linux/man/7-vacuum/">vacuum</a></code>(7)], vacuumdb [<code><a href="/docs/linux/man/1-vacuumdb/">vacuumdb</a></code>(1)], in the documentation, in the documentation </p>
