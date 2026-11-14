---
title: "rollback_prepared(7)"
name: "rollback_prepared"
section: "7"
letter: "r"
url: "/docs/linux/man/7-rollback_prepared/"
description: "ROLLBACK PREPARED – cancel a transaction that was earlier prepared for two-phase commit"
---

<p>ROLLBACK PREPARED &#8211; cancel a transaction that was earlier prepared for two-phase commit </p>
<h2>Synopsis</h2>
<pre>ROLLBACK PREPARED <i>transaction_id</i></pre>
<h2>Description</h2>
<p><code>ROLLBACK PREPARED</code> rolls back a transaction that is in prepared state.</p>
<h2>Parameters</h2>
<dl>
<dt><i>transaction_id</i></p>
<dd>The transaction identifier of the transaction that is to be rolled back.</dl>
<h2>Notes</h2>
<p>To roll back a prepared transaction, you must be either the same user that executed the transaction originally, or a superuser. But you do not have to be in the same session that executed the transaction. </p>
<p> This command cannot be executed inside a transaction block. The prepared transaction is rolled back immediately. </p>
<p> All currently available prepared transactions are listed in the <code>pg_prepared_xacts</code> system view.</p>
<h2>Examples</h2>
<p>Roll back the transaction identified by the transaction identifier foobar: </p>
<pre>ROLLBACK PREPARED 'foobar';</pre>
<h2>See Also</h2>
<p>PREPARE TRANSACTION [<code><a href="/docs/linux/man/7-prepare_transaction/">prepare_transaction</a></code>(7)], COMMIT PREPARED [<code><a href="/docs/linux/man/7-commit_prepared/">commit_prepared</a></code>(7)] </p>
