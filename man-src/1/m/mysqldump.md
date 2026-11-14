---
title: "mysqldump(1)"
name: "mysqldump"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqldump/"
description: "mysqldump – a database backup program"
---

<h2 class="name">NAME</h2>
<p> mysqldump &#8211; a database backup program </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqldump [</code><i>options</i><code>] [</code><i>db_name</i><code> [</code><i>tbl_name</i><code> &#8230;]]</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>mysqldump</code> client utility performs logical backups, producing a set of SQL statements that can be executed to reproduce the original database object definitions and table data. It dumps one or more MySQL databases for backup or transfer to another SQL server. The <code>mysqldump</code> command can also generate output in CSV, other delimited text, or XML format. </p>
<dl>
<dt>
<dd> &bull; Performance and Scalability Considerations</dl>
<dl>
<dt>
<dd> &bull; Invocation Syntax</dl>
<dl>
<dt>
<dd> &bull; Option Syntax &#8211; Alphabetical Summary</dl>
<dl>
<dt>
<dd> &bull; Connection Options</dl>
<dl>
<dt>
<dd> &bull; Option-File Options</dl>
<dl>
<dt>
<dd> &bull; DDL Options</dl>
<dl>
<dt>
<dd> &bull; Debug Options</dl>
<dl>
<dt>
<dd> &bull; Help Options</dl>
<dl>
<dt>
<dd> &bull; Internationalization Options</dl>
<dl>
<dt>
<dd> &bull; Replication Options</dl>
<dl>
<dt>
<dd> &bull; Format Options</dl>
<dl>
<dt>
<dd> &bull; Filtering Options</dl>
<dl>
<dt>
<dd> &bull; Performance Options</dl>
<dl>
<dt>
<dd> &bull; Transactional Options</dl>
<dl>
<dt>
<dd> &bull; Option Groups</dl>
<dl>
<dt>
<dd> &bull; Examples</dl>
<dl>
<dt>
<dd> &bull; Restrictions</dl>
<p> <code>mysqldump</code> requires at least the SELECT privilege for dumped tables, SHOW VIEW for dumped views, TRIGGER for dumped triggers, and LOCK TABLES if the <code>&#8211;single-transaction</code> option is not used. Certain options might require other privileges as noted in the option descriptions. </p>
<p> To reload a dump file, you must have the privileges required to execute the statements that it contains, such as the appropriate CREATE privileges for objects created by those statements. </p>
<p> <code>mysqldump</code> output can include ALTER DATABASE statements that change the database collation. These may be used when dumping stored programs to preserve their character encodings. To reload a dump file containing such statements, the ALTER privilege for the affected database is required. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> A dump made using PowerShell on Windows with output redirection creates a file that has UTF-16 encoding: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqldump [options] &gt; dump.sql</code>
</pre>
</dl>
<p> However, UTF-16 is not permitted as a connection character set (see the section called &#8220;Impermissible Client Character Sets&#8221;), so the dump file will not load correctly. To work around this issue, use the <code>&#8211;result-file</code> option, which creates the output in ASCII format: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqldump [options] --result-file=dump.sql</code>
</pre>
</dl>
</dl>
<p> Performance and Scalability Considerations </p>
<p> mysqldump advantages include the convenience and flexibility of viewing or even editing the output before restoring. You can clone databases for development and DBA work, or produce slight variations of an existing database for testing. It is not intended as a fast or scalable solution for backing up substantial amounts of data. With large data sizes, even if the backup step takes a reasonable time, restoring the data can be very slow because replaying the SQL statements involves disk I/O for insertion, index creation, and so on. </p>
<p> For large-scale backup and restore, a physical backup is more appropriate, to copy the data files in their original format that can be restored quickly: </p>
<dl>
<dt>
<dd> &bull; If your tables are primarily InnoDB tables, or if you have a mix of InnoDB and MyISAM tables, consider using the <code>mysqlbackup</code> command of the MySQL Enterprise Backup product. (Available as part of the Enterprise subscription.) It provides the best performance for InnoDB backups with minimal disruption; it can also back up tables from MyISAM and other storage engines; and it provides a number of convenient options to accommodate different backup scenarios. See Section 30.2, &#8220;MySQL Enterprise Backup Overview&#8221;.</dl>
<p> <code>mysqldump</code> can retrieve and dump table contents row by row, or it can retrieve the entire content from a table and buffer it in memory before dumping it. Buffering in memory can be a problem if you are dumping large tables. To dump tables row by row, use the <code>&#8211;quick</code> option (or <code>&#8211;opt</code>, which enables <code>&#8211;quick</code>). The <code>&#8211;opt</code> option (and hence <code>&#8211;quick</code>) is enabled by default, so to enable memory buffering, use <code>&#8211;skip-quick</code>. </p>
<p> If you are using a recent version of <code>mysqldump</code> to generate a dump to be reloaded into a very old MySQL server, use the <code>&#8211;skip-opt</code> option instead of the <code>&#8211;opt</code> or <code>&#8211;extended-insert</code> option. </p>
<p> For additional information about <code>mysqldump</code>, see Section 7.4, &#8220;Using mysqldump for Backups&#8221;. Invocation Syntax </p>
<p> There are in general three ways to use <code>mysqldump</code>&#8212;in order to dump a set of one or more tables, a set of one or more complete databases, or an entire MySQL server&#8212;as shown here: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; mysqldump[options] db_name[tbl_name...] shell &gt; mysqldump[options]-- databases db_name... shell &gt; mysqldump[options]-- all - databases
</code></pre>
</dl>
<p> To dump entire databases, do not name any tables following <i>db_name</i>, or use the <code>&#8211;databases</code> or <code>&#8211;all-databases</code> option. </p>
<p> To see a list of the options your version of <code>mysqldump</code> supports, issue the command <code>mysqldump &#8211;help</code>. Option Syntax &#8211; Alphabetical Summary </p>
<p> <code>mysqldump</code> supports the following options, which can be specified on the command line or in the [mysqldump] and [client] groups of an option file. For information about option files used by MySQL programs, see Section 4.2.2.2, &#8220;Using Option Files&#8221;. Connection Options </p>
<p> The <code>mysqldump</code> command logs into a MySQL server to extract information. The following options specify how to connect to the MySQL server, either on the same machine or a remote system. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;bind-address=</code><i>ip_address</i> </p>
<p> On a computer having multiple network interfaces, use this option to select which interface to use for connecting to the MySQL server.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;compress</code>, <code>-C</code> </p>
<p> Compress all information sent between the client and the server if possible. See Section 4.2.6, &#8220;Connection Compression Control&#8221;. </p>
<p> As of MySQL 8.0.18, this option is deprecated. It will be removed in a future MySQL version. See the section called &#8220;Legacy Connection Compression Configuration&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;compression-algorithms=</code><i>value</i> The permitted compression algorithms for connections to the server. The available algorithms are the same as for the protocol_compression_algorithms system variable. The default value is uncompressed. </p>
<p> For more information, see Section 4.2.6, &#8220;Connection Compression Control&#8221;. </p>
<p> This option was added in MySQL 8.0.18.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;default-auth=</code><i>plugin</i> </p>
<p> A hint about which client-side authentication plugin to use. See Section 6.2.17, &#8220;Pluggable Authentication&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;enable-cleartext-plugin</code> </p>
<p> Enable the mysql_clear_password cleartext authentication plugin. (See Section 6.4.1.4, &#8220;Client-Side Cleartext Pluggable Authentication&#8221;.)</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;get-server-public-key</code> </p>
<p> Request from the server the public key required for RSA key pair-based password exchange. This option applies to clients that authenticate with the caching_sha2_password authentication plugin. For that plugin, the server does not send the public key unless requested. This option is ignored for accounts that do not authenticate with that plugin. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection. </p>
<p> If <code>&#8211;server-public-key-path=</code><i>file_name</i> is given and specifies a valid public key file, it takes precedence over <code>&#8211;get-server-public-key</code>. </p>
<p> For information about the caching_sha2_password plugin, see Section 6.4.1.2, &#8220;Caching SHA-2 Pluggable Authentication&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;host=</code><i>host_name</i>, <code>-h </code><i>host_name</i> </p>
<p> Dump data from the MySQL server on the given host. The default host is localhost.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;login-path=</code><i>name</i> </p>
<p> Read options from the named login path in the .mylogin.cnf login path file. A &#8220;login path&#8221; is an option group containing options that specify which MySQL server to connect to and which account to authenticate as. To create or modify a login path file, use the <code>mysql_config_editor</code> utility. See <code><a href="/docs/linux/man/1-mysql_config_editor/">mysql_config_editor</a></code>(1). </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;password[=</code><i>password</i><code>]</code>, <code>-p[</code><i>password</i><code>]</code> </p>
<p> The password of the MySQL account used for connecting to the server. The password value is optional. If not given, <code>mysqldump</code> prompts for one. If given, there must be <i>no space</i> between <code>&#8211;password=</code> or <code>-p</code> and the password following it. If no password option is specified, the default is to send no password. </p>
<p> Specifying a password on the command line should be considered insecure. To avoid giving the password on the command line, use an option file. See Section 6.1.2.1, &#8220;End-User Guidelines for Password Security&#8221;. </p>
<p> To explicitly specify that there is no password and that <code>mysqldump</code> should not prompt for one, use the <code>&#8211;skip-password</code> option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;pipe</code>, <code>-W</code> </p>
<p> On Windows, connect to the server using a named pipe. This option applies only if the server was started with the named_pipe system variable enabled to support named-pipe connections. In addition, the user making the connection must be a member of the Windows group specified by the named_pipe_full_access_group system variable.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;plugin-dir=</code><i>dir_name</i> </p>
<p> The directory in which to look for plugins. Specify this option if the <code>&#8211;default-auth</code> option is used to specify an authentication plugin but <code>mysqldump</code> does not find it. See Section 6.2.17, &#8220;Pluggable Authentication&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;port=</code><i>port_num</i>, <code>-P </code><i>port_num</i> </p>
<p> For TCP/IP connections, the port number to use.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;protocol={TCP|SOCKET|PIPE|MEMORY}</code> </p>
<p> The connection protocol to use for connecting to the server. It is useful when the other connection parameters normally result in use of a protocol other than the one you want. For details on the permissible values, see Section 4.2.4, &#8220;Connecting to the MySQL Server Using Command Options&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;server-public-key-path=</code><i>file_name</i> </p>
<p> The path name to a file containing a client-side copy of the public key required by the server for RSA key pair-based password exchange. The file must be in PEM format. This option applies to clients that authenticate with the sha256_password or caching_sha2_password authentication plugin. This option is ignored for accounts that do not authenticate with one of those plugins. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection. </p>
<p> If <code>&#8211;server-public-key-path=</code><i>file_name</i> is given and specifies a valid public key file, it takes precedence over <code>&#8211;get-server-public-key</code>. </p>
<p> For sha256_password, this option applies only if MySQL was built using OpenSSL. </p>
<p> For information about the sha256_password and caching_sha2_password plugins, see Section 6.4.1.3, &#8220;SHA-256 Pluggable Authentication&#8221;, and Section 6.4.1.2, &#8220;Caching SHA-2 Pluggable Authentication&#8221;.</dl>
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
<dd> &bull; <code>&#8211;user=</code><i>user_name</i>, <code>-u </code><i>user_name</i> </p>
<p> The user name of the MySQL account to use for connecting to the server.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;zstd-compression-level=</code><i>level</i> The compression level to use for connections to the server that use the zstd compression algorithm. The permitted levels are from 1 to 22, with larger values indicating increasing levels of compression. The default zstd compression level is 3. The compression level setting has no effect on connections that do not use zstd compression. </p>
<p> For more information, see Section 4.2.6, &#8220;Connection Compression Control&#8221;. </p>
<p> This option was added in MySQL 8.0.18.</dl>
<p> Option-File Options </p>
<p> These options are used to control which option files to read. </p>
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
<p> Read not only the usual option groups, but also groups with the usual names and a suffix of <i>str</i>. For example, <code>mysqldump</code> normally reads the [client] and [mysqldump] groups. If the <code>&#8211;defaults-group-suffix=_other</code> option is given, <code>mysqldump</code> also reads the [client_other] and [mysqldump_other] groups. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-defaults</code> </p>
<p> Do not read any option files. If program startup fails due to reading unknown options from an option file, <code>&#8211;no-defaults</code> can be used to prevent them from being read. </p>
<p> The exception is that the .mylogin.cnf file, if it exists, is read in all cases. This permits passwords to be specified in a safer way than on the command line even when <code>&#8211;no-defaults</code> is used. (.mylogin.cnf is created by the <code>mysql_config_editor</code> utility. See <code><a href="/docs/linux/man/1-mysql_config_editor/">mysql_config_editor</a></code>(1).) </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;print-defaults</code> </p>
<p> Print the program name and all options that it gets from option files. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<p> DDL Options </p>
<p> Usage scenarios for <code>mysqldump</code> include setting up an entire new MySQL instance (including database tables), and replacing data inside an existing instance with existing databases and tables. The following options let you specify which things to tear down and set up when restoring a dump, by encoding various DDL statements within the dump file. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;add-drop-database</code> </p>
<p> Write a DROP DATABASE statement before each CREATE DATABASE statement. This option is typically used in conjunction with the <code>&#8211;all-databases</code> or <code>&#8211;databases</code> option because no CREATE DATABASE statements are written unless one of those options is specified.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;add-drop-table</code> </p>
<p> Write a DROP TABLE statement before each CREATE TABLE statement.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;add-drop-trigger</code> </p>
<p> Write a DROP TRIGGER statement before each CREATE TRIGGER statement.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;all-tablespaces</code>, <code>-Y</code> </p>
<p> Adds to a table dump all SQL statements needed to create any tablespaces used by an NDB table. This information is not otherwise included in the output from <code>mysqldump</code>. This option is currently relevant only to NDB Cluster tables.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-create-db</code>, <code>-n</code> </p>
<p> Suppress the CREATE DATABASE statements that are otherwise included in the output if the <code>&#8211;databases</code> or <code>&#8211;all-databases</code> option is given.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-create-info</code>, <code>-t</code> </p>
<p> Do not write CREATE TABLE statements that create each dumped table. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 This option does <i>not</i> exclude statements creating log file groups or tablespaces from <code>mysqldump</code> output; however, you can use the <code>&#8211;no-tablespaces</code> option for this purpose. </p>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-tablespaces</code>, <code>-y</code> </p>
<p> This option suppresses all CREATE LOGFILE GROUP and CREATE TABLESPACE statements in the output of <code>mysqldump</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;replace</code> </p>
<p> Write REPLACE statements rather than INSERT statements.</dl>
<p> Debug Options </p>
<p> The following options print debugging information, encode debugging information in the dump file, or let the dump operation proceed regardless of potential problems. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;allow-keywords</code> </p>
<p> Permit creation of column names that are keywords. This works by prefixing each column name with the table name.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;comments</code>, <code>-i</code> </p>
<p> Write additional information in the dump file such as program version, server version, and host. This option is enabled by default. To suppress this additional information, use <code>&#8211;skip-comments</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug[=</code><i>debug_options</i><code>]</code>, <code>-# [</code><i>debug_options</i><code>]</code> </p>
<p> Write a debugging log. A typical <i>debug_options</i> string is d:t:o,<i>file_name</i>. The default value is d:t:o,/tmp/mysqldump.trace. </p>
<p> This option is available only if MySQL was built using <code>WITH_DEBUG</code>. MySQL release binaries provided by Oracle are <i>not</i> built using this option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug-check</code> </p>
<p> Print some debugging information when the program exits. </p>
<p> This option is available only if MySQL was built using <code>WITH_DEBUG</code>. MySQL release binaries provided by Oracle are <i>not</i> built using this option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug-info</code> </p>
<p> Print debugging information and memory and CPU usage statistics when the program exits. </p>
<p> This option is available only if MySQL was built using <code>WITH_DEBUG</code>. MySQL release binaries provided by Oracle are <i>not</i> built using this option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;dump-date</code> </p>
<p> If the <code>&#8211;comments</code> option is given, <code>mysqldump</code> produces a comment at the end of the dump of the following form: </p>
<dl>
<dt>
<dd>
<pre>
-- Dump completed on <i>DATE</i>
</pre>
</dl>
<p> However, the date causes dump files taken at different times to appear to be different, even if the data are otherwise identical. <code>&#8211;dump-date</code> and <code>&#8211;skip-dump-date</code> control whether the date is added to the comment. The default is <code>&#8211;dump-date</code> (include the date in the comment). <code>&#8211;skip-dump-date</code> suppresses date printing.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;force</code>, <code>-f</code> </p>
<p> Ignore all errors; continue even if an SQL error occurs during a table dump. </p>
<p> One use for this option is to cause <code>mysqldump</code> to continue executing even when it encounters a view that has become invalid because the definition refers to a table that has been dropped. Without <code>&#8211;force</code>, <code>mysqldump</code> exits with an error message. With <code>&#8211;force</code>, <code>mysqldump</code> prints the error message, but it also writes an SQL comment containing the view definition to the dump output and continues executing. </p>
<p> If the <code>&#8211;ignore-error</code> option is also given to ignore specific errors, <code>&#8211;force</code> takes precedence.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;log-error=</code><i>file_name</i> </p>
<p> Log warnings and errors by appending them to the named file. The default is to do no logging.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;skip-comments</code> </p>
<p> See the description for the <code>&#8211;comments</code> option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;verbose</code>, <code>-v</code> </p>
<p> Verbose mode. Print more information about what the program does.</dl>
<p> Help Options </p>
<p> The following options display information about the <code>mysqldump</code> command itself. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code>, <code>-V</code> </p>
<p> Display version information and exit.</dl>
<p> Internationalization Options </p>
<p> The following options change how the <code>mysqldump</code> command represents character data with national language settings. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;character-sets-dir=</code><i>dir_name</i> </p>
<p> The directory where character sets are installed. See Section 10.15, &#8220;Character Set Configuration&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;default-character-set=</code><i>charset_name</i> </p>
<p> Use <i>charset_name</i> as the default character set. See Section 10.15, &#8220;Character Set Configuration&#8221;. If no character set is specified, <code>mysqldump</code> uses utf8.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-set-names</code>, <code>-N</code> </p>
<p> Turns off the <code>&#8211;set-charset</code> setting, the same as specifying <code>&#8211;skip-set-charset</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;set-charset</code> </p>
<p> Write SET NAMES <i>default_character_set</i> to the output. This option is enabled by default. To suppress the SET NAMES statement, use <code>&#8211;skip-set-charset</code>.</dl>
<p> Replication Options </p>
<p> The <code>mysqldump</code> command is frequently used to create an empty instance, or an instance including data, on a slave server in a replication configuration. The following options apply to dumping and restoring data on replication master and slave servers. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;apply-slave-statements</code> </p>
<p> For a slave dump produced with the <code>&#8211;dump-slave</code> option, add a STOP SLAVE statement before the CHANGE MASTER TO statement and a START SLAVE statement at the end of the output.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;delete-master-logs</code> </p>
<p> On a master replication server, delete the binary logs by sending a PURGE BINARY LOGS statement to the server after performing the dump operation. This option automatically enables <code>&#8211;master-data</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;dump-slave[=</code><i>value</i><code>]</code> </p>
<p> This option is similar to <code>&#8211;master-data</code> except that it is used to dump a replication slave server to produce a dump file that can be used to set up another server as a slave that has the same master as the dumped server. It causes the dump output to include a CHANGE MASTER TO statement that indicates the binary log coordinates (file name and position) of the dumped slave&#8217;s master. The CHANGE MASTER TO statement reads the values of Relay_Master_Log_File and Exec_Master_Log_Pos from the SHOW SLAVE STATUS output and uses them for MASTER_LOG_FILE and MASTER_LOG_POS respectively. These are the master server coordinates from which the slave should start replicating. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 Inconsistencies in the sequence of transactions from the relay log which have been executed can cause the wrong position to be used. See Section 17.5.1.33, &#8220;Replication and Transaction Inconsistencies&#8221; for more information. </p>
</dl>
<p> <code>&#8211;dump-slave</code> causes the coordinates from the master to be used rather than those of the dumped server, as is done by the <code>&#8211;master-data</code> option. In addition, specfiying this option causes the <code>&#8211;master-data</code> option to be overridden, if used, and effectively ignored. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Warning</code> </font><br />
 This option should not be used if the server where the dump is going to be applied uses gtid_mode=ON and MASTER_AUTOPOSITION=1. </p>
</dl>
<p> The option value is handled the same way as for <code>&#8211;master-data</code> (setting no value or 1 causes a CHANGE MASTER TO statement to be written to the dump, setting 2 causes the statement to be written but encased in SQL comments) and has the same effect as <code>&#8211;master-data</code> in terms of enabling or disabling other options and in how locking is handled. </p>
<p> This option causes <code>mysqldump</code> to stop the slave SQL thread before the dump and restart it again after. </p>
<p> In conjunction with <code>&#8211;dump-slave</code>, the <code>&#8211;apply-slave-statements</code> and <code>&#8211;include-master-host-port</code> options can also be used.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;include-master-host-port</code> </p>
<p> For the CHANGE MASTER TO statement in a slave dump produced with the <code>&#8211;dump-slave</code> option, add MASTER_HOST and MASTER_PORT options for the host name and TCP/IP port number of the slave&#8217;s master.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;master-data[=</code><i>value</i><code>]</code> </p>
<p> Use this option to dump a master replication server to produce a dump file that can be used to set up another server as a slave of the master. It causes the dump output to include a CHANGE MASTER TO statement that indicates the binary log coordinates (file name and position) of the dumped server. These are the master server coordinates from which the slave should start replicating after you load the dump file into the slave. </p>
<p> If the option value is 2, the CHANGE MASTER TO statement is written as an SQL comment, and thus is informative only; it has no effect when the dump file is reloaded. If the option value is 1, the statement is not written as a comment and takes effect when the dump file is reloaded. If no option value is specified, the default value is 1. </p>
<p> This option requires the RELOAD privilege and the binary log must be enabled. </p>
<p> The <code>&#8211;master-data</code> option automatically turns off <code>&#8211;lock-tables</code>. It also turns on <code>&#8211;lock-all-tables</code>, unless <code>&#8211;single-transaction</code> also is specified, in which case, a global read lock is acquired only for a short time at the beginning of the dump (see the description for <code>&#8211;single-transaction</code>). In all cases, any action on logs happens at the exact moment of the dump. </p>
<p> It is also possible to set up a slave by dumping an existing slave of the master, using the <code>&#8211;dump-slave</code> option, which overrides <code>&#8211;master-data</code> and causes it to be ignored if both options are used.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;set-gtid-purged=</code><i>value</i> </p>
<p> This option is for servers that use GTID-based replication (gtid_mode=ON). It controls the inclusion of a SET @@GLOBAL.gtid_purged statement in the dump output, which updates the value of gtid_purged on a server where the dump file is reloaded, to add the GTID set from the source server&#8217;s gtid_executed system variable. gtid_purged holds the GTIDs of all transactions that have been applied on the server, but do not exist on any binary log file on the server. <code>mysqldump</code> therefore adds the GTIDs for the transactions that were executed on the source server, so that the target server records these transactions as applied, although it does not have them in its binary logs. <code>&#8211;set-gtid-purged</code> also controls the inclusion of a SET @@SESSION.sql_log_bin=0 statement, which disables binary logging while the dump file is being reloaded. This statement prevents new GTIDs from being generated and assigned to the transactions in the dump file as they are executed, so that the original GTIDs for the transactions are used. </p>
<p> If you do not set the <code>&#8211;set-gtid-purged</code> option, the default is that a SET @@GLOBAL.gtid_purged statement is included in the dump output if GTIDs are enabled on the server you are backing up, and the set of GTIDs in the global value of the gtid_executed system variable is not empty. A SET @@SESSION.sql_log_bin=0 statement is also included if GTIDs are enabled on the server. </p>
<p> In MySQL 5.6 and 5.7, you can replace the value of gtid_purged with a specified GTID set, provided that gtid_executed and gtid_purged are empty. From MySQL 8.0, you can either replace the value of gtid_purged with a specified GTID set, or you can add a plus sign (+) to the statement to append a specified GTID set to the GTID set that is already held by gtid_purged. <code>mysqldump</code>&#8216;s SET @@GLOBAL.gtid_purged statement includes a plus sign (+) in a version comment that takes effect when the dump file is replayed on releases from MySQL 8.0, meaning that for these releases, the GTID set from the dump file is added to the existing gtid_purged value. For MySQL 5.6 and 5.7, the value of gtid_purged is replaced with the GTID set from the dump file, which can only happen when gtid_executed is the empty set (so when replication has not been started previously, or when replication was not previously using GTIDs). For the exact details of how the SET @@GLOBAL.gtid_purged statement operates, see the gtid_purged description for the release where the dump file is to be replayed. </p>
<p> It is important to note that the value that is included by <code>mysqldump</code> for the SET @@GLOBAL.gtid_purged statement includes the GTIDs of all transactions in the gtid_executed set on the server, even those that changed suppressed parts of the database, or other databases on the server that were not included in a partial dump. This can mean that after the gtid_purged value has been updated on the server where the dump file is replayed, GTIDs are present that do not relate to any data on the target server. If you do not replay any further dump files on the target server, the extraneous GTIDs do not cause any problems with the future operation of the server, but they make it harder to compare or reconcile GTID sets on different servers in the replication topology. If you do replay a further dump file on the target server that contains the same GTIDs (for example, another partial dump from the same origin server), any SET @@GLOBAL.gtid_purged statement in the second dump file fails. In this case, either remove the statement manually before replaying the dump file, or output the dump file without the statement. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 For MySQL 5.6 and 5.7, it is not recommended to load a dump file when GTIDs are enabled on the server (gtid_mode=ON), if your dump file includes system tables. <code>mysqldump</code> issues DML instructions for the system tables which use the non-transactional MyISAM storage engine, and this combination is not permitted when GTIDs are enabled. </p>
</dl>
<p> If the SET @@GLOBAL.gtid_purged statement would not have the desired result on your target server, you can exclude the statement from the output, or (from MySQL 8.0.17) include it but comment it out so that it is not actioned automatically. You can also include the statement but manually edit it in the dump file to achieve the desired result. </p>
<p> The possible values for the <code>&#8211;set-gtid-purged</code> option are as follows: </p>
<p> AUTO</p>
<dl>
<dt>
<dd> The default value. If GTIDs are enabled on the server you are backing up and gtid_executed is not empty, SET @@GLOBAL.gtid_purged is added to the output, containing the GTID set from gtid_executed. If GTIDs are enabled, SET @@SESSION.sql_log_bin=0 is added to the output. If GTIDs are not enabled on the server, the statements are not added to the output.</dl>
<p> OFF</p>
<dl>
<dt>
<dd> SET @@GLOBAL.gtid_purged is not added to the output, and SET @@SESSION.sql_log_bin=0 is not added to the output. For a server where GTIDs are not in use, use this option or AUTO. Only use this option for a server where GTIDs are in use if you are sure that the required GTID set is already present in gtid_purged on the target server and should not be changed, or if you plan to identify and add any missing GTIDs manually.</dl>
<p> ON</p>
<dl>
<dt>
<dd> If GTIDs are enabled on the server you are backing up, SET @@GLOBAL.gtid_purged is added to the output (unless gtid_executed is empty), and SET @@SESSION.sql_log_bin=0 is added to the output. An error occurs if you set this option but GTIDs are not enabled on the server. For a server where GTIDs are in use, use this option or AUTO, unless you are sure that the GTIDs in gtid_executed are not needed on the target server.</dl>
<p> COMMENTED</p>
<dl>
<dt>
<dd> Available from MySQL 8.0.17. If GTIDs are enabled on the server you are backing up, SET @@GLOBAL.gtid_purged is added to the output (unless gtid_executed is empty), but it is commented out. This means that the value of gtid_executed is available in the output, but no action is taken automatically when the dump file is reloaded. SET @@SESSION.sql_log_bin=0 is added to the output, and it is not commented out. With COMMENTED, you can control the use of the gtid_executed set manually or through automation. For example, you might prefer to do this if you are migrating data to another server that already has different active databases.</dl>
</dl>
<p> Format Options </p>
<p> The following options specify how to represent the entire dump file or certain kinds of data in the dump file. They also control whether certain optional information is written to the dump file. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;compact</code> </p>
<p> Produce more compact output. This option enables the <code>&#8211;skip-add-drop-table</code>, <code>&#8211;skip-add-locks</code>, <code>&#8211;skip-comments</code>, <code>&#8211;skip-disable-keys</code>, and <code>&#8211;skip-set-charset</code> options.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;compatible=</code><i>name</i> </p>
<p> Produce output that is more compatible with other database systems or with older MySQL servers. The only permitted value for this option is ansi, which has the same meaning as the corresponding option for setting the server SQL mode. See Section 5.1.11, &#8220;Server SQL Modes&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;complete-insert</code>, <code>-c</code> </p>
<p> Use complete INSERT statements that include column names.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;create-options</code> </p>
<p> Include all MySQL-specific table options in the CREATE TABLE statements.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;fields-terminated-by=&#8230;</code>, <code>&#8211;fields-enclosed-by=&#8230;</code>, <code>&#8211;fields-optionally-enclosed-by=&#8230;</code>, <code>&#8211;fields-escaped-by=&#8230;</code> </p>
<p> These options are used with the <code>&#8211;tab</code> option and have the same meaning as the corresponding FIELDS clauses for LOAD DATA. See Section 13.2.7, &#8220;LOAD DATA Statement&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;hex-blob</code> </p>
<p> Dump binary columns using hexadecimal notation (for example, &#8216;abc&#8217; becomes 0x616263). The affected data types are BINARY, VARBINARY, BLOB types, BIT, all spatial data types, and other non-binary data types when used with the binary character set.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;lines-terminated-by=&#8230;</code> </p>
<p> This option is used with the <code>&#8211;tab</code> option and has the same meaning as the corresponding LINES clause for LOAD DATA. See Section 13.2.7, &#8220;LOAD DATA Statement&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;quote-names</code>, <code>-Q</code> </p>
<p> Quote identifiers (such as database, table, and column names) within ` characters. If the ANSI_QUOTES SQL mode is enabled, identifiers are quoted within &quot; characters. This option is enabled by default. It can be disabled with <code>&#8211;skip-quote-names</code>, but this option should be given after any option such as <code>&#8211;compatible</code> that may enable <code>&#8211;quote-names</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;result-file=</code><i>file_name</i>, <code>-r </code><i>file_name</i> </p>
<p> Direct output to the named file. The result file is created and its previous contents overwritten, even if an error occurs while generating the dump. </p>
<p> This option should be used on Windows to prevent newline 
 characters from being converted to 
 carriage return/newline sequences.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;show-create-skip-secondary-engine=</code><i>value</i> Excludes the SECONDARY ENGINE clause from CREATE TABLE statements. It does so by enabling the show_create_table_skip_secondary_engine system variable for the duration of the dump operation. Alternatively, you can enable the show_create_table_skip_secondary_engine system variable prior to using <code>mysqldump</code>. </p>
<p> This option was added in MySQL 8.0.18. Attempting a <code>mysqldump</code> operation with the <code>&#8211;show-create-skip-secondary-engine</code> option on a release prior to MySQL 8.0.18 that does not support the show_create_table_skip_secondary_engine variable causes an error.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;tab=</code><i>dir_name</i>, <code>-T </code><i>dir_name</i> </p>
<p> Produce tab-separated text-format data files. For each dumped table, <code>mysqldump</code> creates a <i>tbl_name</i>.sql file that contains the CREATE TABLE statement that creates the table, and the server writes a <i>tbl_name</i>.txt file that contains its data. The option value is the directory in which to write the files. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 This option should be used only when <code>mysqldump</code> is run on the same machine as the <code>mysqld</code> server. Because the server creates *.txt files in the directory that you specify, the directory must be writable by the server and the MySQL account that you use must have the FILE privilege. Because <code>mysqldump</code> creates *.sql in the same directory, it must be writable by your system login account. </p>
</dl>
<p> By default, the .txt data files are formatted using tab characters between column values and a newline at the end of each line. The format can be specified explicitly using the <code>&#8211;fields-</code><i>xxx</i> and <code>&#8211;lines-terminated-by</code> options. </p>
<p> Column values are converted to the character set specified by the <code>&#8211;default-character-set</code> option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;tz-utc</code> </p>
<p> This option enables TIMESTAMP columns to be dumped and reloaded between servers in different time zones. <code>mysqldump</code> sets its connection time zone to UTC and adds SET TIME_ZONE=&#8217;+00:00&#8242; to the dump file. Without this option, TIMESTAMP columns are dumped and reloaded in the time zones local to the source and destination servers, which can cause the values to change if the servers are in different time zones. <code>&#8211;tz-utc</code> also protects against changes due to daylight saving time. <code>&#8211;tz-utc</code> is enabled by default. To disable it, use <code>&#8211;skip-tz-utc</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;xml</code>, <code>-X</code> </p>
<p> Write dump output as well-formed XML. </p>
<p> <code>NULL</code><code>, </code><code>&#8216;NULL&#8217;</code><code>, and Empty Values</code>: For a column named <i>column_name</i>, the NULL value, an empty string, and the string value &#8216;NULL&#8217; are distinguished from one another in the output generated by this option as follows. </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Value: </code></td>
<td><code> XML Representation: </code>
</td>
</tr>
<tr VALIGN=top>
<td> NULL (<i>unknown value</i>) </td>
<td>
<p> &lt;field name=&quot;<i>column_name</i>&quot; xsi:nil=&quot;true&quot; /&gt;
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
<p> &lt;field name=&quot;<i>column_name</i>&quot;&gt;&lt;/field&gt;
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td>
<p> &lt;field name=&quot;<i>column_name</i>&quot;&gt;NULL&lt;/field&gt;
</td>
</tr>
</table>
<p> The output from the <code>mysql</code> client when run using the <code>&#8211;xml</code> option also follows the preceding rules. (See the section called &#8220;MYSQL CLIENT OPTIONS&#8221;.) </p>
<p> XML output from <code>mysqldump</code> includes the XML namespace, as shown here: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; mysqldump-- xml - u root world City &lt; ? xml version = "1.0" ? &gt;
                                                                          &lt;mysqldump xmlns : xsi = "http://www.w3.org/2001/XMLSchema-instance"&gt;
                                                                          &lt;database name = "world"&gt;
                                                                          &lt;table_structure name = "City"&gt;
                                                                          &lt;field Field = "ID" Type = "int(11)" Null = "NO" Key = "PRI" Extra = "auto_increment" /&gt;
                                                                          &lt;field Field = "Name" Type = "char(35)" Null = "NO" Key = "" Default = "" Extra = "" /&gt;
                                                                          &lt;field Field = "CountryCode" Type = "char(3)" Null = "NO" Key = "" Default = "" Extra = "" /&gt;
                                                                          &lt;field Field = "District" Type = "char(20)" Null = "NO" Key = "" Default = "" Extra = "" /&gt;
                                                                          &lt;field Field = "Population" Type = "int(11)" Null = "NO" Key = "" Default = "0" Extra = "" /&gt;
                                                                          &lt;key Table = "City" Non_unique = "0" Key_name = "PRIMARY" Seq_in_index = "1" Column_name = "ID" Collation = "A" Cardinality = "4079" Null = "" Index_type = "BTREE" Comment = "" /&gt;
                                                                          &lt;options Name = "City" Engine = "MyISAM" Version = "10" Row_format = "Fixed" Rows = "4079" Avg_row_length = "67" Data_length = "273293" Max_data_length = "18858823439613951" Index_length = "43008" Data_free = "0" Auto_increment = "4080" Create_time = "2007-03-31 01:47:01" Update_time = "2007-03-31 01:47:02" Collation = "latin1_swedish_ci" Create_options = "" Comment = "" /&gt;
                                                                          &lt;/ table_structure&gt;
                                                                          &lt;table_data name = "City"&gt;
                                                                          &lt;row&gt;
                                                                          &lt;field name = "ID"&gt; 1 &lt; / field &gt;
                                                                          &lt;field name = "Name"&gt; Kabul&lt;/ field&gt;
                                                                          &lt;field name = "CountryCode"&gt; AFG&lt;/ field&gt;
                                                                          &lt;field name = "District"&gt; Kabol&lt;/ field&gt;
                                                                          &lt;field name = "Population"&gt; 1780000 &lt; / field &gt;
                                                                          &lt;/ row&gt;...&lt;row&gt;
                                                                          &lt;field name = "ID"&gt; 4079 &lt; / field &gt;
                                                                          &lt;field name = "Name"&gt; Rafah&lt;/ field&gt;
                                                                          &lt;field name = "CountryCode"&gt; PSE&lt;/ field&gt;
                                                                          &lt;field name = "District"&gt; Rafah&lt;/ field&gt;
                                                                          &lt;field name = "Population"&gt; 92020 &lt; / field &gt;
                                                                          &lt;/ row&gt;
                                                                          &lt;/ table_data&gt;
                                                                          &lt;/ database&gt;
                                                                          &lt;/ mysqldump&gt;
</code></pre>
</dl>
</dl>
<p> Filtering Options </p>
<p> The following options control which kinds of schema objects are written to the dump file: by category, such as triggers or events; by name, for example, choosing which databases and tables to dump; or even filtering rows from the table data using a WHERE clause. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;all-databases</code>, <code>-A</code> </p>
<p> Dump all tables in all databases. This is the same as using the <code>&#8211;databases</code> option and naming all the databases on the command line. </p>
<p> Prior to MySQL 8.0, the <code>&#8211;routines</code> and <code>&#8211;events</code> options for <code>mysqldump</code> and <code>mysqlpump</code> were not required to include stored routines and events when using the <code>&#8211;all-databases</code> option: The dump included the mysql system database, and therefore also the mysql.proc and mysql.event tables containing stored routine and event definitions. As of MySQL 8.0, the mysql.event and mysql.proc tables are not used. Definitions for the corresponding objects are stored in data dictionary tables, but those tables are not dumped. To include stored routines and events in a dump made using <code>&#8211;all-databases</code>, use the <code>&#8211;routines</code> and <code>&#8211;events</code> options explicitly.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;databases</code>, <code>-B</code> </p>
<p> Dump several databases. Normally, <code>mysqldump</code> treats the first name argument on the command line as a database name and following names as table names. With this option, it treats all name arguments as database names. CREATE DATABASE and USE statements are included in the output before each new database. </p>
<p> This option may be used to dump the performance_schema database, which normally is not dumped even with the <code>&#8211;all-databases</code> option. (Also use the <code>&#8211;skip-lock-tables</code> option.)</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;events</code>, <code>-E</code> </p>
<p> Include Event Scheduler events for the dumped databases in the output. This option requires the EVENT privileges for those databases. </p>
<p> The output generated by using <code>&#8211;events</code> contains CREATE EVENT statements to create the events.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;ignore-error=</code><i>error[,error]&#8230;</i> </p>
<p> Ignore the specified errors. The option value is a list of comma-separated error numbers specifying the errors to ignore during <code>mysqldump</code> execution. If the <code>&#8211;force</code> option is also given to ignore all errors, <code>&#8211;force</code> takes precedence.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;ignore-table=</code><i>db_name.tbl_name</i> </p>
<p> Do not dump the given table, which must be specified using both the database and table names. To ignore multiple tables, use this option multiple times. This option also can be used to ignore views.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-data</code>, <code>-d</code> </p>
<p> Do not write any table row information (that is, do not dump table contents). This is useful if you want to dump only the CREATE TABLE statement for the table (for example, to create an empty copy of the table by loading the dump file).</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;routines</code>, <code>-R</code> </p>
<p> Include stored routines (procedures and functions) for the dumped databases in the output. This option requires the global SELECT privilege. </p>
<p> The output generated by using <code>&#8211;routines</code> contains CREATE PROCEDURE and CREATE FUNCTION statements to create the routines.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;tables</code> </p>
<p> Override the <code>&#8211;databases</code> or <code>-B</code> option. <code>mysqldump</code> regards all name arguments following the option as table names.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;triggers</code> </p>
<p> Include triggers for each dumped table in the output. This option is enabled by default; disable it with <code>&#8211;skip-triggers</code>. </p>
<p> To be able to dump a table&#8217;s triggers, you must have the TRIGGER privilege for the table. </p>
<p> Multiple triggers are permitted. <code>mysqldump</code> dumps triggers in activation order so that when the dump file is reloaded, triggers are created in the same activation order. However, if a <code>mysqldump</code> dump file contains multiple triggers for a table that have the same trigger event and action time, an error occurs for attempts to load the dump file into an older server that does not support multiple triggers. (For a workaround, see m[blue]<code>Downgrade Notes</code>m[]<font SIZE="-2">[1]</font>; you can convert triggers to be compatible with older servers.)</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;where=&#8217;</code><i>where_condition</i><code>&#8216;</code>, <code>-w &#8216;</code><i>where_condition</i><code>&#8216;</code> </p>
<p> Dump only rows selected by the given WHERE condition. Quotes around the condition are mandatory if it contains spaces or other characters that are special to your command interpreter. </p>
<p> Examples: </p>
<dl>
<dt>
<dd>
<pre>
--where=&quot;user='jimf'&quot;
-w&quot;userid&gt;1&quot;
-w&quot;userid&lt;1&quot;
</pre>
</dl>
</dl>
<p> Performance Options </p>
<p> The following options are the most relevant for the performance particularly of the restore operations. For large data sets, restore operation (processing the INSERT statements in the dump file) is the most time-consuming part. When it is urgent to restore data quickly, plan and test the performance of this stage in advance. For restore times measured in hours, you might prefer an alternative backup and restore solution, such as MySQL Enterprise Backup for InnoDB-only and mixed-use databases. </p>
<p> Performance is also affected by the transactional options, primarily for the dump operation. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;column-statistics</code> Add ANALYZE TABLE statements to the output to generate histogram statistics for dumped tables when the dump file is reloaded. This option is disabled by default because histogram generation for large tables can take a long time.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;disable-keys</code>, <code>-K</code> </p>
<p> For each table, surround the INSERT statements with /*!40000 ALTER TABLE <i>tbl_name</i> DISABLE KEYS */; and /*!40000 ALTER TABLE <i>tbl_name</i> ENABLE KEYS */; statements. This makes loading the dump file faster because the indexes are created after all rows are inserted. This option is effective only for nonunique indexes of MyISAM tables.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;extended-insert</code>, <code>-e</code> </p>
<p> Write INSERT statements using multiple-row syntax that includes several VALUES lists. This results in a smaller dump file and speeds up inserts when the file is reloaded.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;insert-ignore</code> </p>
<p> Write INSERT IGNORE statements rather than INSERT statements.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;max-allowed-packet=</code><i>value</i> The maximum size of the buffer for client/server communication. The default is 24MB, the maximum is 1GB.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;net-buffer-length=</code><i>value</i> The initial size of the buffer for client/server communication. When creating multiple-row INSERT statements (as with the <code>&#8211;extended-insert</code> or <code>&#8211;opt</code> option), <code>mysqldump</code> creates rows up to <code>&#8211;net-buffer-length</code> bytes long. If you increase this variable, ensure that the MySQL server net_buffer_length system variable has a value at least this large.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;network-timeout</code>, <code>-M</code> </p>
<p> Enable large tables to be dumped by setting <code>&#8211;max-allowed-packet</code> to its maximum value and network read and write timeouts to a large value. This option is enabled by default. To disable it, use <code>&#8211;skip-network-timeout</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;opt</code> </p>
<p> This option, enabled by default, is shorthand for the combination of <code>&#8211;add-drop-table</code> <code>&#8211;add-locks</code> <code>&#8211;create-options</code> <code>&#8211;disable-keys</code> <code>&#8211;extended-insert</code> <code>&#8211;lock-tables</code> <code>&#8211;quick</code> <code>&#8211;set-charset</code>. It gives a fast dump operation and produces a dump file that can be reloaded into a MySQL server quickly. </p>
<p> Because the <code>&#8211;opt</code> option is enabled by default, you only specify its converse, the <code>&#8211;skip-opt</code> to turn off several default settings. See the discussion of mysqldump option groups for information about selectively enabling or disabling a subset of the options affected by <code>&#8211;opt</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;quick</code>, <code>-q</code> </p>
<p> This option is useful for dumping large tables. It forces <code>mysqldump</code> to retrieve rows for a table from the server a row at a time rather than retrieving the entire row set and buffering it in memory before writing it out.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;skip-opt</code> </p>
<p> See the description for the <code>&#8211;opt</code> option.</dl>
<p> Transactional Options </p>
<p> The following options trade off the performance of the dump operation, against the reliability and consistency of the exported data. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;add-locks</code> </p>
<p> Surround each table dump with LOCK TABLES and UNLOCK TABLES statements. This results in faster inserts when the dump file is reloaded. See Section 8.2.5.1, &#8220;Optimizing INSERT Statements&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;flush-logs</code>, <code>-F</code> </p>
<p> Flush the MySQL server log files before starting the dump. This option requires the RELOAD privilege. If you use this option in combination with the <code>&#8211;all-databases</code> option, the logs are flushed <i>for each database dumped</i>. The exception is when using <code>&#8211;lock-all-tables</code>, <code>&#8211;master-data</code>, or <code>&#8211;single-transaction</code>: In this case, the logs are flushed only once, corresponding to the moment that all tables are locked by FLUSH TABLES WITH READ LOCK. If you want your dump and the log flush to happen at exactly the same moment, you should use <code>&#8211;flush-logs</code> together with <code>&#8211;lock-all-tables</code>, <code>&#8211;master-data</code>, or <code>&#8211;single-transaction</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;flush-privileges</code> </p>
<p> Add a FLUSH PRIVILEGES statement to the dump output after dumping the mysql database. This option should be used any time the dump contains the mysql database and any other database that depends on the data in the mysql database for proper restoration. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 For upgrades to MySQL 5.7.2 or higher from older versions, do not use <code>&#8211;flush-privileges</code>. For upgrade instructions in this case, see Section 2.11.4, &#8220;Changes in MySQL 8.0&#8221;. </p>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;lock-all-tables</code>, <code>-x</code> </p>
<p> Lock all tables across all databases. This is achieved by acquiring a global read lock for the duration of the whole dump. This option automatically turns off <code>&#8211;single-transaction</code> and <code>&#8211;lock-tables</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;lock-tables</code>, <code>-l</code> </p>
<p> For each dumped database, lock all tables to be dumped before dumping them. The tables are locked with READ LOCAL to permit concurrent inserts in the case of MyISAM tables. For transactional tables such as InnoDB, <code>&#8211;single-transaction</code> is a much better option than <code>&#8211;lock-tables</code> because it does not need to lock the tables at all. </p>
<p> Because <code>&#8211;lock-tables</code> locks tables for each database separately, this option does not guarantee that the tables in the dump file are logically consistent between databases. Tables in different databases may be dumped in completely different states. </p>
<p> Some options, such as <code>&#8211;opt</code>, automatically enable <code>&#8211;lock-tables</code>. If you want to override this, use <code>&#8211;skip-lock-tables</code> at the end of the option list.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-autocommit</code> </p>
<p> Enclose the INSERT statements for each dumped table within SET autocommit = 0 and COMMIT statements.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;order-by-primary</code> </p>
<p> Dump each table&#8217;s rows sorted by its primary key, or by its first unique index, if such an index exists. This is useful when dumping a MyISAM table to be loaded into an InnoDB table, but makes the dump operation take considerably longer.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;shared-memory-base-name=</code><i>name</i> </p>
<p> On Windows, the shared-memory name to use for connections made using shared memory to a local server. The default value is MYSQL. The shared-memory name is case-sensitive. </p>
<p> This option applies only if the server was started with the shared_memory system variable enabled to support shared-memory connections.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;single-transaction</code> </p>
<p> This option sets the transaction isolation mode to REPEATABLE READ and sends a START TRANSACTION SQL statement to the server before dumping data. It is useful only with transactional tables such as InnoDB, because then it dumps the consistent state of the database at the time when START TRANSACTION was issued without blocking any applications. </p>
<p> When using this option, you should keep in mind that only InnoDB tables are dumped in a consistent state. For example, any MyISAM or MEMORY tables dumped while using this option may still change state. </p>
<p> While a <code>&#8211;single-transaction</code> dump is in process, to ensure a valid dump file (correct table contents and binary log coordinates), no other connection should use the following statements: ALTER TABLE, CREATE TABLE, DROP TABLE, RENAME TABLE, TRUNCATE TABLE. A consistent read is not isolated from those statements, so use of them on a table to be dumped can cause the SELECT that is performed by <code>mysqldump</code> to retrieve the table contents to obtain incorrect contents or fail. </p>
<p> The <code>&#8211;single-transaction</code> option and the <code>&#8211;lock-tables</code> option are mutually exclusive because LOCK TABLES causes any pending transactions to be committed implicitly. </p>
<p> To dump large tables, combine the <code>&#8211;single-transaction</code> option with the <code>&#8211;quick</code> option.</dl>
<p> Option Groups </p>
<dl>
<dt>
<dd> &bull; The <code>&#8211;opt</code> option turns on several settings that work together to perform a fast dump operation. All of these settings are on by default, because <code>&#8211;opt</code> is on by default. Thus you rarely if ever specify &#8211;opt. Instead, you can turn these settings off as a group by specifying &#8211;skip-opt, the optionally re-enable certain settings by specifying the associated options later on the command line.</dl>
<dl>
<dt>
<dd> &bull; The <code>&#8211;compact</code> option turns off several settings that control whether optional statements and comments appear in the output. Again, you can follow this option with other options that re-enable certain settings, or turn all the settings on by using the &#8211;skip-compact form.</dl>
<p> When you selectively enable or disable the effect of a group option, order is important because options are processed first to last. For example, <code>&#8211;disable-keys</code> <code>&#8211;lock-tables</code> <code>&#8211;skip-opt</code> would not have the intended effect; it is the same as <code>&#8211;skip-opt</code> by itself. Examples </p>
<p> To make a backup of an entire database: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqldump </code><i>db_name</i><code> &gt; </code><i>backup-file.sql</i>
</pre>
</dl>
<p> To load the dump file back into the server: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql </code><i>db_name</i><code> &lt; </code><i>backup-file.sql</i>
</pre>
</dl>
<p> Another way to reload the dump file: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql -e &quot;source </code><i>/path-to-backup/backup-file.sql</i><code>&quot; </code><i>db_name</i>
</pre>
</dl>
<p> <code>mysqldump</code> is also very useful for populating databases by copying data from one MySQL server to another: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqldump --opt </code><i>db_name</i><code> | mysql --host=</code><i>remote_host</i><code> -C </code><i>db_name</i>
</pre>
</dl>
<p> You can dump several databases with one command: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqldump --databases </code><i>db_name1</i><code> [</code><i>db_name2</i><code> ...] &gt; my_databases.sql</code>
</pre>
</dl>
<p> To dump all databases, use the <code>&#8211;all-databases</code> option: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqldump --all-databases &gt; all_databases.sql</code>
</pre>
</dl>
<p> For InnoDB tables, <code>mysqldump</code> provides a way of making an online backup: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqldump --all-databases --master-data --single-transaction &gt; all_databases.sql</code>
</pre>
</dl>
<p> This backup acquires a global read lock on all tables (using FLUSH TABLES WITH READ LOCK) at the beginning of the dump. As soon as this lock has been acquired, the binary log coordinates are read and the lock is released. If long updating statements are running when the FLUSH statement is issued, the MySQL server may get stalled until those statements finish. After that, the dump becomes lock free and does not disturb reads and writes on the tables. If the update statements that the MySQL server receives are short (in terms of execution time), the initial lock period should not be noticeable, even with many updates. </p>
<p> For point-in-time recovery (also known as &#8220;roll-forward,&#8221; when you need to restore an old backup and replay the changes that happened since that backup), it is often useful to rotate the binary log (see Section 5.4.4, &#8220;The Binary Log&#8221;) or at least know the binary log coordinates to which the dump corresponds: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqldump --all-databases --master-data=2 &gt; all_databases.sql</code>
</pre>
</dl>
<p> Or: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqldump --all-databases --flush-logs --master-data=2</code>
              <code>&gt; all_databases.sql</code>
</pre>
</dl>
<p> The <code>&#8211;master-data</code> and <code>&#8211;single-transaction</code> options can be used simultaneously, which provides a convenient way to make an online backup suitable for use prior to point-in-time recovery if tables are stored using the InnoDB storage engine. </p>
<p> For more information on making backups, see Section 7.2, &#8220;Database Backup Methods&#8221;, and Section 7.3, &#8220;Example Backup and Recovery Strategy&#8221;. </p>
<dl>
<dt>
<dd> &bull; To select the effect of <code>&#8211;opt</code> except for some features, use the <code>&#8211;skip</code> option for each feature. To disable extended inserts and memory buffering, use <code>&#8211;opt</code> <code>&#8211;skip-extended-insert</code> <code>&#8211;skip-quick</code>. (Actually, <code>&#8211;skip-extended-insert</code> <code>&#8211;skip-quick</code> is sufficient because <code>&#8211;opt</code> is on by default.)</dl>
<dl>
<dt>
<dd> &bull; To reverse <code>&#8211;opt</code> for all features except index disabling and table locking, use <code>&#8211;skip-opt</code> <code>&#8211;disable-keys</code> <code>&#8211;lock-tables</code>.</dl>
<p> Restrictions </p>
<p> <code>mysqldump</code> does not dump the performance_schema or sys schema by default. To dump any of these, name them explicitly on the command line. You can also name them with the <code>&#8211;databases</code> option. For performance_schema, also use the <code>&#8211;skip-lock-tables</code> option. </p>
<p> <code>mysqldump</code> does not dump the INFORMATION_SCHEMA schema. </p>
<p> <code>mysqldump</code> does not dump InnoDB CREATE TABLESPACE statements. </p>
<p> <code>mysqldump</code> does not dump the NDB Cluster ndbinfo information database. </p>
<p> <code>mysqldump</code> includes statements to recreate the general_log and slow_query_log tables for dumps of the mysql database. Log table contents are not dumped. </p>
<p> If you encounter problems backing up views due to insufficient privileges, see Section 24.9, &#8220;Restrictions on Views&#8221; for a workaround.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1997, 2020, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Downgrade Notes</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://dev.mysql.com/doc/refman/5.7/en/downgrading-to-previous-series.html">https://dev.mysql.com/doc/refman/5.7/en/downgrading-to-previous-series.html</a></dl>
</dl>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
