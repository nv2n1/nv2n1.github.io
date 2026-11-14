---
title: "mysqladmin(1)"
name: "mysqladmin"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqladmin/"
description: "mysqladmin – client for administering a MySQL server"
---

<h2 class="name">NAME</h2>
<p> mysqladmin &#8211; client for administering a MySQL server </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqladmin [</code><i>options</i><code>] </code><i>command</i><code> [</code><i>command-options</i><code>] [</code><i>command</i><code> [</code><i>command-options</i><code>]] &#8230;</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>mysqladmin</code></p>
<dd>is a client for performing administrative operations. You can use it to check the server&#8217;s configuration and current status, to create and drop databases, and more. </p>
<p> Invoke <code>mysqladmin</code> like this: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; mysqladmin[options] command[command - arg][command[command - arg]]...
</code></pre>
</dl>
<p> <code>mysqladmin</code> supports the following commands. Some of the commands take an argument following the command name. </p>
<dl>
<dt>
<dd> &bull; create <i>db_name</i> </p>
<p> Create a new database named <i>db_name</i>.</dl>
<dl>
<dt>
<dd> &bull; debug </p>
<p> Tell the server to write debug information to the error log. The connected user must have the SUPER privilege. Format and content of this information is subject to change. </p>
<p> This includes information about the Event Scheduler. See Section 24.4.5, &#8220;Event Scheduler Status&#8221;.</dl>
<dl>
<dt>
<dd> &bull; drop <i>db_name</i> </p>
<p> Delete the database named <i>db_name</i> and all its tables.</dl>
<dl>
<dt>
<dd> &bull; extended-status </p>
<p> Display the server status variables and their values.</dl>
<dl>
<dt>
<dd> &bull; flush-hosts </p>
<p> Flush all information in the host cache. See Section 8.12.4.2, &#8220;DNS Lookup Optimization and the Host Cache&#8221;.</dl>
<dl>
<dt>
<dd> &bull; flush-logs [<i>log_type</i> &#8230;] </p>
<p> Flush all logs. </p>
<p> The <code>mysqladmin flush-logs</code> command permits optional log types to be given, to specify which logs to flush. Following the flush-logs command, you can provide a space-separated list of one or more of the following log types: binary, engine, error, general, relay, slow. These correspond to the log types that can be specified for the FLUSH LOGS SQL statement.</dl>
<dl>
<dt>
<dd> &bull; flush-privileges </p>
<p> Reload the grant tables (same as reload).</dl>
<dl>
<dt>
<dd> &bull; flush-status </p>
<p> Clear status variables.</dl>
<dl>
<dt>
<dd> &bull; flush-tables </p>
<p> Flush all tables.</dl>
<dl>
<dt>
<dd> &bull; flush-threads </p>
<p> Flush the thread cache.</dl>
<dl>
<dt>
<dd> &bull; kill <i>id</i>,<i>id</i>,&#8230; </p>
<p> Kill server threads. If multiple thread ID values are given, there must be no spaces in the list. </p>
<p> To kill threads belonging to other users, the connected user must have the CONNECTION_ADMIN or SUPER privilege.</dl>
<dl>
<dt>
<dd> &bull; password <i>new_password</i> </p>
<p> Set a new password. This changes the password to <i>new_password</i> for the account that you use with <code>mysqladmin</code> for connecting to the server. Thus, the next time you invoke <code>mysqladmin</code> (or any other client program) using the same account, you will need to specify the new password. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Warning</code> </font><br />
 Setting a password using <code>mysqladmin</code> should be considered <i>insecure</i>. On some systems, your password becomes visible to system status programs such as <code>ps</code> that may be invoked by other users to display command lines. MySQL clients typically overwrite the command-line password argument with zeros during their initialization sequence. However, there is still a brief interval during which the value is visible. Also, on some systems this overwriting strategy is ineffective and the password remains visible to <code>ps</code>. (SystemV Unix systems and perhaps others are subject to this problem.) </p>
</dl>
<p> If the <i>new_password</i> value contains spaces or other characters that are special to your command interpreter, you need to enclose it within quotation marks. On Windows, be sure to use double quotation marks rather than single quotation marks; single quotation marks are not stripped from the password, but rather are interpreted as part of the password. For example: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqladmin password &quot;my new password&quot;</code>
</pre>
</dl>
<p> The new password can be omitted following the password command. In this case, <code>mysqladmin</code> prompts for the password value, which enables you to avoid specifying the password on the command line. Omitting the password value should be done only if password is the final command on the <code>mysqladmin</code> command line. Otherwise, the next argument is taken as the password. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Caution</code> </font><br />
 Do not use this command used if the server was started with the <code>&#8211;skip-grant-tables</code> option. No password change will be applied. This is true even if you precede the password command with flush-privileges on the same command line to re-enable the grant tables because the flush operation occurs after you connect. However, you can use <code>mysqladmin flush-privileges</code> to re-enable the grant table and then use a separate <code>mysqladmin password</code> command to change the password. </p>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; ping </p>
<p> Check whether the server is available. The return status from <code>mysqladmin</code> is 0 if the server is running, 1 if it is not. This is 0 even in case of an error such as Access denied, because this means that the server is running but refused the connection, which is different from the server not running.</dl>
<dl>
<dt>
<dd> &bull; processlist </p>
<p> Show a list of active server threads. This is like the output of the SHOW PROCESSLIST statement. If the <code>&#8211;verbose</code> option is given, the output is like that of SHOW FULL PROCESSLIST. (See Section 13.7.7.29, &#8220;SHOW PROCESSLIST Statement&#8221;.)</dl>
<dl>
<dt>
<dd> &bull; reload </p>
<p> Reload the grant tables.</dl>
<dl>
<dt>
<dd> &bull; refresh </p>
<p> Flush all tables and close and open log files.</dl>
<dl>
<dt>
<dd> &bull; shutdown </p>
<p> Stop the server.</dl>
<dl>
<dt>
<dd> &bull; start-slave </p>
<p> Start replication on a slave server.</dl>
<dl>
<dt>
<dd> &bull; status </p>
<p> Display a short server status message.</dl>
<dl>
<dt>
<dd> &bull; stop-slave </p>
<p> Stop replication on a slave server.</dl>
<dl>
<dt>
<dd> &bull; variables </p>
<p> Display the server system variables and their values.</dl>
<dl>
<dt>
<dd> &bull; version </p>
<p> Display version information from the server.</dl>
<p> All commands can be shortened to any unique prefix. For example: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; mysqladmin proc stat + -- --+-- -- -- -+-- -- -- -- -- -+-- --+-- -- -- -- -+-- -- --+-- -- -- -+-- -- -- -- -- -- -- -- --+ | Id | User | Host | db | Command | Time | State | Info |
    +-- --+-- -- -- -+-- -- -- -- -- -+-- --+-- -- -- -- -+-- -- --+-- -- -- -+-- -- -- -- -- -- -- -- --+ | 51 | jones | localhost | | Query | 0 | | show processlist |
    +-- --+-- -- -- -+-- -- -- -- -- -+-- --+-- -- -- -- -+-- -- --+-- -- -- -+-- -- -- -- -- -- -- -- --+Uptime : 1473624 Threads : 1 Questions : 39487 Slow queries : 0 Opens : 541 Flush tables : 1 Open tables : 19 Queries per second avg : 0.0268
</code></pre>
</dl>
<p> The <code>mysqladmin status</code> command result displays the following values: </p>
<dl>
<dt>
<dd> &bull; Uptime </p>
<p> The number of seconds the MySQL server has been running.</dl>
<dl>
<dt>
<dd> &bull; Threads </p>
<p> The number of active threads (clients).</dl>
<dl>
<dt>
<dd> &bull; Questions </p>
<p> The number of questions (queries) from clients since the server was started.</dl>
<dl>
<dt>
<dd> &bull; Slow queries </p>
<p> The number of queries that have taken more than long_query_time seconds. See Section 5.4.5, &#8220;The Slow Query Log&#8221;.</dl>
<dl>
<dt>
<dd> &bull; Opens </p>
<p> The number of tables the server has opened.</dl>
<dl>
<dt>
<dd> &bull; Flush tables </p>
<p> The number of flush-*, refresh, and reload commands the server has executed.</dl>
<dl>
<dt>
<dd> &bull; Open tables </p>
<p> The number of tables that currently are open.</dl>
<p> If you execute <code>mysqladmin shutdown</code> when connecting to a local server using a Unix socket file, <code>mysqladmin</code> waits until the server&#8217;s process ID file has been removed, to ensure that the server has stopped properly. </p>
<p> <code>mysqladmin</code> supports the following options, which can be specified on the command line or in the [mysqladmin] and [client] groups of an option file. For information about option files used by MySQL programs, see Section 4.2.2.2, &#8220;Using Option Files&#8221;. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;bind-address=</code><i>ip_address</i> </p>
<p> On a computer having multiple network interfaces, use this option to select which interface to use for connecting to the MySQL server.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;character-sets-dir=</code><i>dir_name</i> </p>
<p> The directory where character sets are installed. See Section 10.15, &#8220;Character Set Configuration&#8221;.</dl>
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
<dd> &bull; <code>&#8211;count=</code><i>N</i>, <code>-c </code><i>N</i> </p>
<p> The number of iterations to make for repeated command execution if the <code>&#8211;sleep</code> option is given.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug[=</code><i>debug_options</i><code>]</code>, <code>-# [</code><i>debug_options</i><code>]</code> </p>
<p> Write a debugging log. A typical <i>debug_options</i> string is d:t:o,<i>file_name</i>. The default is d:t:o,/tmp/mysqladmin.trace. </p>
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
<dd> &bull; <code>&#8211;default-auth=</code><i>plugin</i> </p>
<p> A hint about which client-side authentication plugin to use. See Section 6.2.17, &#8220;Pluggable Authentication&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;default-character-set=</code><i>charset_name</i> </p>
<p> Use <i>charset_name</i> as the default character set. See Section 10.15, &#8220;Character Set Configuration&#8221;.</dl>
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
<p> Read not only the usual option groups, but also groups with the usual names and a suffix of <i>str</i>. For example, <code>mysqladmin</code> normally reads the [client] and [mysqladmin] groups. If the <code>&#8211;defaults-group-suffix=_other</code> option is given, <code>mysqladmin</code> also reads the [client_other] and [mysqladmin_other] groups. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;enable-cleartext-plugin</code> </p>
<p> Enable the mysql_clear_password cleartext authentication plugin. (See Section 6.4.1.4, &#8220;Client-Side Cleartext Pluggable Authentication&#8221;.)</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;force</code>, <code>-f</code> </p>
<p> Do not ask for confirmation for the drop <i>db_name</i> command. With multiple commands, continue even if an error occurs.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;get-server-public-key</code> </p>
<p> Request from the server the public key required for RSA key pair-based password exchange. This option applies to clients that authenticate with the caching_sha2_password authentication plugin. For that plugin, the server does not send the public key unless requested. This option is ignored for accounts that do not authenticate with that plugin. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection. </p>
<p> If <code>&#8211;server-public-key-path=</code><i>file_name</i> is given and specifies a valid public key file, it takes precedence over <code>&#8211;get-server-public-key</code>. </p>
<p> For information about the caching_sha2_password plugin, see Section 6.4.1.2, &#8220;Caching SHA-2 Pluggable Authentication&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;host=</code><i>host_name</i>, <code>-h </code><i>host_name</i> </p>
<p> Connect to the MySQL server on the given host.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;login-path=</code><i>name</i> </p>
<p> Read options from the named login path in the .mylogin.cnf login path file. A &#8220;login path&#8221; is an option group containing options that specify which MySQL server to connect to and which account to authenticate as. To create or modify a login path file, use the <code>mysql_config_editor</code> utility. See <code><a href="/docs/linux/man/1-mysql_config_editor/">mysql_config_editor</a></code>(1). </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-beep</code>, <code>-b</code> </p>
<p> Suppress the warning beep that is emitted by default for errors such as a failure to connect to the server.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-defaults</code> </p>
<p> Do not read any option files. If program startup fails due to reading unknown options from an option file, <code>&#8211;no-defaults</code> can be used to prevent them from being read. </p>
<p> The exception is that the .mylogin.cnf file, if it exists, is read in all cases. This permits passwords to be specified in a safer way than on the command line even when <code>&#8211;no-defaults</code> is used. (.mylogin.cnf is created by the <code>mysql_config_editor</code> utility. See <code><a href="/docs/linux/man/1-mysql_config_editor/">mysql_config_editor</a></code>(1).) </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;password[=</code><i>password</i><code>]</code>, <code>-p[</code><i>password</i><code>]</code> </p>
<p> The password of the MySQL account used for connecting to the server. The password value is optional. If not given, <code>mysqladmin</code> prompts for one. If given, there must be <i>no space</i> between <code>&#8211;password=</code> or <code>-p</code> and the password following it. If no password option is specified, the default is to send no password. </p>
<p> Specifying a password on the command line should be considered insecure. To avoid giving the password on the command line, use an option file. See Section 6.1.2.1, &#8220;End-User Guidelines for Password Security&#8221;. </p>
<p> To explicitly specify that there is no password and that <code>mysqladmin</code> should not prompt for one, use the <code>&#8211;skip-password</code> option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;pipe</code>, <code>-W</code> </p>
<p> On Windows, connect to the server using a named pipe. This option applies only if the server was started with the named_pipe system variable enabled to support named-pipe connections. In addition, the user making the connection must be a member of the Windows group specified by the named_pipe_full_access_group system variable.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;plugin-dir=</code><i>dir_name</i> </p>
<p> The directory in which to look for plugins. Specify this option if the <code>&#8211;default-auth</code> option is used to specify an authentication plugin but <code>mysqladmin</code> does not find it. See Section 6.2.17, &#8220;Pluggable Authentication&#8221;.</dl>
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
<dd> &bull; <code>&#8211;relative</code>, <code>-r</code> </p>
<p> Show the difference between the current and previous values when used with the <code>&#8211;sleep</code> option. This option works only with the extended-status command.</dl>
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
<dd> &bull; <code>&#8211;show-warnings</code> </p>
<p> Show warnings resulting from execution of statements sent to the server.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;silent</code>, <code>-s</code> </p>
<p> Exit silently if a connection to the server cannot be established.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;sleep=</code><i>delay</i>, <code>-i </code><i>delay</i> </p>
<p> Execute commands repeatedly, sleeping for <i>delay</i> seconds in between. The <code>&#8211;count</code> option determines the number of iterations. If <code>&#8211;count</code> is not given, <code>mysqladmin</code> executes commands indefinitely until interrupted.</dl>
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
<dd> &bull; <code>&#8211;verbose</code>, <code>-v</code> </p>
<p> Verbose mode. Print more information about what the program does.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code>, <code>-V</code> </p>
<p> Display version information and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;vertical</code>, <code>-E</code> </p>
<p> Print output vertically. This is similar to <code>&#8211;relative</code>, but prints output vertically.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;wait[=</code><i>count</i><code>]</code>, <code>-w[</code><i>count</i><code>]</code> </p>
<p> If the connection cannot be established, wait and retry instead of aborting. If a <i>count</i> value is given, it indicates the number of times to retry. The default is one time.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;zstd-compression-level=</code><i>level</i> The compression level to use for connections to the server that use the zstd compression algorithm. The permitted levels are from 1 to 22, with larger values indicating increasing levels of compression. The default zstd compression level is 3. The compression level setting has no effect on connections that do not use zstd compression. </p>
<p> For more information, see Section 4.2.6, &#8220;Connection Compression Control&#8221;. </p>
<p> This option was added in MySQL 8.0.18.</dl>
<p> You can also set the following variables by using <code>&#8212;</code><i>var_name</i><code>=</code><i>value</i>. </p>
<dl>
<dt>
<dd> &bull; connect_timeout </p>
<p> The maximum number of seconds before connection timeout. The default value is 43200 (12 hours).</dl>
<dl>
<dt>
<dd> &bull; shutdown_timeout </p>
<p> The maximum number of seconds to wait for server shutdown. The default value is 3600 (1 hour).</dl>
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
