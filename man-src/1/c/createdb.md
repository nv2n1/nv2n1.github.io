---
title: "createdb(1)"
name: "createdb"
section: "1"
letter: "c"
url: "/docs/linux/man/1-createdb/"
description: "createdb – create a new PostgreSQL database"
---

<h2 class="name">NAME</h2>
<p> createdb &#8211; create a new PostgreSQL database </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>createdb</code> [<i>connection-option</i>&#8230;] [<i>option</i>&#8230;] [<i>dbname</i>&nbsp;<wbr>[<i>description</i>]]</dl>
<h2>DESCRIPTION</h2>
<dd>createdb creates a new PostgreSQL database. </p>
<p> Normally, the database user who executes this command becomes the owner of the new database. However, a different owner can be specified via the <code>-O</code> option, if the executing user has appropriate privileges. </p>
<p> createdb is a wrapper around the SQL command CREATE DATABASE (<code><a href="/docs/linux/man/7-create_database/">CREATE_DATABASE</a></code>(7)). There is no effective difference between creating databases via this utility and via other methods for accessing the server.</p>
<h2>OPTIONS</h2>
<p> createdb accepts the following command-line arguments: </p>
<p> <i>dbname</i></p>
<dl>
<dt>
<dd> Specifies the name of the database to be created. The name must be unique among all PostgreSQL databases in this cluster. The default is to create a database with the same name as the current system user.</dl>
<p> <i>description</i></p>
<dl>
<dt>
<dd> Specifies a comment to be associated with the newly created database.</dl>
<p> <code>-D </code><i>tablespace</i>, <code>&#8211;tablespace=</code><i>tablespace</i></p>
<dl>
<dt>
<dd> Specifies the default tablespace for the database. (This name is processed as a double-quoted identifier.)</dl>
<p> <code>-e</code>, <code>&#8211;echo</code></p>
<dl>
<dt>
<dd> Echo the commands that createdb generates and sends to the server.</dl>
<p> <code>-E </code><i>encoding</i>, <code>&#8211;encoding=</code><i>encoding</i></p>
<dl>
<dt>
<dd> Specifies the character encoding scheme to be used in this database. The character sets supported by the PostgreSQL server are described in Section 22.3.1, &#8220;Supported Character Sets&#8221;, in the documentation.</dl>
<p> <code>-l </code><i>locale</i>, <code>&#8211;locale=</code><i>locale</i></p>
<dl>
<dt>
<dd> Specifies the locale to be used in this database. This is equivalent to specifying both <code>&#8211;lc-collate</code> and <code>&#8211;lc-ctype</code>.</dl>
<p> <code>&#8211;lc-collate=</code><i>locale</i></p>
<dl>
<dt>
<dd> Specifies the LC_COLLATE setting to be used in this database.</dl>
<p> <code>&#8211;lc-ctype=</code><i>locale</i></p>
<dl>
<dt>
<dd> Specifies the LC_CTYPE setting to be used in this database.</dl>
<p> <code>-O </code><i>owner</i>, <code>&#8211;owner=</code><i>owner</i></p>
<dl>
<dt>
<dd> Specifies the database user who will own the new database. (This name is processed as a double-quoted identifier.)</dl>
<p> <code>-T </code><i>template</i>, <code>&#8211;template=</code><i>template</i></p>
<dl>
<dt>
<dd> Specifies the template database from which to build this database. (This name is processed as a double-quoted identifier.)</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the createdb version and exit.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about createdb command line arguments, and exit.</dl>
<p> The options <code>-D</code>, <code>-l</code>, <code>-E</code>, <code>-O</code>, and <code>-T</code> correspond to options of the underlying SQL command CREATE DATABASE (<code><a href="/docs/linux/man/7-create_database/">CREATE_DATABASE</a></code>(7)); see there for more information about them. </p>
<p> createdb also accepts the following command-line arguments for connection parameters: </p>
<p> <code>-h </code><i>host</i>, <code>&#8211;host=</code><i>host</i></p>
<dl>
<dt>
<dd> Specifies the host name of the machine on which the server is running. If the value begins with a slash, it is used as the directory for the Unix domain socket.</dl>
<p> <code>-p </code><i>port</i>, <code>&#8211;port=</code><i>port</i></p>
<dl>
<dt>
<dd> Specifies the TCP port or the local Unix domain socket file extension on which the server is listening for connections.</dl>
<p> <code>-U </code><i>username</i>, <code>&#8211;username=</code><i>username</i></p>
<dl>
<dt>
<dd> User name to connect as.</dl>
<p> <code>-w</code>, <code>&#8211;no-password</code></p>
<dl>
<dt>
<dd> Never issue a password prompt. If the server requires password authentication and a password is not available by other means such as a .pgpass file, the connection attempt will fail. This option can be useful in batch jobs and scripts where no user is present to enter a password.</dl>
<p> <code>-W</code>, <code>&#8211;password</code></p>
<dl>
<dt>
<dd> Force createdb to prompt for a password before connecting to a database. </p>
<p> This option is never essential, since createdb will automatically prompt for a password if the server demands password authentication. However, createdb will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing <code>-W</code> to avoid the extra connection attempt.</dl>
<p> <code>&#8211;maintenance-db=</code><i>dbname</i></p>
<dl>
<dt>
<dd> Specifies the name of the database to connect to when creating the new database. If not specified, the postgres database will be used; if that does not exist (or if it is the name of the new database being created), template1 will be used.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>PGDATABASE</code></p>
<dl>
<dt>
<dd> If set, the name of the database to create, unless overridden on the command line.</dl>
<p> <code>PGHOST</code>, <code>PGPORT</code>, <code>PGUSER</code></p>
<dl>
<dt>
<dd> Default connection parameters. <code>PGUSER</code> also determines the name of the database to create, if it is not specified on the command line or by <code>PGDATABASE</code>.</dl>
<p> This utility, like most other PostgreSQL utilities, also uses the environment variables supported by libpq (see Section 31.14, &#8220;Environment Variables&#8221;, in the documentation).</p>
<h2>DIAGNOSTICS</h2>
<p> In case of difficulty, see CREATE DATABASE (<code><a href="/docs/linux/man/7-create_database/">CREATE_DATABASE</a></code>(7)) and <code><a href="/docs/linux/man/1-psql/">psql</a></code>(1) for discussions of potential problems and error messages. The database server must be running at the targeted host. Also, any default connection settings and environment variables used by the libpq front-end library will apply.</p>
<h2>EXAMPLES</h2>
<p> To create the database demo using the default database server: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>createdb demo</code>
</pre>
</dl>
<p> To create the database demo using the server on host eden, port 5000, using the LATIN1 encoding scheme with a look at the underlying command: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>createdb -p 5000 -h eden -E LATIN1 -e demo</code>
CREATE DATABASE demo ENCODING 'LATIN1';
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dropdb/">dropdb</a></code>(1), CREATE DATABASE (<code><a href="/docs/linux/man/7-create_database/">CREATE_DATABASE</a></code>(7)) </p>
<h2>Index</h2>
