---
title: "revoke(7)"
name: "revoke"
section: "7"
letter: "r"
url: "/docs/linux/man/7-revoke/"
description: "REVOKE – remove access privileges"
---

<p>REVOKE &#8211; remove access privileges </p>
<h2>Synopsis</h2>
<pre>REVOKE [ GRANT OPTION FOR ]
 { { SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER }
 [,...] | ALL [ PRIVILEGES ] }
 ON [ TABLE ] <i>tablename</i> [, ...]
 FROM { [ GROUP ] <i>rolename</i> | PUBLIC } [, ...]
 [ CASCADE | RESTRICT ]
REVOKE [ GRANT OPTION FOR ]
 { { SELECT | INSERT | UPDATE | REFERENCES } ( <i>column</i> [, ...] )
 [,...] | ALL [ PRIVILEGES ] ( <i>column</i> [, ...] ) }
 ON [ TABLE ] <i>tablename</i> [, ...]
 FROM { [ GROUP ] <i>rolename</i> | PUBLIC } [, ...]
 [ CASCADE | RESTRICT ]
REVOKE [ GRANT OPTION FOR ]
 { { USAGE | SELECT | UPDATE }
 [,...] | ALL [ PRIVILEGES ] }
 ON SEQUENCE <i>sequencename</i> [, ...]
 FROM { [ GROUP ] <i>rolename</i> | PUBLIC } [, ...]
 [ CASCADE | RESTRICT ]
REVOKE [ GRANT OPTION FOR ]
 { { CREATE | CONNECT | TEMPORARY | TEMP } [,...] | ALL [ PRIVILEGES ] }
 ON DATABASE <i>dbname</i> [, ...]
 FROM { [ GROUP ] <i>rolename</i> | PUBLIC } [, ...]
 [ CASCADE | RESTRICT ]
REVOKE [ GRANT OPTION FOR ]
 { USAGE | ALL [ PRIVILEGES ] }
 ON FOREIGN DATA WRAPPER <i>fdwname</i> [, ...]
 FROM { [ GROUP ] <i>rolename</i> | PUBLIC } [, ...]
 [ CASCADE | RESTRICT ]
REVOKE [ GRANT OPTION FOR ]
 { USAGE | ALL [ PRIVILEGES ] }
 ON FOREIGN SERVER <i>servername</i> [, ...]
 FROM { [ GROUP ] <i>rolename</i> | PUBLIC } [, ...]
 [ CASCADE | RESTRICT ]
REVOKE [ GRANT OPTION FOR ]
 { EXECUTE | ALL [ PRIVILEGES ] }
 ON FUNCTION <i>funcname</i> ( [ [ <i>argmode</i> ] [ <i>argname</i> ] <i>argtype</i> [, ...] ] ) [, ...]
 FROM { [ GROUP ] <i>rolename</i> | PUBLIC } [, ...]
 [ CASCADE | RESTRICT ]
REVOKE [ GRANT OPTION FOR ]
 { USAGE | ALL [ PRIVILEGES ] }
 ON LANGUAGE <i>langname</i> [, ...]
 FROM { [ GROUP ] <i>rolename</i> | PUBLIC } [, ...]
 [ CASCADE | RESTRICT ]
REVOKE [ GRANT OPTION FOR ]
 { { CREATE | USAGE } [,...] | ALL [ PRIVILEGES ] }
 ON SCHEMA <i>schemaname</i> [, ...]
 FROM { [ GROUP ] <i>rolename</i> | PUBLIC } [, ...]
 [ CASCADE | RESTRICT ]
REVOKE [ GRANT OPTION FOR ]
 { CREATE | ALL [ PRIVILEGES ] }
 ON TABLESPACE <i>tablespacename</i> [, ...]
 FROM { [ GROUP ] <i>rolename</i> | PUBLIC } [, ...]
 [ CASCADE | RESTRICT ]
