---
title: "mysqlbinlog(1)"
name: "mysqlbinlog"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqlbinlog/"
description: "mysqlbinlog – utility for processing binary log files"
---

<h2 class="name">NAME</h2>
<p> mysqlbinlog &#8211; utility for processing binary log files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqlbinlog [</code><code>options</code><code>] </code><i>log_file</i><code> &#8230;</code></dl>
<h2>DESCRIPTION</h2>
<dd>The server&#8217;s binary log consists of files containing &#8220;events&#8221; that describe modifications to database contents. The server writes these files in binary format. To display their contents in text format, use the <code>mysqlbinlog</code> utility. You can also use <code>mysqlbinlog</code> to display the contents of relay log files written by a slave server in a replication setup because relay logs have the same format as binary logs. The binary log and relay log are discussed further in Section 5.4.4, &#8220;The Binary Log&#8221;, and Section 17.2.4, &#8220;Replication Relay and Status Logs&#8221;. </p>
<p> Invoke <code>mysqlbinlog</code> like this: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlbinlog [</code><i>options</i><code>] </code><i>log_file</i><code> ...</code>
</pre>
</dl>
<p> For example, to display the contents of the binary log file named binlog.000003, use this command: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlbinlog binlog.0000003</code>
</pre>
</dl>
<p> The output includes events contained in binlog.000003. For statement-based logging, event information includes the SQL statement, the ID of the server on which it was executed, the timestamp when the statement was executed, how much time it took, and so forth. For row-based logging, the event indicates a row change rather than an SQL statement. See Section 17.2.1, &#8220;Replication Formats&#8221;, for information about logging modes. </p>
<p> Events are preceded by header comments that provide additional information. For example: </p>
<dl>
<dt>
<dd>
<pre>
# at 141
#100309  9:28:36 server id 123  end_log_pos 245
  Query thread_id=3350  exec_time=11  error_code=0
