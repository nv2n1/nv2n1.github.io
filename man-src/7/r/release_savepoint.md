---
title: "release_savepoint(7)"
name: "release_savepoint"
section: "7"
letter: "r"
url: "/docs/linux/man/7-release_savepoint/"
description: "RELEASE SAVEPOINT – destroy a previously defined savepoint"
---

<p>RELEASE SAVEPOINT &#8211; destroy a previously defined savepoint </p>
<h2>Synopsis</h2>
<pre>RELEASE [ SAVEPOINT ] <i>savepoint_name</i></pre>
<h2>Description</h2>
<p><code>RELEASE SAVEPOINT</code> destroys a savepoint previously defined in the current transaction. </p>
<p> Destroying a savepoint makes it unavailable as a rollback point, but it has no other user visible behavior. It does not undo the effects of commands executed after the savepoint was established. (To do that, see ROLLBACK TO SAVEPOINT [<code><a href="/docs/linux/man/7-rollback_to_savepoint/">rollback_to_savepoint</a></code>(7)].) Destroying a savepoint when it is no longer needed allows the system to reclaim some resources earlier than transaction end. </p>
<p> <code>RELEASE SAVEPOINT</code> also destroys all savepoints that were established after the named savepoint was established.</p>
<h2>Parameters</h2>
<dl>
<dt><i>savepoint_name</i></p>
<dd>The name of the savepoint to destroy.</dl>
<h2>Notes</h2>
<p>Specifying a savepoint name that was not previously defined is an error. </p>
<p> It is not possible to release a savepoint when the transaction is in an aborted state. </p>
<p> If multiple savepoints have the same name, only the one that was most recently defined is released.</p>
<h2>Examples</h2>
<p>To establish and later destroy a savepoint: </p>
<pre>BEGIN;
 INSERT INTO table1 VALUES (3);
 SAVEPOINT my_savepoint;
 INSERT INTO table1 VALUES (4);
 RELEASE SAVEPOINT my_savepoint;
COMMIT;</pre>
<p>The above transaction will insert both 3 and 4.</p>
<h2>Compatibility</h2>
<p>This command conforms to the SQL standard. The standard specifies that the key word SAVEPOINT is mandatory, but PostgreSQL allows it to be omitted.</p>
<h2>See Also</h2>
<p>BEGIN [<code><a href="/docs/linux/man/7-begin/">begin</a></code>(7)], COMMIT [<code><a href="/docs/linux/man/7-commit/">commit</a></code>(7)], ROLLBACK [<code><a href="/docs/linux/man/7-rollback/">rollback</a></code>(7)], ROLLBACK TO SAVEPOINT [<code><a href="/docs/linux/man/7-rollback_to_savepoint/">rollback_to_savepoint</a></code>(7)], SAVEPOINT [<code><a href="/docs/linux/man/7-savepoint/">savepoint</a></code>(7)] </p>
