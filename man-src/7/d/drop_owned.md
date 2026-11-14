---
title: "drop_owned(7)"
name: "drop_owned"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_owned/"
description: "DROP OWNED – remove database objects owned by a database role"
---

<p>DROP OWNED &#8211; remove database objects owned by a database role </p>
<h2>Synopsis</h2>
<pre>DROP OWNED BY <i>name</i> [, ...] [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP OWNED</code> drops all the objects in the current database that are owned by one of the specified roles. Any privileges granted to the given roles on objects in the current database will also be revoked.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of a role whose objects will be dropped, and whose privileges will be revoked.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the affected objects.</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the objects owned by a role if any other database objects depend on one of the affected objects. This is the default.</dl>
<h2>Notes</h2>
<p><code>DROP OWNED</code> is often used to prepare for the removal of one or more roles. Because <code>DROP OWNED</code> only affects the objects in the current database, it is usually necessary to execute this command in each database that contains objects owned by a role that is to be removed. </p>
<p> Using the CASCADE option might make the command recurse to objects owned by other users. </p>
<p> The REASSIGN OWNED [<code><a href="/docs/linux/man/7-reassign_owned/">reassign_owned</a></code>(7)] command is an alternative that reassigns the ownership of all the database objects owned by one or more roles.</p>
<h2>Compatibility</h2>
<p>The <code>DROP OWNED</code> statement is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>REASSIGN OWNED [<code><a href="/docs/linux/man/7-reassign_owned/">reassign_owned</a></code>(7)], DROP ROLE [<code><a href="/docs/linux/man/7-drop_role/">drop_role</a></code>(7)] </p>