</pre>
</dl>
<p> In the first line, the number following at indicates the file offset, or starting position, of the event in the binary log file. </p>
<p> The second line starts with a date and time indicating when the statement started on the server where the event originated. For replication, this timestamp is propagated to slave servers. server id is the server_id value of the server where the event originated. end_log_pos indicates where the next event starts (that is, it is the end position of the current event + 1). thread_id indicates which thread executed the event. exec_time is the time spent executing the event, on a master server. On a slave, it is the difference of the end execution time on the slave minus the beginning execution time on the master. The difference serves as an indicator of how much replication lags behind the master. error_code indicates the result from executing the event. Zero means that no error occurred. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> When using event groups, the file offsets of events may be grouped together and the comments of events may be grouped together. Do not mistake these grouped events for blank file offsets. </p>
</dl>
<p> The output from <code>mysqlbinlog</code> can be re-executed (for example, by using it as input to <code>mysql</code>) to redo the statements in the log. This is useful for recovery operations after a server crash. For other usage examples, see the discussion later in this section and in Section 7.5, &#8220;Point-in-Time (Incremental) Recovery Using the Binary Log&#8221;. To execute the internal-use BINLOG statements used by <code>mysqlbinlog</code>, the user requires the BINLOG_ADMIN or SUPER privilege, or the REPLICATION_APPLIER privilege plus the appropriate privileges to execute each log event. </p>
<p> You can use <code>mysqlbinlog</code> to read binary log files directly and apply them to the local MySQL server. You can also read binary logs from a remote server by using the <code>&#8211;read-from-remote-server</code> option. To read remote binary logs, the connection parameter options can be given to indicate how to connect to the server. These options are <code>&#8211;host</code>, <code>&#8211;password</code>, <code>&#8211;port</code>, <code>&#8211;protocol</code>, <code>&#8211;socket</code>, and <code>&#8211;user</code>. </p>
<p> When binary log files have been encrypted, which can be done from MySQL 8.0.14 onwards, <code>mysqlbinlog</code> cannot read them directly, but can read them from the server using the <code>&#8211;read-from-remote-server</code> option. Binary log files are encrypted when the server&#8217;s binlog_encryption system variable is set to ON. The SHOW BINARY LOGS statement shows whether a particular binary log file is encrypted or unencrypted. Encrypted and unencrypted binary log files can also be distinguished using the magic number at the start of the file header for encrypted log files (0xFD62696E), which differs from that used for unencrypted log files (0xFE62696E). Note that from MySQL 8.0.14, <code>mysqlbinlog</code> returns a suitable error if you attempt to read an encrypted binary log file directly, but older versions of <code>mysqlbinlog</code> do not recognise the file as a binary log file at all. For more information on binary log encryption, see Section 17.3.2, &#8220;Encrypting Binary Log Files and Relay Log Files&#8221;. </p>
<p> When running <code>mysqlbinlog</code> against a large binary log, be careful that the filesystem has enough space for the resulting files. To configure the directory that <code>mysqlbinlog</code> uses for temporary files, use the TMPDIR environment variable. </p>
<p> <code>mysqlbinlog</code> sets the value of pseudo_slave_mode to true before executing any SQL statements. This system variable affects the handling of XA transactions, the original_commit_timestamp replication delay timestamp and the original_server_version system variable, and unsupported SQL modes. </p>
<p> <code>mysqlbinlog</code> supports the following options, which can be specified on the command line or in the [mysqlbinlog] and [client] groups of an option file. For information about option files used by MySQL programs, see Section 4.2.2.2, &#8220;Using Option Files&#8221;. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;base64-output=</code><i>value</i> </p>
<p> This option determines when events should be displayed encoded as base-64 strings using BINLOG statements. The option has these permissible values (not case-sensitive): </p>
<dl>
<dt>
<dd> &bull; AUTO (&quot;automatic&quot;) or UNSPEC (&quot;unspecified&quot;) displays BINLOG statements automatically when necessary (that is, for format description events and row events). If no <code>&#8211;base64-output</code> option is given, the effect is the same as <code>&#8211;base64-output=AUTO</code>. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 Automatic BINLOG display is the only safe behavior if you intend to use the output of <code>mysqlbinlog</code> to re-execute binary log file contents. The other option values are intended only for debugging or testing purposes because they may produce output that does not include all events in executable form. </p>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; NEVER causes BINLOG statements not to be displayed. <code>mysqlbinlog</code> exits with an error if a row event is found that must be displayed using BINLOG.</dl>
<dl>
<dt>
<dd> &bull; DECODE-ROWS specifies to <code>mysqlbinlog</code> that you intend for row events to be decoded and displayed as commented SQL statements by also specifying the <code>&#8211;verbose</code> option. Like NEVER, DECODE-ROWS suppresses display of BINLOG statements, but unlike NEVER, it does not exit with an error if a row event is found.</dl>
<p> For examples that show the effect of <code>&#8211;base64-output</code> and <code>&#8211;verbose</code> on row event output, see the section called &#8220;MYSQLBINLOG ROW EVENT DISPLAY&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;bind-address=</code><i>ip_address</i> </p>
<p> On a computer having multiple network interfaces, use this option to select which interface to use for connecting to the MySQL server.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;binlog-row-event-max-size=</code><i>N</i> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Value </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td> &#8211;binlog-row-event-max-size=#
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> Numeric
</td>
</tr>
<tr VALIGN=top>
<td> <code>Default Value</code> </td>
<td> 4294967040
</td>
</tr>
<tr VALIGN=top>
<td> <code>Minimum Value</code> </td>
<td> 256
</td>
</tr>
<tr VALIGN=top>
<td> <code>Maximum Value</code> </td>
<td> 18446744073709547520
</td>
</tr>
</table>
<p> Specify the maximum size of a row-based binary log event, in bytes. Rows are grouped into events smaller than this size if possible. The value should be a multiple of 256. The default is 4GB.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;character-sets-dir=</code><i>dir_name</i> </p>
<p> The directory where character sets are installed. See Section 10.15, &#8220;Character Set Configuration&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;compress</code> </p>
<p> Compress all information sent between the client and the server if possible. See Section 4.2.6, &#8220;Connection Compression Control&#8221;. </p>
<p> This option was added in MySQL 8.0.17. As of MySQL 8.0.18 it is deprecated. It will be removed in a future MySQL version. See the section called &#8220;Legacy Connection Compression Configuration&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;compression-algorithms=</code><i>value</i> The permitted compression algorithms for connections to the server. The available algorithms are the same as for the protocol_compression_algorithms system variable. The default value is uncompressed. </p>
<p> For more information, see Section 4.2.6, &#8220;Connection Compression Control&#8221;. </p>
<p> This option was added in MySQL 8.0.18.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;connection-server-id=</code><i>server_id</i> </p>
<p> <code>&#8211;connection-server-id</code> specifies the server ID that <code>mysqlbinlog</code> reports when it connects to the server. It can be used to avoid a conflict with the ID of a slave server or another <code>mysqlbinlog</code> process. </p>
<p> If the <code>&#8211;read-from-remote-server</code> option is specified, <code>mysqlbinlog</code> reports a server ID of 0, which tells the server to disconnect after sending the last log file (nonblocking behavior). If the <code>&#8211;stop-never</code> option is also specified to maintain the connection to the server, <code>mysqlbinlog</code> reports a server ID of 1 by default instead of 0, and <code>&#8211;connection-server-id</code> can be used to replace that server ID if required. See the section called &#8220;SPECIFYING THE MYSQLBINLOG SERVER ID&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;database=</code><i>db_name</i>, <code>-d </code><i>db_name</i> </p>
<p> This option causes <code>mysqlbinlog</code> to output entries from the binary log (local log only) that occur while <i>db_name</i> is been selected as the default database by USE. </p>
<p> The <code>&#8211;database</code> option for <code>mysqlbinlog</code> is similar to the <code>&#8211;binlog-do-db</code> option for <code>mysqld</code>, but can be used to specify only one database. If <code>&#8211;database</code> is given multiple times, only the last instance is used. </p>
<p> The effects of this option depend on whether the statement-based or row-based logging format is in use, in the same way that the effects of <code>&#8211;binlog-do-db</code> depend on whether statement-based or row-based logging is in use. </p>
<p> <code>Statement-based logging</code>. The <code>&#8211;database</code> option works as follows: </p>
<dl>
<dt>
<dd> &bull; While <i>db_name</i> is the default database, statements are output whether they modify tables in <i>db_name</i> or a different database.</dl>
<dl>
<dt>
<dd> &bull; Unless <i>db_name</i> is selected as the default database, statements are not output, even if they modify tables in <i>db_name</i>.</dl>
<dl>
<dt>
<dd> &bull; There is an exception for CREATE DATABASE, ALTER DATABASE, and DROP DATABASE. The database being <i>created, altered, or dropped</i> is considered to be the default database when determining whether to output the statement.</dl>
<p> Suppose that the binary log was created by executing these statements using statement-based-logging: </p>
<dl>
<dt>
<dd>
<pre><code>
INSERT INTO test.t1(i) VALUES(100);
INSERT INTO db2.t2(j) VALUES(200);
USE test;
INSERT INTO test.t1(i) VALUES(101);
INSERT INTO t1(i) VALUES(102);
INSERT INTO db2.t2(j) VALUES(201);
USE db2;
INSERT INTO test.t1(i) VALUES(103);
INSERT INTO db2.t2(j) VALUES(202);
INSERT INTO t2(j) VALUES(203);
</code></pre>
</dl>
<p> <code>mysqlbinlog &#8211;database=test</code> does not output the first two INSERT statements because there is no default database. It outputs the three INSERT statements following USE test, but not the three INSERT statements following USE db2. </p>
<p> <code>mysqlbinlog &#8211;database=db2</code> does not output the first two INSERT statements because there is no default database. It does not output the three INSERT statements following USE test, but does output the three INSERT statements following USE db2. </p>
<p> <code>Row-based logging</code>. <code>mysqlbinlog</code> outputs only entries that change tables belonging to <i>db_name</i>. The default database has no effect on this. Suppose that the binary log just described was created using row-based logging rather than statement-based logging. <code>mysqlbinlog &#8211;database=test</code> outputs only those entries that modify t1 in the test database, regardless of whether USE was issued or what the default database is. If a server is running with binlog_format set to MIXED and you want it to be possible to use <code>mysqlbinlog</code> with the <code>&#8211;database</code> option, you must ensure that tables that are modified are in the database selected by USE. (In particular, no cross-database updates should be used.) </p>
<p> When used together with the <code>&#8211;rewrite-db</code> option, the <code>&#8211;rewrite-db</code> option is applied first; then the <code>&#8211;database</code> option is applied, using the rewritten database name. The order in which the options are provided makes no difference in this regard.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug[=</code><i>debug_options</i><code>]</code>, <code>-# [</code><i>debug_options</i><code>]</code> </p>
<p> Write a debugging log. A typical <i>debug_options</i> string is d:t:o,<i>file_name</i>. The default is d:t:o,/tmp/mysqlbinlog.trace. </p>
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
<p> Read not only the usual option groups, but also groups with the usual names and a suffix of <i>str</i>. For example, <code>mysqlbinlog</code> normally reads the [client] and [mysqlbinlog] groups. If the <code>&#8211;defaults-group-suffix=_other</code> option is given, <code>mysqlbinlog</code> also reads the [client_other] and [mysqlbinlog_other] groups. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;disable-log-bin</code>, <code>-D</code> </p>
<p> Disable binary logging. This is useful for avoiding an endless loop if you use the <code>&#8211;to-last-log</code> option and are sending the output to the same MySQL server. This option also is useful when restoring after a crash to avoid duplication of the statements you have logged. </p>
<p> This option causes <code>mysqlbinlog</code> to include a SET sql_log_bin = 0 statement in its output to disable binary logging of the remaining output. Manipulating the session value of the sql_log_bin system variable is a restricted operation, so this option requires that you have privileges sufficient to set restricted session variables. See Section 5.1.9.1, &#8220;System Variable Privileges&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;exclude-gtids=</code><i>gtid_set</i> </p>
<p> Do not display any of the groups listed in the <i>gtid_set</i>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;force-if-open</code>, <code>-F</code> </p>
<p> Read binary log files even if they are open or were not closed properly.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;force-read</code>, <code>-f</code> </p>
<p> With this option, if <code>mysqlbinlog</code> reads a binary log event that it does not recognize, it prints a warning, ignores the event, and continues. Without this option, <code>mysqlbinlog</code> stops if it reads such an event.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;get-server-public-key</code> </p>
<p> Request from the server the public key required for RSA key pair-based password exchange. This option applies to clients that authenticate with the caching_sha2_password authentication plugin. For that plugin, the server does not send the public key unless requested. This option is ignored for accounts that do not authenticate with that plugin. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection. </p>
<p> If <code>&#8211;server-public-key-path=</code><i>file_name</i> is given and specifies a valid public key file, it takes precedence over <code>&#8211;get-server-public-key</code>. </p>
<p> For information about the caching_sha2_password plugin, see Section 6.4.1.2, &#8220;Caching SHA-2 Pluggable Authentication&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;hexdump</code>, <code>-H</code> </p>
<p> Display a hex dump of the log in comments, as described in the section called &#8220;MYSQLBINLOG HEX DUMP FORMAT&#8221;. The hex output can be helpful for replication debugging.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;host=</code><i>host_name</i>, <code>-h </code><i>host_name</i> </p>
<p> Get the binary log from the MySQL server on the given host.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;idempotent</code> </p>
<p> Tell the MySQL Server to use idempotent mode while processing updates; this causes suppression of any duplicate-key or key-not-found errors that the server encounters in the current session while processing updates. This option may prove useful whenever it is desirable or necessary to replay one or more binary logs to a MySQL Server which may not contain all of the data to which the logs refer. </p>
<p> The scope of effect for this option includes the current <code>mysqlbinlog</code> client and session only.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;include-gtids=</code><i>gtid_set</i> </p>
<p> Display only the groups listed in the <i>gtid_set</i>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;local-load=</code><i>dir_name</i>, <code>-l </code><i>dir_name</i> </p>
<p> Prepare local temporary files for LOAD DATA in the specified directory. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Important</code> </font><br />
 These temporary files are not automatically removed by <code>mysqlbinlog</code> or any other MySQL program. </p>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;login-path=</code><i>name</i> </p>
