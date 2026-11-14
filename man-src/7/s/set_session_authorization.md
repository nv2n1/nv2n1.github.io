---
title: "set_session_authorization(7)"
name: "set_session_authorization"
section: "7"
letter: "s"
url: "/docs/linux/man/7-set_session_authorization/"
description: "SET SESSION AUTHORIZATION – set the session user identifier and the current user identifier of the current session"
---

<p>SET SESSION AUTHORIZATION &#8211; set the session user identifier and the current user identifier of the current session </p>
<h2>Synopsis</h2>
<pre>SET [ SESSION | LOCAL ] SESSION AUTHORIZATION <i>username</i>
SET [ SESSION | LOCAL ] SESSION AUTHORIZATION DEFAULT
RESET SESSION AUTHORIZATION</pre>
<h2>Description</h2>
<p>This command sets the session user identifier and the current user identifier of the current SQL session to be <i>username</i>. The user name can be written as either an identifier or a string literal. Using this command, it is possible, for example, to temporarily become an unprivileged user and later switch back to being a superuser. </p>
<p> The session user identifier is initially set to be the (possibly authenticated) user name provided by the client. The current user identifier is normally equal to the session user identifier, but might change temporarily in the context of SECURITY DEFINER functions and similar mechanisms; it can also be changed by SET ROLE [<code><a href="/docs/linux/man/7-set_role/">set_role</a></code>(7)]. The current user identifier is relevant for permission checking. </p>
<p> The session user identifier can be changed only if the initial session user (the <i>authenticated user</i>) had the superuser privilege. Otherwise, the command is accepted only if it specifies the authenticated user name. </p>
<p> The SESSION and LOCAL modifiers act the same as for the regular SET [<code><a href="/docs/linux/man/7-set/">set</a></code>(7)] command. </p>
<p> The DEFAULT and RESET forms reset the session and current user identifiers to be the originally authenticated user name. These forms can be executed by any user.</p>
<h2>Notes</h2>
<p><code>SET SESSION AUTHORIZATION</code> cannot be used within a SECURITY DEFINER function.</p>
<h2>Examples</h2>
<pre>SELECT SESSION_USER, CURRENT_USER;
 session_user | current_user 
--------------+--------------
 peter | peter
SET SESSION AUTHORIZATION 'paul';
SELECT SESSION_USER, CURRENT_USER;
 session_user | current_user 
--------------+--------------
 paul | paul</pre>
<h2>Compatibility</h2>
<p>The SQL standard allows some other expressions to appear in place of the literal <i>username</i>, but these options are not important in practice. PostgreSQL allows identifier syntax (&quot;username&quot;), which SQL does not. SQL does not allow this command during a transaction; PostgreSQL does not make this restriction because there is no reason to. The SESSION and LOCAL modifiers are a PostgreSQL extension, as is the RESET syntax. </p>
<p> The privileges necessary to execute this command are left implementation-defined by the standard.</p>
<h2>See Also</h2>
<p>SET ROLE [<code><a href="/docs/linux/man/7-set_role/">set_role</a></code>(7)] </p>
