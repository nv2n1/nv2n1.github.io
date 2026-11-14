---
title: "create_group(7)"
name: "create_group"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_group/"
description: "CREATE GROUP – define a new database role"
---

<p>CREATE GROUP &#8211; define a new database role </p>
<h2>Synopsis</h2>
<pre>CREATE GROUP <i>name</i> [ [ WITH ] <i>option</i> [ ... ] ]
where <i>option</i> can be:
 
 SUPERUSER | NOSUPERUSER
 | CREATEDB | NOCREATEDB
 | CREATEROLE | NOCREATEROLE
 | CREATEUSER | NOCREATEUSER
 | INHERIT | NOINHERIT
 | LOGIN | NOLOGIN
 | [ ENCRYPTED | UNENCRYPTED ] PASSWORD '<i>password</i>'
 | VALID UNTIL '<i>timestamp</i>' 
 | IN ROLE <i>rolename</i> [, ...]
 | IN GROUP <i>rolename</i> [, ...]
 | ROLE <i>rolename</i> [, ...]
 | ADMIN <i>rolename</i> [, ...]
 | USER <i>rolename</i> [, ...]
 | SYSID <i>uid</i> </pre>
<h2>Description</h2>
<p><code>CREATE GROUP</code> is now an alias for CREATE ROLE [<code><a href="/docs/linux/man/7-create_role/">create_role</a></code>(7)].</p>
<h2>Compatibility</h2>
<p>There is no <code>CREATE GROUP</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE ROLE [<code><a href="/docs/linux/man/7-create_role/">create_role</a></code>(7)] </p>
