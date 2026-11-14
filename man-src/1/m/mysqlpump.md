---
title: "mysqlpump(1)"
name: "mysqlpump"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqlpump/"
description: "mysqlpump – a database backup program"
---

<h2 class="name">NAME</h2>
<p> mysqlpump &#8211; a database backup program </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqlpump [</code><i>options</i><code>] [</code><i>db_name</i><code> [</code><i>tbl_name</i><code> &#8230;]]</code></dl>
<h2>DESCRIPTION</h2>
<dl>
<dt>
<dd> &bull;</p>
<dd>mysqlpump Invocation Syntax</dl>
<dl>
<dt>
<dd> &bull; mysqlpump Option Summary</dl>
<dl>
<dt>
<dd> &bull; mysqlpump Option Descriptions</dl>
<dl>
<dt>
<dd> &bull; mysqlpump Object Selection</dl>
<dl>
<dt>
<dd> &bull; mysqlpump Parallel Processing</dl>
<dl>
<dt>
<dd> &bull; mysqlpump Restrictions</dl>
<p> The <code>mysqlpump</code> client utility performs logical backups, producing a set of SQL statements that can be executed to reproduce the original database object definitions and table data. It dumps one or more MySQL databases for backup or transfer to another SQL server. </p>
<p> <code>mysqlpump</code> features include: </p>
<dl>
<dt>
<dd> &bull; Parallel processing of databases, and of objects within databases, to speed up the dump process</dl>
<dl>
<dt>
<dd> &bull; Better control over which databases and database objects (tables, stored programs, user accounts) to dump</dl>
<dl>
<dt>
<dd> &bull; Dumping of user accounts as account-management statements (CREATE USER, GRANT) rather than as inserts into the mysql system database</dl>
<dl>
<dt>
<dd> &bull; Capability of creating compressed output</dl>
<dl>
<dt>
<dd> &bull; Progress indicator (the values are estimates)</dl>
<dl>
<dt>
<dd> &bull; For dump file reloading, faster secondary index creation for InnoDB tables by adding indexes after rows are inserted</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> <code>mysqlpump</code> uses MySQL features introduced in MySQL 5.7, and thus assumes use with MySQL 5.7 or higher. </p>
</dl>
<p> <code>mysqlpump</code> requires at least the SELECT privilege for dumped tables, SHOW VIEW for dumped views, TRIGGER for dumped triggers, and LOCK TABLES if the <code>&#8211;single-transaction</code> option is not used. The SELECT privilege on the mysql system database is required to dump user definitions. Certain options might require other privileges as noted in the option descriptions. </p>
<p> To reload a dump file, you must have the privileges required to execute the statements that it contains, such as the appropriate CREATE privileges for objects created by those statements. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> A dump made using PowerShell on Windows with output redirection creates a file that has UTF-16 encoding: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlpump [options] &gt; dump.sql</code>
</pre>
</dl>
<p> However, UTF-16 is not permitted as a connection character set (see Section 10.4, &#8220;Connection Character Sets and Collations&#8221;), so the dump file will not load correctly. To work around this issue, use the <code>&#8211;result-file</code> option, which creates the output in ASCII format: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlpump [options] --result-file=dump.sql</code>
</pre>
</dl>
</dl>
<p> mysqlpump Invocation Syntax </p>
<p> By default, <code>mysqlpump</code> dumps all databases (with certain exceptions noted in mysqlpump Restrictions). To specify this behavior explicitly, use the <code>&#8211;all-databases</code> option: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlpump --all-databases</code>
</pre>
</dl>
<p> To dump a single database, or certain tables within that database, name the database on the command line, optionally followed by table names: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlpump </code><i>db_name</i>
shell&gt; <code>mysqlpump </code><i>db_name tbl_name1 tbl_name2 ...</i>
</pre>
</dl>
<p> To treat all name arguments as database names, use the <code>&#8211;databases</code> option: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlpump --databases </code><i>db_name1 db_name2</i><code> ...</code>
</pre>
</dl>
<p> By default, <code>mysqlpump</code> does not dump user account definitions, even if you dump the mysql system database that contains the grant tables. To dump grant table contents as logical definitions in the form of CREATE USER and GRANT statements, use the <code>&#8211;users</code> option and suppress all database dumping: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlpump --exclude-databases=% --users</code>
</pre>
</dl>
<p> In the preceding command, % is a wildcard that matches all database names for the <code>&#8211;exclude-databases</code> option. </p>
<p> <code>mysqlpump</code> supports several options for including or excluding databases, tables, stored programs, and user definitions. See mysqlpump Object Selection. </p>
<p> To reload a dump file, execute the statements that it contains. For example, use the <code>mysql</code> client: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlpump [options] &gt; dump.sql</code>
shell&gt; <code>mysql &lt; dump.sql</code>
</pre>
</dl>
<p> The following discussion provides additional <code>mysqlpump</code> usage examples. </p>
<p> To see a list of the options <code>mysqlpump</code> supports, issue the command <code>mysqlpump &#8211;help</code>. mysqlpump Option Summary </p>
<p> <code>mysqlpump</code> supports the following options, which can be specified on the command line or in the [mysqlpump] and [client] groups of an option file. (Prior to MySQL 8.0.20, <code>mysqlpump</code> read the [mysql_dump] group rather than [mysqlpump]. As of 8.0.20, [mysql_dump] is still accepted but is deprecated.) For information about option files used by MySQL programs, see Section 4.2.2.2, &#8220;Using Option Files&#8221;. mysqlpump Option Descriptions </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;add-drop-database</code> </p>
<p> Write a DROP DATABASE statement before each CREATE DATABASE statement.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;add-drop-table</code> </p>
<p> Write a DROP TABLE statement before each CREATE TABLE statement.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;add-drop-user</code> </p>
<p> Write a DROP USER statement before each CREATE USER statement.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;add-locks</code> </p>
<p> Surround each table dump with LOCK TABLES and UNLOCK TABLES statements. This results in faster inserts when the dump file is reloaded. See Section 8.2.5.1, &#8220;Optimizing INSERT Statements&#8221;. </p>
<p> This option does not work with parallelism because INSERT statements from different tables can be interleaved and UNLOCK TABLES following the end of the inserts for one table could release locks on tables for which inserts remain. </p>
<p> <code>&#8211;add-locks</code> and <code>&#8211;single-transaction</code> are mutually exclusive.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;all-databases</code>, <code>-A</code> </p>
<p> Dump all databases (with certain exceptions noted in mysqlpump Restrictions). This is the default behavior if no other is specified explicitly. </p>
<p> <code>&#8211;all-databases</code> and <code>&#8211;databases</code> are mutually exclusive. </p>
<p> Prior to MySQL 8.0, the <code>&#8211;routines</code> and <code>&#8211;events</code> options for <code>mysqldump</code> and <code>mysqlpump</code> were not required to include stored routines and events when using the <code>&#8211;all-databases</code> option: The dump included the mysql system database, and therefore also the mysql.proc and mysql.event tables containing stored routine and event definitions. As of MySQL 8.0, the mysql.event and mysql.proc tables are not used. Definitions for the corresponding objects are stored in data dictionary tables, but those tables are not dumped. To include stored routines and events in a dump made using <code>&#8211;all-databases</code>, use the <code>&#8211;routines</code> and <code>&#8211;events</code> options explicitly.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;bind-address=</code><i>ip_address</i> </p>
<p> On a computer having multiple network interfaces, use this option to select which interface to use for connecting to the MySQL server.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;character-sets-dir=</code><i>path</i> </p>
<p> The directory where character sets are installed. See Section 10.15, &#8220;Character Set Configuration&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;column-statistics</code> Add ANALYZE TABLE statements to the output to generate histogram statistics for dumped tables when the dump file is reloaded. This option is disabled by default because histogram generation for large tables can take a long time.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;complete-insert</code> </p>
<p> Write complete INSERT statements that include column names.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;compress</code>, <code>-C</code> </p>
<p> Compress all information sent between the client and the server if possible. See Section 4.2.6, &#8220;Connection Compression Control&#8221;. </p>
<p> As of MySQL 8.0.18, this option is deprecated. It will be removed in a future MySQL version. See the section called &#8220;Legacy Connection Compression Configuration&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;compress-output=</code><i>algorithm</i> </p>
<p> By default, <code>mysqlpump</code> does not compress output. This option specifies output compression using the specified algorithm. Permitted algorithms are LZ4 and ZLIB. </p>
<p> To uncompress compressed output, you must have an appropriate utility. If the system commands <code>lz4</code> and <code>openssl zlib</code> are not available, MySQL distributions include <code>lz4_decompress</code> and <code>zlib_decompress</code> utilities that can be used to decompress <code>mysqlpump</code> output that was compressed using the <code>&#8211;compress-output=LZ4</code> and <code>&#8211;compress-output=ZLIB</code> options. For more information, see <code><a href="/docs/linux/man/1-lz4_decompress/">lz4_decompress</a></code>(1), and <code><a href="/docs/linux/man/1-zlib_decompress/">zlib_decompress</a></code>(1).</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;compression-algorithms=</code><i>value</i> The permitted compression algorithms for connections to the server. The available algorithms are the same as for the protocol_compression_algorithms system variable. The default value is uncompressed. </p>
<p> For more information, see Section 4.2.6, &#8220;Connection Compression Control&#8221;. </p>
<p> This option was added in MySQL 8.0.18.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;databases</code>, <code>-B</code> </p>
<p> Normally, <code>mysqlpump</code> treats the first name argument on the command line as a database name and any following names as table names. With this option, it treats all name arguments as database names. CREATE DATABASE statements are included in the output before each new database. </p>
<p> <code>&#8211;all-databases</code> and <code>&#8211;databases</code> are mutually exclusive.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug[=</code><i>debug_options</i><code>]</code>, <code>-# [</code><i>debug_options</i><code>]</code> </p>
<p> Write a debugging log. A typical <i>debug_options</i> string is d:t:o,<i>file_name</i>. The default is d:t:O,/tmp/mysqlpump.trace. </p>
<p> This option is available only if MySQL was built using <code>WITH_DEBUG</code>. MySQL release binaries provided by Oracle are <i>not</i> built using this option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug-check</code> </p>
<p> Print some debugging information when the program exits. </p>
<p> This option is available only if MySQL was built using <code>WITH_DEBUG</code>. MySQL release binaries provided by Oracle are <i>not</i> built using this option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug-info</code>, <code>-T</code> </p>
<p> Print debugging information and memory and CPU usage statistics when the program exits. </p>
<p> This option is available only if MySQL was built using <code>WITH_DEBUG</code>. MySQL release binaries provided by Oracle are <i>not</i> built using this option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;default-auth=</code><i>plugin</i> </p>
<p> A hint about which client-side authentication plugin to use. See Section 6.2.17, &#8220;Pluggable Authentication&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;default-character-set=</code><i>charset_name</i> </p>
<p> Use <i>charset_name</i> as the default character set. See Section 10.15, &#8220;Character Set Configuration&#8221;. If no character set is specified, <code>mysqlpump</code> uses utf8.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;default-parallelism=</code><i>N</i> </p>
<p> The default number of threads for each parallel processing queue. The default is 2. </p>
<p> The <code>&#8211;parallel-schemas</code> option also affects parallelism and can be used to override the default number of threads. For more information, see mysqlpump Parallel Processing. </p>
<p> With <code>&#8211;default-parallelism=0</code> and no <code>&#8211;parallel-schemas</code> options, <code>mysqlpump</code> runs as a single-threaded process and creates no queues. </p>
<p> With parallelism enabled, it is possible for output from different databases to be interleaved.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;defaults-extra-file=</code><i>file_name</i> </p>
<p> Read this option file after the global option file but (on Unix) before the user option file. If the file does not exist or is otherwise inaccessible, an error occurs. <i>file_name</i> is interpreted relative to the current directory if given as a relative path name rather than a full path name. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;defaults-file=</code><i>file_name</i> </p>
<p> Use only the given option file. If the file does not exist or is otherwise inaccessible, an error occurs. <i>file_name</i> is interpreted relative to the current directory if given as a relative path name rather than a full path name. </p>
<p> Exception: Even with <code>&#8211;defaults-file</code>, client programs read .mylogin.cnf. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;defaults-group-suffix=</code><i>str</i> </p>
<p> Read not only the usual option groups, but also groups with the usual names and a suffix of <i>str</i>. For example, <code>mysqlpump</code> normally reads the [client] and [mysqlpump] groups. If the <code>&#8211;defaults-group-suffix=_other</code> option is given, <code>mysqlpump</code> also reads the [client_other] and [mysqlpump_other] groups. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;defer-table-indexes</code> </p>
<p> In the dump output, defer index creation for each table until after its rows have been loaded. This works for all storage engines, but for InnoDB applies only for secondary indexes. </p>
<p> This option is enabled by default; use <code>&#8211;skip-defer-table-indexes</code> to disable it.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;events</code> </p>
<p> Include Event Scheduler events for the dumped databases in the output. Event dumping requires the EVENT privileges for those databases. </p>
<p> The output generated by using <code>&#8211;events</code> contains CREATE EVENT statements to create the events. </p>
<p> This option is enabled by default; use <code>&#8211;skip-events</code> to disable it.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;exclude-databases=</code><i>db_list</i> </p>
<p> Do not dump the databases in <i>db_list</i>, which is a list of one or more comma-separated database names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;exclude-events=</code><i>event_list</i> </p>
<p> Do not dump the databases in <i>event_list</i>, which is a list of one or more comma-separated event names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;exclude-routines=</code><i>routine_list</i> </p>
<p> Do not dump the events in <i>routine_list</i>, which is a list of one or more comma-separated routine (stored procedure or function) names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;exclude-tables=</code><i>table_list</i> </p>
<p> Do not dump the tables in <i>table_list</i>, which is a list of one or more comma-separated table names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;exclude-triggers=</code><i>trigger_list</i> </p>
<p> Do not dump the triggers in <i>trigger_list</i>, which is a list of one or more comma-separated trigger names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;exclude-users=</code><i>user_list</i> </p>
<p> Do not dump the user accounts in <i>user_list</i>, which is a list of one or more comma-separated account names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;extended-insert=</code><i>N</i> </p>
<p> Write INSERT statements using multiple-row syntax that includes several VALUES lists. This results in a smaller dump file and speeds up inserts when the file is reloaded. </p>
<p> The option value indicates the number of rows to include in each INSERT statement. The default is 250. A value of 1 produces one INSERT statement per table row.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;get-server-public-key</code> </p>
<p> Request from the server the public key required for RSA key pair-based password exchange. This option applies to clients that authenticate with the caching_sha2_password authentication plugin. For that plugin, the server does not send the public key unless requested. This option is ignored for accounts that do not authenticate with that plugin. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection. </p>
<p> If <code>&#8211;server-public-key-path=</code><i>file_name</i> is given and specifies a valid public key file, it takes precedence over <code>&#8211;get-server-public-key</code>. </p>
<p> For information about the caching_sha2_password plugin, see Section 6.4.1.2, &#8220;Caching SHA-2 Pluggable Authentication&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;hex-blob</code> </p>
<p> Dump binary columns using hexadecimal notation (for example, &#8216;abc&#8217; becomes 0x616263). The affected data types are BINARY, VARBINARY, BLOB types, BIT, all spatial data types, and other non-binary data types when used with the binary character set.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;host=</code><i>host_name</i>, <code>-h </code><i>host_name</i> </p>
<p> Dump data from the MySQL server on the given host.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;include-databases=</code><i>db_list</i> </p>
<p> Dump the databases in <i>db_list</i>, which is a list of one or more comma-separated database names. The dump includes all objects in the named databases. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;include-events=</code><i>event_list</i> </p>
<p> Dump the events in <i>event_list</i>, which is a list of one or more comma-separated event names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;include-routines=</code><i>routine_list</i> </p>
<p> Dump the routines in <i>routine_list</i>, which is a list of one or more comma-separated routine (stored procedure or function) names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;include-tables=</code><i>table_list</i> </p>
<p> Dump the tables in <i>table_list</i>, which is a list of one or more comma-separated table names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;include-triggers=</code><i>trigger_list</i> </p>
<p> Dump the triggers in <i>trigger_list</i>, which is a list of one or more comma-separated trigger names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;include-users=</code><i>user_list</i> </p>
<p> Dump the user accounts in <i>user_list</i>, which is a list of one or more comma-separated user names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;insert-ignore</code> </p>
<p> Write INSERT IGNORE statements rather than INSERT statements.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;log-error-file=</code><i>file_name</i> </p>
<p> Log warnings and errors by appending them to the named file. If this option is not given, <code>mysqlpump</code> writes warnings and errors to the standard error output.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;login-path=</code><i>name</i> </p>
<p> Read options from the named login path in the .mylogin.cnf login path file. A &#8220;login path&#8221; is an option group containing options that specify which MySQL server to connect to and which account to authenticate as. To create or modify a login path file, use the <code>mysql_config_editor</code> utility. See <code><a href="/docs/linux/man/1-mysql_config_editor/">mysql_config_editor</a></code>(1). </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;max-allowed-packet=</code><i>N</i> </p>
<p> The maximum size of the buffer for client/server communication. The default is 24MB, the maximum is 1GB.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;net-buffer-length=</code><i>N</i> </p>
<p> The initial size of the buffer for client/server communication. When creating multiple-row INSERT statements (as with the <code>&#8211;extended-insert</code> option), <code>mysqlpump</code> creates rows up to <i>N</i> bytes long. If you use this option to increase the value, ensure that the MySQL server net_buffer_length system variable has a value at least this large.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-create-db</code> </p>
<p> Suppress any CREATE DATABASE statements that might otherwise be included in the output.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-create-info</code>, <code>-t</code> </p>
<p> Do not write CREATE TABLE statements that create each dumped table.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-defaults</code> </p>
<p> Do not read any option files. If program startup fails due to reading unknown options from an option file, <code>&#8211;no-defaults</code> can be used to prevent them from being read. </p>
<p> The exception is that the .mylogin.cnf file, if it exists, is read in all cases. This permits passwords to be specified in a safer way than on the command line even when <code>&#8211;no-defaults</code> is used. (.mylogin.cnf is created by the <code>mysql_config_editor</code> utility. See <code><a href="/docs/linux/man/1-mysql_config_editor/">mysql_config_editor</a></code>(1).) </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;parallel-schemas=[</code><i>N</i><code>:]</code><i>db_list</i> </p>
<p> Create a queue for processing the databases in <i>db_list</i>, which is a list of one or more comma-separated database names. If <i>N</i> is given, the queue uses <i>N</i> threads. If <i>N</i> is not given, the <code>&#8211;default-parallelism</code> option determines the number of queue threads. </p>
<p> Multiple instances of this option create multiple queues. <code>mysqlpump</code> also creates a default queue to use for databases not named in any <code>&#8211;parallel-schemas</code> option, and for dumping user definitions if command options select them. For more information, see mysqlpump Parallel Processing.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;password[=</code><i>password</i><code>]</code>, <code>-p[</code><i>password</i><code>]</code> </p>
<p> The password of the MySQL account used for connecting to the server. The password value is optional. If not given, <code>mysqlpump</code> prompts for one. If given, there must be <i>no space</i> between <code>&#8211;password=</code> or <code>-p</code> and the password following it. If no password option is specified, the default is to send no password. </p>
<p> Specifying a password on the command line should be considered insecure. To avoid giving the password on the command line, use an option file. See Section 6.1.2.1, &#8220;End-User Guidelines for Password Security&#8221;. </p>
<p> To explicitly specify that there is no password and that <code>mysqlpump</code> should not prompt for one, use the <code>&#8211;skip-password</code> option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;plugin-dir=</code><i>dir_name</i> </p>
<p> The directory in which to look for plugins. Specify this option if the <code>&#8211;default-auth</code> option is used to specify an authentication plugin but <code>mysqlpump</code> does not find it. See Section 6.2.17, &#8220;Pluggable Authentication&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;port=</code><i>port_num</i>, <code>-P </code><i>port_num</i> </p>
<p> For TCP/IP connections, the port number to use.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;print-defaults</code> </p>
<p> Print the program name and all options that it gets from option files. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;protocol={TCP|SOCKET|PIPE|MEMORY}</code> </p>
<p> The connection protocol to use for connecting to the server. It is useful when the other connection parameters normally result in use of a protocol other than the one you want. For details on the permissible values, see Section 4.2.4, &#8220;Connecting to the MySQL Server Using Command Options&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;replace</code> </p>
<p> Write REPLACE statements rather than INSERT statements.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;result-file=</code><i>file_name</i> </p>
<p> Direct output to the named file. The result file is created and its previous contents overwritten, even if an error occurs while generating the dump. </p>
<p> This option should be used on Windows to prevent newline 
 characters from being converted to 
 carriage return/newline sequences.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;routines</code> </p>
<p> Include stored routines (procedures and functions) for the dumped databases in the output. This option requires the global SELECT privilege. </p>
<p> The output generated by using <code>&#8211;routines</code> contains CREATE PROCEDURE and CREATE FUNCTION statements to create the routines. </p>
<p> This option is enabled by default; use <code>&#8211;skip-routines</code> to disable it.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;server-public-key-path=</code><i>file_name</i> </p>
<p> The path name to a file containing a client-side copy of the public key required by the server for RSA key pair-based password exchange. The file must be in PEM format. This option applies to clients that authenticate with the sha256_password or caching_sha2_password authentication plugin. This option is ignored for accounts that do not authenticate with one of those plugins. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection. </p>
<p> If <code>&#8211;server-public-key-path=</code><i>file_name</i> is given and specifies a valid public key file, it takes precedence over <code>&#8211;get-server-public-key</code>. </p>
<p> For sha256_password, this option applies only if MySQL was built using OpenSSL. </p>
<p> For information about the sha256_password and caching_sha2_password plugins, see Section 6.4.1.3, &#8220;SHA-256 Pluggable Authentication&#8221;, and Section 6.4.1.2, &#8220;Caching SHA-2 Pluggable Authentication&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;set-charset</code> </p>
<p> Write SET NAMES <i>default_character_set</i> to the output. </p>
<p> This option is enabled by default. To disable it and suppress the SET NAMES statement, use <code>&#8211;skip-set-charset</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;set-gtid-purged=</code><i>value</i> </p>
<p> This option enables control over global transaction ID (GTID) information written to the dump file, by indicating whether to add a SET @@GLOBAL.gtid_purged statement to the output. This option may also cause a statement to be written to the output that disables binary logging while the dump file is being reloaded. </p>
<p> The following table shows the permitted option values. The default value is AUTO. </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Value </code></td>
<td><code> Meaning </code>
</td>
</tr>
<tr VALIGN=top>
<td> OFF </td>
<td> Add no SET statement to the output.
</td>
</tr>
<tr VALIGN=top>
<td> ON </td>
<td> Add a SET statement to the output. An error occurs if<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;GTIDs are not enabled on the server.
</td>
</tr>
<tr VALIGN=top>
<td> AUTO </td>
<td> Add a SET statement to the output if GTIDs are<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;enabled on the server.
</td>
</tr>
</table>
<p> The <code>&#8211;set-gtid-purged</code> option has the following effect on binary logging when the dump file is reloaded: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;set-gtid-purged=OFF</code>: SET @@SESSION.SQL_LOG_BIN=0; is not added to the output.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;set-gtid-purged=ON</code>: SET @@SESSION.SQL_LOG_BIN=0; is added to the output.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;set-gtid-purged=AUTO</code>: SET @@SESSION.SQL_LOG_BIN=0; is added to the output if GTIDs are enabled on the server you are backing up (that is, if AUTO evaluates to ON).</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;single-transaction</code> </p>
<p> This option sets the transaction isolation mode to REPEATABLE READ and sends a START TRANSACTION SQL statement to the server before dumping data. It is useful only with transactional tables such as InnoDB, because then it dumps the consistent state of the database at the time when START TRANSACTION was issued without blocking any applications. </p>
<p> When using this option, you should keep in mind that only InnoDB tables are dumped in a consistent state. For example, any MyISAM or MEMORY tables dumped while using this option may still change state. </p>
<p> While a <code>&#8211;single-transaction</code> dump is in process, to ensure a valid dump file (correct table contents and binary log coordinates), no other connection should use the following statements: ALTER TABLE, CREATE TABLE, DROP TABLE, RENAME TABLE, TRUNCATE TABLE. A consistent read is not isolated from those statements, so use of them on a table to be dumped can cause the SELECT that is performed by <code>mysqlpump</code> to retrieve the table contents to obtain incorrect contents or fail. </p>
<p> <code>&#8211;add-locks</code> and <code>&#8211;single-transaction</code> are mutually exclusive.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;skip-definer</code> </p>
<p> Omit DEFINER and SQL SECURITY clauses from the CREATE statements for views and stored programs. The dump file, when reloaded, creates objects that use the default DEFINER and SQL SECURITY values. See Section 24.6, &#8220;Stored Object Access Control&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;skip-dump-rows</code>, <code>-d</code> </p>
<p> Do not dump table rows.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;socket=</code><i>path</i>, <code>-S </code><i>path</i> </p>
<p> For connections to localhost, the Unix socket file to use, or, on Windows, the name of the named pipe to use. </p>
<p> On Windows, this option applies only if the server was started with the named_pipe system variable enabled to support named-pipe connections. In addition, the user making the connection must be a member of the Windows group specified by the named_pipe_full_access_group system variable.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;ssl*</code> </p>
<p> Options that begin with <code>&#8211;ssl</code> specify whether to connect to the server using SSL and indicate where to find SSL keys and certificates. See the section called &#8220;Command Options for Encrypted Connections&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;ssl-fips-mode={OFF|ON|STRICT}</code> Controls whether to enable FIPS mode on the client side. The <code>&#8211;ssl-fips-mode</code> option differs from other <code>&#8211;ssl-</code><i>xxx</i> options in that it is not used to establish encrypted connections, but rather to affect which cryptographic operations are permitted. See Section 6.5, &#8220;FIPS Support&#8221;. </p>
<p> These <code>&#8211;ssl-fips-mode</code> values are permitted: </p>
<dl>
<dt>
<dd> &bull; OFF: Disable FIPS mode.</dl>
<dl>
<dt>
<dd> &bull; ON: Enable FIPS mode.</dl>
<dl>
<dt>
<dd> &bull; STRICT: Enable &#8220;strict&#8221; FIPS mode.</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 If the OpenSSL FIPS Object Module is not available, the only permitted value for <code>&#8211;ssl-fips-mode</code> is OFF. In this case, setting <code>&#8211;ssl-fips-mode</code> to ON or STRICT causes the client to produce a warning at startup and to operate in non-FIPS mode. </p>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;tls-ciphersuites=</code><i>ciphersuite_list</i> </p>
<p> The permissible ciphersuites for encrypted connections that use TLSv1.3. The value is a list of one or more colon-separated ciphersuite names. The ciphersuites that can be named for this option depend on the SSL library used to compile MySQL. For details, see Section 6.3.2, &#8220;Encrypted Connection TLS Protocols and Ciphers&#8221;. </p>
<p> This option was added in MySQL 8.0.16.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;tls-version=</code><i>protocol_list</i> </p>
<p> The permissible TLS protocols for encrypted connections. The value is a list of one or more comma-separated protocol names. The protocols that can be named for this option depend on the SSL library used to compile MySQL. For details, see Section 6.3.2, &#8220;Encrypted Connection TLS Protocols and Ciphers&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;triggers</code> </p>
<p> Include triggers for each dumped table in the output. </p>
<p> This option is enabled by default; use <code>&#8211;skip-triggers</code> to disable it.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;tz-utc</code> </p>
<p> This option enables TIMESTAMP columns to be dumped and reloaded between servers in different time zones. <code>mysqlpump</code> sets its connection time zone to UTC and adds SET TIME_ZONE=&#8217;+00:00&#8242; to the dump file. Without this option, TIMESTAMP columns are dumped and reloaded in the time zones local to the source and destination servers, which can cause the values to change if the servers are in different time zones. <code>&#8211;tz-utc</code> also protects against changes due to daylight saving time. </p>
<p> This option is enabled by default; use <code>&#8211;skip-tz-utc</code> to disable it.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;user=</code><i>user_name</i>, <code>-u </code><i>user_name</i> </p>
<p> The user name of the MySQL account to use for connecting to the server.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;users</code> </p>
<p> Dump user accounts as logical definitions in the form of CREATE USER and GRANT statements. </p>
<p> User definitions are stored in the grant tables in the mysql system database. By default, <code>mysqlpump</code> does not include the grant tables in mysql database dumps. To dump the contents of the grant tables as logical definitions, use the <code>&#8211;users</code> option and suppress all database dumping: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlpump --exclude-databases=% --users</code>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code>, <code>-V</code> </p>
<p> Display version information and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;watch-progress</code> </p>
<p> Periodically display a progress indicator that provides information about the completed and total number of tables, rows, and other objects. </p>
<p> This option is enabled by default; use <code>&#8211;skip-watch-progress</code> to disable it.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;zstd-compression-level=</code><i>level</i> The compression level to use for connections to the server that use the zstd compression algorithm. The permitted levels are from 1 to 22, with larger values indicating increasing levels of compression. The default zstd compression level is 3. The compression level setting has no effect on connections that do not use zstd compression. </p>
<p> For more information, see Section 4.2.6, &#8220;Connection Compression Control&#8221;. </p>
<p> This option was added in MySQL 8.0.18.</dl>
<p> mysqlpump Object Selection </p>
<p> <code>mysqlpump</code> has a set of inclusion and exclusion options that enable filtering of several object types and provide flexible control over which objects to dump: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;include-databases</code> and <code>&#8211;exclude-databases</code> apply to databases and all objects within them.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;include-tables</code> and <code>&#8211;exclude-tables</code> apply to tables. These options also affect triggers associated with tables unless the trigger-specific options are given.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;include-triggers</code> and <code>&#8211;exclude-triggers</code> apply to triggers.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;include-routines</code> and <code>&#8211;exclude-routines</code> apply to stored procedures and functions. If a routine option matches a stored procedure name, it also matches a stored function of the same name.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;include-events</code> and <code>&#8211;exclude-events</code> apply to Event Scheduler events.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;include-users</code> and <code>&#8211;exclude-users</code> apply to user accounts.</dl>
<p> Any inclusion or exclusion option may be given multiple times. The effect is additive. Order of these options does not matter. </p>
<p> The value of each inclusion and exclusion option is a list of comma-separated names of the appropriate object type. For example: </p>
<dl>
<dt>
<dd>
<pre>
--exclude-databases=test,world
--include-tables=customer,invoice
</pre>
</dl>
<p> Wildcard characters are permitted in the object names: </p>
<dl>
<dt>
<dd> &bull; % matches any sequence of zero or more characters.</dl>
<dl>
<dt>
<dd> &bull; _ matches any single character.</dl>
<p> For example, <code>&#8211;include-tables=t%,__tmp</code> matches all table names that begin with t and all five-character table names that end with tmp. </p>
<p> For users, a name specified without a host part is interpreted with an implied host of %. For example, u1 and u1@% are equivalent. This is the same equivalence that applies in MySQL generally (see Section 6.2.4, &#8220;Specifying Account Names&#8221;). </p>
<p> Inclusion and exclusion options interact as follows: </p>
<dl>
<dt>
<dd> &bull; By default, with no inclusion or exclusion options, <code>mysqlpump</code> dumps all databases (with certain exceptions noted in mysqlpump Restrictions).</dl>
<dl>
<dt>
<dd> &bull; If inclusion options are given in the absence of exclusion options, only the objects named as included are dumped.</dl>
<dl>
<dt>
<dd> &bull; If exclusion options are given in the absence of inclusion options, all objects are dumped except those named as excluded.</dl>
<dl>
<dt>
<dd> &bull; If inclusion and exclusion options are given, all objects named as excluded and not named as included are not dumped. All other objects are dumped.</dl>
<p> If multiple databases are being dumped, it is possible to name tables, triggers, and routines in a specific database by qualifying the object names with the database name. The following command dumps databases db1 and db2, but excludes tables db1.t1 and db2.t2: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlpump --include-databases=db1,db2 --exclude-tables=db1.t1,db2.t2</code>
</pre>
</dl>
<p> The following options provide alternative ways to specify which databases to dump: </p>
<dl>
<dt>
<dd> &bull; The <code>&#8211;all-databases</code> option dumps all databases (with certain exceptions noted in mysqlpump Restrictions). It is equivalent to specifying no object options at all (the default <code>mysqlpump</code> action is to dump everything). </p>
<p> <code>&#8211;include-databases=%</code> is similar to <code>&#8211;all-databases</code>, but selects all databases for dumping, even those that are exceptions for <code>&#8211;all-databases</code>.</dl>
<dl>
<dt>
<dd> &bull; The <code>&#8211;databases</code> option causes <code>mysqlpump</code> to treat all name arguments as names of databases to dump. It is equivalent to an <code>&#8211;include-databases</code> option that names the same databases.</dl>
<p> mysqlpump Parallel Processing </p>
<p> <code>mysqlpump</code> can use parallelism to achieve concurrent processing. You can select concurrency between databases (to dump multiple databases simultaneously) and within databases (to dump multiple objects from a given database simultaneously). </p>
<p> By default, <code>mysqlpump</code> sets up one queue with two threads. You can create additional queues and control the number of threads assigned to each one, including the default queue: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;default-parallelism=</code><i>N</i> specifies the default number of threads used for each queue. In the absence of this option, <i>N</i> is 2. </p>
<p> The default queue always uses the default number of threads. Additional queues use the default number of threads unless you specify otherwise.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;parallel-schemas=[</code><i>N</i><code>:]</code><i>db_list</i> sets up a processing queue for dumping the databases named in <i>db_list</i> and optionally specifies how many threads the queue uses. <i>db_list</i> is a list of comma-separated database names. If the option argument begins with <i>N</i>:, the queue uses <i>N</i> threads. Otherwise, the <code>&#8211;default-parallelism</code> option determines the number of queue threads. </p>
<p> Multiple instances of the <code>&#8211;parallel-schemas</code> option create multiple queues. </p>
<p> Names in the database list are permitted to contain the same % and _ wildcard characters supported for filtering options (see mysqlpump Object Selection).</dl>
<p> <code>mysqlpump</code> uses the default queue for processing any databases not named explicitly with a <code>&#8211;parallel-schemas</code> option, and for dumping user definitions if command options select them. </p>
<p> In general, with multiple queues, <code>mysqlpump</code> uses parallelism between the sets of databases processed by the queues, to dump multiple databases simultaneously. For a queue that uses multiple threads, <code>mysqlpump</code> uses parallelism within databases, to dump multiple objects from a given database simultaneously. Exceptions can occur; for example, <code>mysqlpump</code> may block queues while it obtains from the server lists of objects in databases. </p>
<p> With parallelism enabled, it is possible for output from different databases to be interleaved. For example, INSERT statements from multiple tables dumped in parallel can be interleaved; the statements are not written in any particular order. This does not affect reloading because output statements qualify object names with database names or are preceded by USE statements as required. </p>
<p> The granularity for parallelism is a single database object. For example, a single table cannot be dumped in parallel using multiple threads. </p>
<p> Examples: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlpump --parallel-schemas=db1,db2 --parallel-schemas=db3</code>
</pre>
</dl>
<p> <code>mysqlpump</code> sets up a queue to process db1 and db2, another queue to process db3, and a default queue to process all other databases. All queues use two threads. </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlpump --parallel-schemas=db1,db2 --parallel-schemas=db3</code>
         <code>--default-parallelism=4</code>
</pre>
</dl>
<p> This is the same as the previous example except that all queues use four threads. </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlpump --parallel-schemas=5:db1,db2 --parallel-schemas=3:db3</code>
</pre>
</dl>
<p> The queue for db1 and db2 uses five threads, the queue for db3 uses three threads, and the default queue uses the default of two threads. </p>
<p> As a special case, with <code>&#8211;default-parallelism=0</code> and no <code>&#8211;parallel-schemas</code> options, <code>mysqlpump</code> runs as a single-threaded process and creates no queues. mysqlpump Restrictions </p>
<p> <code>mysqlpump</code> does not dump the performance_schema, ndbinfo, or sys schema by default. To dump any of these, name them explicitly on the command line. You can also name them with the <code>&#8211;databases</code> or <code>&#8211;include-databases</code> option. </p>
<p> <code>mysqlpump</code> does not dump the INFORMATION_SCHEMA schema. </p>
<p> <code>mysqlpump</code> does not dump InnoDB CREATE TABLESPACE statements. </p>
<p> <code>mysqlpump</code> dumps user accounts in logical form using CREATE USER and GRANT statements (for example, when you use the <code>&#8211;include-users</code> or <code>&#8211;users</code> option). For this reason, dumps of the mysql system database do not by default include the grant tables that contain user definitions: user, db, tables_priv, columns_priv, procs_priv, or proxies_priv. To dump any of the grant tables, name the mysql database followed by the table names: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlpump mysql user db ...</code>
</pre>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1997, 2020, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
