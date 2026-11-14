---
title: "createuser(1)"
name: "createuser"
section: "1"
letter: "c"
url: "/docs/linux/man/1-createuser/"
description: "createuser – define a new PostgreSQL user account"
---

<h2 class="name">NAME</h2>
<p> createuser &#8211; define a new PostgreSQL user account </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>createuser</code> [<i>connection-option</i>&#8230;] [<i>option</i>&#8230;] [<i>username</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>createuser creates a new PostgreSQL user (or more precisely, a role). Only superusers and users with CREATEROLE privilege can create new users, so createuser must be invoked by someone who can connect as a superuser or a user with CREATEROLE privilege. </p>
<p> If you wish to create a new superuser, you must connect as a superuser, not merely with CREATEROLE privilege. Being a superuser implies the ability to bypass all access permission checks within the database, so superuserdom should not be granted lightly. </p>
<p> createuser is a wrapper around the SQL command CREATE ROLE (<code><a href="/docs/linux/man/7-create_role/">CREATE_ROLE</a></code>(7)). There is no effective difference between creating users via this utility and via other methods for accessing the server.</p>
<h2>OPTIONS</h2>
<p> createuser accepts the following command-line arguments: </p>
<p> <i>username</i></p>
<dl>
<dt>
<dd> Specifies the name of the PostgreSQL user to be created. This name must be different from all existing roles in this PostgreSQL installation.</dl>
<p> <code>-c </code><i>number</i>, <code>&#8211;connection-limit=</code><i>number</i></p>
<dl>
<dt>
<dd> Set a maximum number of connections for the new user. The default is to set no limit.</dl>
<p> <code>-d</code>, <code>&#8211;createdb</code></p>
<dl>
<dt>
<dd> The new user will be allowed to create databases.</dl>
<p> <code>-D</code>, <code>&#8211;no-createdb</code></p>
<dl>
<dt>
<dd> The new user will not be allowed to create databases. This is the default.</dl>
<p> <code>-e</code>, <code>&#8211;echo</code></p>
<dl>
<dt>
<dd> Echo the commands that createuser generates and sends to the server.</dl>
<p> <code>-E</code>, <code>&#8211;encrypted</code></p>
<dl>
<dt>
<dd> Encrypts the user&#8217;s password stored in the database. If not specified, the default password behavior is used.</dl>
<p> <code>-i</code>, <code>&#8211;inherit</code></p>
<dl>
<dt>
<dd> The new role will automatically inherit privileges of roles it is a member of. This is the default.</dl>
<p> <code>-I</code>, <code>&#8211;no-inherit</code></p>
<dl>
<dt>
<dd> The new role will not automatically inherit privileges of roles it is a member of.</dl>
<p> <code>&#8211;interactive</code></p>
<dl>
<dt>
<dd> Prompt for the user name if none is specified on the command line, and also prompt for whichever of the options <code>-d</code>/<code>-D</code>, <code>-r</code>/<code>-R</code>, <code>-s</code>/<code>-S</code> is not specified on the command line. (This was the default behavior up to PostgreSQL 9.1.)</dl>
<p> <code>-l</code>, <code>&#8211;login</code></p>
<dl>
<dt>
<dd> The new user will be allowed to log in (that is, the user name can be used as the initial session user identifier). This is the default.</dl>
<p> <code>-L</code>, <code>&#8211;no-login</code></p>
<dl>
<dt>
<dd> The new user will not be allowed to log in. (A role without login privilege is still useful as a means of managing database permissions.)</dl>
<p> <code>-N</code>, <code>&#8211;unencrypted</code></p>
<dl>
<dt>
<dd> Does not encrypt the user&#8217;s password stored in the database. If not specified, the default password behavior is used.</dl>
<p> <code>-P</code>, <code>&#8211;pwprompt</code></p>
<dl>
<dt>
<dd> If given, createuser will issue a prompt for the password of the new user. This is not necessary if you do not plan on using password authentication.</dl>
<p> <code>-r</code>, <code>&#8211;createrole</code></p>
<dl>
<dt>
<dd> The new user will be allowed to create new roles (that is, this user will have CREATEROLE privilege).</dl>
<p> <code>-R</code>, <code>&#8211;no-createrole</code></p>
<dl>
<dt>
<dd> The new user will not be allowed to create new roles. This is the default.</dl>
<p> <code>-s</code>, <code>&#8211;superuser</code></p>
<dl>
<dt>
<dd> The new user will be a superuser.</dl>
<p> <code>-S</code>, <code>&#8211;no-superuser</code></p>
<dl>
<dt>
<dd> The new user will not be a superuser. This is the default.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the createuser version and exit.</dl>
<p> <code>&#8211;replication</code></p>
<dl>
<dt>
<dd> The new user will have the REPLICATION privilege, which is described more fully in the documentation for CREATE ROLE (<code><a href="/docs/linux/man/7-create_role/">CREATE_ROLE</a></code>(7)).</dl>
<p> <code>&#8211;no-replication</code></p>
<dl>
<dt>
<dd> The new user will not have the REPLICATION privilege, which is described more fully in the documentation for CREATE ROLE (<code><a href="/docs/linux/man/7-create_role/">CREATE_ROLE</a></code>(7)).</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about createuser command line arguments, and exit.</dl>
<p> createuser also accepts the following command-line arguments for connection parameters: </p>
<p> <code>-h </code><i>host</i>, <code>&#8211;host=</code><i>host</i></p>
<dl>
<dt>
<dd> Specifies the host name of the machine on which the server is running. If the value begins with a slash, it is used as the directory for the Unix domain socket.</dl>
<p> <code>-p </code><i>port</i>, <code>&#8211;port=</code><i>port</i></p>
<dl>
<dt>
<dd> Specifies the TCP port or local Unix domain socket file extension on which the server is listening for connections.</dl>
<p> <code>-U </code><i>username</i>, <code>&#8211;username=</code><i>username</i></p>
<dl>
<dt>
<dd> User name to connect as (not the user name to create).</dl>
<p> <code>-w</code>, <code>&#8211;no-password</code></p>
<dl>
<dt>
<dd> Never issue a password prompt. If the server requires password authentication and a password is not available by other means such as a .pgpass file, the connection attempt will fail. This option can be useful in batch jobs and scripts where no user is present to enter a password.</dl>
<p> <code>-W</code>, <code>&#8211;password</code></p>
<dl>
<dt>
<dd> Force createuser to prompt for a password (for connecting to the server, not for the password of the new user). </p>
<p> This option is never essential, since createuser will automatically prompt for a password if the server demands password authentication. However, createuser will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing <code>-W</code> to avoid the extra connection attempt.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>PGHOST</code>, <code>PGPORT</code>, <code>PGUSER</code></p>
<dl>
<dt>
<dd> Default connection parameters</dl>
<p> This utility, like most other PostgreSQL utilities, also uses the environment variables supported by libpq (see Section 31.14, &#8220;Environment Variables&#8221;, in the documentation).</p>
<h2>DIAGNOSTICS</h2>
<p> In case of difficulty, see CREATE ROLE (<code><a href="/docs/linux/man/7-create_role/">CREATE_ROLE</a></code>(7)) and <code><a href="/docs/linux/man/1-psql/">psql</a></code>(1) for discussions of potential problems and error messages. The database server must be running at the targeted host. Also, any default connection settings and environment variables used by the libpq front-end library will apply.</p>
<h2>EXAMPLES</h2>
<p> To create a user joe on the default database server: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>createuser joe</code>
</pre>
</dl>
<p> To create a user joe on the default database server with prompting for some additional attributes: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>createuser --interactive joe</code>
Shall the new role be a superuser? (y/n) <code>n</code>
Shall the new role be allowed to create databases? (y/n) <code>n</code>
Shall the new role be allowed to create more new roles? (y/n) <code>n</code>
</pre>
</dl>
<p> To create the same user joe using the server on host eden, port 5000, with attributes explicitly specified, taking a look at the underlying command: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>createuser -h eden -p 5000 -S -D -R -e joe</code>
CREATE ROLE joe NOSUPERUSER NOCREATEDB NOCREATEROLE INHERIT LOGIN;
</pre>
</dl>
<p> To create the user joe as a superuser, and assign a password immediately: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>createuser -P -s -e joe</code>
Enter password for new role: <code>xyzzy</code>
Enter it again: <code>xyzzy</code>
CREATE ROLE joe PASSWORD 'md5b5f5ba1a423792b526f799ae4eb3d59e' SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;
</pre>
</dl>
<p> In the above example, the new password isn&#8217;t actually echoed when typed, but we show what was typed for clarity. As you see, the password is encrypted before it is sent to the client. If the option <code>&#8211;unencrypted</code> is used, the password <i>will</i> appear in the echoed command (and possibly also in the server log and elsewhere), so you don&#8217;t want to use <code>-e</code> in that case, if anyone else can see your screen.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dropuser/">dropuser</a></code>(1), CREATE ROLE (<code><a href="/docs/linux/man/7-create_role/">CREATE_ROLE</a></code>(7)) </p>
<h2>Index</h2>
