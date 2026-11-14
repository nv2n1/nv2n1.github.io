---
title: "create_role(7)"
name: "create_role"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_role/"
description: "CREATE ROLE – define a new database role"
---

<p>CREATE ROLE &#8211; define a new database role </p>
<h2>Synopsis</h2>
<pre>CREATE ROLE <i>name</i> [ [ WITH ] <i>option</i> [ ... ] ]
where <i>option</i> can be:
 
 SUPERUSER | NOSUPERUSER
 | CREATEDB | NOCREATEDB
 | CREATEROLE | NOCREATEROLE
 | CREATEUSER | NOCREATEUSER
 | INHERIT | NOINHERIT
 | LOGIN | NOLOGIN
 | CONNECTION LIMIT <i>connlimit</i>
 | [ ENCRYPTED | UNENCRYPTED ] PASSWORD '<i>password</i>'
 | VALID UNTIL '<i>timestamp</i>' 
 | IN ROLE <i>rolename</i> [, ...]
 | IN GROUP <i>rolename</i> [, ...]
 | ROLE <i>rolename</i> [, ...]
 | ADMIN <i>rolename</i> [, ...]
 | USER <i>rolename</i> [, ...]
 | SYSID <i>uid</i> </pre>
<h2>Description</h2>
<p><code>CREATE ROLE</code> adds a new role to a PostgreSQL database cluster. A role is an entity that can own database objects and have database privileges; a role can be considered a &#8220;user&#8221;, a &#8220;group&#8221;, or both depending on how it is used. Refer to in the documentation and in the documentation for information about managing users and authentication. You must have CREATEROLE privilege or be a database superuser to use this command. </p>
<p> Note that roles are defined at the database cluster level, and so are valid in all databases in the cluster.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of the new role.</p>
<dt><code>SUPERUSER</code></p>
<dd>
<dt><code>NOSUPERUSER</code></p>
<dd>These clauses determine whether the new role is a &#8220;superuser&#8221;, who can override all access restrictions within the database. Superuser status is dangerous and should be used only when really needed. You must yourself be a superuser to create a new superuser. If not specified, NOSUPERUSER is the default.</p>
<dt><code>CREATEDB</code></p>
<dd>
<dt><code>NOCREATEDB</code></p>
<dd>These clauses define a role&#8217;s ability to create databases. If CREATEDB is specified, the role being defined will be allowed to create new databases. Specifying NOCREATEDB will deny a role the ability to create databases. If not specified, NOCREATEDB is the default.</p>
<dt><code>CREATEROLE</code></p>
<dd>
<dt><code>NOCREATEROLE</code></p>
<dd>These clauses determine whether a role will be permitted to create new roles (that is, execute <code>CREATE ROLE</code>). A role with CREATEROLE privilege can also alter and drop other roles. If not specified, NOCREATEROLE is the default.</p>
<dt><code>CREATEUSER</code></p>
<dd>
<dt><code>NOCREATEUSER</code></p>
<dd>These clauses are an obsolete, but still accepted, spelling of SUPERUSER and NOSUPERUSER. Note that they are <code>not</code> equivalent to CREATEROLE as one might naively expect!</p>
<dt><code>INHERIT</code></p>
<dd>
<dt><code>NOINHERIT</code></p>
<dd>These clauses determine whether a role &#8220;inherits&#8221; the privileges of roles it is a member of. A role with the INHERIT attribute can automatically use whatever database privileges have been granted to all roles it is directly or indirectly a member of. Without INHERIT, membership in another role only grants the ability to <code>SET ROLE</code> to that other role; the privileges of the other role are only available after having done so. If not specified, INHERIT is the default.</p>
<dt><code>LOGIN</code></p>
<dd>
<dt><code>NOLOGIN</code></p>
<dd>These clauses determine whether a role is allowed to log in; that is, whether the role can be given as the initial session authorization name during client connection. A role having the LOGIN attribute can be thought of as a user. Roles without this attribute are useful for managing database privileges, but are not users in the usual sense of the word. If not specified, NOLOGIN is the default, except when <code>CREATE ROLE</code> is invoked through its alternative spelling <code>CREATE USER</code>.</p>
<dt><code>CONNECTION LIMIT </code><i>connlimit</i></p>
<dd>If role can log in, this specifies how many concurrent connections the role can make. -1 (the default) means no limit.</p>
<dt><code>PASSWORD </code><i>password</i></p>
<dd>Sets the role&#8217;s password. (A password is only of use for roles having the LOGIN attribute, but you can nonetheless define one for roles without it.) If you do not plan to use password authentication you can omit this option. If no password is specified, the password will be set to null and password authentication will always fail for that user. A null password can optionally be written explicitly as PASSWORD NULL.</p>
<dt><code>ENCRYPTED</code></p>
<dd>
<dt><code>UNENCRYPTED</code></p>
<dd>These key words control whether the password is stored encrypted in the system catalogs. (If neither is specified, the default behavior is determined by the configuration parameter password_encryption.) If the presented password string is already in MD5-encrypted format, then it is stored encrypted as-is, regardless of whether ENCRYPTED or UNENCRYPTED is specified (since the system cannot decrypt the specified encrypted password string). This allows reloading of encrypted passwords during dump/restore. </p>
<p> Note that older clients might lack support for the MD5 authentication mechanism that is needed to work with passwords that are stored encrypted.</p>
<dt><code>VALID UNTIL &#8216;</code><i>timestamp</i><code>&#8216;</code></p>
<dd>The VALID UNTIL clause sets a date and time after which the role&#8217;s password is no longer valid. If this clause is omitted the password will be valid for all time.</p>
<dt><code>IN ROLE </code><i>rolename</i></p>
<dd>The IN ROLE clause lists one or more existing roles to which the new role will be immediately added as a new member. (Note that there is no option to add the new role as an administrator; use a separate <code>GRANT</code> command to do that.)</p>
<dt><code>IN GROUP </code><i>rolename</i></p>
<dd>IN GROUP is an obsolete spelling of IN ROLE.</p>
<dt><code>ROLE </code><i>rolename</i></p>
<dd>The ROLE clause lists one or more existing roles which are automatically added as members of the new role. (This in effect makes the new role a &#8220;group&#8221;.)</p>
<dt><code>ADMIN </code><i>rolename</i></p>
<dd>The ADMIN clause is like ROLE, but the named roles are added to the new role WITH ADMIN OPTION, giving them the right to grant membership in this role to others.</p>
<dt><code>USER </code><i>rolename</i></p>
<dd>The USER clause is an obsolete spelling of the ROLE clause.</p>
<dt><code>SYSID </code><i>uid</i></p>
<dd>The SYSID clause is ignored, but is accepted for backwards compatibility.</dl>
<h2>Notes</h2>
<p>Use ALTER ROLE [<code><a href="/docs/linux/man/7-alter_role/">alter_role</a></code>(7)] to change the attributes of a role, and DROP ROLE [<code><a href="/docs/linux/man/7-drop_role/">drop_role</a></code>(7)] to remove a role. All the attributes specified by <code>CREATE ROLE</code> can be modified by later <code>ALTER ROLE</code> commands. </p>
<p> The preferred way to add and remove members of roles that are being used as groups is to use GRANT [<code><a href="/docs/linux/man/7-grant/">grant</a></code>(7)] and REVOKE [<code><a href="/docs/linux/man/7-revoke/">revoke</a></code>(7)]. </p>
<p> The VALID UNTIL clause defines an expiration time for a password only, not for the role <i>per se</i>. In particular, the expiration time is not enforced when logging in using a non-password-based authentication method. </p>
<p> The INHERIT attribute governs inheritance of grantable privileges (that is, access privileges for database objects and role memberships). It does not apply to the special role attributes set by <code>CREATE ROLE</code> and <code>ALTER ROLE</code>. For example, being a member of a role with CREATEDB privilege does not immediately grant the ability to create databases, even if INHERIT is set; it would be necessary to become that role via SET ROLE [<code><a href="/docs/linux/man/7-set_role/">set_role</a></code>(7)] before creating a database. </p>
<p> The INHERIT attribute is the default for reasons of backwards compatibility: in prior releases of PostgreSQL, users always had access to all privileges of groups they were members of. However, NOINHERIT provides a closer match to the semantics specified in the SQL standard. </p>
<p> Be careful with the CREATEROLE privilege. There is no concept of inheritance for the privileges of a CREATEROLE-role. That means that even if a role does not have a certain privilege but is allowed to create other roles, it can easily create another role with different privileges than its own (except for creating roles with superuser privileges). For example, if the role &#8220;user&#8221; has the CREATEROLE privilege but not the CREATEDB privilege, nonetheless it can create a new role with the CREATEDB privilege. Therefore, regard roles that have the CREATEROLE privilege as almost-superuser-roles. </p>
<p> PostgreSQL includes a program createuser [<code><a href="/docs/linux/man/1-createuser/">createuser</a></code>(1)] that has the same functionality as <code>CREATE ROLE</code> (in fact, it calls this command) but can be run from the command shell. </p>
<p> The CONNECTION LIMIT option is only enforced approximately; if two new sessions start at about the same time when just one connection &#8220;slot&#8221; remains for the role, it is possible that both will fail. Also, the limit is never enforced for superusers. </p>
<p> Caution must be exercised when specifying an unencrypted password with this command. The password will be transmitted to the server in cleartext, and it might also be logged in the client&#8217;s command history or the server log. The command createuser [<code><a href="/docs/linux/man/1-createuser/">createuser</a></code>(1)], however, transmits the password encrypted. Also, psql [<code><a href="/docs/linux/man/1-psql/">psql</a></code>(1)] contains a command <code>\password</code> that can be used to safely change the password later.</p>
<h2>Examples</h2>
<p>Create a role that can log in, but don&#8217;t give it a password: </p>
<pre>CREATE ROLE jonathan LOGIN;</pre>
<p>Create a role with a password: </p>
<pre>CREATE USER davide WITH PASSWORD 'jw8s0F4';</pre>
<p>(<code>CREATE USER</code> is the same as <code>CREATE ROLE</code> except that it implies LOGIN.) </p>
<p> Create a role with a password that is valid until the end of 2004. After one second has ticked in 2005, the password is no longer valid. </p>
<pre>CREATE ROLE miriam WITH LOGIN PASSWORD 'jw8s0F4' VALID UNTIL '2005-01-01';</pre>
<p>Create a role that can create databases and manage roles: </p>
<pre>CREATE ROLE admin WITH CREATEDB CREATEROLE;</pre>
<h2>Compatibility</h2>
<p>The <code>CREATE ROLE</code> statement is in the SQL standard, but the standard only requires the syntax </p>
<pre>CREATE ROLE <i>name</i> [ WITH ADMIN <i>rolename</i> ]</pre>
<p>Multiple initial administrators, and all the other options of <code>CREATE ROLE</code>, are PostgreSQL extensions. </p>
<p> The SQL standard defines the concepts of users and roles, but it regards them as distinct concepts and leaves all commands defining users to be specified by each database implementation. In PostgreSQL we have chosen to unify users and roles into a single kind of entity. Roles therefore have many more optional attributes than they do in the standard. </p>
<p> The behavior specified by the SQL standard is most closely approximated by giving users the NOINHERIT attribute, while roles are given the INHERIT attribute.</p>
<h2>See Also</h2>
<p>SET ROLE [<code><a href="/docs/linux/man/7-set_role/">set_role</a></code>(7)], ALTER ROLE [<code><a href="/docs/linux/man/7-alter_role/">alter_role</a></code>(7)], DROP ROLE [<code><a href="/docs/linux/man/7-drop_role/">drop_role</a></code>(7)], GRANT [<code><a href="/docs/linux/man/7-grant/">grant</a></code>(7)], REVOKE [<code><a href="/docs/linux/man/7-revoke/">revoke</a></code>(7)], <code><a href="/docs/linux/man/1-createuser/">createuser</a></code>(1) </p>
