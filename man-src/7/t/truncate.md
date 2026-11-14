---
title: "truncate(7)"
name: "truncate"
section: "7"
letter: "t"
url: "/docs/linux/man/7-truncate/"
description: "TRUNCATE – empty a table or set of tables"
---

<p>TRUNCATE &#8211; empty a table or set of tables </p>
<h2>Synopsis</h2>
<pre>TRUNCATE [ TABLE ] [ ONLY ] <i>name</i> [, ... ]
 [ RESTART IDENTITY | CONTINUE IDENTITY ] [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>TRUNCATE</code> quickly removes all rows from a set of tables. It has the same effect as an unqualified <code>DELETE</code> on each table, but since it does not actually scan the tables it is faster. Furthermore, it reclaims disk space immediately, rather than requiring a subsequent <code>VACUUM</code> operation. This is most useful on large tables.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of a table to be truncated. If ONLY is specified, only that table is truncated. If ONLY is not specified, the table and all its descendant tables (if any) are truncated.</p>
<dt><code>RESTART IDENTITY</code></p>
<dd>Automatically restart sequences owned by columns of the truncated table(s).</p>
<dt><code>CONTINUE IDENTITY</code></p>
<dd>Do not change the values of sequences. This is the default.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically truncate all tables that have foreign-key references to any of the named tables, or to any tables added to the group due to CASCADE.</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to truncate if any of the tables have foreign-key references from tables that are not listed in the command. This is the default.</dl>
<h2>Notes</h2>
<p>You must have the TRUNCATE privilege on a table to truncate it. <code>TRUNCATE</code> acquires an ACCESS EXCLUSIVE lock on each table it operates on, which blocks all other concurrent operations on the table. If concurrent access to a table is required, then the <code>DELETE</code> command should be used instead. <code>TRUNCATE</code> cannot be used on a table that has foreign-key references from other tables, unless all such tables are also truncated in the same command. Checking validity in such cases would require table scans, and the whole point is not to do one. The CASCADE option can be used to automatically include all dependent tables &#8212; but be very careful when using this option, or else you might lose data you did not intend to! <code>TRUNCATE</code> will not fire any ON DELETE triggers that might exist for the tables. But it will fire ON TRUNCATE triggers. If ON TRUNCATE triggers are defined for any of the tables, then all BEFORE TRUNCATE triggers are fired before any truncation happens, and all AFTER TRUNCATE triggers are fired after the last truncation is performed. The triggers will fire in the order that the tables are to be processed (first those listed in the command, and then any that were added due to cascading).</p>
<dl>
<dd><code>Warning:</code> <code>TRUNCATE</code> is not MVCC-safe (see in the documentation for general information about MVCC). After truncation, the table will appear empty to all concurrent transactions, even if they are using a snapshot taken before the truncation occurred. This will only be an issue for a transaction that did not access the truncated table before the truncation happened &#8212; any transaction that has done so would hold at least an ACCESS SHARE lock, which would block <code>TRUNCATE</code> until that transaction completes. So truncation will not cause any apparent inconsistency in the table contents for successive queries on the same table, but it could cause visible inconsistency between the contents of the truncated table and other tables in the database.</dl>
<p> <code>TRUNCATE</code> is transaction-safe with respect to the data in the tables: the truncation will be safely rolled back if the surrounding transaction does not commit.</p>
<dl>
<dd><code>Warning:</code> Any <code>ALTER SEQUENCE RESTART</code> operations performed as a consequence of using the RESTART IDENTITY option are nontransactional and will not be rolled back on failure. To minimize the risk, these operations are performed only after all the rest of <code>TRUNCATE</code>&#8216;s work is done. However, there is still a risk if <code>TRUNCATE</code> is performed inside a transaction block that is aborted afterwards. For example, consider </p>
<pre>BEGIN;
TRUNCATE TABLE foo RESTART IDENTITY;
COPY foo FROM ...;
COMMIT;</pre>
<p>If the <code>COPY</code> fails partway through, the table data rolls back correctly, but the sequences will be left with values that are probably smaller than they had before, possibly leading to duplicate-key failures or other problems in later transactions. If this is likely to be a problem, it&#8217;s best to avoid using RESTART IDENTITY, and accept that the new contents of the table will have higher serial numbers than the old.</dl>
<h2>Examples</h2>
<p>Truncate the tables bigtable and fattable: </p>
<pre>TRUNCATE bigtable, fattable;</pre>
<p>The same, and also reset any associated sequence generators: </p>
<pre>TRUNCATE bigtable, fattable RESTART IDENTITY;</pre>
<p>Truncate the table othertable, and cascade to any tables that reference othertable via foreign-key constraints: </p>
<pre>TRUNCATE othertable CASCADE;</pre>
<h2>Compatibility</h2>
<p>The SQL:2008 standard includes a <code>TRUNCATE</code> command with the syntax TRUNCATE TABLE <i>tablename</i>. The clauses CONTINUE IDENTITY/RESTART IDENTITY also appear in that standard but have slightly different but related meanings. Some of the concurrency behavior of this command is left implementation-defined by the standard, so the above notes should be considered and compared with other implementations if necessary.</p>