REVOKE [ ADMIN OPTION FOR ]
 <i>role</i> [, ...] FROM <i>rolename</i> [, ...]
 [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p>The <code>REVOKE</code> command revokes previously granted privileges from one or more roles. The key word PUBLIC refers to the implicitly defined group of all roles. </p>
<p> See the description of the GRANT [<code><a href="/docs/linux/man/7-grant/">grant</a></code>(7)] command for the meaning of the privilege types. </p>
<p> Note that any particular role will have the sum of privileges granted directly to it, privileges granted to any role it is presently a member of, and privileges granted to PUBLIC. Thus, for example, revoking SELECT privilege from PUBLIC does not necessarily mean that all roles have lost SELECT privilege on the object: those who have it granted directly or via another role will still have it. Similarly, revoking SELECT from a user might not prevent that user from using SELECT if PUBLIC or another membership role still has SELECT rights. </p>
<p> If GRANT OPTION FOR is specified, only the grant option for the privilege is revoked, not the privilege itself. Otherwise, both the privilege and the grant option are revoked. </p>
<p> If a user holds a privilege with grant option and has granted it to other users then the privileges held by those other users are called dependent privileges. If the privilege or the grant option held by the first user is being revoked and dependent privileges exist, those dependent privileges are also revoked if CASCADE is specified; if it is not, the revoke action will fail. This recursive revocation only affects privileges that were granted through a chain of users that is traceable to the user that is the subject of this REVOKE command. Thus, the affected users might effectively keep the privilege if it was also granted through other users. </p>
<p> When revoking privileges on a table, the corresponding column privileges (if any) are automatically revoked on each column of the table, as well. </p>
<p> When revoking membership in a role, GRANT OPTION is instead called ADMIN OPTION, but the behavior is similar. Note also that this form of the command does not allow the noise word GROUP.</p>
<h2>Notes</h2>
<p>Use <code><a href="/docs/linux/man/1-psql/">psql</a></code>(1)&#8217;s <code>\dp</code> command to display the privileges granted on existing tables and columns. See GRANT [<code><a href="/docs/linux/man/7-grant/">grant</a></code>(7)] for information about the format. For non-table objects there are other <code>\d</code> commands that can display their privileges. </p>
<p> A user can only revoke privileges that were granted directly by that user. If, for example, user A has granted a privilege with grant option to user B, and user B has in turned granted it to user C, then user A cannot revoke the privilege directly from C. Instead, user A could revoke the grant option from user B and use the CASCADE option so that the privilege is in turn revoked from user C. For another example, if both A and B have granted the same privilege to C, A can revoke his own grant but not B&#8217;s grant, so C will still effectively have the privilege. </p>
<p> When a non-owner of an object attempts to <code>REVOKE</code> privileges on the object, the command will fail outright if the user has no privileges whatsoever on the object. As long as some privilege is available, the command will proceed, but it will revoke only those privileges for which the user has grant options. The <code>REVOKE ALL PRIVILEGES</code> forms will issue a warning message if no grant options are held, while the other forms will issue a warning if grant options for any of the privileges specifically named in the command are not held. (In principle these statements apply to the object owner as well, but since the owner is always treated as holding all grant options, the cases can never occur.) </p>
<p> If a superuser chooses to issue a <code>GRANT</code> or <code>REVOKE</code> command, the command is performed as though it were issued by the owner of the affected object. Since all privileges ultimately come from the object owner (possibly indirectly via chains of grant options), it is possible for a superuser to revoke all privileges, but this might require use of CASCADE as stated above. </p>
<p> <code>REVOKE</code> can also be done by a role that is not the owner of the affected object, but is a member of the role that owns the object, or is a member of a role that holds privileges WITH GRANT OPTION on the object. In this case the command is performed as though it were issued by the containing role that actually owns the object or holds the privileges WITH GRANT OPTION. For example, if table t1 is owned by role g1, of which role u1 is a member, then u1 can revoke privileges on t1 that are recorded as being granted by g1. This would include grants made by u1 as well as by other members of role g1. </p>
<p> If the role executing <code>REVOKE</code> holds privileges indirectly via more than one role membership path, it is unspecified which containing role will be used to perform the command. In such cases it is best practice to use <code>SET ROLE</code> to become the specific role you want to do the <code>REVOKE</code> as. Failure to do so might lead to revoking privileges other than the ones you intended, or not revoking anything at all.</p>
<h2>Examples</h2>
<p>Revoke insert privilege for the public on table films: </p>
<pre>REVOKE INSERT ON films FROM PUBLIC;</pre>
<p>Revoke all privileges from user manuel on view kinds: </p>
<pre>REVOKE ALL PRIVILEGES ON kinds FROM manuel;</pre>
<p>Note that this actually means &#8220;revoke all privileges that I granted&#8221;. </p>
<p> Revoke membership in role admins from user joe: </p>
<pre>REVOKE admins FROM joe;</pre>
<h2>Compatibility</h2>
<p>The compatibility notes of the GRANT [<code><a href="/docs/linux/man/7-grant/">grant</a></code>(7)] command apply analogously to <code>REVOKE</code>. The keyword RESTRICT or CASCADE is required according to the standard, but PostgreSQL assumes RESTRICT by default.</p>
<h2>See Also</h2>
<p>GRANT [<code><a href="/docs/linux/man/7-grant/">grant</a></code>(7)] </p>
