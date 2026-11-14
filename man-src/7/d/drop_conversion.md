---
title: "drop_conversion(7)"
name: "drop_conversion"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_conversion/"
description: "DROP CONVERSION – remove a conversion"
---

<p>DROP CONVERSION &#8211; remove a conversion </p>
<h2>Synopsis</h2>
<pre>DROP CONVERSION [ IF EXISTS ] <i>name</i> [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP CONVERSION</code> removes a previously defined conversion. To be able to drop a conversion, you must own the conversion.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the conversion does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name of the conversion. The conversion name can be schema-qualified.</p>
<dt><code>CASCADE</code></p>
<dd>
<dt><code>RESTRICT</code></p>
<dd>These key words do not have any effect, since there are no dependencies on conversions.</dl>
<h2>Examples</h2>
<p>To drop the conversion named myname: </p>
<pre>DROP CONVERSION myname;</pre>
<h2>Compatibility</h2>
<p>There is no <code>DROP CONVERSION</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>ALTER CONVERSION [<code><a href="/docs/linux/man/7-alter_conversion/">alter_conversion</a></code>(7)], CREATE CONVERSION [<code><a href="/docs/linux/man/7-create_conversion/">create_conversion</a></code>(7)] </p>
