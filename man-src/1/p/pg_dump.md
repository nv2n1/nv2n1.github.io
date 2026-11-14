---
title: "pg_dump(1)"
name: "pg_dump"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pg_dump/"
description: "pg_dump – extract a PostgreSQL database into a script file or other archive file"
---

<h2 class="name">NAME</h2>
<p> pg_dump &#8211; extract a PostgreSQL database into a script file or other archive file </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pg_dump</code> [<i>connection-option</i>&#8230;] [<i>option</i>&#8230;] [<i>dbname</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>pg_dump is a utility for backing up a PostgreSQL database. It makes consistent backups even if the database is being used concurrently. pg_dump does not block other users accessing the database (readers or writers). </p>
<p> Dumps can be output in script or archive file formats. Script dumps are plain-text files containing the SQL commands required to reconstruct the database to the state it was in at the time it was saved. To restore from such a script, feed it to <code><a href="/docs/linux/man/1-psql/">psql</a></code>(1). Script files can be used to reconstruct the database even on other machines and other architectures; with some modifications, even on other SQL database products. </p>
<p> The alternative archive file formats must be used with <code><a href="/docs/linux/man/1-pg_restore/">pg_restore</a></code>(1) to rebuild the database. They allow pg_restore to be selective about what is restored, or even to reorder the items prior to being restored. The archive file formats are designed to be portable across architectures. </p>
<p> When used with one of the archive file formats and combined with pg_restore, pg_dump provides a flexible archival and transfer mechanism. pg_dump can be used to backup an entire database, then pg_restore can be used to examine the archive and/or select which parts of the database are to be restored. The most flexible output file format is the &#8220;custom&#8221; format (<code>-Fc</code>). It allows for selection and reordering of all archived items, and is compressed by default. </p>
<p> While running pg_dump, one should examine the output for any warnings (printed on standard error), especially in light of the limitations listed below.</p>
<h2>OPTIONS</h2>
<p> The following command-line options control the content and format of the output. </p>
<p> <i>dbname</i></p>
<dl>
<dt>
<dd> Specifies the name of the database to be dumped. If this is not specified, the environment variable <code>PGDATABASE</code> is used. If that is not set, the user name specified for the connection is used.</dl>
<p> <code>-a</code>, <code>&#8211;data-only</code></p>
<dl>
<dt>
<dd> Dump only the data, not the schema (data definitions). Table data, large objects, and sequence values are dumped. </p>
<p> This option is similar to, but for historical reasons not identical to, specifying <code>&#8211;section=data</code>.</dl>
<p> <code>-b</code>, <code>&#8211;blobs</code></p>
<dl>
<dt>
<dd> Include large objects in the dump. This is the default behavior except when <code>&#8211;schema</code>, <code>&#8211;table</code>, or <code>&#8211;schema-only</code> is specified, so the <code>-b</code> switch is only useful to add large objects to selective dumps.</dl>
<p> <code>-c</code>, <code>&#8211;clean</code></p>
<dl>
<dt>
<dd> Output commands to clean (drop) database objects prior to outputting the commands for creating them. (Restore might generate some harmless error messages, if any objects were not present in the destination database.) </p>
<p> This option is only meaningful for the plain-text format. For the archive formats, you can specify the option when you call <code>pg_restore</code>.</dl>
<p> <code>-C</code>, <code>&#8211;create</code></p>
<dl>
<dt>
<dd> Begin the output with a command to create the database itself and reconnect to the created database. (With a script of this form, it doesn&#8217;t matter which database in the destination installation you connect to before running the script.) If <code>&#8211;clean</code> is also specified, the script drops and recreates the target database before reconnecting to it. </p>
<p> This option is only meaningful for the plain-text format. For the archive formats, you can specify the option when you call <code>pg_restore</code>.</dl>
<p> <code>-E </code><i>encoding</i>, <code>&#8211;encoding=</code><i>encoding</i></p>
<dl>
<dt>
<dd> Create the dump in the specified character set encoding. By default, the dump is created in the database encoding. (Another way to get the same result is to set the <code>PGCLIENTENCODING</code> environment variable to the desired dump encoding.)</dl>
<p> <code>-f </code><i>file</i>, <code>&#8211;file=</code><i>file</i></p>
<dl>
<dt>
<dd> Send output to the specified file. This parameter can be omitted for file based output formats, in which case the standard output is used. It must be given for the directory output format however, where it specifies the target directory instead of a file. In this case the directory is created by <code>pg_dump</code> and must not exist before.</dl>
<p> <code>-F </code><i>format</i>, <code>&#8211;format=</code><i>format</i></p>
<dl>
<dt>
<dd> Selects the format of the output. <i>format</i> can be one of the following: </p>
<p> p, plain</p>
<dl>
<dt>
<dd> Output a plain-text SQL script file (the default).</dl>
<p> c, custom</p>
<dl>
<dt>
<dd> Output a custom-format archive suitable for input into pg_restore. Together with the directory output format, this is the most flexible output format in that it allows manual selection and reordering of archived items during restore. This format is also compressed by default.</dl>
<p> d, directory</p>
<dl>
<dt>
<dd> Output a directory-format archive suitable for input into pg_restore. This will create a directory with one file for each table and blob being dumped, plus a so-called Table of Contents file describing the dumped objects in a machine-readable format that pg_restore can read. A directory format archive can be manipulated with standard Unix tools; for example, files in an uncompressed archive can be compressed with the gzip tool. This format is compressed by default.</dl>
<p> t, tar</p>
<dl>
<dt>
<dd> Output a <code>tar</code>-format archive suitable for input into pg_restore. The tar format is compatible with the directory format: extracting a tar-format archive produces a valid directory-format archive. However, the tar format does not support compression. Also, when using tar format the relative order of table data items cannot be changed during restore.</dl>
</dl>
<p> <code>-i</code>, <code>&#8211;ignore-version</code></p>
<dl>
<dt>
<dd> A deprecated option that is now ignored.</dl>
<p> <code>-n </code><i>schema</i>, <code>&#8211;schema=</code><i>schema</i></p>
<dl>
<dt>
<dd> Dump only schemas matching <i>schema</i>; this selects both the schema itself, and all its contained objects. When this option is not specified, all non-system schemas in the target database will be dumped. Multiple schemas can be selected by writing multiple <code>-n</code> switches. Also, the <i>schema</i> parameter is interpreted as a pattern according to the same rules used by psql&#8217;s \d commands (see Patterns), so multiple schemas can also be selected by writing wildcard characters in the pattern. When using wildcards, be careful to quote the pattern if needed to prevent the shell from expanding the wildcards; see EXAMPLES. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 When <code>-n</code> is specified, pg_dump makes no attempt to dump any other database objects that the selected schema(s) might depend upon. Therefore, there is no guarantee that the results of a specific-schema dump can be successfully restored by themselves into a clean database. </p>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 Non-schema objects such as blobs are not dumped when <code>-n</code> is specified. You can add blobs back to the dump with the <code>&#8211;blobs</code> switch. </p>
</dl>
</dl>
<p> <code>-N </code><i>schema</i>, <code>&#8211;exclude-schema=</code><i>schema</i></p>
<dl>
<dt>
<dd> Do not dump any schemas matching the <i>schema</i> pattern. The pattern is interpreted according to the same rules as for <code>-n</code>. <code>-N</code> can be given more than once to exclude schemas matching any of several patterns. </p>
<p> When both <code>-n</code> and <code>-N</code> are given, the behavior is to dump just the schemas that match at least one <code>-n</code> switch but no <code>-N</code> switches. If <code>-N</code> appears without <code>-n</code>, then schemas matching <code>-N</code> are excluded from what is otherwise a normal dump.</dl>
<p> <code>-o</code>, <code>&#8211;oids</code></p>
<dl>
<dt>
<dd> Dump object identifiers (OIDs) as part of the data for every table. Use this option if your application references the OID columns in some way (e.g., in a foreign key constraint). Otherwise, this option should not be used.</dl>
<p> <code>-O</code>, <code>&#8211;no-owner</code></p>
<dl>
<dt>
<dd> Do not output commands to set ownership of objects to match the original database. By default, pg_dump issues <code>ALTER OWNER</code> or <code>SET SESSION AUTHORIZATION</code> statements to set ownership of created database objects. These statements will fail when the script is run unless it is started by a superuser (or the same user that owns all of the objects in the script). To make a script that can be restored by any user, but will give that user ownership of all the objects, specify <code>-O</code>. </p>
<p> This option is only meaningful for the plain-text format. For the archive formats, you can specify the option when you call <code>pg_restore</code>.</dl>
<p> <code>-R</code>, <code>&#8211;no-reconnect</code></p>
<dl>
<dt>
<dd> This option is obsolete but still accepted for backwards compatibility.</dl>
<p> <code>-s</code>, <code>&#8211;schema-only</code></p>
<dl>
<dt>
<dd> Dump only the object definitions (schema), not data. </p>
<p> This option is the inverse of <code>&#8211;data-only</code>. It is similar to, but for historical reasons not identical to, specifying <code>&#8211;section=pre-data &#8211;section=post-data</code>. </p>
<p> (Do not confuse this with the <code>&#8211;schema</code> option, which uses the word &#8220;schema&#8221; in a different meaning.) </p>
<p> To exclude table data for only a subset of tables in the database, see <code>&#8211;exclude-table-data</code>.</dl>
<p> <code>-S </code><i>username</i>, <code>&#8211;superuser=</code><i>username</i></p>
<dl>
<dt>
<dd> Specify the superuser user name to use when disabling triggers. This is only relevant if <code>&#8211;disable-triggers</code> is used. (Usually, it&#8217;s better to leave this out, and instead start the resulting script as superuser.)</dl>
<p> <code>-t </code><i>table</i>, <code>&#8211;table=</code><i>table</i></p>
<dl>
<dt>
<dd> Dump only tables (or views or sequences or foreign tables) matching <i>table</i>. Multiple tables can be selected by writing multiple <code>-t</code> switches. Also, the <i>table</i> parameter is interpreted as a pattern according to the same rules used by psql&#8217;s \d commands (see Patterns), so multiple tables can also be selected by writing wildcard characters in the pattern. When using wildcards, be careful to quote the pattern if needed to prevent the shell from expanding the wildcards; see EXAMPLES. </p>
<p> The <code>-n</code> and <code>-N</code> switches have no effect when <code>-t</code> is used, because tables selected by <code>-t</code> will be dumped regardless of those switches, and non-table objects will not be dumped. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 When <code>-t</code> is specified, pg_dump makes no attempt to dump any other database objects that the selected table(s) might depend upon. Therefore, there is no guarantee that the results of a specific-table dump can be successfully restored by themselves into a clean database. </p>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 The behavior of the <code>-t</code> switch is not entirely upward compatible with pre-8.2 PostgreSQL versions. Formerly, writing -t tab would dump all tables named tab, but now it just dumps whichever one is visible in your default search path. To get the old behavior you can write -t &#8216;*.tab&#8217;. Also, you must write something like -t sch.tab to select a table in a particular schema, rather than the old locution of -n sch -t tab. </p>
</dl>
</dl>
<p> <code>-T </code><i>table</i>, <code>&#8211;exclude-table=</code><i>table</i></p>
<dl>
<dt>
<dd> Do not dump any tables matching the <i>table</i> pattern. The pattern is interpreted according to the same rules as for <code>-t</code>. <code>-T</code> can be given more than once to exclude tables matching any of several patterns. </p>
<p> When both <code>-t</code> and <code>-T</code> are given, the behavior is to dump just the tables that match at least one <code>-t</code> switch but no <code>-T</code> switches. If <code>-T</code> appears without <code>-t</code>, then tables matching <code>-T</code> are excluded from what is otherwise a normal dump.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Specifies verbose mode. This will cause pg_dump to output detailed object comments and start/stop times to the dump file, and progress messages to standard error.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the pg_dump version and exit.</dl>
<p> <code>-x</code>, <code>&#8211;no-privileges</code>, <code>&#8211;no-acl</code></p>
<dl>
<dt>
<dd> Prevent dumping of access privileges (grant/revoke commands).</dl>
<p> <code>-Z </code><i>0..9</i>, <code>&#8211;compress=</code><i>0..9</i></p>
<dl>
<dt>
<dd> Specify the compression level to use. Zero means no compression. For the custom archive format, this specifies compression of individual table-data segments, and the default is to compress at a moderate level. For plain text output, setting a nonzero compression level causes the entire output file to be compressed, as though it had been fed through gzip; but the default is not to compress. The tar archive format currently does not support compression at all.</dl>
<p> <code>&#8211;binary-upgrade</code></p>
<dl>
<dt>
<dd> This option is for use by in-place upgrade utilities. Its use for other purposes is not recommended or supported. The behavior of the option may change in future releases without notice.</dl>
<p> <code>&#8211;column-inserts</code>, <code>&#8211;attribute-inserts</code></p>
<dl>
<dt>
<dd> Dump data as <code>INSERT</code> commands with explicit column names (INSERT INTO <i>table</i> (<i>column</i>, &#8230;) VALUES &#8230;). This will make restoration very slow; it is mainly useful for making dumps that can be loaded into non-PostgreSQL databases. However, since this option generates a separate command for each row, an error in reloading a row causes only that row to be lost rather than the entire table contents.</dl>
<p> <code>&#8211;disable-dollar-quoting</code></p>
<dl>
<dt>
<dd> This option disables the use of dollar quoting for function bodies, and forces them to be quoted using SQL standard string syntax.</dl>
<p> <code>&#8211;disable-triggers</code></p>
<dl>
<dt>
<dd> This option is only relevant when creating a data-only dump. It instructs pg_dump to include commands to temporarily disable triggers on the target tables while the data is reloaded. Use this if you have referential integrity checks or other triggers on the tables that you do not want to invoke during data reload. </p>
<p> Presently, the commands emitted for <code>&#8211;disable-triggers</code> must be done as superuser. So, you should also specify a superuser name with <code>-S</code>, or preferably be careful to start the resulting script as a superuser. </p>
<p> This option is only meaningful for the plain-text format. For the archive formats, you can specify the option when you call <code>pg_restore</code>.</dl>
<p> <code>&#8211;exclude-table-data=</code><i>table</i></p>
<dl>
<dt>
<dd> Do not dump data for any tables matching the <i>table</i> pattern. The pattern is interpreted according to the same rules as for <code>-t</code>. <code>&#8211;exclude-table-data</code> can be given more than once to exclude tables matching any of several patterns. This option is useful when you need the definition of a particular table even though you do not need the data in it. </p>
<p> To exclude data for all tables in the database, see <code>&#8211;schema-only</code>.</dl>
<p> <code>&#8211;inserts</code></p>
<dl>
<dt>
<dd> Dump data as <code>INSERT</code> commands (rather than <code>COPY</code>). This will make restoration very slow; it is mainly useful for making dumps that can be loaded into non-PostgreSQL databases. However, since this option generates a separate command for each row, an error in reloading a row causes only that row to be lost rather than the entire table contents. Note that the restore might fail altogether if you have rearranged column order. The <code>&#8211;column-inserts</code> option is safe against column order changes, though even slower.</dl>
<p> <code>&#8211;lock-wait-timeout=</code><i>timeout</i></p>
<dl>
<dt>
<dd> Do not wait forever to acquire shared table locks at the beginning of the dump. Instead fail if unable to lock a table within the specified <i>timeout</i>. The timeout may be specified in any of the formats accepted by <code>SET statement_timeout</code>. (Allowed values vary depending on the server version you are dumping from, but an integer number of milliseconds is accepted by all versions since 7.3. This option is ignored when dumping from a pre-7.3 server.)</dl>
<p> <code>&#8211;no-security-labels</code></p>
<dl>
<dt>
<dd> Do not dump security labels.</dl>
<p> <code>&#8211;no-tablespaces</code></p>
<dl>
<dt>
<dd> Do not output commands to select tablespaces. With this option, all objects will be created in whichever tablespace is the default during restore. </p>
<p> This option is only meaningful for the plain-text format. For the archive formats, you can specify the option when you call <code>pg_restore</code>.</dl>
<p> <code>&#8211;no-unlogged-table-data</code></p>
<dl>
<dt>
<dd> Do not dump the contents of unlogged tables. This option has no effect on whether or not the table definitions (schema) are dumped; it only suppresses dumping the table data. Data in unlogged tables is always excluded when dumping from a standby server.</dl>
<p> <code>&#8211;quote-all-identifiers</code></p>
<dl>
<dt>
<dd> Force quoting of all identifiers. This option is recommended when dumping a database from a server whose PostgreSQL major version is different from pg_dump&#8217;s, or when the output is intended to be loaded into a server of a different major version. By default, pg_dump quotes only identifiers that are reserved words in its own major version. This sometimes results in compatibility issues when dealing with servers of other versions that may have slightly different sets of reserved words. Using <code>&#8211;quote-all-identifiers</code> prevents such issues, at the price of a harder-to-read dump script.</dl>
<p> <code>&#8211;section=</code><i>sectionname</i></p>
<dl>
<dt>
<dd> Only dump the named section. The section name can be <code>pre-data</code>, <code>data</code>, or <code>post-data</code>. This option can be specified more than once to select multiple sections. The default is to dump all sections. </p>
<p> The data section contains actual table data, large-object contents, and sequence values. Post-data items include definitions of indexes, triggers, rules, and constraints other than validated check constraints. Pre-data items include all other data definition items.</dl>
<p> <code>&#8211;serializable-deferrable</code></p>
<dl>
<dt>
<dd> Use a serializable transaction for the dump, to ensure that the snapshot used is consistent with later database states; but do this by waiting for a point in the transaction stream at which no anomalies can be present, so that there isn&#8217;t a risk of the dump failing or causing other transactions to roll back with a serialization_failure. See Chapter 13, Concurrency Control, in the documentation for more information about transaction isolation and concurrency control. </p>
<p> This option is not beneficial for a dump which is intended only for disaster recovery. It could be useful for a dump used to load a copy of the database for reporting or other read-only load sharing while the original database continues to be updated. Without it the dump may reflect a state which is not consistent with any serial execution of the transactions eventually committed. For example, if batch processing techniques are used, a batch may show as closed in the dump without all of the items which are in the batch appearing. </p>
<p> This option will make no difference if there are no read-write transactions active when pg_dump is started. If read-write transactions are active, the start of the dump may be delayed for an indeterminate length of time. Once running, performance with or without the switch is the same.</dl>
<p> <code>&#8211;use-set-session-authorization</code></p>
<dl>
<dt>
<dd> Output SQL-standard <code>SET SESSION AUTHORIZATION</code> commands instead of <code>ALTER OWNER</code> commands to determine object ownership. This makes the dump more standards-compatible, but depending on the history of the objects in the dump, might not restore properly. Also, a dump using <code>SET SESSION AUTHORIZATION</code> will certainly require superuser privileges to restore correctly, whereas <code>ALTER OWNER</code> requires lesser privileges.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about pg_dump command line arguments, and exit.</dl>
<p> The following command-line options control the database connection parameters. </p>
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
<dd> Force pg_dump to prompt for a password before connecting to a database. </p>
<p> This option is never essential, since pg_dump will automatically prompt for a password if the server demands password authentication. However, pg_dump will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing <code>-W</code> to avoid the extra connection attempt.</dl>
<p> <code>&#8211;role=</code><i>rolename</i></p>
<dl>
<dt>
<dd> Specifies a role name to be used to create the dump. This option causes pg_dump to issue a <code>SET ROLE</code><i>rolename</i> command after connecting to the database. It is useful when the authenticated user (specified by <code>-U</code>) lacks privileges needed by pg_dump, but can switch to a role with the required rights. Some installations have a policy against logging in directly as a superuser, and use of this option allows dumps to be made without violating the policy.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>PGDATABASE</code>, <code>PGHOST</code>, <code>PGOPTIONS</code>, <code>PGPORT</code>, <code>PGUSER</code></p>
<dl>
<dt>
<dd> Default connection parameters.</dl>
<p> This utility, like most other PostgreSQL utilities, also uses the environment variables supported by libpq (see Section 31.14, &#8220;Environment Variables&#8221;, in the documentation).</p>
<h2>DIAGNOSTICS</h2>
<p> pg_dump internally executes <code>SELECT</code> statements. If you have problems running pg_dump, make sure you are able to select information from the database using, for example, <code><a href="/docs/linux/man/1-psql/">psql</a></code>(1). Also, any default connection settings and environment variables used by the libpq front-end library will apply. </p>
<p> The database activity of pg_dump is normally collected by the statistics collector. If this is undesirable, you can set parameter <i>track_counts</i> to false via <code>PGOPTIONS</code> or the ALTER USER command.</p>
<h2>NOTES</h2>
<p> If your database cluster has any local additions to the template1 database, be careful to restore the output of pg_dump into a truly empty database; otherwise you are likely to get errors due to duplicate definitions of the added objects. To make an empty database without any local additions, copy from template0 not template1, for example: </p>
<dl>
<dt>
<dd>
<pre>
CREATE DATABASE foo WITH TEMPLATE template0;
</pre>
</dl>
<p> When a data-only dump is chosen and the option <code>&#8211;disable-triggers</code> is used, pg_dump emits commands to disable triggers on user tables before inserting the data, and then commands to re-enable them after the data has been inserted. If the restore is stopped in the middle, the system catalogs might be left in the wrong state. </p>
<p> The dump file produced by pg_dump does not contain the statistics used by the optimizer to make query planning decisions. Therefore, it is wise to run <code>ANALYZE</code> after restoring from a dump file to ensure optimal performance; see Section 23.1.3, &#8220;Updating Planner Statistics&#8221;, in the documentation and Section 23.1.6, &#8220;The Autovacuum Daemon&#8221;, in the documentation for more information. The dump file also does not contain any <code>ALTER DATABASE &#8230; SET</code> commands; these settings are dumped by <code><a href="/docs/linux/man/1-pg_dumpall/">pg_dumpall</a></code>(1), along with database users and other installation-wide settings. </p>
<p> Because pg_dump is used to transfer data to newer versions of PostgreSQL, the output of pg_dump can be expected to load into PostgreSQL server versions newer than pg_dump&#8217;s version. pg_dump can also dump from PostgreSQL servers older than its own version. (Currently, servers back to version 7.0 are supported.) However, pg_dump cannot dump from PostgreSQL servers newer than its own major version; it will refuse to even try, rather than risk making an invalid dump. Also, it is not guaranteed that pg_dump&#8217;s output can be loaded into a server of an older major version &#8212; not even if the dump was taken from a server of that version. Loading a dump file into an older server may require manual editing of the dump file to remove syntax not understood by the older server. Use of the <code>&#8211;quote-all-identifiers</code> option is recommended in cross-version cases, as it can prevent problems arising from varying reserved-word lists in different PostgreSQL versions.</p>
<h2>EXAMPLES</h2>
<p> To dump a database called mydb into a SQL-script file: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>pg_dump mydb &gt; db.sql</code>
</pre>
</dl>
<p> To reload such a script into a (freshly created) database named newdb: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>psql -d newdb -f db.sql</code>
</pre>
</dl>
<p> To dump a database into a custom-format archive file: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>pg_dump -Fc mydb &gt; db.dump</code>
</pre>
</dl>
<p> To dump a database into a directory-format archive: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>pg_dump -Fd mydb -f dumpdir</code>
</pre>
</dl>
<p> To reload an archive file into a (freshly created) database named newdb: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>pg_restore -d newdb db.dump</code>
</pre>
</dl>
<p> To dump a single table named mytab: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>pg_dump -t mytab mydb &gt; db.sql</code>
</pre>
</dl>
<p> To dump all tables whose names start with emp in the detroit schema, except for the table named employee_log: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>pg_dump -t 'detroit.emp*' -T detroit.employee_log mydb &gt; db.sql</code>
</pre>
</dl>
<p> To dump all schemas whose names start with east or west and end in gsm, excluding any schemas whose names contain the word test: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>pg_dump -n 'east*gsm' -n 'west*gsm' -N '*test*' mydb &gt; db.sql</code>
</pre>
</dl>
<p> The same, using regular expression notation to consolidate the switches: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>pg_dump -n '(east|west)*gsm' -N '*test*' mydb &gt; db.sql</code>
</pre>
</dl>
<p> To dump all database objects except for tables whose names begin with ts_: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>pg_dump -T 'ts_*' mydb &gt; db.sql</code>
</pre>
</dl>
<p> To specify an upper-case or mixed-case name in <code>-t</code> and related switches, you need to double-quote the name; else it will be folded to lower case (see Patterns). But double quotes are special to the shell, so in turn they must be quoted. Thus, to dump a single table with a mixed-case name, you need something like </p>
<dl>
<dt>
<dd>
<pre>
$ <code>pg_dump -t '&quot;MixedCaseName&quot;' mydb &gt; mytab.sql</code>
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pg_dumpall/">pg_dumpall</a></code>(1), <code><a href="/docs/linux/man/1-pg_restore/">pg_restore</a></code>(1), <code><a href="/docs/linux/man/1-psql/">psql</a></code>(1) </p>
<h2>Index</h2>