<p> Read options from the named login path in the .mylogin.cnf login path file. A &#8220;login path&#8221; is an option group containing options that specify which MySQL server to connect to and which account to authenticate as. To create or modify a login path file, use the <code>mysql_config_editor</code> utility. See <code><a href="/docs/linux/man/1-mysql_config_editor/">mysql_config_editor</a></code>(1). </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-defaults</code> </p>
<p> Do not read any option files. If program startup fails due to reading unknown options from an option file, <code>&#8211;no-defaults</code> can be used to prevent them from being read. </p>
<p> The exception is that the .mylogin.cnf file, if it exists, is read in all cases. This permits passwords to be specified in a safer way than on the command line even when <code>&#8211;no-defaults</code> is used. (.mylogin.cnf is created by the <code>mysql_config_editor</code> utility. See <code><a href="/docs/linux/man/1-mysql_config_editor/">mysql_config_editor</a></code>(1).) </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;offset=</code><i>N</i>, <code>-o </code><i>N</i> </p>
<p> Skip the first <i>N</i> entries in the log.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;open-files-limit=</code><i>N</i> Specify the number of open file descriptors to reserve.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;password[=</code><i>password</i><code>]</code>, <code>-p[</code><i>password</i><code>]</code> </p>
<p> The password of the MySQL account used for connecting to the server. The password value is optional. If not given, <code>mysqlbinlog</code> prompts for one. If given, there must be <i>no space</i> between <code>&#8211;password=</code> or <code>-p</code> and the password following it. If no password option is specified, the default is to send no password. </p>
<p> Specifying a password on the command line should be considered insecure. To avoid giving the password on the command line, use an option file. See Section 6.1.2.1, &#8220;End-User Guidelines for Password Security&#8221;. </p>
<p> To explicitly specify that there is no password and that <code>mysqlbinlog</code> should not prompt for one, use the <code>&#8211;skip-password</code> option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;plugin-dir=</code><i>dir_name</i> </p>
<p> The directory in which to look for plugins. Specify this option if the <code>&#8211;default-auth</code> option is used to specify an authentication plugin but <code>mysqlbinlog</code> does not find it. See Section 6.2.17, &#8220;Pluggable Authentication&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;port=</code><i>port_num</i>, <code>-P </code><i>port_num</i> </p>
<p> The TCP/IP port number to use for connecting to a remote server.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;print-defaults</code> </p>
<p> Print the program name and all options that it gets from option files. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;print-table-metadata</code> </p>
<p> Print table related metadata from the binary log. Configure the amount of table related metadata binary logged using binlog-row-metadata.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;protocol={TCP|SOCKET|PIPE|MEMORY}</code> </p>
<p> The connection protocol to use for connecting to the server. It is useful when the other connection parameters normally result in use of a protocol other than the one you want. For details on the permissible values, see Section 4.2.4, &#8220;Connecting to the MySQL Server Using Command Options&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;raw</code> </p>
<p> By default, <code>mysqlbinlog</code> reads binary log files and writes events in text format. The <code>&#8211;raw</code> option tells <code>mysqlbinlog</code> to write them in their original binary format. Its use requires that <code>&#8211;read-from-remote-server</code> also be used because the files are requested from a server. <code>mysqlbinlog</code> writes one output file for each file read from the server. The <code>&#8211;raw</code> option can be used to make a backup of a server&#8217;s binary log. With the <code>&#8211;stop-never</code> option, the backup is &#8220;live&#8221; because <code>mysqlbinlog</code> stays connected to the server. By default, output files are written in the current directory with the same names as the original log files. Output file names can be modified using the <code>&#8211;result-file</code> option. For more information, see the section called &#8220;USING MYSQLBINLOG TO BACK UP BINARY LOG FILES&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;read-from-remote-master=</code><i>type</i> </p>
<p> Read binary logs from a MySQL server with the COM_BINLOG_DUMP or COM_BINLOG_DUMP_GTID commands by setting the option value to either BINLOG-DUMP-NON-GTIDS or BINLOG-DUMP-GTIDS, respectively. If <code>&#8211;read-from-remote-master=BINLOG-DUMP-GTIDS</code> is combined with <code>&#8211;exclude-gtids</code>, transactions can be filtered out on the master, avoiding unnecessary network traffic. </p>
<p> The connection parameter options are used with this option or the <code>&#8211;read-from-remote-server</code> option. These options are <code>&#8211;host</code>, <code>&#8211;password</code>, <code>&#8211;port</code>, <code>&#8211;protocol</code>, <code>&#8211;socket</code>, and <code>&#8211;user</code>. If neither of the remote options is specified, the connection parameter options are ignored. </p>
<p> The REPLICATION SLAVE privilege is required to use this option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;read-from-remote-server</code>, <code>-R</code> </p>
<p> Read the binary log from a MySQL server rather than reading a local log file. This option requires that the remote server be running. It works only for binary log files on the remote server, not relay log files. </p>
<p> The connection parameter options are used with this option or the <code>&#8211;read-from-remote-master</code> option. These options are <code>&#8211;host</code>, <code>&#8211;password</code>, <code>&#8211;port</code>, <code>&#8211;protocol</code>, <code>&#8211;socket</code>, and <code>&#8211;user</code>. If neither of the remote options is specified, the connection parameter options are ignored. </p>
<p> The REPLICATION SLAVE privilege is required to use this option. </p>
<p> This option is like <code>&#8211;read-from-remote-master=BINLOG-DUMP-NON-GTIDS</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;result-file=</code><i>name</i>, <code>-r </code><i>name</i> </p>
<p> Without the <code>&#8211;raw</code> option, this option indicates the file to which <code>mysqlbinlog</code> writes text output. With <code>&#8211;raw</code>, <code>mysqlbinlog</code> writes one binary output file for each log file transferred from the server, writing them by default in the current directory using the same names as the original log file. In this case, the <code>&#8211;result-file</code> option value is treated as a prefix that modifies output file names.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;require-row-format</code> </p>
<p> Require row-based binary logging format for events. This option enforces row-based replication events for <code>mysqlbinlog</code> output. The stream of events produced with this option would be accepted by a replication channel that is secured using the REQUIRE_ROW_FORMAT option of the CHANGE MASTER TO statement. binlog_format=ROW must be set on the server where the binary log was written. When you specify this option, <code>mysqlbinlog</code> stops with an error message if it encounters any events that are disallowed under the REQUIRE_ROW_FORMAT restrictions, including LOAD DATA INFILE instructions, creating or dropping temporary tables, INTVAR, RAND, or USER_VAR events, and non-row-based events within a DML transaction. <code>mysqlbinlog</code> also prints a SET @@session.require_row_format statement at the start of its output to apply the restrictions when the output is executed, and does not print the SET @@session.pseudo_thread_id statement. </p>
<p> This option was added in MySQL 8.0.19.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;rewrite-db=&#8217;</code><i>from_name</i><code>-&gt;</code><i>to_name</i><code>&#8216;</code> </p>
<p> When reading from a row-based or statement-based log, rewrite all occurrences of <i>from_name</i> to <i>to_name</i>. Rewriting is done on the rows, for row-based logs, as well as on the USE clauses, for statement-based logs. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Warning</code> </font><br />
 Statements in which table names are qualified with database names are not rewritten to use the new name when using this option. </p>
