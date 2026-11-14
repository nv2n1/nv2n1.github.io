---
title: "alter_database(7)"
name: "alter_database"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_database/"
description: "ALTER DATABASE – change a database"
---

<p>ALTER DATABASE &#8211; change a database </p>
<h2>Synopsis</h2>
<pre>ALTER DATABASE <i>name</i> [ [ WITH ] <i>option</i> [ ... ] ]
where <i>option</i> can be:
 CONNECTION LIMIT <i>connlimit</i>
ALTER DATABASE <i>name</i> RENAME TO <i>newname</i>
ALTER DATABASE <i>name</i> OWNER TO <i>new_owner</i>
ALTER DATABASE <i>name</i> SET TABLESPACE <i>new_tablespace</i>
ALTER DATABASE <i>name</i> SET <i>configuration_parameter</i> { TO | = } { <i>value</i> | DEFAULT }
ALTER DATABASE <i>name</i> SET <i>configuration_parameter</i> FROM CURRENT
ALTER DATABASE <i>name</i> RESET <i>configuration_parameter</i>
ALTER DATABASE <i>name</i> RESET ALL</pre>
<h2>Description</h2>
<p><code>ALTER DATABASE</code> changes the attributes of a database. </p>
<p> The first form changes certain per-database settings. (See below for details.) Only the database owner or a superuser can change these settings. </p>
<p> The second form changes the name of the database. Only the database owner or a superuser can rename a database; non-superuser owners must also have the CREATEDB privilege. The current database cannot be renamed. (Connect to a different database if you need to do that.) </p>
<p> The third form changes the owner of the database. To alter the owner, you must own the database and also be a direct or indirect member of the new owning role, and you must have the CREATEDB privilege. (Note that superusers have all these privileges automatically.) </p>
<p> The fourth form changes the default tablespace of the database. Only the database owner or a superuser can do this; you must also have create privilege for the new tablespace. This command physically moves any tables or indexes in the database&#8217;s old default tablespace to the new tablespace. Note that tables and indexes in non-default tablespaces are not affected. </p>
<p> The remaining forms change the session default for a run-time configuration variable for a PostgreSQL database. Whenever a new session is subsequently started in that database, the specified value becomes the session default value. The database-specific default overrides whatever setting is present in <i>postgresql.conf</i> or has been received from the <code>postgres</code> command line. Only the database owner or a superuser can change the session defaults for a database. Certain variables cannot be set this way, or can only be set by a superuser.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of the database whose attributes are to be altered.</p>
<dt><i>connlimit</i></p>
<dd>How many concurrent connections can be made to this database. -1 means no limit.</p>
<dt><i>newname</i></p>
<dd>The new name of the database.</p>
<dt><i>new_owner</i></p>
<dd>The new owner of the database.</p>
<dt><i>new_tablespace</i></p>
<dd>The new default tablespace of the database.</p>
<dt><i>configuration_parameter</i></p>
<dd>
<dt><i>value</i></p>
<dd>Set this database&#8217;s session default for the specified configuration parameter to the given value. If <i>value</i> is DEFAULT or, equivalently, RESET is used, the database-specific setting is removed, so the system-wide default setting will be inherited in new sessions. Use RESET ALL to clear all database-specific settings. SET FROM CURRENT saves the session&#8217;s current value of the parameter as the database-specific value. </p>
<p> See SET [<code><a href="/docs/linux/man/7-set/">set</a></code>(7)] and in the documentation for more information about allowed parameter names and values.</dl>
<h2>Notes</h2>
<p>It is also possible to tie a session default to a specific role rather than to a database; see ALTER ROLE [<code><a href="/docs/linux/man/7-alter_role/">alter_role</a></code>(7)]. Role-specific settings override database-specific ones if there is a conflict.</p>
<h2>Examples</h2>
<p>To disable index scans by default in the database test: </p>
<pre>ALTER DATABASE test SET enable_indexscan TO off;</pre>
<h2>Compatibility</h2>
<p>The <code>ALTER DATABASE</code> statement is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>CREATE DATABASE [<code><a href="/docs/linux/man/7-create_database/">create_database</a></code>(7)], DROP DATABASE [<code><a href="/docs/linux/man/7-drop_database/">drop_database</a></code>(7)], SET [<code><a href="/docs/linux/man/7-set/">set</a></code>(7)], CREATE TABLESPACE [<code><a href="/docs/linux/man/7-create_tablespace/">create_tablespace</a></code>(7)] </p>
