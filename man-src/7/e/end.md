---
title: "end(7)"
name: "end"
section: "7"
letter: "e"
url: "/docs/linux/man/7-end/"
description: "END – commit the current transaction"
---

<p>END &#8211; commit the current transaction </p>
<h2>Synopsis</h2>
<pre>END [ WORK | TRANSACTION ]</pre>
<h2>Description</h2>
<p><code>END</code> commits the current transaction. All changes made by the transaction become visible to others and are guaranteed to be durable if a crash occurs. This command is a PostgreSQL extension that is equivalent to COMMIT [<code><a href="/docs/linux/man/7-commit/">commit</a></code>(7)].</p>
<h2>Parameters</h2>
<dl>
<dt><code>WORK</code></p>
<dd>
<dt><code>TRANSACTION</code></p>
<dd>Optional key words. They have no effect.</dl>
<h2>Notes</h2>
<p>Use ROLLBACK [<code><a href="/docs/linux/man/7-rollback/">rollback</a></code>(7)] to abort a transaction. </p>
<p> Issuing <code>END</code> when not inside a transaction does no harm, but it will provoke a warning message.</p>
<h2>Examples</h2>
<p>To commit the current transaction and make all changes permanent: </p>
<pre>END;</pre>
<h2>Compatibility</h2>
<p><code>END</code> is a PostgreSQL extension that provides functionality equivalent to COMMIT [<code><a href="/docs/linux/man/7-commit/">commit</a></code>(7)], which is specified in the SQL standard.</p>
<h2>See Also</h2>
<p>BEGIN [<code><a href="/docs/linux/man/7-begin/">begin</a></code>(7)], COMMIT [<code><a href="/docs/linux/man/7-commit/">commit</a></code>(7)], ROLLBACK [<code><a href="/docs/linux/man/7-rollback/">rollback</a></code>(7)] </p>
