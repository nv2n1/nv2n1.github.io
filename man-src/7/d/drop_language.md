---
title: "drop_language(7)"
name: "drop_language"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_language/"
description: "DROP LANGUAGE – remove a procedural language"
---

<p>DROP LANGUAGE &#8211; remove a procedural language </p>
<h2>Synopsis</h2>
<pre>DROP [ PROCEDURAL ] LANGUAGE [ IF EXISTS ] <i>name</i> [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP LANGUAGE</code> removes the definition of a previously registered procedural language. You must be a superuser or the owner of the language to use <code>DROP LANGUAGE</code>.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></dt>
<dd>Do not throw an error if the language does not exist. A notice is issued in this case.</dd>
<dt><i>name</i></dt>
<dd>The name of an existing procedural language. For backward compatibility, the name can be enclosed by single quotes.</dd>
<dt><code>CASCADE</code></dt>
<dd>Automatically drop objects that depend on the language (such as functions in the language).</dd>
<dt><code>RESTRICT</code></dt>
<dd>Refuse to drop the language if any objects depend on it. This is the default.</dd></dl>
<h2>Examples</h2>
<p>This command removes the procedural language plsample: </p>
<pre>DROP LANGUAGE plsample;</pre>
<h2>Compatibility</h2>
<p>There is no <code>DROP LANGUAGE</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>ALTER LANGUAGE [<code><a href="/docs/linux/man/7-alter_language/">alter_language</a></code>(7)], CREATE LANGUAGE [<code><a href="/docs/linux/man/7-create_language/">create_language</a></code>(7)], <code><a href="/docs/linux/man/1-droplang/">droplang</a></code>(1) </p>
