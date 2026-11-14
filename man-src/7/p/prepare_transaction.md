---
title: "prepare_transaction(7)"
name: "prepare_transaction"
section: "7"
letter: "p"
url: "/docs/linux/man/7-prepare_transaction/"
description: "PREPARE TRANSACTION – prepare the current transaction for two-phase commit"
---

<p>PREPARE TRANSACTION &#8211; prepare the current transaction for two-phase commit </p>
<h2>Synopsis</h2>
<pre>PREPARE TRANSACTION <i>transaction_id</i></pre>
<h2>Description</h2>
<p><code>PREPARE TRANSACTION</code> prepares the current transaction for two-phase commit. After this command, the transaction is no longer associated with the current session; instead, its state is fully stored on disk, and there is a very high probability that it can be committed successfully, even if a database crash occurs before the commit is requested. </p>
<p> Once prepared, a transaction can later be committed or rolled back with COMMIT PREPARED [<code><a href="/docs/linux/man/7-commit_prepared/">commit_prepared</a></code>(7)] or ROLLBACK PREPARED [<code><a href="/docs/linux/man/7-rollback_prepared/">rollback_prepared</a></code>(7)], respectively. Those commands can be issued from any session, not only the one that executed the original transaction. </p>
<p> From the point of view of the issuing session, <code>PREPARE TRANSACTION</code> is not unlike a <code>ROLLBACK</code> command: after executing it, there is no active current transaction, and the effects of the prepared transaction are no longer visible. (The effects will become visible again if the transaction is committed.) </p>
<p> If the <code>PREPARE TRANSACTION</code> command fails for any reason, it becomes a <code>ROLLBACK</code>: the current transaction is canceled.</p>
<h2>Parameters</h2>
<dl>
<dt><i>transaction_id</i></p>
<dd>An arbitrary identifier that later identifies this transaction for <code>COMMIT PREPARED</code> or <code>ROLLBACK PREPARED</code>. The identifier must be written as a string literal, and must be less than 200 bytes long. It must not be the same as the identifier used for any currently prepared transaction.</dl>
<h2>Notes</h2>
<p>This command must be used inside a transaction block. Use BEGIN [<code><a href="/docs/linux/man/7-begin/">begin</a></code>(7)] to start one. It is not currently allowed to <code>PREPARE</code> a transaction that has executed any operations involving temporary tables, created any cursors WITH HOLD, or executed <code>LISTEN</code> or <code>UNLISTEN</code>. Those features are too tightly tied to the current session to be useful in a transaction to be prepared. If the transaction modified any run-time parameters with <code>SET</code> (without the LOCAL option), those effects persist after <code>PREPARE TRANSACTION</code>, and will not be affected by any later <code>COMMIT PREPARED</code> or <code>ROLLBACK PREPARED</code>. Thus, in this one respect <code>PREPARE TRANSACTION</code> acts more like <code>COMMIT</code> than <code>ROLLBACK</code>. All currently available prepared transactions are listed in the <code>pg_prepared_xacts</code> system view.</p>
<dl>
<dd><code>Caution:</code> It is unwise to leave transactions in the prepared state for a long time. This will interfere with the ability of <code>VACUUM</code> to reclaim storage, and in extreme cases could cause the database to shut down to prevent transaction ID wraparound (see in the documentation). Keep in mind also that the transaction continues to hold whatever locks it held. The intended usage of the feature is that a prepared transaction will normally be committed or rolled back as soon as an external transaction manager has verified that other databases are also prepared to commit. If you have not set up an external transaction manager to track prepared transactions and ensure they get closed out promptly, it is best to keep the prepared-transaction feature disabled by setting max_prepared_transactions to zero. This will prevent accidental creation of prepared transactions that might then be forgotten and eventually cause problems.</dl>
<h2>Examples</h2>
<p>Prepare the current transaction for two-phase commit, using foobar as the transaction identifier: </p>
<pre>PREPARE TRANSACTION 'foobar';</pre>
<h2>See Also</h2>
<p>COMMIT PREPARED [<code><a href="/docs/linux/man/7-commit_prepared/">commit_prepared</a></code>(7)], ROLLBACK PREPARED [<code><a href="/docs/linux/man/7-rollback_prepared/">rollback_prepared</a></code>(7)] </p>
