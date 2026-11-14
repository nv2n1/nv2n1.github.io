---
title: "close(7)"
name: "close"
section: "7"
letter: "c"
url: "/docs/linux/man/7-close/"
description: "CLOSE – close a cursor"
---

<p>CLOSE &#8211; close a cursor </p>
<h2>Synopsis</h2>
<pre>CLOSE { <i>name</i> | ALL }</pre>
<h2>Description</h2>
<p><code>CLOSE</code> frees the resources associated with an open cursor. After the cursor is closed, no subsequent operations are allowed on it. A cursor should be closed when it is no longer needed. </p>
<p> Every non-holdable open cursor is implicitly closed when a transaction is terminated by <code>COMMIT</code> or <code>ROLLBACK</code>. A holdable cursor is implicitly closed if the transaction that created it aborts via <code>ROLLBACK</code>. If the creating transaction successfully commits, the holdable cursor remains open until an explicit <code>CLOSE</code> is executed, or the client disconnects.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of an open cursor to close.</p>
<dt><code>ALL</code></p>
<dd>Close all open cursors.</dl>
<h2>Notes</h2>
<p>PostgreSQL does not have an explicit <code>OPEN</code> cursor statement; a cursor is considered open when it is declared. Use the DECLARE [<code><a href="/docs/linux/man/7-declare/">declare</a></code>(7)] statement to declare a cursor. </p>
<p> You can see all available cursors by querying the <code>pg_cursors</code> system view. </p>
<p> If a cursor is closed after a savepoint which is later rolled back, the <code>CLOSE</code> is not rolled back; that is, the cursor remains closed.</p>
<h2>Examples</h2>
<p>Close the cursor liahona: </p>
<pre>CLOSE liahona;</pre>
<h2>Compatibility</h2>
<p><code>CLOSE</code> is fully conforming with the SQL standard. <code>CLOSE ALL</code> is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>DECLARE [<code><a href="/docs/linux/man/7-declare/">declare</a></code>(7)], FETCH [<code><a href="/docs/linux/man/7-fetch/">fetch</a></code>(7)], MOVE [<code><a href="/docs/linux/man/7-move/">move</a></code>(7)] </p>
