---
title: "begin(7)"
name: "begin"
section: "7"
letter: "b"
url: "/docs/linux/man/7-begin/"
description: "BEGIN – start a transaction block"
---

<p>BEGIN &#8211; start a transaction block </p>
<h2>Synopsis</h2>
<pre>BEGIN [ WORK | TRANSACTION ] [ <i>transaction_mode</i> [, ...] ]
where <i>transaction_mode</i> is one of:
 ISOLATION LEVEL { SERIALIZABLE | REPEATABLE READ | READ COMMITTED | READ UNCOMMITTED }
 READ WRITE | READ ONLY</pre>
<h2>Description</h2>
<p><code>BEGIN</code> initiates a transaction block, that is, all statements after a <code>BEGIN</code> command will be executed in a single transaction until an explicit COMMIT [<code><a href="/docs/linux/man/7-commit/">commit</a></code>(7)] or ROLLBACK [<code><a href="/docs/linux/man/7-rollback/">rollback</a></code>(7)] is given. By default (without <code>BEGIN</code>), PostgreSQL executes transactions in &#8220;autocommit&#8221; mode, that is, each statement is executed in its own transaction and a commit is implicitly performed at the end of the statement (if execution was successful, otherwise a rollback is done). </p>
<p> Statements are executed more quickly in a transaction block, because transaction start/commit requires significant CPU and disk activity. Execution of multiple statements inside a transaction is also useful to ensure consistency when making several related changes: other sessions will be unable to see the intermediate states wherein not all the related updates have been done. </p>
<p> If the isolation level or read/write mode is specified, the new transaction has those characteristics, as if SET TRANSACTION [<code><a href="/docs/linux/man/7-set_transaction/">set_transaction</a></code>(7)] was executed.</p>
<h2>Parameters</h2>
<dl>
<dt><code>WORK</code></p>
<dd>
<dt><code>TRANSACTION</code></p>
<dd>Optional key words. They have no effect.</dl>
<p> Refer to SET TRANSACTION [<code><a href="/docs/linux/man/7-set_transaction/">set_transaction</a></code>(7)] for information on the meaning of the other parameters to this statement.</p>
<h2>Notes</h2>
<p>START TRANSACTION [<code><a href="/docs/linux/man/7-start_transaction/">start_transaction</a></code>(7)] has the same functionality as <code>BEGIN</code>. </p>
<p> Use COMMIT [<code><a href="/docs/linux/man/7-commit/">commit</a></code>(7)] or ROLLBACK [<code><a href="/docs/linux/man/7-rollback/">rollback</a></code>(7)] to terminate a transaction block. </p>
<p> Issuing <code>BEGIN</code> when already inside a transaction block will provoke a warning message. The state of the transaction is not affected. To nest transactions within a transaction block, use savepoints (see SAVEPOINT [<code><a href="/docs/linux/man/7-savepoint/">savepoint</a></code>(7)]). </p>
<p> For reasons of backwards compatibility, the commas between successive <i>transaction_modes</i> can be omitted.</p>
<h2>Examples</h2>
<p>To begin a transaction block: </p>
<pre>BEGIN;</pre>
<h2>Compatibility</h2>
<p><code>BEGIN</code> is a PostgreSQL language extension. It is equivalent to the SQL-standard command START TRANSACTION [<code><a href="/docs/linux/man/7-start_transaction/">start_transaction</a></code>(7)], whose reference page contains additional compatibility information. </p>
<p> Incidentally, the BEGIN key word is used for a different purpose in embedded SQL. You are advised to be careful about the transaction semantics when porting database applications.</p>
<h2>See Also</h2>
<p>COMMIT [<code><a href="/docs/linux/man/7-commit/">commit</a></code>(7)], ROLLBACK [<code><a href="/docs/linux/man/7-rollback/">rollback</a></code>(7)], START TRANSACTION [<code><a href="/docs/linux/man/7-start_transaction/">start_transaction</a></code>(7)], SAVEPOINT [<code><a href="/docs/linux/man/7-savepoint/">savepoint</a></code>(7)] </p>
