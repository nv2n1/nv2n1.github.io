---
title: "grant(7)"
name: "grant"
section: "7"
letter: "g"
url: "/docs/linux/man/7-grant/"
description: "GRANT – define access privileges"
---

<p>GRANT &#8211; define access privileges </p>
<h2>Synopsis</h2>
<pre>GRANT { { SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER }
 [,...] | ALL [ PRIVILEGES ] }
 ON [ TABLE ] <i>tablename</i> [, ...]
 TO { [ GROUP ] <i>rolename</i> | PUBLIC } [, ...] [ WITH GRANT OPTION ]
GRANT { { SELECT | INSERT | UPDATE | REFERENCES } ( <i>column</i> [, ...] )
 [,...] | ALL [ PRIVILEGES ] ( <i>column</i> [, ...] ) }
 ON [ TABLE ] <i>tablename</i> [, ...]
 TO { [ GROUP ] <i>rolename</i> | PUBLIC } [, ...] [ WITH GRANT OPTION ]
GRANT { { USAGE | SELECT | UPDATE }
 [,...] | ALL [ PRIVILEGES ] }
 ON SEQUENCE <i>sequencename</i> [, ...]
 TO { [ GROUP ] <i>rolename</i> | PUBLIC } [, ...] [ WITH GRANT OPTION ]
GRANT { { CREATE | CONNECT | TEMPORARY | TEMP } [,...] | ALL [ PRIVILEGES ] }
 ON DATABASE <i>dbname</i> [, ...]
 TO { [ GROUP ] <i>rolename</i> | PUBLIC } [, ...] [ WITH GRANT OPTION ]
GRANT { USAGE | ALL [ PRIVILEGES ] }
 ON FOREIGN DATA WRAPPER <i>fdwname</i> [, ...]
 TO { [ GROUP ] <i>rolename</i> | PUBLIC } [, ...] [ WITH GRANT OPTION ]
GRANT { USAGE | ALL [ PRIVILEGES ] }
 ON FOREIGN SERVER <i>servername</i> [, ...]
 TO { [ GROUP ] <i>rolename</i> | PUBLIC } [, ...] [ WITH GRANT OPTION ]
GRANT { EXECUTE | ALL [ PRIVILEGES ] }
 ON FUNCTION <i>funcname</i> ( [ [ <i>argmode</i> ] [ <i>argname</i> ] <i>argtype</i> [, ...] ] ) [, ...]
 TO { [ GROUP ] <i>rolename</i> | PUBLIC } [, ...] [ WITH GRANT OPTION ]
GRANT { USAGE | ALL [ PRIVILEGES ] }
 ON LANGUAGE <i>langname</i> [, ...]
 TO { [ GROUP ] <i>rolename</i> | PUBLIC } [, ...] [ WITH GRANT OPTION ]
GRANT { { CREATE | USAGE } [,...] | ALL [ PRIVILEGES ] }
 ON SCHEMA <i>schemaname</i> [, ...]
 TO { [ GROUP ] <i>rolename</i> | PUBLIC } [, ...] [ WITH GRANT OPTION ]
GRANT { CREATE | ALL [ PRIVILEGES ] }
 ON TABLESPACE <i>tablespacename</i> [, ...]
 TO { [ GROUP ] <i>rolename</i> | PUBLIC } [, ...] [ WITH GRANT OPTION ]
