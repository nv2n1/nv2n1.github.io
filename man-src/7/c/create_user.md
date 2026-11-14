---
title: "create_user(7)"
name: "create_user"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_user/"
description: "CREATE USER – define a new database role"
---

<p>CREATE USER &#8211; define a new database role </p>
<h2>Synopsis</h2>
<pre>CREATE USER <i>name</i> [ [ WITH ] <i>option</i> [ ... ] ]
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
<p><code>CREATE USER</code> is now an alias for CREATE ROLE [<code><a href="/docs/linux/man/7-create_role/">create_role</a></code>(7)]. The only difference is that when the command is spelled <code>CREATE USER</code>, LOGIN is assumed by default, whereas NOLOGIN is assumed when the command is spelled <code>CREATE ROLE</code>.</p>
<h2>Compatibility</h2>
<p>The <code>CREATE USER</code> statement is a PostgreSQL extension. The SQL standard leaves the definition of users to the implementation.</p>
<h2>See Also</h2>
<p>CREATE ROLE [<code><a href="/docs/linux/man/7-create_role/">create_role</a></code>(7)] </p>
