---
title: "abort(7)"
name: "abort"
section: "7"
letter: "a"
url: "/docs/linux/man/7-abort/"
description: "ABORT – abort the current transaction"
---

<p>ABORT &#8211; abort the current transaction </p>
<h2>Synopsis</h2>
<pre>ABORT [ WORK | TRANSACTION ]</pre>
<h2>Description</h2>
<p><code>ABORT</code> rolls back the current transaction and causes all the updates made by the transaction to be discarded. This command is identical in behavior to the standard SQL command ROLLBACK [<code><a href="/docs/linux/man/7-rollback/">rollback</a></code>(7)], and is present only for historical reasons.</p>
<h2>Parameters</h2>
<dl>
<dt><code>WORK</code></p>
<dd>
<dt><code>TRANSACTION</code></p>
<dd>Optional key words. They have no effect.</dl>
<h2>Notes</h2>
<p>Use COMMIT [<code><a href="/docs/linux/man/7-commit/">commit</a></code>(7)] to successfully terminate a transaction. </p>
<p> Issuing <code>ABORT</code> when not inside a transaction does no harm, but it will provoke a warning message.</p>
<h2>Examples</h2>
<p>To abort all changes: </p>
<pre>ABORT;</pre>
<h2>Compatibility</h2>
<p>This command is a PostgreSQL extension present for historical reasons. <code>ROLLBACK</code> is the equivalent standard SQL command.</p>
<h2>See Also</h2>
<p>BEGIN [<code><a href="/docs/linux/man/7-begin/">begin</a></code>(7)], COMMIT [<code><a href="/docs/linux/man/7-commit/">commit</a></code>(7)], ROLLBACK [<code><a href="/docs/linux/man/7-rollback/">rollback</a></code>(7)] </p>
