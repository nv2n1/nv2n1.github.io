---
title: "pg_dumpall(1)"
name: "pg_dumpall"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pg_dumpall/"
description: "pg_dumpall – extract a PostgreSQL database cluster into a script file"
---

<h2 class="name">NAME</h2>
<p> pg_dumpall &#8211; extract a PostgreSQL database cluster into a script file </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pg_dumpall</code> [<i>connection-option</i>&#8230;] [<i>option</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>pg_dumpall is a utility for writing out (&#8220;dumping&#8221;) all PostgreSQL databases of a cluster into one script file. The script file contains SQL commands that can be used as input to <code><a href="/docs/linux/man/1-psql/">psql</a></code>(1) to restore the databases. It does this by calling <code><a href="/docs/linux/man/1-pg_dump/">pg_dump</a></code>(1) for each database in a cluster. pg_dumpall also dumps global objects that are common to all databases. (pg_dump does not save these objects.) This currently includes information about database users and groups, tablespaces, and properties such as access permissions that apply to databases as a whole. </p>
<p> Since pg_dumpall reads tables from all databases you will most likely have to connect as a database superuser in order to produce a complete dump. Also you will need superuser privileges to execute the saved script in order to be allowed to add users and groups, and to create databases. </p>
<p> The SQL script will be written to the standard output. Use the [-f|file] option or shell operators to redirect it into a file. </p>
<p> pg_dumpall needs to connect several times to the PostgreSQL server (once per database). If you use password authentication it will ask for a password each time. It is convenient to have a ~/.pgpass file in such cases. See Section 31.15, &#8220;The Password File&#8221;, in the documentation for more information.</p>
<h2>OPTIONS</h2>
<p> The following command-line options control the content and format of the output. </p>
<p> <code>-a</code>, <code>&#8211;data-only</code></p>
<dl>
<dt>
<dd> Dump only the data, not the schema (data definitions).</dl>
<p> <code>-c</code>, <code>&#8211;clean</code></p>
<dl>
<dt>
<dd> Include SQL commands to clean (drop) databases before recreating them. <code>DROP</code> commands for roles and tablespaces are added as well.</dl>
<p> <code>-f </code><i>filename</i>, <code>&#8211;file=</code><i>filename</i></p>
<dl>
<dt>
<dd> Send output to the specified file. If this is omitted, the standard output is used.</dl>
<p> <code>-g</code>, <code>&#8211;globals-only</code></p>
<dl>
<dt>
<dd> Dump only global objects (roles and tablespaces), no databases.</dl>
<p> <code>-i</code>, <code>&#8211;ignore-version</code></p>
<dl>
<dt>
<dd> A deprecated option that is now ignored.</dl>
<p> <code>-o</code>, <code>&#8211;oids</code></p>
<dl>
<dt>
<dd> Dump object identifiers (OIDs) as part of the data for every table. Use this option if your application references the OID columns in some way (e.g., in a foreign key constraint). Otherwise, this option should not be used.</dl>
<p> <code>-O</code>, <code>&#8211;no-owner</code></p>
<dl>
<dt>
<dd> Do not output commands to set ownership of objects to match the original database. By default, pg_dumpall issues <code>ALTER OWNER</code> or <code>SET SESSION AUTHORIZATION</code> statements to set ownership of created schema elements. These statements will fail when the script is run unless it is started by a superuser (or the same user that owns all of the objects in the script). To make a script that can be restored by any user, but will give that user ownership of all the objects, specify <code>-O</code>.</dl>
<p> <code>-r</code>, <code>&#8211;roles-only</code></p>
<dl>
<dt>
<dd> Dump only roles, no databases or tablespaces.</dl>
<p> <code>-s</code>, <code>&#8211;schema-only</code></p>
<dl>
<dt>
<dd> Dump only the object definitions (schema), not data.</dl>
<p> <code>-S </code><i>username</i>, <code>&#8211;superuser=</code><i>username</i></p>
<dl>
<dt>
<dd> Specify the superuser user name to use when disabling triggers. This is only relevant if <code>&#8211;disable-triggers</code> is used. (Usually, it&#8217;s better to leave this out, and instead start the resulting script as superuser.)</dl>
<p> <code>-t</code>, <code>&#8211;tablespaces-only</code></p>
<dl>
<dt>
<dd> Dump only tablespaces, no databases or roles.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Specifies verbose mode. This will cause pg_dumpall to output start/stop times to the dump file, and progress messages to standard error. It will also enable verbose output in pg_dump.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the pg_dumpall version and exit.</dl>
<p> <code>-x</code>, <code>&#8211;no-privileges</code>, <code>&#8211;no-acl</code></p>
<dl>
<dt>
<dd> Prevent dumping of access privileges (grant/revoke commands).</dl>
<p> <code>&#8211;binary-upgrade</code></p>
<dl>
<dt>
<dd> This option is for use by in-place upgrade utilities. Its use for other purposes is not recommended or supported. The behavior of the option may change in future releases without notice.</dl>
<p> <code>&#8211;column-inserts</code>, <code>&#8211;attribute-inserts</code></p>
<dl>
<dt>
<dd> Dump data as <code>INSERT</code> commands with explicit column names (INSERT INTO <i>table</i> (<i>column</i>, &#8230;) VALUES &#8230;). This will make restoration very slow; it is mainly useful for making dumps that can be loaded into non-PostgreSQL databases.</dl>
<p> <code>&#8211;disable-dollar-quoting</code></p>
<dl>
<dt>
<dd> This option disables the use of dollar quoting for function bodies, and forces them to be quoted using SQL standard string syntax.</dl>
<p> <code>&#8211;disable-triggers</code></p>
<dl>
<dt>
<dd> This option is only relevant when creating a data-only dump. It instructs pg_dumpall to include commands to temporarily disable triggers on the target tables while the data is reloaded. Use this if you have referential integrity checks or other triggers on the tables that you do not want to invoke during data reload. </p>
<p> Presently, the commands emitted for <code>&#8211;disable-triggers</code> must be done as superuser. So, you should also specify a superuser name with <code>-S</code>, or preferably be careful to start the resulting script as a superuser.</dl>
<p> <code>&#8211;inserts</code></p>
<dl>
<dt>
<dd> Dump data as <code>INSERT</code> commands (rather than <code>COPY</code>). This will make restoration very slow; it is mainly useful for making dumps that can be loaded into non-PostgreSQL databases. Note that the restore might fail altogether if you have rearranged column order. The <code>&#8211;column-inserts</code> option is safer, though even slower.</dl>
<p> <code>&#8211;lock-wait-timeout=</code><i>timeout</i></p>
<dl>
<dt>
<dd> Do not wait forever to acquire shared table locks at the beginning of the dump. Instead, fail if unable to lock a table within the specified <i>timeout</i>. The timeout may be specified in any of the formats accepted by <code>SET statement_timeout</code>. Allowed values vary depending on the server version you are dumping from, but an integer number of milliseconds is accepted by all versions since 7.3. This option is ignored when dumping from a pre-7.3 server.</dl>
<p> <code>&#8211;no-security-labels</code></p>
<dl>
<dt>
<dd> Do not dump security labels.</dl>
<p> <code>&#8211;no-tablespaces</code></p>
<dl>
<dt>
<dd> Do not output commands to create tablespaces nor select tablespaces for objects. With this option, all objects will be created in whichever tablespace is the default during restore.</dl>
<p> <code>&#8211;no-unlogged-table-data</code></p>
<dl>
<dt>
<dd> Do not dump the contents of unlogged tables. This option has no effect on whether or not the table definitions (schema) are dumped; it only suppresses dumping the table data.</dl>
<p> <code>&#8211;quote-all-identifiers</code></p>
<dl>
<dt>
<dd> Force quoting of all identifiers. This option is recommended when dumping a database from a server whose PostgreSQL major version is different from pg_dumpall&#8217;s, or when the output is intended to be loaded into a server of a different major version. By default, pg_dumpall quotes only identifiers that are reserved words in its own major version. This sometimes results in compatibility issues when dealing with servers of other versions that may have slightly different sets of reserved words. Using <code>&#8211;quote-all-identifiers</code> prevents such issues, at the price of a harder-to-read dump script.</dl>
<p> <code>&#8211;use-set-session-authorization</code></p>
<dl>
<dt>
<dd> Output SQL-standard <code>SET SESSION AUTHORIZATION</code> commands instead of <code>ALTER OWNER</code> commands to determine object ownership. This makes the dump more standards compatible, but depending on the history of the objects in the dump, might not restore properly.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about pg_dumpall command line arguments, and exit.</dl>
<p> The following command-line options control the database connection parameters. </p>
<p> <code>-h </code><i>host</i>, <code>&#8211;host=</code><i>host</i></p>
<dl>
<dt>
<dd> Specifies the host name of the machine on which the database server is running. If the value begins with a slash, it is used as the directory for the Unix domain socket. The default is taken from the <code>PGHOST</code> environment variable, if set, else a Unix domain socket connection is attempted.</dl>
<p> <code>-l </code><i>dbname</i>, <code>&#8211;database=</code><i>dbname</i></p>
<dl>
<dt>
<dd> Specifies the name of the database to connect to to dump global objects and discover what other databases should be dumped. If not specified, the postgres database will be used, and if that does not exist, template1 will be used.</dl>
<p> <code>-p </code><i>port</i>, <code>&#8211;port=</code><i>port</i></p>
<dl>
<dt>
<dd> Specifies the TCP port or local Unix domain socket file extension on which the server is listening for connections. Defaults to the <code>PGPORT</code> environment variable, if set, or a compiled-in default.</dl>
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
<dd> Force pg_dumpall to prompt for a password before connecting to a database. </p>
<p> This option is never essential, since pg_dumpall will automatically prompt for a password if the server demands password authentication. However, pg_dumpall will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing <code>-W</code> to avoid the extra connection attempt. </p>
<p> Note that the password prompt will occur again for each database to be dumped. Usually, it&#8217;s better to set up a ~/.pgpass file than to rely on manual password entry.</dl>
<p> <code>&#8211;role=</code><i>rolename</i></p>
<dl>
<dt>
<dd> Specifies a role name to be used to create the dump. This option causes pg_dumpall to issue a <code>SET ROLE</code><i>rolename</i> command after connecting to the database. It is useful when the authenticated user (specified by <code>-U</code>) lacks privileges needed by pg_dumpall, but can switch to a role with the required rights. Some installations have a policy against logging in directly as a superuser, and use of this option allows dumps to be made without violating the policy.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>PGHOST</code>, <code>PGOPTIONS</code>, <code>PGPORT</code>, <code>PGUSER</code></p>
<dl>
<dt>
<dd> Default connection parameters</dl>
<p> This utility, like most other PostgreSQL utilities, also uses the environment variables supported by libpq (see Section 31.14, &#8220;Environment Variables&#8221;, in the documentation).</p>
<h2>NOTES</h2>
<p> Since pg_dumpall calls pg_dump internally, some diagnostic messages will refer to pg_dump. </p>
<p> Once restored, it is wise to run <code>ANALYZE</code> on each database so the optimizer has useful statistics. You can also run <code>vacuumdb -a -z</code> to analyze all databases. </p>
<p> pg_dumpall requires all needed tablespace directories to exist before the restore; otherwise, database creation will fail for databases in non-default locations.</p>
<h2>EXAMPLES</h2>
<p> To dump all databases: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>pg_dumpall &gt; db.out</code>
</pre>
</dl>
<p> To reload database(s) from this file, you can use: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>psql -f db.out postgres</code>
</pre>
</dl>
<p> (It is not important to which database you connect here since the script file created by pg_dumpall will contain the appropriate commands to create and connect to the saved databases.)</p>
<h2>SEE ALSO</h2>
<p> Check <code><a href="/docs/linux/man/1-pg_dump/">pg_dump</a></code>(1) for details on possible error conditions. </p>
<h2>Index</h2>
