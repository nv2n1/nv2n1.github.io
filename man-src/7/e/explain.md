---
title: "explain(7)"
name: "explain"
section: "7"
letter: "e"
url: "/docs/linux/man/7-explain/"
description: "EXPLAIN – show the execution plan of a statement"
---

<p>EXPLAIN &#8211; show the execution plan of a statement </p>
<h2>Synopsis</h2>
<pre>EXPLAIN [ ANALYZE ] [ VERBOSE ] <i>statement</i></pre>
<h2>Description</h2>
<p>This command displays the execution plan that the PostgreSQL planner generates for the supplied statement. The execution plan shows how the table(s) referenced by the statement will be scanned &#8212; by plain sequential scan, index scan, etc. &#8212; and if multiple tables are referenced, what join algorithms will be used to bring together the required rows from each input table. The most critical part of the display is the estimated statement execution cost, which is the planner&#8217;s guess at how long it will take to run the statement (measured in units of disk page fetches). Actually two numbers are shown: the start-up time before the first row can be returned, and the total time to return all the rows. For most queries the total time is what matters, but in contexts such as a subquery in EXISTS, the planner will choose the smallest start-up time instead of the smallest total time (since the executor will stop after getting one row, anyway). Also, if you limit the number of rows to return with a LIMIT clause, the planner makes an appropriate interpolation between the endpoint costs to estimate which plan is really the cheapest. The ANALYZE option causes the statement to be actually executed, not only planned. The total elapsed time expended within each plan node (in milliseconds) and total number of rows it actually returned are added to the display. This is useful for seeing whether the planner&#8217;s estimates are close to reality.</p>
<dl>
<dd><code>Important:</code> Keep in mind that the statement is actually executed when the ANALYZE option is used. Although <code>EXPLAIN</code> will discard any output that a <code>SELECT</code> would return, other side effects of the statement will happen as usual. If you wish to use <code>EXPLAIN ANALYZE</code> on an <code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code>, <code>CREATE TABLE AS</code>, or <code>EXECUTE</code> statement without letting the command affect your data, use this approach: </p>
<pre>BEGIN;
EXPLAIN ANALYZE ...;
ROLLBACK;</pre>
</dl>
<h2>Parameters</h2>
<dl>
<dt><code>ANALYZE</code></p>
<dd>Carry out the command and show the actual run times.</p>
<dt><code>VERBOSE</code></p>
<dd>Include the output column list for each node in the plan tree.</p>
<dt><i>statement</i></p>
<dd>Any <code>SELECT</code>, <code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code>, <code>VALUES</code>, <code>EXECUTE</code>, <code>DECLARE</code>, or <code>CREATE TABLE AS</code> statement, whose execution plan you wish to see.</dl>
<h2>Notes</h2>
<p>There is only sparse documentation on the optimizer&#8217;s use of cost information in PostgreSQL. Refer to in the documentation for more information. </p>
<p> In order to allow the PostgreSQL query planner to make reasonably informed decisions when optimizing queries, the ANALYZE [<code><a href="/docs/linux/man/7-analyze/">analyze</a></code>(7)] statement should be run to record statistics about the distribution of data within the table. If you have not done this (or if the statistical distribution of the data in the table has changed significantly since the last time <code>ANALYZE</code> was run), the estimated costs are unlikely to conform to the real properties of the query, and consequently an inferior query plan might be chosen. </p>
<p> Genetic query optimization (GEQO) randomly tests execution plans. Therefore, when the number of join relations exceeds geqo_threshold causing genetic query optimization to be used, the execution plan is likely to change each time the statement is executed. </p>
<p> In order to measure the run-time cost of each node in the execution plan, the current implementation of <code>EXPLAIN ANALYZE</code> can add considerable profiling overhead to query execution. As a result, running <code>EXPLAIN ANALYZE</code> on a query can sometimes take significantly longer than executing the query normally. The amount of overhead depends on the nature of the query.</p>
<h2>Examples</h2>
<p>To show the plan for a simple query on a table with a single <code>integer</code> column and 10000 rows: </p>
<pre>EXPLAIN SELECT * FROM foo;
 QUERY PLAN
---------------------------------------------------------
 Seq Scan on foo (cost=0.00..155.00 rows=10000 width=4)
(1 row)</pre>
<p>If there is an index and we use a query with an indexable WHERE condition, <code>EXPLAIN</code> might show a different plan: </p>
<pre>EXPLAIN SELECT * FROM foo WHERE i = 4;
 QUERY PLAN
--------------------------------------------------------------
 Index Scan using fi on foo (cost=0.00..5.98 rows=1 width=4)
 Index Cond: (i = 4)
(2 rows)</pre>
<p>Here is an example of a query plan for a query using an aggregate function: </p>
<pre>EXPLAIN SELECT sum(i) FROM foo WHERE i &lt; 10;
 QUERY PLAN
---------------------------------------------------------------------
 Aggregate (cost=23.93..23.93 rows=1 width=4)
 -&gt; Index Scan using fi on foo (cost=0.00..23.92 rows=6 width=4)
 Index Cond: (i &lt; 10)
(3 rows)</pre>
<p>Here is an example of using <code>EXPLAIN EXECUTE</code> to display the execution plan for a prepared query: </p>
<pre>PREPARE query(int, int) AS SELECT sum(bar) FROM test
 WHERE id &gt; $1 AND id &lt; $2
 GROUP BY foo;
EXPLAIN ANALYZE EXECUTE query(100, 200);
 QUERY PLAN 
-------------------------------------------------------------------------------------------------------------------------
 HashAggregate (cost=39.53..39.53 rows=1 width=8) (actual time=0.661..0.672 rows=7 loops=1)
 -&gt; Index Scan using test_pkey on test (cost=0.00..32.97 rows=1311 width=8) (actual time=0.050..0.395 rows=99 loops=1)
 Index Cond: ((id &gt; $1) AND (id &lt; $2))
 Total runtime: 0.851 ms
(4 rows)</pre>
<p>Of course, the specific numbers shown here depend on the actual contents of the tables involved. Also note that the numbers, and even the selected query strategy, might vary between PostgreSQL releases due to planner improvements. In addition, the <code>ANALYZE</code> command uses random sampling to estimate data statistics; therefore, it is possible for cost estimates to change after a fresh run of <code>ANALYZE</code>, even if the actual distribution of data in the table has not changed.</p>
<h2>Compatibility</h2>
<p>There is no <code>EXPLAIN</code> statement defined in the SQL standard.</p>
<h2>See Also</h2>
<p>ANALYZE [<code><a href="/docs/linux/man/7-analyze/">analyze</a></code>(7)] </p>
