---
title: "alter_group(7)"
name: "alter_group"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_group/"
description: "ALTER GROUP – change role name or membership"
---

<p>ALTER GROUP &#8211; change role name or membership </p>
<h2>Synopsis</h2>
<pre>ALTER GROUP <i>groupname</i> ADD USER <i>username</i> [, ... ]
ALTER GROUP <i>groupname</i> DROP USER <i>username</i> [, ... ]
ALTER GROUP <i>groupname</i> RENAME TO <i>newname</i></pre>
<h2>Description</h2>
<p><code>ALTER GROUP</code> changes the attributes of a user group. This is an obsolete command, though still accepted for backwards compatibility, because groups (and users too) have been superseded by the more general concept of roles. </p>
<p> The first two variants add users to a group or remove them from a group. (Any role can play the part of either a &#8220;user&#8221; or a &#8220;group&#8221; for this purpose.) These variants are effectively equivalent to granting or revoking membership in the role named as the &#8220;group&#8221;; so the preferred way to do this is to use GRANT [<code><a href="/docs/linux/man/7-grant/">grant</a></code>(7)] or REVOKE [<code><a href="/docs/linux/man/7-revoke/">revoke</a></code>(7)]. </p>
<p> The third variant changes the name of the group. This is exactly equivalent to renaming the role with ALTER ROLE [<code><a href="/docs/linux/man/7-alter_role/">alter_role</a></code>(7)].</p>
<h2>Parameters</h2>
<dl>
<dt><i>groupname</i></p>
<dd>The name of the group (role) to modify.</p>
<dt><i>username</i></p>
<dd>Users (roles) that are to be added to or removed from the group. The users must already exist; <code>ALTER GROUP</code> does not create or drop users.</p>
<dt><i>newname</i></p>
<dd>The new name of the group.</dl>
<h2>Examples</h2>
<p>Add users to a group: </p>
<pre>ALTER GROUP staff ADD USER karl, john;</pre>
<p>Remove a user from a group: </p>
<pre>ALTER GROUP workers DROP USER beth;</pre>
<h2>Compatibility</h2>
<p>There is no <code>ALTER GROUP</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>GRANT [<code><a href="/docs/linux/man/7-grant/">grant</a></code>(7)], REVOKE [<code><a href="/docs/linux/man/7-revoke/">revoke</a></code>(7)], ALTER ROLE [<code><a href="/docs/linux/man/7-alter_role/">alter_role</a></code>(7)] </p>
