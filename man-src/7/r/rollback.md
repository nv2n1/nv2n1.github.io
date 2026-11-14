---
title: "rollback(7)"
name: "rollback"
section: "7"
letter: "r"
url: "/docs/linux/man/7-rollback/"
description: "ROLLBACK – abort the current transaction"
---

<p>ROLLBACK &#8211; abort the current transaction </p>
<h2>Synopsis</h2>
<pre>ROLLBACK [ WORK | TRANSACTION ]</pre>
<h2>Description</h2>
<p><code>ROLLBACK</code> rolls back the current transaction and causes all the updates made by the transaction to be discarded.</p>
<h2>Parameters</h2>
<dl>
<dt><code>WORK</code></p>
<dd>
<dt><code>TRANSACTION</code></p>
<dd>Optional key words. They have no effect.</dl>
<h2>Notes</h2>
<p>Use COMMIT [<code><a href="/docs/linux/man/7-commit/">commit</a></code>(7)] to successfully terminate a transaction. </p>
<p> Issuing <code>ROLLBACK</code> when not inside a transaction does no harm, but it will provoke a warning message.</p>
<h2>Examples</h2>
<p>To abort all changes: </p>
<pre>ROLLBACK;</pre>
<h2>Compatibility</h2>
<p>The SQL standard only specifies the two forms ROLLBACK and ROLLBACK WORK. Otherwise, this command is fully conforming.</p>
<h2>See Also</h2>
<p>BEGIN [<code><a href="/docs/linux/man/7-begin/">begin</a></code>(7)], COMMIT [<code><a href="/docs/linux/man/7-commit/">commit</a></code>(7)], ROLLBACK TO SAVEPOINT [<code><a href="/docs/linux/man/7-rollback_to_savepoint/">rollback_to_savepoint</a></code>(7)] </p>
