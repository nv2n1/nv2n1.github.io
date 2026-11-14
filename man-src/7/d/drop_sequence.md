---
title: "drop_sequence(7)"
name: "drop_sequence"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_sequence/"
description: "DROP SEQUENCE – remove a sequence"
---

<p>DROP SEQUENCE &#8211; remove a sequence </p>
<h2>Synopsis</h2>
<pre>DROP SEQUENCE [ IF EXISTS ] <i>name</i> [, ...] [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP SEQUENCE</code> removes sequence number generators. A sequence can only be dropped by its owner or a superuser.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the sequence does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of a sequence.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the sequence.</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the sequence if any objects depend on it. This is the default.</dl>
<h2>Examples</h2>
<p>To remove the sequence serial: </p>
<pre>DROP SEQUENCE serial;</pre>
<h2>Compatibility</h2>
<p><code>DROP SEQUENCE</code> conforms to the SQL standard, except that the standard only allows one sequence to be dropped per command, and apart from the IF EXISTS option, which is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>CREATE SEQUENCE [<code><a href="/docs/linux/man/7-create_sequence/">create_sequence</a></code>(7)], ALTER SEQUENCE [<code><a href="/docs/linux/man/7-alter_sequence/">alter_sequence</a></code>(7)] </p>
