---
title: "drop_cast(7)"
name: "drop_cast"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_cast/"
description: "DROP CAST – remove a cast"
---

<p>DROP CAST &#8211; remove a cast </p>
<h2>Synopsis</h2>
<pre>DROP CAST [ IF EXISTS ] (<i>sourcetype</i> AS <i>targettype</i>) [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP CAST</code> removes a previously defined cast. </p>
<p> To be able to drop a cast, you must own the source or the target data type. These are the same privileges that are required to create a cast.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the cast does not exist. A notice is issued in this case.</p>
<dt><i>sourcetype</i></p>
<dd>The name of the source data type of the cast.</p>
<dt><i>targettype</i></p>
<dd>The name of the target data type of the cast.</p>
<dt><code>CASCADE</code></p>
<dd>
<dt><code>RESTRICT</code></p>
<dd>These key words do not have any effect, since there are no dependencies on casts.</dl>
<h2>Examples</h2>
<p>To drop the cast from type <code>text</code> to type <code>int</code>: </p>
<pre>DROP CAST (text AS int);</pre>
<h2>Compatibility</h2>
<p>The <code>DROP CAST</code> command conforms to the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE CAST [<code><a href="/docs/linux/man/7-create_cast/">create_cast</a></code>(7)] </p>
