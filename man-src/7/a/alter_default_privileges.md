---
title: "alter_default_privileges(7)"
name: "alter_default_privileges"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_default_privileges/"
description: "ALTER_DEFAULT_PRIVILEGES – define default access privileges"
---

<p>ALTER_DEFAULT_PRIVILEGES &#8211; define default access privileges</p>
<h2>Synopsis</h2>
<pre>ALTER DEFAULT PRIVILEGES
 [ FOR { ROLE | USER } <i>target_role</i> [, ...] ]
 [ IN SCHEMA <i>schema_name</i> [, ...] ]
 <i>abbreviated_grant_or_revoke</i>
where <i>abbreviated_grant_or_revoke</i> is one of:
GRANT { { SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER }
 [, ...] | ALL [ PRIVILEGES ] }
 ON TABLES
 TO { [ GROUP ] <i>role_name</i> | PUBLIC } [, ...] [ WITH GRANT OPTION ]
GRANT { { USAGE | SELECT | UPDATE }
 [, ...] | ALL [ PRIVILEGES ] }
 ON SEQUENCES
 TO { [ GROUP ] <i>role_name</i> | PUBLIC } [, ...] [ WITH GRANT OPTION ]
GRANT { EXECUTE | ALL [ PRIVILEGES ] }
 ON FUNCTIONS
 TO { [ GROUP ] <i>role_name</i> | PUBLIC } [, ...] [ WITH GRANT OPTION ]
GRANT { USAGE | ALL [ PRIVILEGES ] }
 ON TYPES
 TO { [ GROUP ] <i>role_name</i> | PUBLIC } [, ...] [ WITH GRANT OPTION ]
REVOKE [ GRANT OPTION FOR ]
 { { SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER }
 [, ...] | ALL [ PRIVILEGES ] }
 ON TABLES
 FROM { [ GROUP ] <i>role_name</i> | PUBLIC } [, ...]
 [ CASCADE | RESTRICT ]
REVOKE [ GRANT OPTION FOR ]
 { { USAGE | SELECT | UPDATE }
 [, ...] | ALL [ PRIVILEGES ] }
 ON SEQUENCES
 FROM { [ GROUP ] <i>role_name</i> | PUBLIC } [, ...]
 [ CASCADE | RESTRICT ]
REVOKE [ GRANT OPTION FOR ]
 { EXECUTE | ALL [ PRIVILEGES ] }
 ON FUNCTIONS
 FROM { [ GROUP ] <i>role_name</i> | PUBLIC } [, ...]
 [ CASCADE | RESTRICT ]
REVOKE [ GRANT OPTION FOR ]
 { USAGE | ALL [ PRIVILEGES ] }
 ON TYPES
 FROM { [ GROUP ] <i>role_name</i> | PUBLIC } [, ...]
 [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>ALTER DEFAULT PRIVILEGES</code> allows you to set the privileges that will be applied to objects created in the future. (It does not affect privileges assigned to already-existing objects.) Currently, only the privileges for tables (including views and foreign tables), sequences, functions, and types (including domains) can be altered. </p>
<p> You can change default privileges only for objects that will be created by yourself or by roles that you are a member of. The privileges can be set globally (i.e., for all objects created in the current database), or just for objects created in specified schemas. Default privileges that are specified per-schema are added to whatever the global default privileges are for the particular object type. </p>
<p> As explained under <code><a href="/docs/linux/man/7-grant/">GRANT</a></code>(7), the default privileges for any object type normally grant all grantable permissions to the object owner, and may grant some privileges to PUBLIC as well. However, this behavior can be changed by altering the global default privileges with <code>ALTER DEFAULT PRIVILEGES</code>.</p>
<h3>Parameters</h3>
<p><i>target_role</i></p>
<dl>
<dd>The name of an existing role of which the current role is a member. If FOR ROLE is omitted, the current role is assumed.</dl>
<p> <i>schema_name</i></p>
<dl>
<dd>The name of an existing schema. If specified, the default privileges are altered for objects later created in that schema. If IN SCHEMA is omitted, the global default privileges are altered.</dl>
<p> <i>role_name</i></p>
<dl>
<dd>The name of an existing role to grant or revoke privileges for. This parameter, and all the other parameters in <i>abbreviated_grant_or_revoke</i>, act as described under <code><a href="/docs/linux/man/7-grant/">GRANT</a></code>(7) or <code><a href="/docs/linux/man/7-revoke/">REVOKE</a></code>(7), except that one is setting permissions for a whole class of objects rather than specific named objects.</dl>
<h2>Notes</h2>
<p>Use <code><a href="/docs/linux/man/1-psql/">psql</a></code>(1)&#8217;s <code>\ddp</code> command to obtain information about existing assignments of default privileges. The meaning of the privilege values is the same as explained for <code>\dp</code> under <code><a href="/docs/linux/man/7-grant/">GRANT</a></code>(7). </p>
<p> If you wish to drop a role for which the default privileges have been altered, it is necessary to reverse the changes in its default privileges or use <code>DROP OWNED BY</code> to get rid of the default privileges entry for the role.</p>
<h2>Examples</h2>
<p>Grant SELECT privilege to everyone for all tables (and views) you subsequently create in schema myschema, and allow role webuser to INSERT into them too: </p>
<dl>
<dd>
<pre>ALTER DEFAULT PRIVILEGES IN SCHEMA myschema GRANT SELECT ON TABLES TO PUBLIC;
ALTER DEFAULT PRIVILEGES IN SCHEMA myschema GRANT INSERT ON TABLES TO webuser;</pre>
</dl>
<p> Undo the above, so that subsequently-created tables won&#8217;t have any more permissions than normal: </p>
<dl>
<dd>
<pre>ALTER DEFAULT PRIVILEGES IN SCHEMA myschema REVOKE SELECT ON TABLES FROM PUBLIC;
ALTER DEFAULT PRIVILEGES IN SCHEMA myschema REVOKE INSERT ON TABLES FROM webuser;</pre>
</dl>
<p> Remove the public EXECUTE permission that is normally granted on functions, for all functions subsequently created by role admin: </p>
<dl>
<dd>
<pre>ALTER DEFAULT PRIVILEGES FOR ROLE admin REVOKE EXECUTE ON FUNCTIONS FROM PUBLIC;</pre>
</dl>
<h2>Compatibility</h2>
<p>There is no <code>ALTER DEFAULT PRIVILEGES</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-grant/">GRANT</a></code>(7), <code><a href="/docs/linux/man/7-revoke/">REVOKE</a></code>(7) </p>
