---
title: "dropuser(1)"
name: "dropuser"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dropuser/"
description: "dropuser – remove a PostgreSQL user account"
---

<h2 class="name">NAME</h2>
<p> dropuser &#8211; remove a PostgreSQL user account </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>dropuser</code> [<i>connection-option</i>&#8230;] [<i>option</i>&#8230;] [<i>username</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>dropuser removes an existing PostgreSQL user. Only superusers and users with the CREATEROLE privilege can remove PostgreSQL users. (To remove a superuser, you must yourself be a superuser.) </p>
<p> dropuser is a wrapper around the SQL command DROP ROLE (<code><a href="/docs/linux/man/7-drop_role/">DROP_ROLE</a></code>(7)). There is no effective difference between dropping users via this utility and via other methods for accessing the server.</p>
<h2>OPTIONS</h2>
<p> dropuser accepts the following command-line arguments: </p>
<p> <i>username</i></p>
<dl>
<dt>
<dd> Specifies the name of the PostgreSQL user to be removed. You will be prompted for a name if none is specified on the command line and the <code>-i</code>/<code>&#8211;interactive</code> option is used.</dl>
<p> <code>-e</code>, <code>&#8211;echo</code></p>
<dl>
<dt>
<dd> Echo the commands that dropuser generates and sends to the server.</dl>
<p> <code>-i</code>, <code>&#8211;interactive</code></p>
<dl>
<dt>
<dd> Prompt for confirmation before actually removing the user, and prompt for the user name if none is specified on the command line.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the dropuser version and exit.</dl>
<p> <code>&#8211;if-exists</code></p>
<dl>
<dt>
<dd> Do not throw an error if the user does not exist. A notice is issued in this case.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about dropuser command line arguments, and exit.</dl>
<p> dropuser also accepts the following command-line arguments for connection parameters: </p>
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
<dd> User name to connect as (not the user name to drop).</dl>
<p> <code>-w</code>, <code>&#8211;no-password</code></p>
<dl>
<dt>
<dd> Never issue a password prompt. If the server requires password authentication and a password is not available by other means such as a .pgpass file, the connection attempt will fail. This option can be useful in batch jobs and scripts where no user is present to enter a password.</dl>
<p> <code>-W</code>, <code>&#8211;password</code></p>
<dl>
<dt>
<dd> Force dropuser to prompt for a password before connecting to a database. </p>
<p> This option is never essential, since dropuser will automatically prompt for a password if the server demands password authentication. However, dropuser will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing <code>-W</code> to avoid the extra connection attempt.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>PGHOST</code>, <code>PGPORT</code>, <code>PGUSER</code></p>
<dl>
<dt>
<dd> Default connection parameters</dl>
<p> This utility, like most other PostgreSQL utilities, also uses the environment variables supported by libpq (see Section 31.14, &#8220;Environment Variables&#8221;, in the documentation).</p>
<h2>DIAGNOSTICS</h2>
<p> In case of difficulty, see DROP ROLE (<code><a href="/docs/linux/man/7-drop_role/">DROP_ROLE</a></code>(7)) and <code><a href="/docs/linux/man/1-psql/">psql</a></code>(1) for discussions of potential problems and error messages. The database server must be running at the targeted host. Also, any default connection settings and environment variables used by the libpq front-end library will apply.</p>
<h2>EXAMPLES</h2>
<p> To remove user joe from the default database server: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>dropuser joe</code>
</pre>
</dl>
<p> To remove user joe using the server on host eden, port 5000, with verification and a peek at the underlying command: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>dropuser -p 5000 -h eden -i -e joe</code>
Role &quot;joe&quot; will be permanently removed.
Are you sure? (y/n) <code>y</code>
DROP ROLE joe;
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-createuser/">createuser</a></code>(1), DROP ROLE (<code><a href="/docs/linux/man/7-drop_role/">DROP_ROLE</a></code>(7)) </p>
<h2>Index</h2>
