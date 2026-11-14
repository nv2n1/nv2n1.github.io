---
title: "savepoint(7)"
name: "savepoint"
section: "7"
letter: "s"
url: "/docs/linux/man/7-savepoint/"
description: "SAVEPOINT – define a new savepoint within the current transaction"
---

<p>SAVEPOINT &#8211; define a new savepoint within the current transaction </p>
<h2>Synopsis</h2>
<pre>SAVEPOINT <i>savepoint_name</i></pre>
<h2>Description</h2>
<p><code>SAVEPOINT</code> establishes a new savepoint within the current transaction. </p>
<p> A savepoint is a special mark inside a transaction that allows all commands that are executed after it was established to be rolled back, restoring the transaction state to what it was at the time of the savepoint.</p>
<h2>Parameters</h2>
<dl>
<dt><i>savepoint_name</i></p>
<dd>The name to give to the new savepoint.</dl>
<h2>Notes</h2>
<p>Use ROLLBACK TO SAVEPOINT [<code><a href="/docs/linux/man/7-rollback_to_savepoint/">rollback_to_savepoint</a></code>(7)] to rollback to a savepoint. Use RELEASE SAVEPOINT [<code><a href="/docs/linux/man/7-release_savepoint/">release_savepoint</a></code>(7)] to destroy a savepoint, keeping the effects of commands executed after it was established. </p>
<p> Savepoints can only be established when inside a transaction block. There can be multiple savepoints defined within a transaction.</p>
<h2>Examples</h2>
<p>To establish a savepoint and later undo the effects of all commands executed after it was established: </p>
<pre>BEGIN;
 INSERT INTO table1 VALUES (1);
 SAVEPOINT my_savepoint;
 INSERT INTO table1 VALUES (2);
 ROLLBACK TO SAVEPOINT my_savepoint;
 INSERT INTO table1 VALUES (3);
COMMIT;</pre>
<p>The above transaction will insert the values 1 and 3, but not 2. </p>
<p> To establish and later destroy a savepoint: </p>
<pre>BEGIN;
 INSERT INTO table1 VALUES (3);
 SAVEPOINT my_savepoint;
 INSERT INTO table1 VALUES (4);
 RELEASE SAVEPOINT my_savepoint;
COMMIT;</pre>
<p>The above transaction will insert both 3 and 4.</p>
<h2>Compatibility</h2>
<p>SQL requires a savepoint to be destroyed automatically when another savepoint with the same name is established. In PostgreSQL, the old savepoint is kept, though only the more recent one will be used when rolling back or releasing. (Releasing the newer savepoint will cause the older one to again become accessible to <code>ROLLBACK TO SAVEPOINT</code> and <code>RELEASE SAVEPOINT</code>.) Otherwise, <code>SAVEPOINT</code> is fully SQL conforming.</p>
<h2>See Also</h2>
<p>BEGIN [<code><a href="/docs/linux/man/7-begin/">begin</a></code>(7)], COMMIT [<code><a href="/docs/linux/man/7-commit/">commit</a></code>(7)], RELEASE SAVEPOINT [<code><a href="/docs/linux/man/7-release_savepoint/">release_savepoint</a></code>(7)], ROLLBACK [<code><a href="/docs/linux/man/7-rollback/">rollback</a></code>(7)], ROLLBACK TO SAVEPOINT [<code><a href="/docs/linux/man/7-rollback_to_savepoint/">rollback_to_savepoint</a></code>(7)] </p>