</dl>
<p> The rewrite rule employed as a value for this option is a string having the form &#8216;<i>from_name</i>-&gt;<i>to_name</i>&#8216;, as shown previously, and for this reason must be enclosed by quotation marks. </p>
<p> To employ multiple rewrite rules, specify the option multiple times, as shown here: </p>
<dl>
<dt>
<dd>
shell &gt; mysqlbinlog&#8211; rewrite &#8211; db = &#8216;dbcurrent-&gt;dbold&#8217; &#8211;rewrite &#8211; db = &#8216;dbtest-&gt;dbcurrent&#8217; binlog .00001 &gt; / tmp / statements.sql
</dl>
<p> When used together with the <code>&#8211;database</code> option, the <code>&#8211;rewrite-db</code> option is applied first; then <code>&#8211;database</code> option is applied, using the rewritten database name. The order in which the options are provided makes no difference in this regard. </p>
<p> This means that, for example, if <code>mysqlbinlog</code> is started with <code>&#8211;rewrite-db=&#8217;mydb-&gt;yourdb&#8217; &#8211;database=yourdb</code>, then all updates to any tables in databases mydb and yourdb are included in the output. On the other hand, if it is started with <code>&#8211;rewrite-db=&#8217;mydb-&gt;yourdb&#8217; &#8211;database=mydb</code>, then <code>mysqlbinlog</code> outputs no statements at all: since all updates to mydb are first rewritten as updates to yourdb before applying the <code>&#8211;database</code> option, there remain no updates that match <code>&#8211;database=mydb</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;server-id=</code><i>id</i> </p>
<p> Display only those events created by the server having the given server ID.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;server-id-bits=</code><i>N</i> </p>
<p> Use only the first <i>N</i> bits of the server_id to identify the server. If the binary log was written by a <code>mysqld</code> with server-id-bits set to less than 32 and user data stored in the most significant bit, running <code>mysqlbinlog</code> with <code>&#8211;server-id-bits</code> set to 32 enables this data to be seen. </p>
<p> This option is supported only by the version of <code>mysqlbinlog</code> supplied with the NDB Cluster distribution, or built with NDB Cluster support.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;server-public-key-path=</code><i>file_name</i> </p>
<p> The path name to a file containing a client-side copy of the public key required by the server for RSA key pair-based password exchange. The file must be in PEM format. This option applies to clients that authenticate with the sha256_password or caching_sha2_password authentication plugin. This option is ignored for accounts that do not authenticate with one of those plugins. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection. </p>
<p> If <code>&#8211;server-public-key-path=</code><i>file_name</i> is given and specifies a valid public key file, it takes precedence over <code>&#8211;get-server-public-key</code>. </p>
<p> For sha256_password, this option applies only if MySQL was built using OpenSSL. </p>
<p> For information about the sha256_password and caching_sha2_password plugins, see Section 6.4.1.3, &#8220;SHA-256 Pluggable Authentication&#8221;, and Section 6.4.1.2, &#8220;Caching SHA-2 Pluggable Authentication&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;set-charset=</code><i>charset_name</i> </p>
<p> Add a SET NAMES <i>charset_name</i> statement to the output to specify the character set to be used for processing log files.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;shared-memory-base-name=</code><i>name</i> </p>
<p> On Windows, the shared-memory name to use for connections made using shared memory to a local server. The default value is MYSQL. The shared-memory name is case-sensitive. </p>
<p> This option applies only if the server was started with the shared_memory system variable enabled to support shared-memory connections.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;short-form</code>, <code>-s</code> </p>
<p> Display only the statements contained in the log, without any extra information or row-based events. This is for testing only, and should not be used in production systems. It is deprecated, and will be removed in a future release.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;skip-gtids[=(true|false)]</code> </p>
<p> Do not display any GTIDs in the output. This is needed when writing to a dump file from one or more binary logs containing GTIDs, as shown in this example: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlbinlog --skip-gtids binlog.000001 &gt;  /tmp/dump.sql</code>
shell&gt; <code>mysqlbinlog --skip-gtids binlog.000002 &gt;&gt; /tmp/dump.sql</code>
shell&gt; <code>mysql -u root -p -e &quot;source /tmp/dump.sql&quot;</code>
</pre>
</dl>
<p> The use of this option is otherwise not normally recommended in production.</dl>
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
<dd> &bull; <code>&#8211;start-datetime=</code><i>datetime</i> </p>
<p> Start reading the binary log at the first event having a timestamp equal to or later than the <i>datetime</i> argument. The <i>datetime</i> value is relative to the local time zone on the machine where you run <code>mysqlbinlog</code>. The value should be in a format accepted for the DATETIME or TIMESTAMP data types. For example: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlbinlog --start-datetime=&quot;2005-12-25 11:25:56&quot; binlog.000003</code>
</pre>
</dl>
<p> This option is useful for point-in-time recovery. See Section 7.3, &#8220;Example Backup and Recovery Strategy&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;start-position=</code><i>N</i>, <code>-j </code><i>N</i> </p>
<p> Start reading the binary log at the first event having a position equal to or greater than <i>N</i>. This option applies to the first log file named on the command line. </p>
<p> This option is useful for point-in-time recovery. See Section 7.3, &#8220;Example Backup and Recovery Strategy&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;stop-datetime=</code><i>datetime</i> </p>
<p> Stop reading the binary log at the first event having a timestamp equal to or later than the <i>datetime</i> argument. This option is useful for point-in-time recovery. See the description of the <code>&#8211;start-datetime</code> option for information about the <i>datetime</i> value. </p>
<p> This option is useful for point-in-time recovery. See Section 7.3, &#8220;Example Backup and Recovery Strategy&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;stop-never</code> </p>
<p> This option is used with <code>&#8211;read-from-remote-server</code>. It tells <code>mysqlbinlog</code> to remain connected to the server. Otherwise <code>mysqlbinlog</code> exits when the last log file has been transferred from the server. <code>&#8211;stop-never</code> implies <code>&#8211;to-last-log</code>, so only the first log file to transfer need be named on the command line. </p>
<p> <code>&#8211;stop-never</code> is commonly used with <code>&#8211;raw</code> to make a live binary log backup, but also can be used without <code>&#8211;raw</code> to maintain a continuous text display of log events as the server generates them. </p>
<p> With <code>&#8211;stop-never</code>, by default, <code>mysqlbinlog</code> reports a server ID of 1 when it connects to the server. Use <code>&#8211;connection-server-id</code> to explicitly specify an alternative ID to report. It can be used to avoid a conflict with the ID of a slave server or another <code>mysqlbinlog</code> process. See the section called &#8220;SPECIFYING THE MYSQLBINLOG SERVER ID&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;stop-never-slave-server-id=</code><i>id</i> </p>
<p> This option is deprecated and will be removed in a future release. Use the <code>&#8211;connection-server-id</code> option instead to specify a server ID for mysqlbinlog to report.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;stop-position=</code><i>N</i> </p>
<p> Stop reading the binary log at the first event having a position equal to or greater than <i>N</i>. This option applies to the last log file named on the command line. </p>
<p> This option is useful for point-in-time recovery. See Section 7.3, &#8220;Example Backup and Recovery Strategy&#8221;.</dl>
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
<dd> &bull; <code>&#8211;to-last-log</code>, <code>-t</code> </p>
<p> Do not stop at the end of the requested binary log from a MySQL server, but rather continue printing until the end of the last binary log. If you send the output to the same MySQL server, this may lead to an endless loop. This option requires <code>&#8211;read-from-remote-server</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;user=</code><i>user_name</i>, <code>-u </code><i>user_name</i> </p>
<p> The user name of the MySQL account to use when connecting to a remote server.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;verbose</code>, <code>-v</code> </p>
<p> Reconstruct row events and display them as commented SQL statements, with table partition information where applicable. If this option is given twice (by passing in either &quot;-vv&quot; or &quot;&#8211;verbose &#8211;verbose&quot;), the output includes comments to indicate column data types and some metadata, and informational log events such as row query log events if the binlog_rows_query_log_events system variable is set to TRUE. </p>
<p> For examples that show the effect of <code>&#8211;base64-output</code> and <code>&#8211;verbose</code> on row event output, see the section called &#8220;MYSQLBINLOG ROW EVENT DISPLAY&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;verify-binlog-checksum</code>, <code>-c</code> </p>
<p> Verify checksums in binary log files.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code>, <code>-V</code> </p>
<p> Display version information and exit. </p>
<p> The <code>mysqlbinlog</code> version number shown when using this option is 3.4.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;zstd-compression-level=</code><i>level</i> The compression level to use for connections to the server that use the zstd compression algorithm. The permitted levels are from 1 to 22, with larger values indicating increasing levels of compression. The default zstd compression level is 3. The compression level setting has no effect on connections that do not use zstd compression. </p>
<p> For more information, see Section 4.2.6, &#8220;Connection Compression Control&#8221;. </p>
<p> This option was added in MySQL 8.0.18.</dl>
<p> You can pipe the output of <code>mysqlbinlog</code> into the <code>mysql</code> client to execute the events contained in the binary log. This technique is used to recover from a crash when you have an old backup (see Section 7.5, &#8220;Point-in-Time (Incremental) Recovery Using the Binary Log&#8221;). For example: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlbinlog binlog.000001 | mysql -u root -p</code>
</pre>
</dl>
<p> Or: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlbinlog binlog.[0-9]* | mysql -u root -p</code>
</pre>
</dl>
<p> If the statements produced by <code>mysqlbinlog</code> may contain BLOB values, these may cause problems when <code>mysql</code> processes them. In this case, invoke <code>mysql</code> with the <code>&#8211;binary-mode</code> option. </p>
<p> You can also redirect the output of <code>mysqlbinlog</code> to a text file instead, if you need to modify the statement log first (for example, to remove statements that you do not want to execute for some reason). After editing the file, execute the statements that it contains by using it as input to the <code>mysql</code> program: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlbinlog binlog.000001 &gt; tmpfile</code>
shell&gt; ... <i>edit tmpfile</i> ...
shell&gt; <code>mysql -u root -p &lt; tmpfile</code>
</pre>
</dl>
<p> When <code>mysqlbinlog</code> is invoked with the <code>&#8211;start-position</code> option, it displays only those events with an offset in the binary log greater than or equal to a given position (the given position must match the start of one event). It also has options to stop and start when it sees an event with a given date and time. This enables you to perform point-in-time recovery using the <code>&#8211;stop-datetime</code> option (to be able to say, for example, &#8220;roll forward my databases to how they were today at 10:30 a.m.&#8221;). </p>
<p> <code>Processing multiple files</code>. If you have more than one binary log to execute on the MySQL server, the safe method is to process them all using a single connection to the server. Here is an example that demonstrates what may be <i>unsafe</i>: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlbinlog binlog.000001 | mysql -u root -p # DANGER!!</code>
shell&gt; <code>mysqlbinlog binlog.000002 | mysql -u root -p # DANGER!!</code>
</pre>
</dl>
<p> Processing binary logs this way using multiple connections to the server causes problems if the first log file contains a CREATE TEMPORARY TABLE statement and the second log contains a statement that uses the temporary table. When the first <code>mysql</code> process terminates, the server drops the temporary table. When the second <code>mysql</code> process attempts to use the table, the server reports &#8220;unknown table.&#8221; </p>
<p> To avoid problems like this, use a <i>single</i> <code>mysql</code> process to execute the contents of all binary logs that you want to process. Here is one way to do so: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlbinlog binlog.000001 binlog.000002 | mysql -u root -p</code>
</pre>
</dl>
<p> Another approach is to write all the logs to a single file and then process the file: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlbinlog binlog.000001 &gt;  /tmp/statements.sql</code>
shell&gt; <code>mysqlbinlog binlog.000002 &gt;&gt; /tmp/statements.sql</code>
shell&gt; <code>mysql -u root -p -e &quot;source /tmp/statements.sql&quot;</code>
</pre>
</dl>
<p> From MySQL 8.0.12, you can also supply multiple binary log files to <code>mysqlbinlog</code> as streamed input using a shell pipe. An archive of compressed binary log files can be decompressed and provided directly to <code>mysqlbinlog</code>. In this example, binlog-files_1.gz contains multiple binary log files for processing. The pipeline extracts the contents of binlog-files_1.gz, pipes the binary log files to <code>mysqlbinlog</code> as standard input, and pipes the output of <code>mysqlbinlog</code> into the <code>mysql</code> client for execution: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>gzip -cd binlog-files_1.gz | ./mysqlbinlog - | ./mysql -uroot&nbsp; -p</code>
</pre>
</dl>
<p> You can specify more than one archive file, for example: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>gzip -cd binlog-files_1.gz binlog-files_2.gz | ./mysqlbinlog - | ./mysql -uroot&nbsp; -p</code>
</pre>
</dl>
<p> For streamed input, do not use &#8211;stop-position, because <code>mysqlbinlog</code> cannot identify the last log file to apply this option. </p>
<p> <code>LOAD DATA operations</code>. <code>mysqlbinlog</code> can produce output that reproduces a LOAD DATA operation without the original data file. <code>mysqlbinlog</code> copies the data to a temporary file and writes a LOAD DATA LOCAL statement that refers to the file. The default location of the directory where these files are written is system-specific. To specify a directory explicitly, use the <code>&#8211;local-load</code> option. </p>
<p> Because <code>mysqlbinlog</code> converts LOAD DATA statements to LOAD DATA LOCAL statements (that is, it adds LOCAL), both the client and the server that you use to process the statements must be configured with the LOCAL capability enabled. See Section 6.1.6, &#8220;Security Issues with LOAD DATA LOCAL&#8221;. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Warning</code> </font> </p>
<p> The temporary files created for LOAD DATA LOCAL statements are <i>not</i> automatically deleted because they are needed until you actually execute those statements. You should delete the temporary files yourself after you no longer need the statement log. The files can be found in the temporary file directory and have names like <i>original_file_name-#-#</i>. </p>
</dl>
<h2>MYSQLBINLOG HEX DUMP FORMAT</h2>
<p> The <code>&#8211;hexdump</code> option causes <code>mysqlbinlog</code> to produce a hex dump of the binary log contents: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlbinlog --hexdump master-bin.000001</code>
</pre>
</dl>
<p> The hex output consists of comment lines beginning with #, so the output might look like this for the preceding command: </p>
<dl>
<dt>
<dd>
<pre>
/*!40019 SET @@SESSION.max_insert_delayed_threads=0*/;
/*!50003 SET @OLD_COMPLETION_TYPE=@@COMPLETION_TYPE,COMPLETION_TYPE=0*/;
# at 4
#051024 17:24:13 server id 1  end_log_pos 98
# Position  Timestamp   Type   Master ID        Size      Master Pos    Flags
# 00000004 9d fc 5c 43   0f   01 00 00 00   5e 00 00 00   62 00 00 00   00 00
# 00000017 04 00 35 2e 30 2e 31 35  2d 64 65 62 75 67 2d 6c |..5.0.15.debug.l|
# 00000027 6f 67 00 00 00 00 00 00  00 00 00 00 00 00 00 00 |og..............|
# 00000037 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00 |................|
# 00000047 00 00 00 00 9d fc 5c 43  13 38 0d 00 08 00 12 00 |.......C.8......|
# 00000057 04 04 04 04 12 00 00 4b  00 04 1a                |.......K...|
#       Start: binlog v 4, server v 5.0.15-debug-log created 051024 17:24:13
#       at startup
ROLLBACK;
</pre>
</dl>
<p> Hex dump output currently contains the elements in the following list. This format is subject to change. For more information about binary log format, see m[blue]<code>MySQL Internals: The Binary Log</code>m[]<font SIZE="-2">[1]</font>. </p>
<dl>
<dt>
<dd> &bull; Position: The byte position within the log file.</dl>
<dl>
<dt>
<dd> &bull; Timestamp: The event timestamp. In the example shown, &#8216;9d fc 5c 43&#8217; is the representation of &#8216;051024 17:24:13&#8217; in hexadecimal.</dl>
<dl>
<dt>
<dd> &bull; Type: The event type code.</dl>
<dl>
<dt>
<dd> &bull; Master ID: The server ID of the master that created the event.</dl>
<dl>
<dt>
<dd> &bull; Size: The size in bytes of the event.</dl>
<dl>
<dt>
<dd> &bull; Master Pos: The position of the next event in the original master log file.</dl>
<dl>
<dt>
<dd> &bull; Flags: Event flag values.</dl>
<h2>MYSQLBINLOG ROW EVENT DISPLAY</h2>
<p> The following examples illustrate how <code>mysqlbinlog</code> displays row events that specify data modifications. These correspond to events with the WRITE_ROWS_EVENT, UPDATE_ROWS_EVENT, and DELETE_ROWS_EVENT type codes. The <code>&#8211;base64-output=DECODE-ROWS</code> and <code>&#8211;verbose</code> options may be used to affect row event output. </p>
<p> Suppose that the server is using row-based binary logging and that you execute the following sequence of statements: </p>
<dl>
<dt>
<dd>
CREATE TABLE t(<br />
    id INT NOT NULL,<br />
    name VARCHAR(20) NOT NULL,<br />
    date DATE NULL) ENGINE = InnoDB;<br />
START TRANSACTION;<br />
INSERT INTO t VALUES(1, &#8216;apple&#8217;, NULL);<br />
UPDATE t SET name = &#8216;pear&#8217;, date = &#8216;2009-01-01&#8217; WHERE id = 1;<br />
DELETE FROM t WHERE id = 1;<br />
COMMIT;
</dl>
<p> By default, <code>mysqlbinlog</code> displays row events encoded as base-64 strings using BINLOG statements. Omitting extraneous lines, the output for the row events produced by the preceding statement sequence looks like this: </p>
<dl>
<dt>
<dd>
shell &gt; mysqlbinlog log_file&#8230;<br />
#at 218<br />
# 080828 15 : 03 : 08 server id 1 end_log_pos 258 Write_rows : table id 17 flags : STMT_END_F<br />
    BINLOG &#8216; fAS3SBMBAAAALAAAANoAAAAAABEAAAAAAAAABHRlc3QAAXQAAwMPCgIUAAQ =<br />
    fAS3SBcBAAAAKAAAAAIBAAAQABEAAAAAAAEAA // 8AQAAAAVhcHBsZQ==<br />
&#8216;/*!*/; &#8230;<br />
#at 302<br />
# 080828 15 : 03 : 08 server id 1 end_log_pos 356 Update_rows : table id 17 flags : STMT_END_F<br />
    BINLOG &#8216; fAS3SBMBAAAALAAAAC4BAAAAABEAAAAAAAAABHRlc3QAAXQAAwMPCgIUAAQ =<br />
        fAS3SBgBAAAANgAAAGQBAAAQABEAAAAAAAEAA ////AEAAAAFYXBwbGX4AQAAAARwZWFyIbIP<br />
&#8216;/*!*/; &#8230;<br />
#at 400<br />
# 080828 15 : 03 : 08 server id 1 end_log_pos 442 Delete_rows : table id 17 flags : STMT_END_F<br />
    BINLOG &#8216; fAS3SBMBAAAALAAAAJABAAAAABEAAAAAAAAABHRlc3QAAXQAAwMPCgIUAAQ =<br />
        fAS3SBkBAAAAKgAAALoBAAAQABEAAAAAAAEAA // 4AQAAAARwZWFyIbIP<br />
&#8216;/*!*/;
</dl>
<p> To see the row events as comments in the form of &#8220;pseudo-SQL&#8221; statements, run <code>mysqlbinlog</code> with the <code>&#8211;verbose</code> or <code>-v</code> option. This output level also shows table partition information where applicable. The output will contain lines beginning with ###: </p>
<dl>
<dt>
<dd>
shell &gt; mysqlbinlog &#8211; v log_file&#8230;<br />
#at 218<br />
# 080828 15 : 03 : 08 server id 1 end_log_pos 258 Write_rows : table id 17 flags : STMT_END_F<br />
            BINLOG &#8216; fAS3SBMBAAAALAAAANoAAAAAABEAAAAAAAAABHRlc3QAAXQAAwMPCgIUAAQ =<br />
    fAS3SBcBAAAAKAAAAAIBAAAQABEAAAAAAAEAA // 8AQAAAAVhcHBsZQ==<br />
&#8216;/*!*/; ## #INSERT INTO test.t## #SET## #@1 = 1## #@2 = &#8216;apple&#8217;## #@3 = NULL&#8230;<br />
#at 302<br />
# 080828 15 : 03 : 08 server id 1 end_log_pos 356 Update_rows : table id 17 flags : STMT_END_F<br />
    BINLOG &#8216; fAS3SBMBAAAALAAAAC4BAAAAABEAAAAAAAAABHRlc3QAAXQAAwMPCgIUAAQ =<br />
        fAS3SBgBAAAANgAAAGQBAAAQABEAAAAAAAEAA ////AEAAAAFYXBwbGX4AQAAAARwZWFyIbIP<br />
&#8216;/*!*/; ## #UPDATE test.t## #WHERE## #@1 = 1## #@2 = &#8216;apple&#8217;## #@3 = NULL## #SET## #@1 = 1## #@2 = &#8216;pear&#8217;## #@3 = &#8216;2009:01:01&#8217; &#8230;<br />
#at 400<br />
# 080828 15 : 03 : 08 server id 1 end_log_pos 442 Delete_rows : table id 17 flags : STMT_END_F<br />
    BINLOG &#8216; fAS3SBMBAAAALAAAAJABAAAAABEAAAAAAAAABHRlc3QAAXQAAwMPCgIUAAQ =<br />
        fAS3SBkBAAAAKgAAALoBAAAQABEAAAAAAAEAA // 4AQAAAARwZWFyIbIP<br />
&#8216;/*!*/; ## #DELETE FROM test.t## #WHERE## #@1 = 1## #@2 = &#8216;pear&#8217;## #@3 = &#8216;2009:01:01&#8217;
</dl>
<p> Specify <code>&#8211;verbose</code> or <code>-v</code> twice to also display data types and some metadata for each column, and informational log events such as row query log events if the binlog_rows_query_log_events system variable is set to TRUE. The output will contain an additional comment following each column change: </p>
<dl>
<dt>
<dd>
shell &gt; mysqlbinlog &#8211; vv log_file&#8230;<br />
#at 218<br />
# 080828 15 : 03 : 08 server id 1 end_log_pos 258 Write_rows : table id 17 flags : STMT_END_F<br />
            BINLOG &#8216; fAS3SBMBAAAALAAAANoAAAAAABEAAAAAAAAABHRlc3QAAXQAAwMPCgIUAAQ =<br />
    fAS3SBcBAAAAKAAAAAIBAAAQABEAAAAAAAEAA        // 8AQAAAAVhcHBsZQ==<br />
&#8216;/*!*/; ## #INSERT INTO test.t## #SET## #@1 = 1 /* INT meta=0 nullable=0 is_null=0 */<br />
    ## #@2 = &#8216;apple&#8217;                             /* VARSTRING(20) meta=20 nullable=0 is_null=0 */<br />
    ## #@3 = NULL                                /* VARSTRING(20) meta=0 nullable=1 is_null=1 */<br />
    &#8230;<br />
#at 302<br />
# 080828 15 : 03 : 08 server id 1 end_log_pos 356 Update_rows : table id 17 flags : STMT_END_F<br />
    BINLOG &#8216; fAS3SBMBAAAALAAAAC4BAAAAABEAAAAAAAAABHRlc3QAAXQAAwMPCgIUAAQ =<br />
        fAS3SBgBAAAANgAAAGQBAAAQABEAAAAAAAEAA ////AEAAAAFYXBwbGX4AQAAAARwZWFyIbIP<br />
&#8216;/*!*/; ## #UPDATE test.t## #WHERE## #@1 = 1 /* INT meta=0 nullable=0 is_null=0 */<br />
    ## #@2 = &#8216;apple&#8217;                          /* VARSTRING(20) meta=20 nullable=0 is_null=0 */<br />
    ## #@3 = NULL                             /* VARSTRING(20) meta=0 nullable=1 is_null=1 */<br />
    ## #SET## #@1 = 1                         /* INT meta=0 nullable=0 is_null=0 */<br />
    ## #@2 = &#8216;pear&#8217;                           /* VARSTRING(20) meta=20 nullable=0 is_null=0 */<br />
    ## #@3 = &#8216;2009:01:01&#8217;                     /* DATE meta=0 nullable=1 is_null=0 */<br />
    &#8230;<br />
#at 400<br />
# 080828 15 : 03 : 08 server id 1 end_log_pos 442 Delete_rows : table id 17 flags : STMT_END_F<br />
    BINLOG &#8216; fAS3SBMBAAAALAAAAJABAAAAABEAAAAAAAAABHRlc3QAAXQAAwMPCgIUAAQ =<br />
        fAS3SBkBAAAAKgAAALoBAAAQABEAAAAAAAEAA      // 4AQAAAARwZWFyIbIP<br />
&#8216;/*!*/; ## #DELETE FROM test.t## #WHERE## #@1 = 1 /* INT meta=0 nullable=0 is_null=0 */<br />
    ## #@2 = &#8216;pear&#8217;                                /* VARSTRING(20) meta=20 nullable=0 is_null=0 */<br />
    ## #@3 = &#8216;2009:01:01&#8217;                          /* DATE meta=0 nullable=1 is_null=0 */
</dl>
<p> You can tell <code>mysqlbinlog</code> to suppress the BINLOG statements for row events by using the <code>&#8211;base64-output=DECODE-ROWS</code> option. This is similar to <code>&#8211;base64-output=NEVER</code> but does not exit with an error if a row event is found. The combination of <code>&#8211;base64-output=DECODE-ROWS</code> and <code>&#8211;verbose</code> provides a convenient way to see row events only as SQL statements: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlbinlog -v --base64-output=DECODE-ROWS </code><i>log_file</i>
...
# at 218
#080828 15:03:08 server id 1  end_log_pos 258   Write_rows: table id 17 flags: STMT_END_F
### INSERT INTO test.t
### SET
###   @1=1
###   @2='apple'
###   @3=NULL
...
# at 302
#080828 15:03:08 server id 1  end_log_pos 356   Update_rows: table id 17 flags: STMT_END_F
### UPDATE test.t
### WHERE
###   @1=1
###   @2='apple'
###   @3=NULL
### SET
###   @1=1
###   @2='pear'
###   @3='2009:01:01'
...
# at 400
#080828 15:03:08 server id 1  end_log_pos 442   Delete_rows: table id 17 flags: STMT_END_F
### DELETE FROM test.t
### WHERE
###   @1=1
###   @2='pear'
###   @3='2009:01:01'
</pre>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> You should not suppress BINLOG statements if you intend to re-execute <code>mysqlbinlog</code> output. </p>
</dl>
<p> The SQL statements produced by <code>&#8211;verbose</code> for row events are much more readable than the corresponding BINLOG statements. However, they do not correspond exactly to the original SQL statements that generated the events. The following limitations apply: </p>
<dl>
<dt>
<dd> &bull; The original column names are lost and replaced by @<i>N</i>, where <i>N</i> is a column number.</dl>
<dl>
<dt>
<dd> &bull; Character set information is not available in the binary log, which affects string column display: </p>
<dl>
<dt>
<dd> &bull; There is no distinction made between corresponding binary and nonbinary string types (BINARY and CHAR, VARBINARY and VARCHAR, BLOB and TEXT). The output uses a data type of STRING for fixed-length strings and VARSTRING for variable-length strings.</dl>
<dl>
<dt>
<dd> &bull; For multibyte character sets, the maximum number of bytes per character is not present in the binary log, so the length for string types is displayed in bytes rather than in characters. For example, <a href="/docs/linux/man/4-string/">STRING</a>(4) will be used as the data type for values from either of these column types: </p>
<dl>
<dt>
<dd>
<pre>
<a href="//www.systutorials.com/docs/linux/man/4-CHAR/">CHAR</a>(4) CHARACTER SET latin1
<a href="//www.systutorials.com/docs/linux/man/2-CHAR/">CHAR</a>(2) CHARACTER SET ucs2
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Due to the storage format for events of type UPDATE_ROWS_EVENT, UPDATE statements are displayed with the WHERE clause preceding the SET clause.</dl>
</dl>
<p> Proper interpretation of row events requires the information from the format description event at the beginning of the binary log. Because <code>mysqlbinlog</code> does not know in advance whether the rest of the log contains row events, by default it displays the format description event using a BINLOG statement in the initial part of the output. </p>
<p> If the binary log is known not to contain any events requiring a BINLOG statement (that is, no row events), the <code>&#8211;base64-output=NEVER</code> option can be used to prevent this header from being written.</p>
<h2>USING MYSQLBINLOG TO BACK UP BINARY LOG FILES</h2>
<p> By default, <code>mysqlbinlog</code> reads binary log files and displays their contents in text format. This enables you to examine events within the files more easily and to re-execute them (for example, by using the output as input to <code>mysql</code>). <code>mysqlbinlog</code> can read log files directly from the local file system, or, with the <code>&#8211;read-from-remote-server</code> option, it can connect to a server and request binary log contents from that server. <code>mysqlbinlog</code> writes text output to its standard output, or to the file named as the value of the <code>&#8211;result-file=</code><i>file_name</i> option if that option is given. </p>
<dl>
<dt>
<dd> &bull; mysqlbinlog Backup Capabilities</dl>
<dl>
<dt>
<dd> &bull; mysqlbinlog Backup Options</dl>
<dl>
<dt>
<dd> &bull; Static and Live Backups</dl>
<dl>
<dt>
<dd> &bull; Output File Naming</dl>
<dl>
<dt>
<dd> &bull; Example: mysqldump + mysqlbinlog for Backup and Restore</dl>
<dl>
<dt>
<dd> &bull; mysqlbinlog Backup Restrictions</dl>
<p> mysqlbinlog Backup Capabilities </p>
<p> <code>mysqlbinlog</code> can read binary log files and write new files containing the same content&#8212;that is, in binary format rather than text format. This capability enables you to easily back up a binary log in its original format. <code>mysqlbinlog</code> can make a static backup, backing up a set of log files and stopping when the end of the last file is reached. It can also make a continuous (&#8220;live&#8221;) backup, staying connected to the server when it reaches the end of the last log file and continuing to copy new events as they are generated. In continuous-backup operation, <code>mysqlbinlog</code> runs until the connection ends (for example, when the server exits) or <code>mysqlbinlog</code> is forcibly terminated. When the connection ends, <code>mysqlbinlog</code> does not wait and retry the connection, unlike a slave replication server. To continue a live backup after the server has been restarted, you must also restart <code>mysqlbinlog</code>. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Important</code> </font> </p>
<p> <code>mysqlbinlog</code> can back up both encrypted and unencrypted binary log files . However, copies of encrypted binary log files that are generated using <code>mysqlbinlog</code> are stored in an unencrypted format. </p>
</dl>
<p> mysqlbinlog Backup Options </p>
<p> Binary log backup requires that you invoke <code>mysqlbinlog</code> with two options at minimum: </p>
<dl>
<dt>
<dd> &bull; The <code>&#8211;read-from-remote-server</code> (or <code>-R</code>) option tells <code>mysqlbinlog</code> to connect to a server and request its binary log. (This is similar to a slave replication server connecting to its master server.)</dl>
<dl>
<dt>
<dd> &bull; The <code>&#8211;raw</code> option tells <code>mysqlbinlog</code> to write raw (binary) output, not text output.</dl>
<p> Along with <code>&#8211;read-from-remote-server</code>, it is common to specify other options: <code>&#8211;host</code> indicates where the server is running, and you may also need to specify connection options such as <code>&#8211;user</code> and <code>&#8211;password</code>. </p>
<p> Several other options are useful in conjunction with <code>&#8211;raw</code>: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;stop-never</code>: Stay connected to the server after reaching the end of the last log file and continue to read new events.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;connection-server-id=</code><i>id</i>: The server ID that <code>mysqlbinlog</code> reports when it connects to a server. When <code>&#8211;stop-never</code> is used, the default reported server ID is 1. If this causes a conflict with the ID of a slave server or another <code>mysqlbinlog</code> process, use <code>&#8211;connection-server-id</code> to specify an alternative server ID. See the section called &#8220;SPECIFYING THE MYSQLBINLOG SERVER ID&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;result-file</code>: A prefix for output file names, as described later.</dl>
<p> Static and Live Backups </p>
<p> To back up a server&#8217;s binary log files with <code>mysqlbinlog</code>, you must specify file names that actually exist on the server. If you do not know the names, connect to the server and use the SHOW BINARY LOGS statement to see the current names. Suppose that the statement produces this output: </p>
<dl>
<dt>
<dd>
mysql &gt; SHOW BINARY LOGS;<br />
+ &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; -+ | Log_name | File_size | Encrypted |<br />
    +&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; -+ | binlog .000130 | 27459 | No |<br />
    | binlog .000131 | 13719 | No |<br />
    | binlog .000132 | 43268 | No |<br />
    +&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; -+
</dl>
<p> With that information, you can use <code>mysqlbinlog</code> to back up the binary log to the current directory as follows (enter each command on a single line): </p>
<dl>
<dt>
<dd> &bull; To make a static backup of binlog.000130 through binlog.000132, use either of these commands: </p>
<dl>
<dt>
<dd>
mysqlbinlog&#8211; read &#8211; from &#8211; remote &#8211; server&#8211; host = host_name&#8211; raw<br />
                                                         binlog .000130 binlog .000131 binlog .000132 mysqlbinlog&#8211; read &#8211;<br />
                                                     from &#8211; remote &#8211; server&#8211; host = host_name&#8211; raw&#8211; to &#8211; last &#8211; log binlog .000130
</dl>
<p> The first command specifies every file name explicitly. The second names only the first file and uses <code>&#8211;to-last-log</code> to read through the last. A difference between these commands is that if the server happens to open binlog.000133 before <code>mysqlbinlog</code> reaches the end of binlog.000132, the first command will not read it, but the second command will.</dl>
<dl>
<dt>
<dd> &bull; To make a live backup in which <code>mysqlbinlog</code> starts with binlog.000130 to copy existing log files, then stays connected to copy new events as the server generates them: </p>
<dl>
<dt>
<dd>
mysqlbinlog&#8211; read &#8211; from &#8211; remote &#8211; server&#8211; host = host_name&#8211; raw&#8211; stop &#8211; never binlog .000130
</dl>
<p> With <code>&#8211;stop-never</code>, it is not necessary to specify <code>&#8211;to-last-log</code> to read to the last log file because that option is implied.</dl>
<p> Output File Naming </p>
<p> Without <code>&#8211;raw</code>, <code>mysqlbinlog</code> produces text output and the <code>&#8211;result-file</code> option, if given, specifies the name of the single file to which all output is written. With <code>&#8211;raw</code>, <code>mysqlbinlog</code> writes one binary output file for each log file transferred from the server. By default, <code>mysqlbinlog</code> writes the files in the current directory with the same names as the original log files. To modify the output file names, use the <code>&#8211;result-file</code> option. In conjunction with <code>&#8211;raw</code>, the <code>&#8211;result-file</code> option value is treated as a prefix that modifies the output file names. </p>
<p> Suppose that a server currently has binary log files named binlog.000999 and up. If you use <code>mysqlbinlog &#8211;raw</code> to back up the files, the <code>&#8211;result-file</code> option produces output file names as shown in the following table. You can write the files to a specific directory by beginning the <code>&#8211;result-file</code> value with the directory path. If the <code>&#8211;result-file</code> value consists only of a directory name, the value must end with the pathname separator character. Output files are overwritten if they exist. </p>
<table BORDER>
<tr VALIGN=top>
<td><code> <code>&#8211;result-file</code> Option </code></td>
<td><code> Output File Names </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>&#8211;result-file=x</code> </td>
<td> xbinlog.000999 and up
</td>
</tr>
<tr VALIGN=top>
<td> <code>&#8211;result-file=/tmp/</code> </td>
<td> /tmp/binlog.000999 and up
</td>
</tr>
<tr VALIGN=top>
<td> <code>&#8211;result-file=/tmp/x</code> </td>
<td> /tmp/xbinlog.000999 and up
</td>
</tr>
</table>
<p> Example: mysqldump + mysqlbinlog for Backup and Restore </p>
<p> The following example describes a simple scenario that shows how to use <code>mysqldump</code> and <code>mysqlbinlog</code> together to back up a server&#8217;s data and binary log, and how to use the backup to restore the server if data loss occurs. The example assumes that the server is running on host <i>host_name</i> and its first binary log file is named binlog.000999. Enter each command on a single line. </p>
<p> Use <code>mysqlbinlog</code> to make a continuous backup of the binary log: </p>
<dl>
<dt>
<dd>
mysqlbinlog&#8211; read &#8211; from &#8211; remote &#8211; server&#8211; host = host_name&#8211; raw&#8211; stop &#8211; never binlog .000999
</dl>
<p> Use <code>mysqldump</code> to create a dump file as a snapshot of the server&#8217;s data. Use <code>&#8211;all-databases</code>, <code>&#8211;events</code>, and <code>&#8211;routines</code> to back up all data, and <code>&#8211;master-data=2</code> to include the current binary log coordinates in the dump file. </p>
<dl>
<dt>
<dd>
<pre><code>
mysqldump-- host = host_name-- all - databases-- events-- routines-- master - data = 2 &gt; dump_file
</code></pre>
</dl>
<p> Execute the <code>mysqldump</code> command periodically to create newer snapshots as desired. </p>
<p> If data loss occurs (for example, if the server crashes), use the most recent dump file to restore the data: </p>
<dl>
<dt>
<dd>
<pre>
mysql --host=<i>host_name</i> -u root -p &lt; <i>dump_file</i>
</pre>
</dl>
<p> Then use the binary log backup to re-execute events that were written after the coordinates listed in the dump file. Suppose that the coordinates in the file look like this: </p>
<dl>
<dt>
<dd>
<pre>
-- CHANGE MASTER TO MASTER_LOG_FILE='binlog.001002', MASTER_LOG_POS=27284;
</pre>
</dl>
<p> If the most recent backed-up log file is named binlog.001004, re-execute the log events like this: </p>
<dl>
<dt>
<dd>
<pre>
mysqlbinlog --start-position=27284 binlog.001002 binlog.001003 binlog.001004
  | mysql --host=<i>host_name</i> -u root -p
</pre>
</dl>
<p> You might find it easier to copy the backup files (dump file and binary log files) to the server host to make it easier to perform the restore operation, or if MySQL does not allow remote root access. mysqlbinlog Backup Restrictions </p>
<p> Binary log backups with <code>mysqlbinlog</code> are subject to these restrictions: </p>
<dl>
<dt>
<dd> &bull; <code>mysqlbinlog</code> does not automatically reconnect to the MySQL server if the connection is lost (for example, if a server restart occurs or there is a network outage).</dl>
<dl>
<dt>
<dd> &bull; The delay for a backup is similar to the delay for a replication slave.</dl>
<h2>SPECIFYING THE MYSQLBINLOG SERVER ID</h2>
<p> When invoked with the <code>&#8211;read-from-remote-server</code> option, <code>mysqlbinlog</code> connects to a MySQL server, specifies a server ID to identify itself, and requests binary log files from the server. You can use <code>mysqlbinlog</code> to request log files from a server in several ways: </p>
<dl>
<dt>
<dd> &bull; Specify an explicitly named set of files: For each file, <code>mysqlbinlog</code> connects and issues a Binlog dump command. The server sends the file and disconnects. There is one connection per file.</dl>
<dl>
<dt>
<dd> &bull; Specify the beginning file and <code>&#8211;to-last-log</code>: <code>mysqlbinlog</code> connects and issues a Binlog dump command for all files. The server sends all files and disconnects.</dl>
<dl>
<dt>
<dd> &bull; Specify the beginning file and <code>&#8211;stop-never</code> (which implies <code>&#8211;to-last-log</code>): <code>mysqlbinlog</code> connects and issues a Binlog dump command for all files. The server sends all files, but does not disconnect after sending the last one.</dl>
<p> With <code>&#8211;read-from-remote-server</code> only, <code>mysqlbinlog</code> connects using a server ID of 0, which tells the server to disconnect after sending the last requested log file. </p>
<p> With <code>&#8211;read-from-remote-server</code> and <code>&#8211;stop-never</code>, <code>mysqlbinlog</code> connects using a nonzero server ID, so the server does not disconnect after sending the last log file. The server ID is 1 by default, but this can be changed with <code>&#8211;connection-server-id</code>. </p>
<p> Thus, for the first two ways of requesting files, the server disconnects because <code>mysqlbinlog</code> specifies a server ID of 0. It does not disconnect if <code>&#8211;stop-never</code> is given because <code>mysqlbinlog</code> specifies a nonzero server ID.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1997, 2020, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> MySQL Internals: The Binary Log</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://dev.mysql.com/doc/internals/en/binary-log.html">https://dev.mysql.com/doc/internals/en/binary-log.html</a></dl>
</dl>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