GRANT <i>role</i> [, ...] TO <i>rolename</i> [, ...] [ WITH ADMIN OPTION ]</pre>
<h2>Description</h2>
<p>The <code>GRANT</code> command has two basic variants: one that grants privileges on a database object (table, column, view, sequence, database, foreign-data wrapper, foreign server, function, procedural language, schema, or tablespace), and one that grants membership in a role. These variants are similar in many ways, but they are different enough to be described separately. </p>
<p> As of PostgreSQL 8.1, the concepts of users and groups have been unified into a single kind of entity called a role. It is therefore no longer necessary to use the keyword GROUP to identify whether a grantee is a user or a group. GROUP is still allowed in the command, but it is a noise word.</p>
<h3>Grant On Database Objects</h3>
<p>This variant of the <code>GRANT</code> command gives specific privileges on a database object to one or more roles. These privileges are added to those already granted, if any. </p>
<p> The key word PUBLIC indicates that the privileges are to be granted to all roles, including those that might be created later. PUBLIC can be thought of as an implicitly defined group that always includes all roles. Any particular role will have the sum of privileges granted directly to it, privileges granted to any role it is presently a member of, and privileges granted to PUBLIC. </p>
<p> If WITH GRANT OPTION is specified, the recipient of the privilege can in turn grant it to others. Without a grant option, the recipient cannot do that. Grant options cannot be granted to PUBLIC. </p>
<p> There is no need to grant privileges to the owner of an object (usually the user that created it), as the owner has all privileges by default. (The owner could, however, choose to revoke some of his own privileges for safety.) The right to drop an object, or to alter its definition in any way is not described by a grantable privilege; it is inherent in the owner, and cannot be granted or revoked. The owner implicitly has all grant options for the object, too. </p>
<p> Depending on the type of object, the initial default privileges might include granting some privileges to PUBLIC. The default is no public access for tables, columns, schemas, and tablespaces; CONNECT privilege and TEMP table creation privilege for databases; EXECUTE privilege for functions; and USAGE privilege for languages. The object owner can of course revoke these privileges. (For maximum security, issue the <code>REVOKE</code> in the same transaction that creates the object; then there is no window in which another user can use the object.) </p>
<p> The possible privileges are:</p>
<dl>
<dt><code>SELECT</code></p>
<dd>Allows SELECT [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] from any column, or the specific columns listed, of the specified table, view, or sequence. Also allows the use of COPY [<code><a href="/docs/linux/man/7-copy/">copy</a></code>(7)] TO. This privilege is also needed to reference existing column values in UPDATE [<code><a href="/docs/linux/man/7-update/">update</a></code>(7)] or DELETE [<code><a href="/docs/linux/man/7-delete/">delete</a></code>(7)]. For sequences, this privilege also allows the use of the <code>currval</code> function.</p>
<dt><code>INSERT</code></p>
<dd>Allows INSERT [<code><a href="/docs/linux/man/7-insert/">insert</a></code>(7)] of a new row into the specified table. If specific columns are listed, only those columns may be assigned to in the <code>INSERT</code> command (other columns will therefore receive default values). Also allows COPY [<code><a href="/docs/linux/man/7-copy/">copy</a></code>(7)] FROM.</p>
<dt><code>UPDATE</code></p>
<dd>Allows UPDATE [<code><a href="/docs/linux/man/7-update/">update</a></code>(7)] of any column, or the specific columns listed, of the specified table. (In practice, any nontrivial <code>UPDATE</code> command will require SELECT privilege as well, since it must reference table columns to determine which rows to update, and/or to compute new values for columns.) SELECT &#8230; FOR UPDATE and SELECT &#8230; FOR SHARE also require this privilege on at least one column, in addition to the SELECT privilege. For sequences, this privilege allows the use of the <code>nextval</code> and <code>setval</code> functions.</p>
<dt><code>DELETE</code></p>
<dd>Allows DELETE [<code><a href="/docs/linux/man/7-delete/">delete</a></code>(7)] of a row from the specified table. (In practice, any nontrivial <code>DELETE</code> command will require SELECT privilege as well, since it must reference table columns to determine which rows to delete.)</p>
<dt><code>TRUNCATE</code></p>
<dd>Allows TRUNCATE [<code><a href="/docs/linux/man/7-truncate/">truncate</a></code>(7)] on the specified table.</p>
<dt><code>REFERENCES</code></p>
<dd>To create a foreign key constraint, it is necessary to have this privilege on both the referencing and referenced columns. The privilege may be granted for all columns of a table, or just specific columns.</p>
<dt><code>TRIGGER</code></p>
<dd>Allows the creation of a trigger on the specified table. (See the CREATE TRIGGER [<code><a href="/docs/linux/man/7-create_trigger/">create_trigger</a></code>(7)] statement.)</p>
<dt><code>CREATE</code></p>
<dd>For databases, allows new schemas to be created within the database. </p>
<p> For schemas, allows new objects to be created within the schema. To rename an existing object, you must own the object <code>and</code> have this privilege for the containing schema. </p>
<p> For tablespaces, allows tables, indexes, and temporary files to be created within the tablespace, and allows databases to be created that have the tablespace as their default tablespace. (Note that revoking this privilege will not alter the placement of existing objects.)</p>
<dt><code>CONNECT</code></p>
<dd>Allows the user to connect to the specified database. This privilege is checked at connection startup (in addition to checking any restrictions imposed by <i>pg_hba.conf</i>).</p>
<dt><code>TEMPORARY</code></p>
<dd>
<dt><code>TEMP</code></p>
<dd>Allows temporary tables to be created while using the specified database.</p>
<dt><code>EXECUTE</code></p>
<dd>Allows the use of the specified function and the use of any operators that are implemented on top of the function. This is the only type of privilege that is applicable to functions. (This syntax works for aggregate functions, as well.)</p>
<dt><code>USAGE</code></p>
<dd>For procedural languages, allows the use of the specified language for the creation of functions in that language. This is the only type of privilege that is applicable to procedural languages. </p>
<p> For schemas, allows access to objects contained in the specified schema (assuming that the objects&#8217; own privilege requirements are also met). Essentially this allows the grantee to &#8220;look up&#8221; objects within the schema. Without this permission, it is still possible to see the object names, e.g. by querying the system tables. Also, after revoking this permission, existing backends might have statements that have previously performed this lookup, so this is not a completely secure way to prevent object access. </p>
<p> For sequences, this privilege allows the use of the <code>currval</code> and <code>nextval</code> functions. </p>
<p> For foreign-data wrappers, this privilege enables the grantee to create new servers using that foreign-data wrapper. </p>
<p> For servers, this privilege enables the grantee to query the options of the server and associated user mappings.</p>
<dt><code>ALL PRIVILEGES</code></p>
<dd>Grant all of the available privileges at once. The PRIVILEGES key word is optional in PostgreSQL, though it is required by strict SQL.</dl>
<p> The privileges required by other commands are listed on the reference page of the respective command.</p>
<h3>Grant On Roles</h3>
<p>This variant of the <code>GRANT</code> command grants membership in a role to one or more other roles. Membership in a role is significant because it conveys the privileges granted to a role to each of its members. </p>
<p> If WITH ADMIN OPTION is specified, the member can in turn grant membership in the role to others, and revoke membership in the role as well. Without the admin option, ordinary users cannot do that. However, database superusers can grant or revoke membership in any role to anyone. Roles having CREATEROLE privilege can grant or revoke membership in any role that is not a superuser. </p>
<p> Unlike the case with privileges, membership in a role cannot be granted to PUBLIC. Note also that this form of the command does not allow the noise word GROUP.</p>
<h2>Notes</h2>
<p>The REVOKE [<code><a href="/docs/linux/man/7-revoke/">revoke</a></code>(7)] command is used to revoke access privileges. </p>
<p> A user may perform <code>SELECT</code>, <code>INSERT</code>, etc. on a column if he holds that privilege for either the specific column or its whole table. Granting the privilege at the table level and then revoking it for one column will not do what you might wish: the table-level grant is unaffected by a column-level operation. </p>
<p> When a non-owner of an object attempts to <code>GRANT</code> privileges on the object, the command will fail outright if the user has no privileges whatsoever on the object. As long as some privilege is available, the command will proceed, but it will grant only those privileges for which the user has grant options. The <code>GRANT ALL PRIVILEGES</code> forms will issue a warning message if no grant options are held, while the other forms will issue a warning if grant options for any of the privileges specifically named in the command are not held. (In principle these statements apply to the object owner as well, but since the owner is always treated as holding all grant options, the cases can never occur.) </p>
<p> It should be noted that database superusers can access all objects regardless of object privilege settings. This is comparable to the rights of root in a Unix system. As with root, it&#8217;s unwise to operate as a superuser except when absolutely necessary. </p>
<p> If a superuser chooses to issue a <code>GRANT</code> or <code>REVOKE</code> command, the command is performed as though it were issued by the owner of the affected object. In particular, privileges granted via such a command will appear to have been granted by the object owner. (For role membership, the membership appears to have been granted by the containing role itself.) </p>
<p> <code>GRANT</code> and <code>REVOKE</code> can also be done by a role that is not the owner of the affected object, but is a member of the role that owns the object, or is a member of a role that holds privileges WITH GRANT OPTION on the object. In this case the privileges will be recorded as having been granted by the role that actually owns the object or holds the privileges WITH GRANT OPTION. For example, if table t1 is owned by role g1, of which role u1 is a member, then u1 can grant privileges on t1 to u2, but those privileges will appear to have been granted directly by g1. Any other member of role g1 could revoke them later. </p>
<p> If the role executing <code>GRANT</code> holds the required privileges indirectly via more than one role membership path, it is unspecified which containing role will be recorded as having done the grant. In such cases it is best practice to use <code>SET ROLE</code> to become the specific role you want to do the <code>GRANT</code> as. </p>
<p> Granting permission on a table does not automatically extend permissions to any sequences used by the table, including sequences tied to <code>SERIAL</code> columns. Permissions on sequences must be set separately. </p>
<p> Use <code><a href="/docs/linux/man/1-psql/">psql</a></code>(1)&#8217;s <code>\dp</code> command to obtain information about existing privileges for tables and columns. For example: </p>
<pre>=&gt; \dp mytable
 Access privileges
 Schema | Name | Type | Access privileges | Column access privileges 
--------+---------+-------+-----------------------+--------------------------
 public | mytable | table | miriam=arwdDxt/miriam | col1:
 : =r/miriam : miriam_rw=rw/miriam
 : admin=arw/miriam 
(1 row)</pre>
<p>The entries shown by <code>\dp</code> are interpreted thus: </p>
<pre> rolename=xxxx -- privileges granted to a role
 =xxxx -- privileges granted to PUBLIC
 r -- SELECT (&quot;read&quot;)
 w -- UPDATE (&quot;write&quot;)
 a -- INSERT (&quot;append&quot;)
 d -- DELETE
 D -- TRUNCATE
 x -- REFERENCES
 t -- TRIGGER
 X -- EXECUTE
 U -- USAGE
 C -- CREATE
 c -- CONNECT
 T -- TEMPORARY
 arwdDxt -- ALL PRIVILEGES (for tables, varies for other objects)
 * -- grant option for preceding privilege
 /yyyy -- role that granted this privilege</pre>
<p>The above example display would be seen by user miriam after creating table mytable and doing: </p>
<pre>GRANT SELECT ON mytable TO PUBLIC;
GRANT SELECT, UPDATE, INSERT ON mytable TO admin;
GRANT SELECT (col1), UPDATE (col1) ON mytable TO miriam_rw;</pre>
<p>For non-table objects there are other <code>\d</code> commands that can display their privileges. </p>
<p> If the &#8220;Access privileges&#8221; column is empty for a given object, it means the object has default privileges (that is, its privileges column is null). Default privileges always include all privileges for the owner, and can include some privileges for PUBLIC depending on the object type, as explained above. The first <code>GRANT</code> or <code>REVOKE</code> on an object will instantiate the default privileges (producing, for example, {miriam=arwdDxt/miriam}) and then modify them per the specified request. Entries are shown in &#8220;Column access privileges&#8221; only for columns with nondefault privileges. </p>
<p> Notice that the owner&#8217;s implicit grant options are not marked in the access privileges display. A * will appear only when grant options have been explicitly granted to someone.</p>
<h2>Examples</h2>
<p>Grant insert privilege to all users on table films: </p>
<pre>GRANT INSERT ON films TO PUBLIC;</pre>
<p>Grant all available privileges to user manuel on view kinds: </p>
<pre>GRANT ALL PRIVILEGES ON kinds TO manuel;</pre>
<p>Note that while the above will indeed grant all privileges if executed by a superuser or the owner of kinds, when executed by someone else it will only grant those permissions for which the someone else has grant options. </p>
<p> Grant membership in role admins to user joe: </p>
<pre>GRANT admins TO joe;</pre>
<h2>Compatibility</h2>
<p>According to the SQL standard, the PRIVILEGES key word in ALL PRIVILEGES is required. The SQL standard does not support setting the privileges on more than one object per command. </p>
<p> PostgreSQL allows an object owner to revoke his own ordinary privileges: for example, a table owner can make the table read-only to himself by revoking his own INSERT, UPDATE, DELETE, and TRUNCATE privileges. This is not possible according to the SQL standard. The reason is that PostgreSQL treats the owner&#8217;s privileges as having been granted by the owner to himself; therefore he can revoke them too. In the SQL standard, the owner&#8217;s privileges are granted by an assumed entity &#8220;_SYSTEM&#8221;. Not being &#8220;_SYSTEM&#8221;, the owner cannot revoke these rights. </p>
<p> The SQL standard provides for a USAGE privilege on other kinds of objects: character sets, collations, translations, domains. </p>
<p> Privileges on databases, tablespaces, schemas, and languages are PostgreSQL extensions.</p>
<h2>See Also</h2>
<p>REVOKE [<code><a href="/docs/linux/man/7-revoke/">revoke</a></code>(7)] </p>
