---
title: "set_transaction(7)"
name: "set_transaction"
section: "7"
letter: "s"
url: "/docs/linux/man/7-set_transaction/"
description: "SET TRANSACTION – set the characteristics of the current transaction"
---

<p>SET TRANSACTION &#8211; set the characteristics of the current transaction </p>
<h2>Synopsis</h2>
<pre>SET TRANSACTION <i>transaction_mode</i> [, ...]
SET SESSION CHARACTERISTICS AS TRANSACTION <i>transaction_mode</i> [, ...]
where <i>transaction_mode</i> is one of:
 ISOLATION LEVEL { SERIALIZABLE | REPEATABLE READ | READ COMMITTED | READ UNCOMMITTED }
 READ WRITE | READ ONLY</pre>
<h2>Description</h2>
<p>The <code>SET TRANSACTION</code> command sets the characteristics of the current transaction. It has no effect on any subsequent transactions. <code>SET SESSION CHARACTERISTICS</code> sets the default transaction characteristics for subsequent transactions of a session. These defaults can be overridden by <code>SET TRANSACTION</code> for an individual transaction. </p>
<p> The available transaction characteristics are the transaction isolation level and the transaction access mode (read/write or read-only). </p>
<p> The isolation level of a transaction determines what data the transaction can see when other transactions are running concurrently:</p>
<dl>
<dt><code>READ COMMITTED</code></p>
<dd>A statement can only see rows committed before it began. This is the default.</p>
<dt><code>SERIALIZABLE</code></p>
<dd>All statements of the current transaction can only see rows committed before the first query or data-modification statement was executed in this transaction.</dl>
<p> The SQL standard defines two additional levels, READ UNCOMMITTED and REPEATABLE READ. In PostgreSQL READ UNCOMMITTED is treated as READ COMMITTED, while REPEATABLE READ is treated as SERIALIZABLE. </p>
<p> The transaction isolation level cannot be changed after the first query or data-modification statement (<code>SELECT</code>, <code>INSERT</code>, <code>DELETE</code>, <code>UPDATE</code>, <code>FETCH</code>, or <code>COPY</code>) of a transaction has been executed. See in the documentation for more information about transaction isolation and concurrency control. </p>
<p> The transaction access mode determines whether the transaction is read/write or read-only. Read/write is the default. When a transaction is read-only, the following SQL commands are disallowed: INSERT, UPDATE, DELETE, and COPY FROM if the table they would write to is not a temporary table; all CREATE, ALTER, and DROP commands; COMMENT, GRANT, REVOKE, TRUNCATE; and EXPLAIN ANALYZE and EXECUTE if the command they would execute is among those listed. This is a high-level notion of read-only that does not prevent all writes to disk.</p>
<h2>Notes</h2>
<p>If <code>SET TRANSACTION</code> is executed without a prior <code>START TRANSACTION</code> or <code>BEGIN</code>, it will appear to have no effect, since the transaction will immediately end. </p>
<p> It is possible to dispense with <code>SET TRANSACTION</code> by instead specifying the desired <i>transaction_modes</i> in <code>BEGIN</code> or <code>START TRANSACTION</code>. </p>
<p> The session default transaction modes can also be set by setting the configuration parameters default_transaction_isolation and default_transaction_read_only. (In fact <code>SET SESSION CHARACTERISTICS</code> is just a verbose equivalent for setting these variables with <code>SET</code>.) This means the defaults can be set in the configuration file, via <code>ALTER DATABASE</code>, etc. Consult in the documentation for more information.</p>
<h2>Compatibility</h2>
<p>Both commands are defined in the SQL standard. SERIALIZABLE is the default transaction isolation level in the standard. In PostgreSQL the default is ordinarily READ COMMITTED, but you can change it as mentioned above. Because of lack of predicate locking, the SERIALIZABLE level is not truly serializable. See in the documentation for details. </p>
<p> In the SQL standard, there is one other transaction characteristic that can be set with these commands: the size of the diagnostics area. This concept is specific to embedded SQL, and therefore is not implemented in the PostgreSQL server. </p>
<p> The SQL standard requires commas between successive <i>transaction_modes</i>, but for historical reasons PostgreSQL allows the commas to be omitted.</p>
