---
title: "alter_role(7)"
name: "alter_role"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_role/"
---

ALTER ROLE - change a database role 

<h2>Synopsis</h2>

<pre>ALTER ROLE <i>name</i> [ [ WITH ] <i>option</i> [ ... ] ]
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
ALTER ROLE <i>name</i> RENAME TO <i>newname</i>
ALTER ROLE <i>name</i> SET <i>configuration_parameter</i> { TO | = } { <i>value</i> | DEFAULT }
ALTER ROLE <i>name</i> SET <i>configuration_parameter</i> FROM CURRENT
ALTER ROLE <i>name</i> RESET <i>configuration_parameter</i>
ALTER ROLE <i>name</i> RESET ALL</pre>

<h2>Description</h2>

<b>ALTER ROLE</b> changes the attributes of a PostgreSQL role. 

 The first variant of this command listed in the synopsis can change many of the role attributes that can be specified in CREATE ROLE [<b><a HREF="/docs/linux/man/7-create_role/">create_role</a></b>(7)]. (All the possible attributes are covered, except that there are no options for adding or removing memberships; use GRANT [<b><a HREF="/docs/linux/man/7-grant/">grant</a></b>(7)] and REVOKE [<b><a HREF="/docs/linux/man/7-revoke/">revoke</a></b>(7)] for that.) Attributes not mentioned in the command retain their previous settings. Database superusers can change any of these settings for any role. Roles having CREATEROLE privilege can change any of these settings, but only for non-superuser roles. Ordinary roles can only change their own password. 

 The second variant changes the name of the role. Database superusers can rename any role. Roles having CREATEROLE privilege can rename non-superuser roles. The current session user cannot be renamed. (Connect as a different user if you need to do that.) Because MD5-encrypted passwords use the role name as cryptographic salt, renaming a role clears its password if the password is MD5-encrypted. 

 The remaining variants change a role's session default for a specified configuration variable. Whenever the role subsequently starts a new session, the specified value becomes the session default, overriding whatever setting is present in <i>postgresql.conf</i> or has been received from the postgres command line. This only happens at login time, so configuration settings associated with a role to which you've SET ROLE [<b><a HREF="/docs/linux/man/7-set_role/">set_role</a></b>(7)] will be ignored. Superusers can change anyone's session defaults. Roles having CREATEROLE privilege can change defaults for non-superuser roles. Certain variables cannot be set this way, or can only be set if a superuser issues the command.

<h2>Parameters</h2>

<dl><dt><i>name</i>
<dd>The name of the role whose attributes are to be altered.
<dt><b>SUPERUSER</b>
<dd><dt><b>NOSUPERUSER</b>
<dd><dt><b>CREATEDB</b>
<dd><dt><b>NOCREATEDB</b>
<dd><dt><b>CREATEROLE</b>
<dd><dt><b>NOCREATEROLE</b>
<dd><dt><b>CREATEUSER</b>
<dd><dt><b>NOCREATEUSER</b>
<dd><dt><b>INHERIT</b>
<dd><dt><b>NOINHERIT</b>
<dd><dt><b>LOGIN</b>
<dd><dt><b>NOLOGIN</b>
<dd><dt><b>CONNECTION LIMIT </b><i>connlimit</i>
<dd><dt><b>PASSWORD </b><i>password</i>
<dd><dt><b>ENCRYPTED</b>
<dd><dt><b>UNENCRYPTED</b>
<dd><dt><b>VALID UNTIL '</b><i>timestamp</i><b>'</b>
<dd>These clauses alter attributes originally set by CREATE ROLE [<b><a HREF="/docs/linux/man/7-create_role/">create_role</a></b>(7)]. For more information, see the <b>CREATE ROLE</b> reference page.
<dt><i>newname</i>
<dd>The new name of the role.
<dt><i>configuration_parameter</i>
<dd><dt><i>value</i>
<dd>Set this role's session default for the specified configuration parameter to the given value. If <i>value</i> is DEFAULT or, equivalently, RESET is used, the role-specific variable setting is removed, so the role will inherit the system-wide default setting in new sessions. Use RESET ALL to clear all role-specific settings. SET FROM CURRENT saves the session's current value of the parameter as the role-specific value. 

 Role-specific variable setting take effect only at login; SET ROLE [<b><a HREF="/docs/linux/man/7-set_role/">set_role</a></b>(7)] does not process role-specific variable settings. 

 See SET [<b><a HREF="/docs/linux/man/7-set/">set</a></b>(7)] and in the documentation for more information about allowed parameter names and values.</dl>

<h2>Notes</h2>

Use CREATE ROLE [<b><a HREF="/docs/linux/man/7-create_role/">create_role</a></b>(7)] to add new roles, and DROP ROLE [<b><a HREF="/docs/linux/man/7-drop_role/">drop_role</a></b>(7)] to remove a role. 

 <b>ALTER ROLE</b> cannot change a role's memberships. Use GRANT [<b><a HREF="/docs/linux/man/7-grant/">grant</a></b>(7)] and REVOKE [<b><a HREF="/docs/linux/man/7-revoke/">revoke</a></b>(7)] to do that. 

 Caution must be exercised when specifying an unencrypted password with this command. The password will be transmitted to the server in cleartext, and it might also be logged in the client's command history or the server log. psql [<b><a HREF="/docs/linux/man/1-psql/">psql</a></b>(1)] contains a command <b>\password</b> that can be used to safely change a role's password. 

 It is also possible to tie a session default to a specific database rather than to a role; see ALTER DATABASE [<b><a HREF="/docs/linux/man/7-alter_database/">alter_database</a></b>(7)]. Role-specific settings override database-specific ones if there is a conflict.

<h2>Examples</h2>

Change a role's password: <pre>ALTER ROLE davide WITH PASSWORD 'hu8jmn3';</pre>Remove a role's password: <pre>ALTER ROLE davide WITH PASSWORD NULL;</pre>Change a password expiration date, specifying that the password should expire at midday on 4th May 2015 using the time zone which is one hour ahead of UTC: <pre>ALTER ROLE chris VALID UNTIL 'May 4 12:00:00 2015 +1';</pre>Make a password valid forever: <pre>ALTER ROLE fred VALID UNTIL 'infinity';</pre>Give a role the ability to create other roles and new databases: <pre>ALTER ROLE miriam CREATEROLE CREATEDB;</pre>Give a role a non-default setting of the maintenance_work_mem parameter: <pre><code>ALTER ROLE worker_bee SET maintenance_work_mem = 100000;</code></pre>

<h2>Compatibility</h2>

The <b>ALTER ROLE</b> statement is a PostgreSQL extension.

<h2>See Also</h2>

CREATE ROLE [<b><a HREF="/docs/linux/man/7-create_role/">create_role</a></b>(7)], DROP ROLE [<b><a HREF="/docs/linux/man/7-drop_role/">drop_role</a></b>(7)], SET [<b><a HREF="/docs/linux/man/7-set/">set</a></b>(7)] 
