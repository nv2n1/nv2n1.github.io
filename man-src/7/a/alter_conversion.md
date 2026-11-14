---
title: "alter_conversion(7)"
name: "alter_conversion"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_conversion/"
description: "ALTER CONVERSION – change the definition of a conversion"
---

<p>ALTER CONVERSION &#8211; change the definition of a conversion </p>
<h2>Synopsis</h2>
<pre>ALTER CONVERSION <i>name</i> RENAME TO <i>newname</i>
ALTER CONVERSION <i>name</i> OWNER TO <i>newowner</i></pre>
<h2>Description</h2>
<p><code>ALTER CONVERSION</code> changes the definition of a conversion. </p>
<p> You must own the conversion to use <code>ALTER CONVERSION</code>. To alter the owner, you must also be a direct or indirect member of the new owning role, and that role must have CREATE privilege on the conversion&#8217;s schema. (These restrictions enforce that altering the owner doesn&#8217;t do anything you couldn&#8217;t do by dropping and recreating the conversion. However, a superuser can alter ownership of any conversion anyway.)</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing conversion.</p>
<dt><i>newname</i></p>
<dd>The new name of the conversion.</p>
<dt><i>newowner</i></p>
<dd>The new owner of the conversion.</dl>
<h2>Examples</h2>
<p>To rename the conversion iso_8859_1_to_utf8 to latin1_to_unicode: </p>
<pre>ALTER CONVERSION iso_8859_1_to_utf8 RENAME TO latin1_to_unicode;</pre>
<p>To change the owner of the conversion iso_8859_1_to_utf8 to joe: </p>
<pre>ALTER CONVERSION iso_8859_1_to_utf8 OWNER TO joe;</pre>
<h2>Compatibility</h2>
<p>There is no <code>ALTER CONVERSION</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE CONVERSION [<code><a href="/docs/linux/man/7-create_conversion/">create_conversion</a></code>(7)], DROP CONVERSION [<code><a href="/docs/linux/man/7-drop_conversion/">drop_conversion</a></code>(7)] </p>
