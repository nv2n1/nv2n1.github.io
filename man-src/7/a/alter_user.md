---
title: "alter_user(7)"
name: "alter_user"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_user/"
description: "ALTER USER – change a database role"
---

<p>ALTER USER &#8211; change a database role </p>
<h2>Synopsis</h2>
<pre>ALTER USER <i>name</i> [ [ WITH ] <i>option</i> [ ... ] ]
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
ALTER USER <i>name</i> RENAME TO <i>newname</i>
ALTER USER <i>name</i> SET <i>configuration_parameter</i> { TO | = } { <i>value</i> | DEFAULT }
ALTER USER <i>name</i> SET <i>configuration_parameter</i> FROM CURRENT
ALTER USER <i>name</i> RESET <i>configuration_parameter</i>
ALTER USER <i>name</i> RESET ALL</pre>
<h2>Description</h2>
<p><code>ALTER USER</code> is now an alias for ALTER ROLE [<code><a href="/docs/linux/man/7-alter_role/">alter_role</a></code>(7)].</p>
<h2>Compatibility</h2>
<p>The <code>ALTER USER</code> statement is a PostgreSQL extension. The SQL standard leaves the definition of users to the implementation.</p>
<h2>See Also</h2>
<p>ALTER ROLE [<code><a href="/docs/linux/man/7-alter_role/">alter_role</a></code>(7)] </p>
