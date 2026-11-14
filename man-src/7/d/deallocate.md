---
title: "deallocate(7)"
name: "deallocate"
section: "7"
letter: "d"
url: "/docs/linux/man/7-deallocate/"
description: "DEALLOCATE – deallocate a prepared statement"
---

<p>DEALLOCATE &#8211; deallocate a prepared statement </p>
<h2>Synopsis</h2>
<pre>DEALLOCATE [ PREPARE ] { <i>name</i> | ALL }</pre>
<h2>Description</h2>
<p><code>DEALLOCATE</code> is used to deallocate a previously prepared SQL statement. If you do not explicitly deallocate a prepared statement, it is deallocated when the session ends. </p>
<p> For more information on prepared statements, see PREPARE [<code><a href="/docs/linux/man/7-prepare/">prepare</a></code>(7)].</p>
<h2>Parameters</h2>
<dl>
<dt><code>PREPARE</code></p>
<dd>This key word is ignored.</p>
<dt><i>name</i></p>
<dd>The name of the prepared statement to deallocate.</p>
<dt><code>ALL</code></p>
<dd>Deallocate all prepared statements.</dl>
<h2>Compatibility</h2>
<p>The SQL standard includes a <code>DEALLOCATE</code> statement, but it is only for use in embedded SQL.</p>
<h2>See Also</h2>
<p>EXECUTE [<code><a href="/docs/linux/man/7-execute/">execute</a></code>(7)], PREPARE [<code><a href="/docs/linux/man/7-prepare/">prepare</a></code>(7)] </p>
