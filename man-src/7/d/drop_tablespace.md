---
title: "drop_tablespace(7)"
name: "drop_tablespace"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_tablespace/"
description: "DROP TABLESPACE – remove a tablespace"
---

<p>DROP TABLESPACE &#8211; remove a tablespace </p>
<h2>Synopsis</h2>
<pre>DROP TABLESPACE [ IF EXISTS ] <i>tablespacename</i></pre>
<h2>Description</h2>
<p><code>DROP TABLESPACE</code> removes a tablespace from the system. </p>
<p> A tablespace can only be dropped by its owner or a superuser. The tablespace must be empty of all database objects before it can be dropped. It is possible that objects in other databases might still reside in the tablespace even if no objects in the current database are using the tablespace. Also, if the tablespace is listed in the temp_tablespaces setting of any active session, the <code>DROP</code> might fail due to temporary files residing in the tablespace.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the tablespace does not exist. A notice is issued in this case.</p>
<dt><i>tablespacename</i></p>
<dd>The name of a tablespace.</dl>
<h2>Notes</h2>
<p><code>DROP TABLESPACE</code> cannot be executed inside a transaction block.</p>
<h2>Examples</h2>
<p>To remove tablespace mystuff from the system: </p>
<pre>DROP TABLESPACE mystuff;</pre>
<h2>Compatibility</h2>
<p><code>DROP TABLESPACE</code> is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>CREATE TABLESPACE [<code><a href="/docs/linux/man/7-create_tablespace/">create_tablespace</a></code>(7)], ALTER TABLESPACE [<code><a href="/docs/linux/man/7-alter_tablespace/">alter_tablespace</a></code>(7)] </p>
