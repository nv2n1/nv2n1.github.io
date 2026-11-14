---
title: "pg_restore(1)"
name: "pg_restore"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pg_restore/"
description: "pg_restore – restore a PostgreSQL database from an archive file created by pg_dump"
---

<h2 class="name">NAME</h2>
<p> pg_restore &#8211; restore a PostgreSQL database from an archive file created by pg_dump </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pg_restore</code> [<i>connection-option</i>&#8230;] [<i>option</i>&#8230;] [<i>filename</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>pg_restore is a utility for restoring a PostgreSQL database from an archive created by <code><a href="/docs/linux/man/1-pg_dump/">pg_dump</a></code>(1) in one of the non-plain-text formats. It will issue the commands necessary to reconstruct the database to the state it was in at the time it was saved. The archive files also allow pg_restore to be selective about what is restored, or even to reorder the items prior to being restored. The archive files are designed to be portable across architectures. </p>
<p> pg_restore can operate in two modes. If a database name is specified, pg_restore connects to that database and restores archive contents directly into the database. Otherwise, a script containing the SQL commands necessary to rebuild the database is created and written to a file or standard output. This script output is equivalent to the plain text output format of pg_dump. Some of the options controlling the output are therefore analogous to pg_dump options. </p>
<p> Obviously, pg_restore cannot restore information that is not present in the archive file. For instance, if the archive was made using the &#8220;dump data as <code>INSERT</code> commands&#8221; option, pg_restore will not be able to load the data using <code>COPY</code> statements.</p>
<h2>OPTIONS</h2>
<p> pg_restore accepts the following command line arguments. </p>
<p> <i>filename</i></p>
<dl>
<dt>
<dd> Specifies the location of the archive file (or directory, for a directory-format archive) to be restored. If not specified, the standard input is used.</dl>
<p> <code>-a</code>, <code>&#8211;data-only</code></p>
<dl>
<dt>
<dd> Restore only the data, not the schema (data definitions). Table data, large objects, and sequence values are restored, if present in the archive. </p>
<p> This option is similar to, but for historical reasons not identical to, specifying <code>&#8211;section=data</code>.</dl>
<p> <code>-c</code>, <code>&#8211;clean</code></p>
<dl>
<dt>
<dd> Clean (drop) database objects before recreating them. (This might generate some harmless error messages, if any objects were not present in the destination database.)</dl>
<p> <code>-C</code>, <code>&#8211;create</code></p>
<dl>
<dt>
<dd> Create the database before restoring into it. If <code>&#8211;clean</code> is also specified, drop and recreate the target database before connecting to it. </p>
<p> When this option is used, the database named with <code>-d</code> is used only to issue the initial <code>DROP DATABASE</code> and <code>CREATE DATABASE</code> commands. All data is restored into the database name that appears in the archive.</dl>
<p> <code>-d </code><i>dbname</i>, <code>&#8211;dbname=</code><i>dbname</i></p>
<dl>
<dt>
<dd> Connect to database <i>dbname</i> and restore directly into the database.</dl>
<p> <code>-e</code>, <code>&#8211;exit-on-error</code></p>
<dl>
<dt>
<dd> Exit if an error is encountered while sending SQL commands to the database. The default is to continue and to display a count of errors at the end of the restoration.</dl>
<p> <code>-f </code><i>filename</i>, <code>&#8211;file=</code><i>filename</i></p>
<dl>
<dt>
<dd> Specify output file for generated script, or for the listing when used with <code>-l</code>. Default is the standard output.</dl>
<p> <code>-F </code><i>format</i>, <code>&#8211;format=</code><i>format</i></p>
<dl>
<dt>
<dd> Specify format of the archive. It is not necessary to specify the format, since pg_restore will determine the format automatically. If specified, it can be one of the following: </p>
<p> c, custom</p>
<dl>
<dt>
<dd> The archive is in the custom format of pg_dump.</dl>
<p> d, directory</p>
<dl>
<dt>
<dd> The archive is a directory archive.</dl>
<p> t, tar</p>
<dl>
<dt>
<dd> The archive is a <code>tar</code> archive.</dl>
</dl>
<p> <code>-i</code>, <code>&#8211;ignore-version</code></p>
<dl>
<dt>
<dd> A deprecated option that is now ignored.</dl>
<p> <code>-I </code><i>index</i>, <code>&#8211;index=</code><i>index</i></p>
<dl>
<dt>
<dd> Restore definition of named index only.</dl>
<p> <code>-j </code><i>number-of-jobs</i>, <code>&#8211;jobs=</code><i>number-of-jobs</i></p>
<dl>
<dt>
<dd> Run the most time-consuming parts of pg_restore &#8212; those which load data, create indexes, or create constraints &#8212; using multiple concurrent jobs. This option can dramatically reduce the time to restore a large database to a server running on a multiprocessor machine. </p>
<p> Each job is one process or one thread, depending on the operating system, and uses a separate connection to the server. </p>
<p> The optimal value for this option depends on the hardware setup of the server, of the client, and of the network. Factors include the number of CPU cores and the disk setup. A good place to start is the number of CPU cores on the server, but values larger than that can also lead to faster restore times in many cases. Of course, values that are too high will lead to decreased performance because of thrashing. </p>
<p> Only the custom archive format is supported with this option. The input file must be a regular file (not, for example, a pipe). This option is ignored when emitting a script rather than connecting directly to a database server. Also, multiple jobs cannot be used together with the option <code>&#8211;single-transaction</code>.</dl>
<p> <code>-l</code>, <code>&#8211;list</code></p>
<dl>
<dt>
<dd> List the contents of the archive. The output of this operation can be used as input to the <code>-L</code> option. Note that if filtering switches such as <code>-n</code> or <code>-t</code> are used with <code>-l</code>, they will restrict the items listed.</dl>
<p> <code>-L </code><i>list-file</i>, <code>&#8211;use-list=</code><i>list-file</i></p>
<dl>
<dt>
<dd> Restore only those archive elements that are listed in <i>list-file</i>, and restore them in the order they appear in the file. Note that if filtering switches such as <code>-n</code> or <code>-t</code> are used with <code>-L</code>, they will further restrict the items restored. </p>
<p> <i>list-file</i> is normally created by editing the output of a previous <code>-l</code> operation. Lines can be moved or removed, and can also be commented out by placing a semicolon (;) at the start of the line. See below for examples.</dl>
<p> <code>-n </code><i>namespace</i>, <code>&#8211;schema=</code><i>schema</i></p>
<dl>
<dt>
<dd> Restore only objects that are in the named schema. This can be combined with the <code>-t</code> option to restore just a specific table.</dl>
<p> <code>-O</code>, <code>&#8211;no-owner</code></p>
<dl>
<dt>
<dd> Do not output commands to set ownership of objects to match the original database. By default, pg_restore issues <code>ALTER OWNER</code> or <code>SET SESSION AUTHORIZATION</code> statements to set ownership of created schema elements. These statements will fail unless the initial connection to the database is made by a superuser (or the same user that owns all of the objects in the script). With <code>-O</code>, any user name can be used for the initial connection, and this user will own all the created objects.</dl>
<p> <code>-P </code><i>function-name(argtype [, &#8230;])</i>, <code>&#8211;function=</code><i>function-name(argtype [, &#8230;])</i></p>
<dl>
<dt>
<dd> Restore the named function only. Be careful to spell the function name and arguments exactly as they appear in the dump file&#8217;s table of contents.</dl>
<p> <code>-R</code>, <code>&#8211;no-reconnect</code></p>
<dl>
<dt>
<dd> This option is obsolete but still accepted for backwards compatibility.</dl>
<p> <code>-s</code>, <code>&#8211;schema-only</code></p>
<dl>
<dt>
<dd> Restore only the schema (data definitions), not data, to the extent that schema entries are present in the archive. </p>
<p> This option is the inverse of <code>&#8211;data-only</code>. It is similar to, but for historical reasons not identical to, specifying <code>&#8211;section=pre-data &#8211;section=post-data</code>. </p>
<p> (Do not confuse this with the <code>&#8211;schema</code> option, which uses the word &#8220;schema&#8221; in a different meaning.)</dl>
<p> <code>-S </code><i>username</i>, <code>&#8211;superuser=</code><i>username</i></p>
<dl>
<dt>
<dd> Specify the superuser user name to use when disabling triggers. This is only relevant if <code>&#8211;disable-triggers</code> is used.</dl>
<p> <code>-t </code><i>table</i>, <code>&#8211;table=</code><i>table</i></p>
<dl>
<dt>
<dd> Restore definition and/or data of named table only. This can be combined with the <code>-n</code> option to specify a schema.</dl>
<p> <code>-T </code><i>trigger</i>, <code>&#8211;trigger=</code><i>trigger</i></p>
<dl>
<dt>
<dd> Restore named trigger only.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Specifies verbose mode.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the pg_restore version and exit.</dl>
<p> <code>-x</code>, <code>&#8211;no-privileges</code>, <code>&#8211;no-acl</code></p>
<dl>
<dt>
<dd> Prevent restoration of access privileges (grant/revoke commands).</dl>
<p> <code>-1</code>, <code>&#8211;single-transaction</code></p>
<dl>
<dt>
<dd> Execute the restore as a single transaction (that is, wrap the emitted commands in <code>BEGIN</code>/<code>COMMIT</code>). This ensures that either all the commands complete successfully, or no changes are applied. This option implies <code>&#8211;exit-on-error</code>.</dl>
<p> <code>&#8211;disable-triggers</code></p>
<dl>
<dt>
<dd> This option is only relevant when performing a data-only restore. It instructs pg_restore to execute commands to temporarily disable triggers on the target tables while the data is reloaded. Use this if you have referential integrity checks or other triggers on the tables that you do not want to invoke during data reload. </p>
<p> Presently, the commands emitted for <code>&#8211;disable-triggers</code> must be done as superuser. So, you should also specify a superuser name with <code>-S</code>, or preferably run pg_restore as a PostgreSQL superuser.</dl>
<p> <code>&#8211;no-data-for-failed-tables</code></p>
<dl>
<dt>
<dd> By default, table data is restored even if the creation command for the table failed (e.g., because it already exists). With this option, data for such a table is skipped. This behavior is useful if the target database already contains the desired table contents. For example, auxiliary tables for PostgreSQL extensions such as PostGIS might already be loaded in the target database; specifying this option prevents duplicate or obsolete data from being loaded into them. </p>
<p> This option is effective only when restoring directly into a database, not when producing SQL script output.</dl>
<p> <code>&#8211;no-security-labels</code></p>
<dl>
<dt>
<dd> Do not output commands to restore security labels, even if the archive contains them.</dl>
<p> <code>&#8211;no-tablespaces</code></p>
<dl>
<dt>
<dd> Do not output commands to select tablespaces. With this option, all objects will be created in whichever tablespace is the default during restore.</dl>
<p> <code>&#8211;section=</code><i>sectionname</i></p>
<dl>
<dt>
<dd> Only restore the named section. The section name can be <code>pre-data</code>, <code>data</code>, or <code>post-data</code>. This option can be specified more than once to select multiple sections. The default is to restore all sections. </p>
<p> The data section contains actual table data as well as large-object definitions. Post-data items consist of definitions of indexes, triggers, rules and constraints other than validated check constraints. Pre-data items consist of all other data definition items.</dl>
<p> <code>&#8211;use-set-session-authorization</code></p>
<dl>
<dt>
<dd> Output SQL-standard <code>SET SESSION AUTHORIZATION</code> commands instead of <code>ALTER OWNER</code> commands to determine object ownership. This makes the dump more standards-compatible, but depending on the history of the objects in the dump, might not restore properly.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about pg_restore command line arguments, and exit.</dl>
<p> pg_restore also accepts the following command line arguments for connection parameters: </p>
<p> <code>-h </code><i>host</i>, <code>&#8211;host=</code><i>host</i></p>
<dl>
<dt>
<dd> Specifies the host name of the machine on which the server is running. If the value begins with a slash, it is used as the directory for the Unix domain socket. The default is taken from the <code>PGHOST</code> environment variable, if set, else a Unix domain socket connection is attempted.</dl>
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
<dd> Force pg_restore to prompt for a password before connecting to a database. </p>
<p> This option is never essential, since pg_restore will automatically prompt for a password if the server demands password authentication. However, pg_restore will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing <code>-W</code> to avoid the extra connection attempt.</dl>
<p> <code>&#8211;role=</code><i>rolename</i></p>
<dl>
<dt>
<dd> Specifies a role name to be used to perform the restore. This option causes pg_restore to issue a <code>SET ROLE</code><i>rolename</i> command after connecting to the database. It is useful when the authenticated user (specified by <code>-U</code>) lacks privileges needed by pg_restore, but can switch to a role with the required rights. Some installations have a policy against logging in directly as a superuser, and use of this option allows restores to be performed without violating the policy.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>PGHOST</code>, <code>PGOPTIONS</code>, <code>PGPORT</code>, <code>PGUSER</code></p>
<dl>
<dt>
<dd> Default connection parameters</dl>
<p> This utility, like most other PostgreSQL utilities, also uses the environment variables supported by libpq (see Section 31.14, &#8220;Environment Variables&#8221;, in the documentation).</p>
<h2>DIAGNOSTICS</h2>
<p> When a direct database connection is specified using the <code>-d</code> option, pg_restore internally executes SQL statements. If you have problems running pg_restore, make sure you are able to select information from the database using, for example, <code><a href="/docs/linux/man/1-psql/">psql</a></code>(1). Also, any default connection settings and environment variables used by the libpq front-end library will apply.</p>
<h2>NOTES</h2>
<p> If your installation has any local additions to the template1 database, be careful to load the output of pg_restore into a truly empty database; otherwise you are likely to get errors due to duplicate definitions of the added objects. To make an empty database without any local additions, copy from template0 not template1, for example: </p>
<dl>
<dt>
<dd>
<pre>
CREATE DATABASE foo WITH TEMPLATE template0;
</pre>
</dl>
<p> The limitations of pg_restore are detailed below. </p>
<dl>
<dt>
<dd> &bull; When restoring data to a pre-existing table and the option <code>&#8211;disable-triggers</code> is used, pg_restore emits commands to disable triggers on user tables before inserting the data, then emits commands to re-enable them after the data has been inserted. If the restore is stopped in the middle, the system catalogs might be left in the wrong state.</dl>
<dl>
<dt>
<dd> &bull; pg_restore cannot restore large objects selectively; for instance, only those for a specific table. If an archive contains large objects, then all large objects will be restored, or none of them if they are excluded via <code>-L</code>, <code>-t</code>, or other options.</dl>
<p> See also the <code><a href="/docs/linux/man/1-pg_dump/">pg_dump</a></code>(1) documentation for details on limitations of pg_dump. </p>
<p> Once restored, it is wise to run <code>ANALYZE</code> on each restored table so the optimizer has useful statistics; see Section 23.1.3, &#8220;Updating Planner Statistics&#8221;, in the documentation and Section 23.1.6, &#8220;The Autovacuum Daemon&#8221;, in the documentation for more information.</p>
<h2>EXAMPLES</h2>
<p> Assume we have dumped a database called mydb into a custom-format dump file: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>pg_dump -Fc mydb &gt; db.dump</code>
</pre>
</dl>
<p> To drop the database and recreate it from the dump: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>dropdb mydb</code>
$ <code>pg_restore -C -d postgres db.dump</code>
</pre>
</dl>
<p> The database named in the <code>-d</code> switch can be any database existing in the cluster; pg_restore only uses it to issue the <code>CREATE DATABASE</code> command for mydb. With <code>-C</code>, data is always restored into the database name that appears in the dump file. </p>
<p> To reload the dump into a new database called newdb: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>createdb -T template0 newdb</code>
$ <code>pg_restore -d newdb db.dump</code>
</pre>
</dl>
<p> Notice we don&#8217;t use <code>-C</code>, and instead connect directly to the database to be restored into. Also note that we clone the new database from template0 not template1, to ensure it is initially empty. </p>
<p> To reorder database items, it is first necessary to dump the table of contents of the archive: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>pg_restore -l db.dump &gt; db.list</code>
</pre>
</dl>
<p> The listing file consists of a header and one line for each item, e.g.: </p>
<dl>
<dt>
<dd>
<pre><code>
;
;
Archive created at Mon Sep 14 13 : 55 : 39 2009;
dbname : DBDEMOS;
TOC Entries : 81;
Compression : 9;
Dump Version : 1.10 - 0;
Format : CUSTOM;
Integer : 4 bytes;
Offset : 8 bytes;
Dumped from database version : 8.3.5;
Dumped by pg_dump version : 8.3.8;
;
;
Selected TOC Entries:;
3;
2615 2200 SCHEMA - public pasha 1861;
0 0 COMMENT - SCHEMA public pasha 1862;
0 0 ACL - public pasha 317;
1247 17715 TYPE public composite pasha 319;
1247 25899 DOMAIN public domain0 pasha
</code></pre>
</dl>
<p> Semicolons start a comment, and the numbers at the start of lines refer to the internal archive ID assigned to each item. </p>
<p> Lines in the file can be commented out, deleted, and reordered. For example: </p>
<dl>
<dt>
<dd>
<pre><code>
10;
145433 TABLE map_resolutions postgres;
2;
145344 TABLE species postgres;
4;
145359 TABLE nt_header postgres 6;
145402 TABLE species_records postgres;
8;
145416 TABLE ss_old postgres
</code></pre>
</dl>
<p> could be used as input to pg_restore and would only restore items 10 and 6, in that order: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>pg_restore -L db.list db.dump</code>
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pg_dump/">pg_dump</a></code>(1), <code><a href="/docs/linux/man/1-pg_dumpall/">pg_dumpall</a></code>(1), <code><a href="/docs/linux/man/1-psql/">psql</a></code>(1) </p>
<h2>Index</h2>
