---
title: "mysqlslap(1)"
name: "mysqlslap"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqlslap/"
description: "mysqlslap – load emulation client"
---

<h2 class="name">NAME</h2>
<p> mysqlslap &#8211; load emulation client </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqlslap [</code><i>options</i><code>]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>mysqlslap</code></p>
<dd>is a diagnostic program designed to emulate client load for a MySQL server and to report the timing of each stage. It works as if multiple clients are accessing the server. </p>
<p> Invoke <code>mysqlslap</code> like this: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlslap [</code><i>options</i><code>]</code>
</pre>
</dl>
<p> Some options such as <code>&#8211;create</code> or <code>&#8211;query</code> enable you to specify a string containing an SQL statement or a file containing statements. If you specify a file, by default it must contain one statement per line. (That is, the implicit statement delimiter is the newline character.) Use the <code>&#8211;delimiter</code> option to specify a different delimiter, which enables you to specify statements that span multiple lines or place multiple statements on a single line. You cannot include comments in a file; <code>mysqlslap</code> does not understand them. </p>
<p> <code>mysqlslap</code> runs in three stages: </p>
<dl>
<dt>
<dd> 1. Create schema, table, and optionally any stored programs or data to use for the test. This stage uses a single client connection.</dl>
<dl>
<dt>
<dd> 2. Run the load test. This stage can use many client connections.</dl>
<dl>
<dt>
<dd> 3. Clean up (disconnect, drop table if specified). This stage uses a single client connection.</dl>
<p> Examples: </p>
<p> Supply your own create and query SQL statements, with 50 clients querying and 200 selects for each (enter the command on a single line): </p>
<dl>
<dt>
<dd>
<pre><code>
mysqlslap-- delimiter = ";" --create = "CREATE TABLE a (b int);INSERT INTO a VALUES (23)" --query = "SELECT * FROM a" --concurrency = 50 --iterations = 200
</code></pre>
</dl>
<p> Let <code>mysqlslap</code> build the query SQL statement with a table of two INT columns and three VARCHAR columns. Use five clients querying 20 times each. Do not create the table or insert the data (that is, use the previous test&#8217;s schema and data): </p>
<dl>
<dt>
<dd>
mysqlslap&#8211; concurrency = 5 &#8211;iterations = 20 &#8211;number &#8211; int &#8211; cols = 2 &#8211;number &#8211; char &#8211; cols = 3 &#8211;auto &#8211; generate &#8211; sql
</dl>
<p> Tell the program to load the create, insert, and query SQL statements from the specified files, where the create.sql file has multiple table creation statements delimited by &#8216;;&#8217; and multiple insert statements delimited by &#8216;;&#8217;. The <code>&#8211;query</code> file will have multiple queries delimited by &#8216;;&#8217;. Run all the load statements, then run all the queries in the query file with five clients (five times each): </p>
<dl>
<dt>
<dd>
mysqlslap&#8211; concurrency = 5 &#8211;iterations = 5 &#8211;query = query.sql&#8211; create = create.sql&#8211; delimiter = &#8220;;&#8221;
</dl>
<p> <code>mysqlslap</code> supports the following options, which can be specified on the command line or in the [mysqlslap] and [client] groups of an option file. For information about option files used by MySQL programs, see Section 4.2.2.2, &#8220;Using Option Files&#8221;. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;auto-generate-sql</code>, <code>-a</code> </p>
<p> Generate SQL statements automatically when they are not supplied in files or using command options.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;auto-generate-sql-add-autoincrement</code> </p>
<p> Add an AUTO_INCREMENT column to automatically generated tables.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;auto-generate-sql-execute-number=</code><i>N</i> </p>
<p> Specify how many queries to generate automatically.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;auto-generate-sql-guid-primary</code> </p>
<p> Add a GUID-based primary key to automatically generated tables.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;auto-generate-sql-load-type=</code><i>type</i> </p>
<p> Specify the test load type. The permissible values are read (scan tables), write (insert into tables), key (read primary keys), update (update primary keys), or mixed (half inserts, half scanning selects). The default is mixed.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;auto-generate-sql-secondary-indexes=</code><i>N</i> </p>
<p> Specify how many secondary indexes to add to automatically generated tables. By default, none are added.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;auto-generate-sql-unique-query-number=</code><i>N</i> </p>
<p> How many different queries to generate for automatic tests. For example, if you run a key test that performs 1000 selects, you can use this option with a value of 1000 to run 1000 unique queries, or with a value of 50 to perform 50 different selects. The default is 10.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;auto-generate-sql-unique-write-number=</code><i>N</i> </p>
<p> How many different queries to generate for <code>&#8211;auto-generate-sql-write-number</code>. The default is 10.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;auto-generate-sql-write-number=</code><i>N</i> </p>
<p> How many row inserts to perform. The default is 100.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;commit=</code><i>N</i> </p>
<p> How many statements to execute before committing. The default is 0 (no commits are done).</dl>
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
<dd> &bull; <code>&#8211;concurrency=</code><i>N</i>, <code>-c </code><i>N</i> </p>
<p> The number of parallel clients to simulate.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;create=</code><i>value</i> </p>
<p> The file or string containing the statement to use for creating the table.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;create-schema=</code><i>value</i> </p>
<p> The schema in which to run the tests. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 If the <code>&#8211;auto-generate-sql</code> option is also given, <code>mysqlslap</code> drops the schema at the end of the test run. To avoid this, use the <code>&#8211;no-drop</code> option as well. </p>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;csv[=</code><i>file_name</i><code>]</code> </p>
<p> Generate output in comma-separated values format. The output goes to the named file, or to the standard output if no file is given.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug[=</code><i>debug_options</i><code>]</code>, <code>-# [</code><i>debug_options</i><code>]</code> </p>
<p> Write a debugging log. A typical <i>debug_options</i> string is d:t:o,<i>file_name</i>. The default is d:t:o,/tmp/mysqlslap.trace. </p>
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
<p> Read not only the usual option groups, but also groups with the usual names and a suffix of <i>str</i>. For example, <code>mysqlslap</code> normally reads the [client] and [mysqlslap] groups. If the <code>&#8211;defaults-group-suffix=_other</code> option is given, <code>mysqlslap</code> also reads the [client_other] and [mysqlslap_other] groups. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;delimiter=</code><i>str</i>, <code>-F </code><i>str</i> </p>
<p> The delimiter to use in SQL statements supplied in files or using command options.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;detach=</code><i>N</i> </p>
<p> Detach (close and reopen) each connection after each <i>N</i> statements. The default is 0 (connections are not detached).</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;enable-cleartext-plugin</code> </p>
<p> Enable the mysql_clear_password cleartext authentication plugin. (See Section 6.4.1.4, &#8220;Client-Side Cleartext Pluggable Authentication&#8221;.)</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;engine=</code><i>engine_name</i>, <code>-e </code><i>engine_name</i> </p>
<p> The storage engine to use for creating tables.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;get-server-public-key</code> </p>
<p> Request from the server the RSA public key that it uses for key pair-based password exchange. This option applies to clients that connect to the server using an account that authenticates with the caching_sha2_password authentication plugin. For connections by such accounts, the server does not send the public key to the client unless requested. The option is ignored for accounts that do not authenticate with that plugin. It is also ignored if RSA-based password exchange is not needed, as is the case when the client connects to the server using a secure connection. </p>
<p> If <code>&#8211;server-public-key-path=</code><i>file_name</i> is given and specifies a valid public key file, it takes precedence over <code>&#8211;get-server-public-key</code>. </p>
<p> For information about the caching_sha2_password plugin, see Section 6.4.1.2, &#8220;Caching SHA-2 Pluggable Authentication&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;host=</code><i>host_name</i>, <code>-h </code><i>host_name</i> </p>
<p> Connect to the MySQL server on the given host.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;iterations=</code><i>N</i>, <code>-i </code><i>N</i> </p>
<p> The number of times to run the tests.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;login-path=</code><i>name</i> </p>
<p> Read options from the named login path in the .mylogin.cnf login path file. A &#8220;login path&#8221; is an option group containing options that specify which MySQL server to connect to and which account to authenticate as. To create or modify a login path file, use the <code>mysql_config_editor</code> utility. See <code><a href="/docs/linux/man/1-mysql_config_editor/">mysql_config_editor</a></code>(1). </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-drop</code> </p>
<p> Prevent <code>mysqlslap</code> from dropping any schema it creates during the test run.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-defaults</code> </p>
<p> Do not read any option files. If program startup fails due to reading unknown options from an option file, <code>&#8211;no-defaults</code> can be used to prevent them from being read. </p>
<p> The exception is that the .mylogin.cnf file, if it exists, is read in all cases. This permits passwords to be specified in a safer way than on the command line even when <code>&#8211;no-defaults</code> is used. (.mylogin.cnf is created by the <code>mysql_config_editor</code> utility. See <code><a href="/docs/linux/man/1-mysql_config_editor/">mysql_config_editor</a></code>(1).) </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;number-char-cols=</code><i>N</i>, <code>-x </code><i>N</i> </p>
<p> The number of VARCHAR columns to use if <code>&#8211;auto-generate-sql</code> is specified.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;number-int-cols=</code><i>N</i>, <code>-y </code><i>N</i> </p>
<p> The number of INT columns to use if <code>&#8211;auto-generate-sql</code> is specified.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;number-of-queries=</code><i>N</i> </p>
<p> Limit each client to approximately this many queries. Query counting takes into account the statement delimiter. For example, if you invoke <code>mysqlslap</code> as follows, the ; delimiter is recognized so that each instance of the query string counts as two queries. As a result, 5 rows (not 10) are inserted. </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; mysqlslap-- delimiter = ";" --number - of - queries = 10 --query = "use test;insert into t values(null)"
</code></pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;only-print</code> </p>
<p> Do not connect to databases. <code>mysqlslap</code> only prints what it would have done.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;password[=</code><i>password</i><code>]</code>, <code>-p[</code><i>password</i><code>]</code> </p>
<p> The password of the MySQL account used for connecting to the server. The password value is optional. If not given, <code>mysqlslap</code> prompts for one. If given, there must be <i>no space</i> between <code>&#8211;password=</code> or <code>-p</code> and the password following it. If no password option is specified, the default is to send no password. </p>
<p> Specifying a password on the command line should be considered insecure. To avoid giving the password on the command line, use an option file. See Section 6.1.2.1, &#8220;End-User Guidelines for Password Security&#8221;. </p>
<p> To explicitly specify that there is no password and that <code>mysqlslap</code> should not prompt for one, use the <code>&#8211;skip-password</code> option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;pipe</code>, <code>-W</code> </p>
<p> On Windows, connect to the server using a named pipe. This option applies only if the server was started with the named_pipe system variable enabled to support named-pipe connections. In addition, the user making the connection must be a member of the Windows group specified by the named_pipe_full_access_group system variable.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;plugin-dir=</code><i>dir_name</i> </p>
<p> The directory in which to look for plugins. Specify this option if the <code>&#8211;default-auth</code> option is used to specify an authentication plugin but <code>mysqlslap</code> does not find it. See Section 6.2.17, &#8220;Pluggable Authentication&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;port=</code><i>port_num</i>, <code>-P </code><i>port_num</i> </p>
<p> For TCP/IP connections, the port number to use.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;post-query=</code><i>value</i> </p>
<p> The file or string containing the statement to execute after the tests have completed. This execution is not counted for timing purposes.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;post-system=</code><i>str</i> </p>
<p> The string to execute using system() after the tests have completed. This execution is not counted for timing purposes.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;pre-query=</code><i>value</i> </p>
<p> The file or string containing the statement to execute before running the tests. This execution is not counted for timing purposes.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;pre-system=</code><i>str</i> </p>
<p> The string to execute using system() before running the tests. This execution is not counted for timing purposes.</dl>
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
<dd> &bull; <code>&#8211;query=</code><i>value</i>, <code>-q </code><i>value</i> </p>
<p> The file or string containing the SELECT statement to use for retrieving data.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;server-public-key-path=</code><i>file_name</i> </p>
<p> The path name to a file containing a client-side copy of the public key required by the server for RSA key pair-based password exchange. The file must be in PEM format. This option applies to clients that authenticate with the sha256_password or caching_sha2_password authentication plugin. This option is ignored for accounts that do not authenticate with one of those plugins. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection. </p>
<p> If <code>&#8211;server-public-key-path=</code><i>file_name</i> is given and specifies a valid public key file, it takes precedence over <code>&#8211;get-server-public-key</code>. </p>
<p> For sha256_password, this option applies only if MySQL was built using OpenSSL. </p>
<p> For information about the sha256_password and caching_sha2_password plugins, see Section 6.4.1.3, &#8220;SHA-256 Pluggable Authentication&#8221;, and Section 6.4.1.2, &#8220;Caching SHA-2 Pluggable Authentication&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;shared-memory-base-name=</code><i>name</i> </p>
<p> On Windows, the shared-memory name to use for connections made using shared memory to a local server. The default value is MYSQL. The shared-memory name is case-sensitive. </p>
<p> This option applies only if the server was started with the shared_memory system variable enabled to support shared-memory connections.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;silent</code>, <code>-s</code> </p>
<p> Silent mode. No output.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;socket=</code><i>path</i>, <code>-S </code><i>path</i> </p>
<p> For connections to localhost, the Unix socket file to use, or, on Windows, the name of the named pipe to use. </p>
<p> On Windows, this option applies only if the server was started with the named_pipe system variable enabled to support named-pipe connections. In addition, the user making the connection must be a member of the Windows group specified by the named_pipe_full_access_group system variable.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;sql-mode=</code><i>mode</i> </p>
<p> Set the SQL mode for the client session.</dl>
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
<dd> &bull; <code>&#8211;verbose</code>, <code>-v</code> </p>
<p> Verbose mode. Print more information about what the program does. This option can be used multiple times to increase the amount of information.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code>, <code>-V</code> </p>
<p> Display version information and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;zstd-compression-level=</code><i>level</i> The compression level to use for connections to the server that use the zstd compression algorithm. The permitted levels are from 1 to 22, with larger values indicating increasing levels of compression. The default zstd compression level is 3. The compression level setting has no effect on connections that do not use zstd compression. </p>
<p> For more information, see Section 4.2.6, &#8220;Connection Compression Control&#8221;. </p>
<p> This option was added in MySQL 8.0.18.</dl>
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
