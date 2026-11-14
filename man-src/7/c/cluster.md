---
title: "cluster(7)"
name: "cluster"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cluster/"
description: "CLUSTER – cluster a table according to an index"
---

<p>CLUSTER &#8211; cluster a table according to an index </p>
<h2>Synopsis</h2>
<pre>CLUSTER [VERBOSE] <i>tablename</i> [ USING <i>indexname</i> ]
CLUSTER [VERBOSE]</pre>
<h2>Description</h2>
<p><code>CLUSTER</code> instructs PostgreSQL to cluster the table specified by <i>tablename</i> based on the index specified by <i>indexname</i>. The index must already have been defined on <i>tablename</i>. </p>
<p> When a table is clustered, it is physically reordered based on the index information. Clustering is a one-time operation: when the table is subsequently updated, the changes are not clustered. That is, no attempt is made to store new or updated rows according to their index order. (If one wishes, one can periodically recluster by issuing the command again. Also, setting the table&#8217;s FILLFACTOR storage parameter to less than 100% can aid in preserving cluster ordering during updates, since updated rows are preferentially kept on the same page.) </p>
<p> When a table is clustered, PostgreSQL remembers which index it was clustered by. The form <code>CLUSTER </code><i>tablename</i> reclusters the table using the same index as before. </p>
<p> <code>CLUSTER</code> without any parameter reclusters all the previously-clustered tables in the current database that the calling user owns, or all such tables if called by a superuser. This form of <code>CLUSTER</code> cannot be executed inside a transaction block. </p>
<p> When a table is being clustered, an ACCESS EXCLUSIVE lock is acquired on it. This prevents any other database operations (both reads and writes) from operating on the table until the <code>CLUSTER</code> is finished.</p>
<h2>Parameters</h2>
<dl>
<dt><i>tablename</i></p>
<dd>The name (possibly schema-qualified) of a table.</p>
<dt><i>indexname</i></p>
<dd>The name of an index.</p>
<dt><code>VERBOSE</code></p>
<dd>Prints a progress report as each table is clustered.</dl>
<h2>Notes</h2>
<p>In cases where you are accessing single rows randomly within a table, the actual order of the data in the table is unimportant. However, if you tend to access some data more than others, and there is an index that groups them together, you will benefit from using <code>CLUSTER</code>. If you are requesting a range of indexed values from a table, or a single indexed value that has multiple rows that match, <code>CLUSTER</code> will help because once the index identifies the table page for the first row that matches, all other rows that match are probably already on the same table page, and so you save disk accesses and speed up the query. </p>
<p> During the cluster operation, a temporary copy of the table is created that contains the table data in the index order. Temporary copies of each index on the table are created as well. Therefore, you need free space on disk at least equal to the sum of the table size and the index sizes. </p>
<p> Because <code>CLUSTER</code> remembers the clustering information, one can cluster the tables one wants clustered manually the first time, and setup a timed event similar to <code>VACUUM</code> so that the tables are periodically reclustered. </p>
<p> Because the planner records statistics about the ordering of tables, it is advisable to run ANALYZE [<code><a href="/docs/linux/man/7-analyze/">analyze</a></code>(7)] on the newly clustered table. Otherwise, the planner might make poor choices of query plans. </p>
<p> There is another way to cluster data. The <code>CLUSTER</code> command reorders the original table by scanning it using the index you specify. This can be slow on large tables because the rows are fetched from the table in index order, and if the table is disordered, the entries are on random pages, so there is one disk page retrieved for every row moved. (PostgreSQL has a cache, but the majority of a big table will not fit in the cache.) The other way to cluster a table is to use: </p>
<pre>CREATE TABLE <i>newtable</i> AS
 SELECT * FROM <i>table</i> ORDER BY <i>columnlist</i>;</pre>
<p>which uses the PostgreSQL sorting code to produce the desired order; this is usually much faster than an index scan for disordered data. Then you drop the old table, use <code>ALTER TABLE &#8230; RENAME</code> to rename <i>newtable</i> to the old name, and recreate the table&#8217;s indexes. The big disadvantage of this approach is that it does not preserve OIDs, constraints, foreign key relationships, granted privileges, and other ancillary properties of the table &#8212; all such items must be manually recreated. Another disadvantage is that this way requires a sort temporary file about the same size as the table itself, so peak disk usage is about three times the table size instead of twice the table size.</p>
<h2>Examples</h2>
<p>Cluster the table employees on the basis of its index employees_ind: </p>
<pre>CLUSTER employees USING employees_ind;</pre>
<p>Cluster the employees table using the same index that was used before: </p>
<pre>CLUSTER employees;</pre>
<p>Cluster all tables in the database that have previously been clustered: </p>
<pre>CLUSTER;</pre>
<h2>Compatibility</h2>
<p>There is no <code>CLUSTER</code> statement in the SQL standard. </p>
<p> The syntax </p>
<pre>CLUSTER <i>indexname</i> ON <i>tablename</i></pre>
<p>is also supported for compatibility with pre-8.3 PostgreSQL versions.</p>
<h2>See Also</h2>
<p>clusterdb [<code><a href="/docs/linux/man/1-clusterdb/">clusterdb</a></code>(1)] </p>
