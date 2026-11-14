---
title: "reindex(7)"
name: "reindex"
section: "7"
letter: "r"
url: "/docs/linux/man/7-reindex/"
description: "REINDEX – rebuild indexes"
---

<p>REINDEX &#8211; rebuild indexes </p>
<h2>Synopsis</h2>
<pre>REINDEX { INDEX | TABLE | DATABASE | SYSTEM } <i>name</i> [ FORCE ]</pre>
<h2>Description</h2>
<p><code>REINDEX</code> rebuilds an index using the data stored in the index&#8217;s table, replacing the old copy of the index. There are several scenarios in which to use <code>REINDEX</code>:</p>
<dl>
<dt>*</p>
<dd>An index has become corrupted, and no longer contains valid data. Although in theory this should never happen, in practice indexes can become corrupted due to software bugs or hardware failures. <code>REINDEX</code> provides a recovery method.</p>
<dt>*</p>
<dd>An index has become &#8220;bloated&#8221;, that it is contains many empty or nearly-empty pages. This can occur with B-tree indexes in PostgreSQL under certain uncommon access patterns. <code>REINDEX</code> provides a way to reduce the space consumption of the index by writing a new version of the index without the dead pages. See in the documentation for more information.</p>
<dt>*</p>
<dd>You have altered a storage parameter (such as fillfactor) for an index, and wish to ensure that the change has taken full effect.</p>
<dt>*</p>
<dd>An index build with the CONCURRENTLY option failed, leaving an &#8220;invalid&#8221; index. Such indexes are useless but it can be convenient to use <code>REINDEX</code> to rebuild them. Note that <code>REINDEX</code> will not perform a concurrent build. To build the index without interfering with production you should drop the index and reissue the <code>CREATE INDEX CONCURRENTLY</code> command.</dl>
<h2>Parameters</h2>
<dl>
<dt><code>INDEX</code></p>
<dd>Recreate the specified index.</p>
<dt><code>TABLE</code></p>
<dd>Recreate all indexes of the specified table. If the table has a secondary &#8220;TOAST&#8221; table, that is reindexed as well.</p>
<dt><code>DATABASE</code></p>
<dd>Recreate all indexes within the current database. Indexes on shared system catalogs are skipped except in stand-alone mode (see below). This form of <code>REINDEX</code> cannot be executed inside a transaction block.</p>
<dt><code>SYSTEM</code></p>
<dd>Recreate all indexes on system catalogs within the current database. Indexes on user tables are not processed. Also, indexes on shared system catalogs are skipped except in stand-alone mode (see below). This form of <code>REINDEX</code> cannot be executed inside a transaction block.</p>
<dt><i>name</i></p>
<dd>The name of the specific index, table, or database to be reindexed. Index and table names can be schema-qualified. Presently, <code>REINDEX DATABASE</code> and <code>REINDEX SYSTEM</code> can only reindex the current database, so their parameter must match the current database&#8217;s name.</p>
<dt><code>FORCE</code></p>
<dd>This is an obsolete option; it is ignored if specified.</dl>
<h2>Notes</h2>
<p>If you suspect corruption of an index on a user table, you can simply rebuild that index, or all indexes on the table, using <code>REINDEX INDEX</code> or <code>REINDEX TABLE</code>. </p>
<p> Things are more difficult if you need to recover from corruption of an index on a system table. In this case it&#8217;s important for the system to not have used any of the suspect indexes itself. (Indeed, in this sort of scenario you might find that server processes are crashing immediately at start-up, due to reliance on the corrupted indexes.) To recover safely, the server must be started with the <code>-P</code> option, which prevents it from using indexes for system catalog lookups. </p>
<p> One way to do this is to shut down the server and start a single-user PostgreSQL server with the <code>-P</code> option included on its command line. Then, <code>REINDEX DATABASE</code>, <code>REINDEX SYSTEM</code>, <code>REINDEX TABLE</code>, or <code>REINDEX INDEX</code> can be issued, depending on how much you want to reconstruct. If in doubt, use <code>REINDEX SYSTEM</code> to select reconstruction of all system indexes in the database. Then quit the single-user server session and restart the regular server. See the <code><a href="/docs/linux/man/1-postgres/">postgres</a></code>(1) reference page for more information about how to interact with the single-user server interface. </p>
<p> Alternatively, a regular server session can be started with <code>-P</code> included in its command line options. The method for doing this varies across clients, but in all <code>libpq</code>-based clients, it is possible to set the <code>PGOPTIONS</code> environment variable to -P before starting the client. Note that while this method does not require locking out other clients, it might still be wise to prevent other users from connecting to the damaged database until repairs have been completed. </p>
<p> If corruption is suspected in the indexes of any of the shared system catalogs (which are <code>pg_authid</code>, <code>pg_auth_members</code>, <code>pg_database</code>, <code>pg_pltemplate</code>, <code>pg_shdepend</code>, <code>pg_shdescription</code>, and <code>pg_tablespace</code>), then a standalone server must be used to repair it. <code>REINDEX</code> will not process shared catalogs in multiuser mode. </p>
<p> For all indexes except the shared system catalogs, <code>REINDEX</code> is crash-safe and transaction-safe. <code>REINDEX</code> is not crash-safe for shared indexes, which is why this case is disallowed during normal operation. If a failure occurs while reindexing one of these catalogs in standalone mode, it will not be possible to restart the regular server until the problem is rectified. (The typical symptom of a partially rebuilt shared index is &#8220;index is not a btree&#8221; errors.) </p>
<p> <code>REINDEX</code> is similar to a drop and recreate of the index in that the index contents are rebuilt from scratch. However, the locking considerations are rather different. <code>REINDEX</code> locks out writes but not reads of the index&#8217;s parent table. It also takes an exclusive lock on the specific index being processed, which will block reads that attempt to use that index. In contrast, <code>DROP INDEX</code> momentarily takes exclusive lock on the parent table, blocking both writes and reads. The subsequent <code>CREATE INDEX</code> locks out writes but not reads; since the index is not there, no read will attempt to use it, meaning that there will be no blocking but reads might be forced into expensive sequential scans. </p>
<p> Reindexing a single index or table requires being the owner of that index or table. Reindexing a database requires being the owner of the database (note that the owner can therefore rebuild indexes of tables owned by other users). Of course, superusers can always reindex anything. </p>
<p> Prior to PostgreSQL 8.1, <code>REINDEX DATABASE</code> processed only system indexes, not all indexes as one would expect from the name. This has been changed to reduce the surprise factor. The old behavior is available as <code>REINDEX SYSTEM</code>. </p>
<p> Prior to PostgreSQL 7.4, <code>REINDEX TABLE</code> did not automatically process TOAST tables, and so those had to be reindexed by separate commands. This is still possible, but redundant.</p>
<h2>Examples</h2>
<p>Rebuild a single index: </p>
<pre>REINDEX INDEX my_index;</pre>
<p>Rebuild all the indexes on the table my_table: </p>
<pre>REINDEX TABLE my_table;</pre>
<p>Rebuild all indexes in a particular database, without trusting the system indexes to be valid already: </p>
<pre>$ <code>export PGOPTIONS=&quot;-P&quot;</code>
$ <code>psql broken_db</code>
broken_db=&gt; REINDEX DATABASE broken_db;
broken_db=&gt; \q</pre>
<h2>Compatibility</h2>
<p>There is no <code>REINDEX</code> command in the SQL standard.</p>
