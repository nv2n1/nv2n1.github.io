---
title: "set_role(7)"
name: "set_role"
section: "7"
letter: "s"
url: "/docs/linux/man/7-set_role/"
description: "SET ROLE – set the current user identifier of the current session"
---

<p>SET ROLE &#8211; set the current user identifier of the current session </p>
<h2>Synopsis</h2>
<pre>SET [ SESSION | LOCAL ] ROLE <i>rolename</i>
SET [ SESSION | LOCAL ] ROLE NONE
RESET ROLE</pre>
<h2>Description</h2>
<p>This command sets the current user identifier of the current SQL session to be <i>rolename</i>. The role name can be written as either an identifier or a string literal. After <code>SET ROLE</code>, permissions checking for SQL commands is carried out as though the named role were the one that had logged in originally. </p>
<p> The specified <i>rolename</i> must be a role that the current session user is a member of. (If the session user is a superuser, any role can be selected.) </p>
<p> The SESSION and LOCAL modifiers act the same as for the regular SET [<code><a href="/docs/linux/man/7-set/">set</a></code>(7)] command. </p>
<p> The NONE and RESET forms reset the current user identifier to be the current session user identifier. These forms can be executed by any user.</p>
<h2>Notes</h2>
<p>Using this command, it is possible to either add privileges or restrict one&#8217;s privileges. If the session user role has the INHERITS attribute, then it automatically has all the privileges of every role that it could <code>SET ROLE</code> to; in this case <code>SET ROLE</code> effectively drops all the privileges assigned directly to the session user and to the other roles it is a member of, leaving only the privileges available to the named role. On the other hand, if the session user role has the NOINHERITS attribute, <code>SET ROLE</code> drops the privileges assigned directly to the session user and instead acquires the privileges available to the named role. </p>
<p> In particular, when a superuser chooses to <code>SET ROLE</code> to a non-superuser role, she loses her superuser privileges. </p>
<p> <code>SET ROLE</code> has effects comparable to SET SESSION AUTHORIZATION [<code><a href="/docs/linux/man/7-set_session_authorization/">set_session_authorization</a></code>(7)], but the privilege checks involved are quite different. Also, <code>SET SESSION AUTHORIZATION</code> determines which roles are allowable for later <code>SET ROLE</code> commands, whereas changing roles with <code>SET ROLE</code> does not change the set of roles allowed to a later <code>SET ROLE</code>. </p>
<p> <code>SET ROLE</code> does not process session variables as specified by the role&#8217;s ALTER ROLE [<code><a href="/docs/linux/man/7-alter_role/">alter_role</a></code>(7)] settings; this only happens during login. </p>
<p> <code>SET ROLE</code> cannot be used within a SECURITY DEFINER function.</p>
<h2>Examples</h2>
<pre>SELECT SESSION_USER, CURRENT_USER;
 session_user | current_user 
--------------+--------------
 peter | peter
SET ROLE 'paul';
SELECT SESSION_USER, CURRENT_USER;
 session_user | current_user 
--------------+--------------
 peter | paul</pre>
<h2>Compatibility</h2>
<p>PostgreSQL allows identifier syntax (&quot;rolename&quot;), while the SQL standard requires the role name to be written as a string literal. SQL does not allow this command during a transaction; PostgreSQL does not make this restriction because there is no reason to. The SESSION and LOCAL modifiers are a PostgreSQL extension, as is the RESET syntax.</p>
<h2>See Also</h2>
<p>SET SESSION AUTHORIZATION [<code><a href="/docs/linux/man/7-set_session_authorization/">set_session_authorization</a></code>(7)] </p>
