---
title: "rollback_to_savepoint(7)"
name: "rollback_to_savepoint"
section: "7"
letter: "r"
url: "/docs/linux/man/7-rollback_to_savepoint/"
description: "ROLLBACK TO SAVEPOINT – roll back to a savepoint"
---

<p>ROLLBACK TO SAVEPOINT &#8211; roll back to a savepoint </p>
<h2>Synopsis</h2>
<pre>ROLLBACK [ WORK | TRANSACTION ] TO [ SAVEPOINT ] <i>savepoint_name</i></pre>
<h2>Description</h2>
<p>Roll back all commands that were executed after the savepoint was established. The savepoint remains valid and can be rolled back to again later, if needed. </p>
<p> <code>ROLLBACK TO SAVEPOINT</code> implicitly destroys all savepoints that were established after the named savepoint.</p>
<h2>Parameters</h2>
<dl>
<dt><i>savepoint_name</i></p>
<dd>The savepoint to roll back to.</dl>
<h2>Notes</h2>
<p>Use RELEASE SAVEPOINT [<code><a href="/docs/linux/man/7-release_savepoint/">release_savepoint</a></code>(7)] to destroy a savepoint without discarding the effects of commands executed after it was established. </p>
<p> Specifying a savepoint name that has not been established is an error. </p>
<p> Cursors have somewhat non-transactional behavior with respect to savepoints. Any cursor that is opened inside a savepoint will be closed when the savepoint is rolled back. If a previously opened cursor is affected by a <code>FETCH</code> command inside a savepoint that is later rolled back, the cursor position remains at the position that <code>FETCH</code> left it pointing to (that is, <code>FETCH</code> is not rolled back). Closing a cursor is not undone by rolling back, either. A cursor whose execution causes a transaction to abort is put in a cannot-execute state, so while the transaction can be restored using <code>ROLLBACK TO SAVEPOINT</code>, the cursor can no longer be used.</p>
<h2>Examples</h2>
<p>To undo the effects of the commands executed after my_savepoint was established: </p>
<pre>ROLLBACK TO SAVEPOINT my_savepoint;</pre>
<p>Cursor positions are not affected by savepoint rollback: </p>
<pre>BEGIN;
DECLARE foo CURSOR FOR SELECT 1 UNION SELECT 2;
SAVEPOINT foo;
FETCH 1 FROM foo;
 ?column? 
----------
 1
ROLLBACK TO SAVEPOINT foo;
FETCH 1 FROM foo;
 ?column? 
----------
 2
COMMIT;</pre>
<h2>Compatibility</h2>
<p>The SQL standard specifies that the key word SAVEPOINT is mandatory, but PostgreSQL and Oracle allow it to be omitted. SQL allows only WORK, not TRANSACTION, as a noise word after ROLLBACK. Also, SQL has an optional clause AND [ NO ] CHAIN which is not currently supported by PostgreSQL. Otherwise, this command conforms to the SQL standard.</p>
<h2>See Also</h2>
<p>BEGIN [<code><a href="/docs/linux/man/7-begin/">begin</a></code>(7)], COMMIT [<code><a href="/docs/linux/man/7-commit/">commit</a></code>(7)], RELEASE SAVEPOINT [<code><a href="/docs/linux/man/7-release_savepoint/">release_savepoint</a></code>(7)], ROLLBACK [<code><a href="/docs/linux/man/7-rollback/">rollback</a></code>(7)], SAVEPOINT [<code><a href="/docs/linux/man/7-savepoint/">savepoint</a></code>(7)] </p>
