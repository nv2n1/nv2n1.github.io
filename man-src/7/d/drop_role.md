---
title: "drop_role(7)"
name: "drop_role"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_role/"
description: "DROP ROLE – remove a database role"
---

<p>DROP ROLE &#8211; remove a database role </p>
<h2>Synopsis</h2>
<pre>DROP ROLE [ IF EXISTS ] <i>name</i> [, ...]</pre>
<h2>Description</h2>
<p><code>DROP ROLE</code> removes the specified role(s). To drop a superuser role, you must be a superuser yourself; to drop non-superuser roles, you must have CREATEROLE privilege. </p>
<p> A role cannot be removed if it is still referenced in any database of the cluster; an error will be raised if so. Before dropping the role, you must drop all the objects it owns (or reassign their ownership) and revoke any privileges the role has been granted. The REASSIGN OWNED [<code><a href="/docs/linux/man/7-reassign_owned/">reassign_owned</a></code>(7)] and DROP OWNED [<code><a href="/docs/linux/man/7-drop_owned/">drop_owned</a></code>(7)] commands can be useful for this purpose. </p>
<p> However, it is not necessary to remove role memberships involving the role; <code>DROP ROLE</code> automatically revokes any memberships of the target role in other roles, and of other roles in the target role. The other roles are not dropped nor otherwise affected.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the role does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name of the role to remove.</dl>
<h2>Notes</h2>
<p>PostgreSQL includes a program dropuser [<code><a href="/docs/linux/man/1-dropuser/">dropuser</a></code>(1)] that has the same functionality as this command (in fact, it calls this command) but can be run from the command shell.</p>
<h2>Examples</h2>
<p>To drop a role: </p>
<pre>DROP ROLE jonathan;</pre>
<h2>Compatibility</h2>
<p>The SQL standard defines <code>DROP ROLE</code>, but it allows only one role to be dropped at a time, and it specifies different privilege requirements than PostgreSQL uses.</p>
<h2>See Also</h2>
<p>CREATE ROLE [<code><a href="/docs/linux/man/7-create_role/">create_role</a></code>(7)], ALTER ROLE [<code><a href="/docs/linux/man/7-alter_role/">alter_role</a></code>(7)], SET ROLE [<code><a href="/docs/linux/man/7-set_role/">set_role</a></code>(7)] </p>
