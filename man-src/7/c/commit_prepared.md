---
title: "commit_prepared(7)"
name: "commit_prepared"
section: "7"
letter: "c"
url: "/docs/linux/man/7-commit_prepared/"
description: "COMMIT PREPARED – commit a transaction that was earlier prepared for two-phase commit"
---

<p>COMMIT PREPARED &#8211; commit a transaction that was earlier prepared for two-phase commit </p>
<h2>Synopsis</h2>
<pre>COMMIT PREPARED <i>transaction_id</i></pre>
<h2>Description</h2>
<p><code>COMMIT PREPARED</code> commits a transaction that is in prepared state.</p>
<h2>Parameters</h2>
<dl>
<dt><i>transaction_id</i></p>
<dd>The transaction identifier of the transaction that is to be committed.</dl>
<h2>Notes</h2>
<p>To commit a prepared transaction, you must be either the same user that executed the transaction originally, or a superuser. But you do not have to be in the same session that executed the transaction. </p>
<p> This command cannot be executed inside a transaction block. The prepared transaction is committed immediately. </p>
<p> All currently available prepared transactions are listed in the <code>pg_prepared_xacts</code> system view.</p>
<h2>Examples</h2>
<p>Commit the transaction identified by the transaction identifier foobar: </p>
<pre>COMMIT PREPARED 'foobar';</pre>
<h2>See Also</h2>
<p>PREPARE TRANSACTION [<code><a href="/docs/linux/man/7-prepare_transaction/">prepare_transaction</a></code>(7)], ROLLBACK PREPARED [<code><a href="/docs/linux/man/7-rollback_prepared/">rollback_prepared</a></code>(7)] </p>
