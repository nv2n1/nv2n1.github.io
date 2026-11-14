---
title: "start_transaction(7)"
name: "start_transaction"
section: "7"
letter: "s"
url: "/docs/linux/man/7-start_transaction/"
description: "START TRANSACTION – start a transaction block"
---

<p>START TRANSACTION &#8211; start a transaction block </p>
<h2>Synopsis</h2>
<pre>START TRANSACTION [ <i>transaction_mode</i> [, ...] ]
where <i>transaction_mode</i> is one of:
 ISOLATION LEVEL { SERIALIZABLE | REPEATABLE READ | READ COMMITTED | READ UNCOMMITTED }
 READ WRITE | READ ONLY</pre>
<h2>Description</h2>
<p>This command begins a new transaction block. If the isolation level or read/write mode is specified, the new transaction has those characteristics, as if SET TRANSACTION [<code><a href="/docs/linux/man/7-set_transaction/">set_transaction</a></code>(7)] was executed. This is the same as the BEGIN [<code><a href="/docs/linux/man/7-begin/">begin</a></code>(7)] command.</p>
<h2>Parameters</h2>
<p>Refer to SET TRANSACTION [<code><a href="/docs/linux/man/7-set_transaction/">set_transaction</a></code>(7)] for information on the meaning of the parameters to this statement.</p>
<h2>Compatibility</h2>
<p>In the standard, it is not necessary to issue <code>START TRANSACTION</code> to start a transaction block: any SQL command implicitly begins a block. PostgreSQL&#8217;s behavior can be seen as implicitly issuing a <code>COMMIT</code> after each command that does not follow <code>START TRANSACTION</code> (or <code>BEGIN</code>), and it is therefore often called &#8220;autocommit&#8221;. Other relational database systems might offer an autocommit feature as a convenience. </p>
<p> The SQL standard requires commas between successive <i>transaction_modes</i>, but for historical reasons PostgreSQL allows the commas to be omitted. </p>
<p> See also the compatibility section of SET TRANSACTION [<code><a href="/docs/linux/man/7-set_transaction/">set_transaction</a></code>(7)].</p>
<h2>See Also</h2>
<p>BEGIN [<code><a href="/docs/linux/man/7-begin/">begin</a></code>(7)], COMMIT [<code><a href="/docs/linux/man/7-commit/">commit</a></code>(7)], ROLLBACK [<code><a href="/docs/linux/man/7-rollback/">rollback</a></code>(7)], SAVEPOINT [<code><a href="/docs/linux/man/7-savepoint/">savepoint</a></code>(7)], SET TRANSACTION [<code><a href="/docs/linux/man/7-set_transaction/">set_transaction</a></code>(7)] </p>
