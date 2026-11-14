---
title: "drop_database(7)"
name: "drop_database"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_database/"
description: "DROP DATABASE – remove a database"
---

<p>DROP DATABASE &#8211; remove a database </p>
<h2>Synopsis</h2>
<pre>DROP DATABASE [ IF EXISTS ] <i>name</i></pre>
<h2>Description</h2>
<p><code>DROP DATABASE</code> drops a database. It removes the catalog entries for the database and deletes the directory containing the data. It can only be executed by the database owner. Also, it cannot be executed while you or anyone else are connected to the target database. (Connect to postgres or any other database to issue this command.) </p>
<p> <code>DROP DATABASE</code> cannot be undone. Use it with care!</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the database does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name of the database to remove.</dl>
<h2>Notes</h2>
<p><code>DROP DATABASE</code> cannot be executed inside a transaction block. </p>
<p> This command cannot be executed while connected to the target database. Thus, it might be more convenient to use the program dropdb [<code><a href="/docs/linux/man/1-dropdb/">dropdb</a></code>(1)] instead, which is a wrapper around this command.</p>
<h2>Compatibility</h2>
<p>There is no <code>DROP DATABASE</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE DATABASE [<code><a href="/docs/linux/man/7-create_database/">create_database</a></code>(7)] </p>
