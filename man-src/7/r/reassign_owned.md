---
title: "reassign_owned(7)"
name: "reassign_owned"
section: "7"
letter: "r"
url: "/docs/linux/man/7-reassign_owned/"
description: "REASSIGN OWNED – change the ownership of database objects owned by a database role"
---

<p>REASSIGN OWNED &#8211; change the ownership of database objects owned by a database role </p>
<h2>Synopsis</h2>
<pre>REASSIGN OWNED BY <i>old_role</i> [, ...] TO <i>new_role</i></pre>
<h2>Description</h2>
<p><code>REASSIGN OWNED</code> instructs the system to change the ownership of the database objects owned by one of the old_roles, to new_role.</p>
<h2>Parameters</h2>
<dl>
<dt><i>old_role</i></p>
<dd>The name of a role. The ownership of all the objects in the current database owned by this role will be reassigned to <i>new_role</i>.</p>
<dt><i>new_role</i></p>
<dd>The name of the role that will be made the new owner of the affected objects.</dl>
<h2>Notes</h2>
<p><code>REASSIGN OWNED</code> is often used to prepare for the removal of one or more roles. Because <code>REASSIGN OWNED</code> only affects the objects in the current database, it is usually necessary to execute this command in each database that contains objects owned by a role that is to be removed. </p>
<p> The DROP OWNED [<code><a href="/docs/linux/man/7-drop_owned/">drop_owned</a></code>(7)] command is an alternative that drops all the database objects owned by one or more roles. </p>
<p> The <code>REASSIGN OWNED</code> command does not affect the privileges granted to the old_roles in objects that are not owned by them. Use <code>DROP OWNED</code> to revoke those privileges.</p>
<h2>Compatibility</h2>
<p>The <code>REASSIGN OWNED</code> statement is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>DROP OWNED [<code><a href="/docs/linux/man/7-drop_owned/">drop_owned</a></code>(7)], DROP ROLE [<code><a href="/docs/linux/man/7-drop_role/">drop_role</a></code>(7)] </p>
