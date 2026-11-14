---
title: "drop_domain(7)"
name: "drop_domain"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_domain/"
description: "DROP DOMAIN – remove a domain"
---

<p>DROP DOMAIN &#8211; remove a domain </p>
<h2>Synopsis</h2>
<pre>DROP DOMAIN [ IF EXISTS ] <i>name</i> [, ...] [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP DOMAIN</code> removes a domain. Only the owner of a domain can remove it.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the domain does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing domain.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the domain (such as table columns).</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the domain if any objects depend on it. This is the default.</dl>
<h2>Examples</h2>
<p>To remove the domain <code>box</code>: </p>
<pre>DROP DOMAIN box;</pre>
<h2>Compatibility</h2>
<p>This command conforms to the SQL standard, except for the IF EXISTS option, which is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>CREATE DOMAIN [<code><a href="/docs/linux/man/7-create_domain/">create_domain</a></code>(7)], ALTER DOMAIN [<code><a href="/docs/linux/man/7-alter_domain/">alter_domain</a></code>(7)] </p>
