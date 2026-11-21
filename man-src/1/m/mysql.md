---

title: "mysql(1)"
name: "mysql"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysql/"
description: "mysql – the MySQL command-line client"
---

<dl>
<dt><code>mysql [</code><i>options</i><code>] </code><i>db_name</i></dt>
</dl>
<p> <code>mysql</code> </p>
<dd> <p> is a simple SQL shell with input line editing capabilities. It supports interactive and noninteractive use. When used interactively, query results are presented in an ASCII-table format. When used noninteractively (for example, as a filter), the result is presented in tab-separated format. The output format can be changed using command options. </p>
<p> If you have problems due to insufficient memory for large result sets, use the <code>--quick</code> option. This forces <code>mysql</code> to retrieve results from the server a row at a time rather than retrieving the entire result set and buffering it in memory before displaying it. This is done by returning the result set using the mysql_use_result() C API function in the client/server library rather than mysql_store_result(). </p>
 </dd>
<dl>
<dd> <p> <br />
 <font SIZE="+1"> <code>Note</code> </font> <br />
 </p>
<p> Alternatively, MySQL Shell offers access to the X DevAPI. For details, see m[blue]<code>MySQL Shell 8.0 (part of MySQL 8.0)</code>m[]<font SIZE="-2">[1]</font>. </p>
 </dd></dl>
<p> Using <code>mysql</code> is very easy. Invoke it from the prompt of your command interpreter as follows: </p>
<dl>
<dd> <pre><code>shell&gt; mysql  db_name 
</code></pre>
 </dd></dl>
<p> Or: </p>
<dl>
<dd> <pre><code>shell&gt; mysql --user=  user_name   --password  db_name Enter password: your_password 
</code></pre>
 </dd></dl>
<p> Then type an SQL statement, end it with ;, \g, or \G and press Enter. </p>
<p> Typing Control+C interrupts the current statement if there is one, or cancels any partial input line otherwise. </p>
<p> You can execute SQL statements in a script file (batch file) like this: </p>
<dl>
<dd> <pre><code>shell&gt; mysql  db_name   &lt;  script.sql   &gt;  output.tab 
</code></pre>
 </dd></dl>
<p> On Unix, the <code>mysql</code> client logs statements executed interactively to a history file. See the section called "MYSQL CLIENT LOGGING".  </p>
<h2>MYSQL CLIENT OPTIONS</h2>
<p> <code>mysql</code> supports the following options, which can be specified on the command line or in the [mysql] and [client] groups of an option file. For information about option files used by MySQL programs, see Section 4.2.2.2, "Using Option Files". </p>
<dl>
<dd> <p> &bull; <code>--help</code>, <code>-?</code> </p>
<p> Display a help message and exit. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--auto-rehash</code> </p>
<p> Enable automatic rehashing. This option is on by default, which enables database, table, and column name completion. Use <code>--disable-auto-rehash</code> to disable rehashing. That causes <code>mysql</code> to start faster, but you must issue the rehash command or its \# shortcut if you want to use name completion. </p>
<p> To complete a name, enter the first part and press Tab. If the name is unambiguous, <code>mysql</code> completes it. Otherwise, you can press Tab again to see the possible names that begin with what you have typed so far. Completion does not occur if there is no default database. </p>
 </dd>
<dl>
<dd> <p> <br />
 <font SIZE="+1"> <code>Note</code> </font> <br />
 This feature requires a MySQL client that is compiled with the <code>readline</code> library. Typically, the <code>readline</code> library is not available on Windows. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> &bull; <code>--auto-vertical-output</code> </p>
<p> Cause result sets to be displayed vertically if they are too wide for the current window, and using normal tabular format otherwise. (This applies to statements terminated by ; or \G.) </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--batch</code>, <code>-B</code> </p>
<p> Print results using tab as the column separator, with each row on a new line. With this option, <code>mysql</code> does not use the history file. </p>
<p> Batch mode results in nontabular output format and escaping of special characters. Escaping may be disabled by using raw mode; see the description for the <code>--raw</code> option. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--binary-as-hex</code> </p>
<p> When this option is given, <code>mysql</code> displays binary data using hexadecimal notation (0x <i>value</i>). This occurs whether the overall output dislay format is tabular, vertical, HTML, or XML. </p>
<p> As of MySQL 8.0.19, when <code>mysql</code> operates in interactive mode, this option is enabled by default. In addition, output from the status (or \s) command includes this line when the option is enabled implicitly or explicitly: </p>
 </dd>
<dl>
<dd> <pre><code>Binary data as: Hexadecimal
</code></pre>
 </dd></dl>
<p> To disable hexadecimal notation, use <code>--skip-binary-as-hex</code> </dl>
 </p>
<dl>
<dd> <p> &bull; <code>--binary-mode</code> </p>
<p> This option helps when processing <code>mysqlbinlog</code> output that may contain BLOB values. By default, <code>mysql</code> translates \r\n in statement strings to \n and interprets \0 as the statement terminator. <code>--binary-mode</code> disables both features. It also disables all <code>mysql</code> commands except charset and delimiter in noninteractive mode (for input piped to <code>mysql</code> or loaded using the source command). </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--bind-address=</code><i>ip_address</i> </p>
<p> On a computer having multiple network interfaces, use this option to select which interface to use for connecting to the MySQL server. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--character-sets-dir=</code><i>dir_name</i> </p>
<p> The directory where character sets are installed. See Section 10.15, "Character Set Configuration". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--column-names</code> </p>
<p> Write column names in results. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--column-type-info</code> </p>
<p> Display result set metadata. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--comments</code>, <code>-c</code> </p>
<p> Whether to strip or preserve comments in statements sent to the server. The default is <code>--skip-comments</code> (strip comments), enable with <code>--comments</code> (preserve comments). </p>
 </dd>
<dl>
<dd> <p> <br />
 <font SIZE="+1"> <code>Note</code> </font> <br />
 The <code>mysql</code> client always passes optimizer hints to the server, regardless of whether this option is given. </p>
<p> Comment stripping is deprecated. This feature and the options to control it will be removed in a future MySQL release. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> &bull; <code>--compress</code>, <code>-C</code> </p>
<p> Compress all information sent between the client and the server if possible. See Section 4.2.6, "Connection Compression Control". </p>
<p> As of MySQL 8.0.18, this option is deprecated. It will be removed in a future MySQL version. See the section called "Legacy Connection Compression Configuration". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--compression-algorithms=</code><i>value</i> The permitted compression algorithms for connections to the server. The available algorithms are the same as for the protocol_compression_algorithms system variable. The default value is uncompressed. </p>
<p> For more information, see Section 4.2.6, "Connection Compression Control". </p>
<p> This option was added in MySQL 8.0.18. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--connect-expired-password</code> </p>
<p> Indicate to the server that the client can handle sandbox mode if the account used to connect has an expired password. This can be useful for noninteractive invocations of <code>mysql</code> because normally the server disconnects noninteractive clients that attempt to connect using an account with an expired password. (See Section 6.2.16, "Server Handling of Expired Passwords".) </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--connect-timeout=</code><i>value</i> The number of seconds before connection timeout. (Default value is 0.) </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--database=</code><i>db_name</i>, <code>-D </code><i>db_name</i> </p>
<p> The database to use. This is useful primarily in an option file. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--debug[=</code><i>debug_options</i><code>]</code>, <code>-# [</code><i>debug_options</i><code>]</code> </p>
<p> Write a debugging log. A typical <i>debug_options</i> string is d:t:o,<i>file_name</i>. The default is d:t:o,/tmp/mysql.trace. </p>
<p> This option is available only if MySQL was built using <code>WITH_DEBUG</code>. MySQL release binaries provided by Oracle are <i>not</i> built using this option. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--debug-check</code> </p>
<p> Print some debugging information when the program exits. </p>
<p> This option is available only if MySQL was built using <code>WITH_DEBUG</code>. MySQL release binaries provided by Oracle are <i>not</i> built using this option. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--debug-info</code>, <code>-T</code> </p>
<p> Print debugging information and memory and CPU usage statistics when the program exits. </p>
<p> This option is available only if MySQL was built using <code>WITH_DEBUG</code>. MySQL release binaries provided by Oracle are <i>not</i> built using this option. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--default-auth=</code><i>plugin</i> </p>
<p> A hint about which client-side authentication plugin to use. See Section 6.2.17, "Pluggable Authentication". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--default-character-set=</code><i>charset_name</i> </p>
<p> Use <i>charset_name</i> as the default character set for the client and connection. </p>
<p> This option can be useful if the operating system uses one character set and the <code>mysql</code> client by default uses another. In this case, output may be formatted incorrectly. You can usually fix such issues by using this option to force the client to use the system character set instead. </p>
<p> For more information, see Section 10.4, "Connection Character Sets and Collations", and Section 10.15, "Character Set Configuration". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--defaults-extra-file=</code><i>file_name</i> </p>
<p> Read this option file after the global option file but (on Unix) before the user option file. If the file does not exist or is otherwise inaccessible, an error occurs. <i>file_name</i> is interpreted relative to the current directory if given as a relative path name rather than a full path name. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, "Command-Line Options that Affect Option-File Handling". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--defaults-file=</code><i>file_name</i> </p>
<p> Use only the given option file. If the file does not exist or is otherwise inaccessible, an error occurs. <i>file_name</i> is interpreted relative to the current directory if given as a relative path name rather than a full path name. </p>
<p> Exception: Even with <code>--defaults-file</code>, client programs read .mylogin.cnf. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, "Command-Line Options that Affect Option-File Handling". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--defaults-group-suffix=</code><i>str</i> </p>
<p> Read not only the usual option groups, but also groups with the usual names and a suffix of <i>str</i>. For example, <code>mysql</code> normally reads the [client] and [mysql] groups. If the <code>--defaults-group-suffix=_other</code> option is given, <code>mysql</code> also reads the [client_other] and [mysql_other] groups. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, "Command-Line Options that Affect Option-File Handling". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--delimiter=</code><i>str</i> </p>
<p> Set the statement delimiter. The default is the semicolon character (;). </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--disable-named-commands</code> </p>
<p> Disable named commands. Use the \* form only, or use named commands only at the beginning of a line ending with a semicolon (;). <code>mysql</code> starts with this option <i>enabled</i> by default. However, even with this option, long-format commands still work from the first line. See the section called "MYSQL CLIENT COMMANDS". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--enable-cleartext-plugin</code> </p>
<p> Enable the mysql_clear_password cleartext authentication plugin. (See Section 6.4.1.4, "Client-Side Cleartext Pluggable Authentication".) </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--execute=</code><i>statement</i>, <code>-e </code><i>statement</i> </p>
<p> Execute the statement and quit. The default output format is like that produced with <code>--batch</code>. See Section 4.2.2.1, "Using Options on the Command Line", for some examples. With this option, <code>mysql</code> does not use the history file. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--force</code>, <code>-f</code> </p>
<p> Continue even if an SQL error occurs. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--get-server-public-key</code> </p>
<p> Request from the server the public key required for RSA key pair-based password exchange. This option applies to clients that authenticate with the caching_sha2_password authentication plugin. For that plugin, the server does not send the public key unless requested. This option is ignored for accounts that do not authenticate with that plugin. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection. </p>
<p> If <code>--server-public-key-path=</code><i>file_name</i> is given and specifies a valid public key file, it takes precedence over <code>--get-server-public-key</code>. </p>
<p> For information about the caching_sha2_password plugin, see Section 6.4.1.2, "Caching SHA-2 Pluggable Authentication". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--histignore</code> </p>
<p> A list of one or more colon-separated patterns specifying statements to ignore for logging purposes. These patterns are added to the default pattern list (&quot;*IDENTIFIED*:*PASSWORD*&quot;). The value specified for this option affects logging of statements written to the history file, and to syslog if the <code>--syslog</code> option is given. For more information, see the section called "MYSQL CLIENT LOGGING". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--host=</code><i>host_name</i>, <code>-h </code><i>host_name</i> </p>
<p> Connect to the MySQL server on the given host. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--html</code>, <code>-H</code> </p>
<p> Produce HTML output. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--ignore-spaces</code>, <code>-i</code> </p>
<p> Ignore spaces after function names. The effect of this is described in the discussion for the IGNORE_SPACE SQL mode (see Section 5.1.11, "Server SQL Modes"). </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--init-command=str</code> </p>
<p> SQL statement to execute after connecting to the server. If auto-reconnect is enabled, the statement is executed again after reconnection occurs. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--line-numbers</code> </p>
<p> Write line numbers for errors. Disable this with <code>--skip-line-numbers</code>. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--local-infile[={0|1}]</code> </p>
<p> By default, LOCAL capability for LOAD DATA is determined by the default compiled into the MySQL client library. To enable or disable LOCAL explicitly, use the <code>--local-infile</code> option. When given with no value, the option enables LOCAL. When given as <code>--local-infile=0</code> or <code>--local-infile=1</code>, the option explicitly disables or enables LOCAL. </p>
<p> Successful use of LOCAL load operations within <code>mysql</code> also requires that the server permits local loading; see Section 6.1.6, "Security Issues with LOAD DATA LOCAL" </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--login-path=</code><i>name</i> </p>
<p> Read options from the named login path in the .mylogin.cnf login path file. A "login path" is an option group containing options that specify which MySQL server to connect to and which account to authenticate as. To create or modify a login path file, use the <code>mysql_config_editor</code> utility. See <code><a href="/docs/linux/man/1-mysql_config_editor/">mysql_config_editor</a></code>(1). </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, "Command-Line Options that Affect Option-File Handling". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--max-allowed-packet=</code><i>value</i> The maximum size of the buffer for client/server communication. The default is 16MB, the maximum is 1GB. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--max-join-size=</code><i>value</i> The automatic limit for rows in a join when using <code>--safe-updates</code>. (Default value is 1,000,000.) </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--named-commands</code>, <code>-G</code> </p>
<p> Enable named <code>mysql</code> commands. Long-format commands are permitted, not just short-format commands. For example, quit and \q both are recognized. Use <code>--skip-named-commands</code> to disable named commands. See the section called "MYSQL CLIENT COMMANDS". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--net-buffer-length=</code><i>value</i> The buffer size for TCP/IP and socket communication. (Default value is 16KB.) </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--no-auto-rehash</code>, <code>-A</code> </p>
<p> This has the same effect as <code>--skip-auto-rehash</code>. See the description for <code>--auto-rehash</code>. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--no-beep</code>, <code>-b</code> </p>
<p> Do not beep when errors occur. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--no-defaults</code> </p>
<p> Do not read any option files. If program startup fails due to reading unknown options from an option file, <code>--no-defaults</code> can be used to prevent them from being read. </p>
<p> The exception is that the .mylogin.cnf file, if it exists, is read in all cases. This permits passwords to be specified in a safer way than on the command line even when <code>--no-defaults</code> is used. (.mylogin.cnf is created by the <code>mysql_config_editor</code> utility. See <code><a href="/docs/linux/man/1-mysql_config_editor/">mysql_config_editor</a></code>(1).) </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, "Command-Line Options that Affect Option-File Handling". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--one-database</code>, <code>-o</code> </p>
<p> Ignore statements except those that occur while the default database is the one named on the command line. This option is rudimentary and should be used with care. Statement filtering is based only on USE statements. </p>
<p> Initially, <code>mysql</code> executes statements in the input because specifying a database <i>db_name</i> on the command line is equivalent to inserting USE <i>db_name</i> at the beginning of the input. Then, for each USE statement encountered, <code>mysql</code> accepts or rejects following statements depending on whether the database named is the one on the command line. The content of the statements is immaterial. </p>
<p> Suppose that <code>mysql</code> is invoked to process this set of statements: </p>
 </dd>
<dl>
<dd> <pre><code>DELETE FROM db2.t2;
USE db2;
DROP TABLE db1.t1;
CREATE TABLE db1.t1 (i INT);
USE db1;
INSERT INTO t1 (i)VALUES(1);
CREATE TABLE db2.t1 (j INT);
</code></pre>
 </dd></dl>
<p> If the command line is <code>mysql --force --one-database db1</code>, <code>mysql</code> handles the input as follows: </p>
<dl>
<dd> <p> &bull; The DELETE statement is executed because the default database is db1, even though the statement names a table in a different database. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; The DROP TABLE and CREATE TABLE statements are not executed because the default database is not db1, even though the statements name a table in db1. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; The INSERT and CREATE TABLE statements are executed because the default database is db1, even though the CREATE TABLE statement names a table in a different database. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> &bull; <code>--pager[=</code><i>command</i><code>]</code> </p>
<p> Use the given command for paging query output. If the command is omitted, the default pager is the value of your PAGER environment variable. Valid pagers are <code>less</code>, <code>more</code>, <code>cat [&gt; filename]</code>, and so forth. This option works only on Unix and only in interactive mode. To disable paging, use <code>--skip-pager</code>. the section called "MYSQL CLIENT COMMANDS", discusses output paging further. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--password[=</code><i>password</i><code>]</code>, <code>-p[</code><i>password</i><code>]</code> </p>
<p> The password of the MySQL account used for connecting to the server. The password value is optional. If not given, <code>mysql</code> prompts for one. If given, there must be <i>no space</i> between <code>--password=</code> or <code>-p</code> and the password following it. If no password option is specified, the default is to send no password. </p>
<p> Specifying a password on the command line should be considered insecure. To avoid giving the password on the command line, use an option file. See Section 6.1.2.1, "End-User Guidelines for Password Security". </p>
<p> To explicitly specify that there is no password and that <code>mysql</code> should not prompt for one, use the <code>--skip-password</code> option. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--pipe</code>, <code>-W</code> </p>
<p> On Windows, connect to the server using a named pipe. This option applies only if the server was started with the named_pipe system variable enabled to support named-pipe connections. In addition, the user making the connection must be a member of the Windows group specified by the named_pipe_full_access_group system variable. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--plugin-dir=</code><i>dir_name</i> </p>
<p> The directory in which to look for plugins. Specify this option if the <code>--default-auth</code> option is used to specify an authentication plugin but <code>mysql</code> does not find it. See Section 6.2.17, "Pluggable Authentication". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--port=</code><i>port_num</i>, <code>-P </code><i>port_num</i> </p>
<p> For TCP/IP connections, the port number to use. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--print-defaults</code> </p>
<p> Print the program name and all options that it gets from option files. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, "Command-Line Options that Affect Option-File Handling". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--prompt=</code><i>format_str</i> </p>
<p> Set the prompt to the specified format. The default is mysql&gt;. The special sequences that the prompt can contain are described in the section called "MYSQL CLIENT COMMANDS". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--protocol={TCP|SOCKET|PIPE|MEMORY}</code> </p>
<p> The connection protocol to use for connecting to the server. It is useful when the other connection parameters normally result in use of a protocol other than the one you want. For details on the permissible values, see Section 4.2.4, "Connecting to the MySQL Server Using Command Options". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--quick</code>, <code>-q</code> </p>
<p> Do not cache each query result, print each row as it is received. This may slow down the server if the output is suspended. With this option, <code>mysql</code> does not use the history file. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--raw</code>, <code>-r</code> </p>
<p> For tabular output, the "boxing" around columns enables one column value to be distinguished from another. For nontabular output (such as is produced in batch mode or when the <code>--batch</code> or <code>--silent</code> option is given), special characters are escaped in the output so they can be identified easily. Newline, tab, NUL, and backslash are written as \n, \t, \0, and \\. The <code>--raw</code> option disables this character escaping. </p>
<p> The following example demonstrates tabular versus nontabular output and the use of raw mode to disable escaping: </p>
 </dd>
<dl>
<dd> <pre><code>% mysql mysql&gt; SELECT CHAR(92);
+----------+
| CHAR(92) |
+----------+
| \ |
+----------+
% mysql -s mysql&gt; SELECT CHAR(92);
CHAR(92)
\\
% mysql -s -r mysql&gt; SELECT CHAR(92);
CHAR(92)
\
</code></pre>
 </dd></dl>
</dl>
<dl>
<dd> <p> &bull; <code>--reconnect</code> </p>
<p> If the connection to the server is lost, automatically try to reconnect. A single reconnect attempt is made each time the connection is lost. To suppress reconnection behavior, use <code>--skip-reconnect</code>. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--safe-updates</code>, <code>--i-am-a-dummy</code>, <code>-U</code> </p>
<p> If this option is enabled, UPDATE and DELETE statements that do not use a key in the WHERE clause or a LIMIT clause produce an error. In addition, restrictions are placed on SELECT statements that produce (or are estimated to produce) very large result sets. If you have set this option in an option file, you can use <code>--skip-safe-updates</code> on the command line to override it. For more information about this option, see Using Safe-Updates Mode (--safe-updates). </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--select-limit=</code><i>value</i> The automatic limit for SELECT statements when using <code>--safe-updates</code>. (Default value is 1,000.) </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--server-public-key-path=</code><i>file_name</i> </p>
<p> The path name to a file containing a client-side copy of the public key required by the server for RSA key pair-based password exchange. The file must be in PEM format. This option applies to clients that authenticate with the sha256_password or caching_sha2_password authentication plugin. This option is ignored for accounts that do not authenticate with one of those plugins. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection. </p>
<p> If <code>--server-public-key-path=</code><i>file_name</i> is given and specifies a valid public key file, it takes precedence over <code>--get-server-public-key</code>. </p>
<p> This option is available only if MySQL was built using OpenSSL. </p>
<p> For information about the sha256_password and caching_sha2_password plugins, see Section 6.4.1.3, "SHA-256 Pluggable Authentication", and Section 6.4.1.2, "Caching SHA-2 Pluggable Authentication". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--shared-memory-base-name=</code><i>name</i> </p>
<p> On Windows, the shared-memory name to use for connections made using shared memory to a local server. The default value is MYSQL. The shared-memory name is case-sensitive. </p>
<p> This option applies only if the server was started with the shared_memory system variable enabled to support shared-memory connections. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--show-warnings</code> </p>
<p> Cause warnings to be shown after each statement if there are any. This option applies to interactive and batch mode. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--sigint-ignore</code> </p>
<p> Ignore SIGINT signals (typically the result of typing Control+C). </p>
<p> Without this option, typing Control+C interrupts the current statement if there is one, or cancels any partial input line otherwise. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--silent</code>, <code>-s</code> </p>
<p> Silent mode. Produce less output. This option can be given multiple times to produce less and less output. </p>
<p> This option results in nontabular output format and escaping of special characters. Escaping may be disabled by using raw mode; see the description for the <code>--raw</code> option. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--skip-column-names</code>, <code>-N</code> </p>
<p> Do not write column names in results. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--skip-line-numbers</code>, <code>-L</code> </p>
<p> Do not write line numbers for errors. Useful when you want to compare result files that include error messages. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--socket=</code><i>path</i>, <code>-S </code><i>path</i> </p>
<p> For connections to localhost, the Unix socket file to use, or, on Windows, the name of the named pipe to use. </p>
<p> On Windows, this option applies only if the server was started with the named_pipe system variable enabled to support named-pipe connections. In addition, the user making the connection must be a member of the Windows group specified by the named_pipe_full_access_group system variable. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--ssl*</code> </p>
<p> Options that begin with <code>--ssl</code> specify whether to connect to the server using SSL and indicate where to find SSL keys and certificates. See the section called "Command Options for Encrypted Connections". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--ssl-fips-mode={OFF|ON|STRICT}</code> Controls whether to enable FIPS mode on the client side. The <code>--ssl-fips-mode</code> option differs from other <code>--ssl-</code><i>xxx</i> options in that it is not used to establish encrypted connections, but rather to affect which cryptographic operations are permitted. See Section 6.5, "FIPS Support". </p>
<p> These <code>--ssl-fips-mode</code> values are permitted: </p>
 </dd>
<dl>
<dd> <p> &bull; OFF: Disable FIPS mode. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; ON: Enable FIPS mode. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; STRICT: Enable "strict" FIPS mode. </p>
 </dd></dl>
<dl>
<dd> <p> <br />
 <font SIZE="+1"> <code>Note</code> </font> <br />
 If the OpenSSL FIPS Object Module is not available, the only permitted value for <code>--ssl-fips-mode</code> is OFF. In this case, setting <code>--ssl-fips-mode</code> to ON or STRICT causes the client to produce a warning at startup and to operate in non-FIPS mode. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> &bull; <code>--syslog</code>, <code>-j</code> </p>
<p> This option causes <code>mysql</code> to send interactive statements to the system logging facility. On Unix, this is syslog; on Windows, it is the Windows Event Log. The destination where logged messages appear is system dependent. On Linux, the destination is often the /var/log/messages file. </p>
<p> Here is a sample of output generated on Linux by using <code>--syslog</code>. This output is formatted for readability; each logged message actually takes a single line. </p>
 </dd>
<dl>
<dd> <pre><code>Mar 7 12:39:25 myhost MysqlClient[20824]:
  SYSTEM_USER:'oscar', MYSQL_USER:'my_oscar', CONNECTION_ID:23,
  DB_SERVER:'127.0.0.1', DB:'--', QUERY:'USE test;'
Mar 7 12:39:28 myhost MysqlClient[20824]:
  SYSTEM_USER:'oscar', MYSQL_USER:'my_oscar', CONNECTION_ID:23,
  DB_SERVER:'127.0.0.1', DB:'test', QUERY:'SHOW TABLES;'
</code></pre>
 </dd></dl>
<p> For more information, see the section called "MYSQL CLIENT LOGGING". </dl>
 </p>
<dl>
<dd> <p> &bull; <code>--table</code>, <code>-t</code> </p>
<p> Display output in table format. This is the default for interactive use, but can be used to produce table output in batch mode. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--tee=</code><i>file_name</i> </p>
<p> Append a copy of output to the given file. This option works only in interactive mode. the section called "MYSQL CLIENT COMMANDS", discusses tee files further. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--tls-ciphersuites=</code><i>ciphersuite_list</i> </p>
<p> The permissible ciphersuites for encrypted connections that use TLSv1.3. The value is a list of one or more colon-separated ciphersuite names. The ciphersuites that can be named for this option depend on the SSL library used to compile MySQL. For details, see Section 6.3.2, "Encrypted Connection TLS Protocols and Ciphers". </p>
<p> This option was added in MySQL 8.0.16. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--tls-version=</code><i>protocol_list</i> </p>
<p> The permissible TLS protocols for encrypted connections. The value is a list of one or more comma-separated protocol names. The protocols that can be named for this option depend on the SSL library used to compile MySQL. For details, see Section 6.3.2, "Encrypted Connection TLS Protocols and Ciphers". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--unbuffered</code>, <code>-n</code> </p>
<p> Flush the buffer after each query. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--user=</code><i>user_name</i>, <code>-u </code><i>user_name</i> </p>
<p> The user name of the MySQL account to use for connecting to the server. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--verbose</code>, <code>-v</code> </p>
<p> Verbose mode. Produce more output about what the program does. This option can be given multiple times to produce more and more output. (For example, <code>-v -v -v</code> produces table output format even in batch mode.) </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--version</code>, <code>-V</code> </p>
<p> Display version information and exit. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--vertical</code>, <code>-E</code> </p>
<p> Print query output rows vertically (one line per column value). Without this option, you can specify vertical output for individual statements by terminating them with \G. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--wait</code>, <code>-w</code> </p>
<p> If the connection cannot be established, wait and retry instead of aborting. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>--xml</code>, <code>-X</code> </p>
<p> Produce XML output. </p>
 </dd>
<dl>
<dd> <pre><code>&lt;field name=&quot; column_name &quot;&gt;NULL&lt;/field&gt;
</code></pre>
 </dd></dl>
<p> The output when <code>--xml</code> is used with <code>mysql</code> matches that of <code>mysqldump</code> <code>--xml</code>. See <code><a href="/docs/linux/man/1-mysqldump/">mysqldump</a></code>(1), for details. </p>
<p> The XML output also uses an XML namespace, as shown here: </p>
<dl>
<dd> <pre><code>shell&gt; mysql --xml -uroot -e &quot;SHOW VARIABLES LIKE 'version%'&quot; &lt;?xml version=&quot;1.0&quot;?&gt;
&lt;resultset statement=&quot;SHOW VARIABLES LIKE 'version%'&quot; xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot;&gt;
&lt;row&gt;
&lt;field name=&quot;Variable_name&quot;&gt;version&lt;/field&gt;
&lt;field name=&quot;Value&quot;&gt;5.0.40-debug&lt;/field&gt;
&lt;/row&gt;
&lt;row&gt;
&lt;field name=&quot;Variable_name&quot;&gt;version_comment&lt;/field&gt;
&lt;field name=&quot;Value&quot;&gt;Source distribution&lt;/field&gt;
&lt;/row&gt;
&lt;row&gt;
&lt;field name=&quot;Variable_name&quot;&gt;version_compile_machine&lt;/field&gt;
&lt;field name=&quot;Value&quot;&gt;i686&lt;/field&gt;
&lt;/row&gt;
&lt;row&gt;
&lt;field name=&quot;Variable_name&quot;&gt;version_compile_os&lt;/field&gt;
&lt;field name=&quot;Value&quot;&gt;suse-linux-gnu&lt;/field&gt;
&lt;/row&gt;
&lt;/resultset&gt;
</code></pre>
 </dd></dl>
</dl>
<dl>
<dd> <p> &bull; <code>--zstd-compression-level=</code><i>level</i> The compression level to use for connections to the server that use the zstd compression algorithm. The permitted levels are from 1 to 22, with larger values indicating increasing levels of compression. The default zstd compression level is 3. The compression level setting has no effect on connections that do not use zstd compression. </p>
<p> For more information, see Section 4.2.6, "Connection Compression Control". </p>
<p> This option was added in MySQL 8.0.18. </p>
 </dd></dl>
<h2>MYSQL CLIENT COMMANDS</h2>
<p> <code>mysql</code> sends each SQL statement that you issue to the server to be executed. There is also a set of commands that <code>mysql</code> itself interprets. For a list of these commands, type help or \h at the mysql&gt; prompt: </p>
<dl>
<dd> <pre><code>mysql&gt; help List of all MySQL commands:
Note that all text commands must be first on line and end with ';'
? (\?) Synonym for `help'.
clear (\c) Clear the current input statement.
connect (\r) Reconnect to the server. Optional arguments are db and host.
delimiter (\d) Set statement delimiter.
edit (\e) Edit command with $EDITOR.
ego (\G) Send command to mysql server, display result vertically.
exit (\q) Exit mysql. Same as quit.
go (\g) Send command to mysql server.
help (\h) Display this help.
nopager (\n) Disable pager, print to stdout.
notee (\t) Don't write into outfile.
pager (\P) Set PAGER [to_pager]. Print the query results via PAGER.
print (\p) Print current command.
prompt (\R) Change your mysql prompt.
quit (\q) Quit mysql.
rehash (\#) Rebuild completion hash.
source (\.) Execute an SQL script file. Takes a file name as an argument.
status (\s) Get status information from the server.
system (\!) Execute a system shell command.
tee (\T) Set outfile [to_outfile]. Append everything into given
               outfile.
use (\u) Use another database. Takes database name as argument.
charset (\C) Switch to another charset. Might be needed for processing
               binlog with multi-byte charsets.
warnings (\W) Show warnings after every statement.
nowarning (\w) Don't show warnings after every statement.
resetconnection(\x) Clean session context.
For server side help, type 'help contents'
</code></pre>
 </dd></dl>
<p> If <code>mysql</code> is invoked with the <code>--binary-mode</code> option, all <code>mysql</code> commands are disabled except charset and delimiter in noninteractive mode (for input piped to <code>mysql</code> or loaded using the source command). </p>
<p> Each command has both a long and short form. The long form is not case-sensitive; the short form is. The long form can be followed by an optional semicolon terminator, but the short form should not. </p>
<p> The use of short-form commands within multiple-line /* ... */ comments is not supported. Short-form commands do work within single-line /*! ... */ version comments, as do /*+ ... */ optimizer-hint comments, which are stored in object definitions. If there is a concern that optimizer-hint comments may be stored in object definitions so that dump files when reloaded with mysql would result in execution of such commands, either invoke <code>mysql</code> with the <code>--binary-mode</code> option or use a reload client other than <code>mysql</code>. </p>
<dl>
<dd> <p> &bull; help [<i>arg</i>], \h [<i>arg</i>], \? [<i>arg</i>], ? [<i>arg</i>] </p>
<p> Display a help message listing the available <code>mysql</code> commands. </p>
<p> If you provide an argument to the help command, <code>mysql</code> uses it as a search string to access server-side help from the contents of the MySQL Reference Manual. For more information, see the section called "MYSQL CLIENT SERVER-SIDE HELP". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; charset <i>charset_name</i>, \C <i>charset_name</i> </p>
<p> Change the default character set and issue a SET NAMES statement. This enables the character set to remain synchronized on the client and server if <code>mysql</code> is run with auto-reconnect enabled (which is not recommended), because the specified character set is used for reconnects. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; clear, \c </p>
<p> Clear the current input. Use this if you change your mind about executing the statement that you are entering. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; connect [<i>db_name</i> <i>host_name</i>]], \r [<i>db_name</i> <i>host_name</i>]] </p>
<p> Reconnect to the server. The optional database name and host name arguments may be given to specify the default database or the host where the server is running. If omitted, the current values are used. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; delimiter <i>str</i>, \d <i>str</i> </p>
<p> Change the string that <code>mysql</code> interprets as the separator between SQL statements. The default is the semicolon character (;). </p>
<p> The delimiter string can be specified as an unquoted or quoted argument on the delimiter command line. Quoting can be done with either single quote (&#8216;), double quote (&quot;), or backtick (`) characters. To include a quote within a quoted string, either quote the string with a different quote character or escape the quote with a backslash (\) character. Backslash should be avoided outside of quoted strings because it is the escape character for MySQL. For an unquoted argument, the delimiter is read up to the first space or end of line. For a quoted argument, the delimiter is read up to the matching quote on the line. </p>
<p> <code>mysql</code> interprets instances of the delimiter string as a statement delimiter anywhere it occurs, except within quoted strings. Be careful about defining a delimiter that might occur within other words. For example, if you define the delimiter as X, you will be unable to use the word INDEX in statements. <code>mysql</code> interprets this as INDE followed by the delimiter X. </p>
<p> When the delimiter recognized by <code>mysql</code> is set to something other than the default of ;, instances of that character are sent to the server without interpretation. However, the server itself still interprets ; as a statement delimiter and processes statements accordingly. This behavior on the server side comes into play for multiple-statement execution (see Section 28.7.22, "C API Multiple Statement Execution Support"), and for parsing the body of stored procedures and functions, triggers, and events (see Section 24.1, "Defining Stored Programs"). </p>
 </dd></dl>
<dl>
<dd> <p> &bull; edit, \e </p>
<p> Edit the current input statement. <code>mysql</code> checks the values of the EDITOR and VISUAL environment variables to determine which editor to use. The default editor is <code>vi</code> if neither variable is set. </p>
<p> The edit command works only in Unix. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; ego, \G </p>
<p> Send the current statement to the server to be executed and display the result using vertical format. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; exit, \q </p>
<p> Exit <code>mysql</code>. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; go, \g </p>
<p> Send the current statement to the server to be executed. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; nopager, \n </p>
<p> Disable output paging. See the description for pager. </p>
<p> The nopager command works only in Unix. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; notee, \t </p>
<p> Disable output copying to the tee file. See the description for tee. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; nowarning, \w </p>
<p> Disable display of warnings after each statement. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; pager [<i>command</i>], \P [<i>command</i>] </p>
<p> Enable output paging. By using the <code>--pager</code> option when you invoke <code>mysql</code>, it is possible to browse or search query results in interactive mode with Unix programs such as <code>less</code>, <code>more</code>, or any other similar program. If you specify no value for the option, <code>mysql</code> checks the value of the PAGER environment variable and sets the pager to that. Pager functionality works only in interactive mode. </p>
<p> Output paging can be enabled interactively with the pager command and disabled with nopager. The command takes an optional argument; if given, the paging program is set to that. With no argument, the pager is set to the pager that was set on the command line, or stdout if no pager was specified. </p>
<p> Output paging works only in Unix because it uses the popen() function, which does not exist on Windows. For Windows, the tee option can be used instead to save query output, although it is not as convenient as pager for browsing output in some situations. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; print, \p </p>
<p> Print the current input statement without executing it. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; prompt [<i>str</i>], \R [<i>str</i>] </p>
<p> Reconfigure the <code>mysql</code> prompt to the given string. The special character sequences that can be used in the prompt are described later in this section. </p>
<p> If you specify the prompt command with no argument, <code>mysql</code> resets the prompt to the default of mysql&gt;. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; quit, \q </p>
<p> Exit <code>mysql</code>. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; rehash, \# </p>
<p> Rebuild the completion hash that enables database, table, and column name completion while you are entering statements. (See the description for the <code>--auto-rehash</code> option.) </p>
 </dd></dl>
<dl>
<dd> <p> &bull; resetconnection, \x </p>
<p> Reset the connection to clear the session state. </p>
<p> Resetting a connection has effects similar to mysql_change_user() or an auto-reconnect except that the connection is not closed and reopened, and re-authentication is not done. See Section 28.7.6.3, "mysql_change_user()", and Section 28.7.27, "C API Automatic Reconnection Control". </p>
<p> This example shows how resetconnection clears a value maintained in the session state: </p>
 </dd>
<dl>
<dd> <pre><code>mysql&gt; SELECTLAST_INSERT_ID(3); +-------------------+
|LAST_INSERT_ID(3) |
+-------------------+
| 3 |
+-------------------+
mysql&gt; SELECT LAST_INSERT_ID(); +------------------+
| LAST_INSERT_ID() |
+------------------+
| 3 |
+------------------+
mysql&gt; resetconnection; mysql&gt; SELECT LAST_INSERT_ID(); +------------------+
| LAST_INSERT_ID() |
+------------------+
| 0 |
+------------------+
</code></pre>
 </dd></dl>
</dl>
<dl>
<dd> <p> &bull; source <i>file_name</i>, \. <i>file_name</i> </p>
<p> Read the named file and executes the statements contained therein. On Windows, specify path name separators as / or \\. </p>
<p> Quote characters are taken as part of the file name itself. For best results, the name should not include space characters. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; status, \s </p>
<p> Provide status information about the connection and the server you are using. If you are running with <code>--safe-updates</code> enabled, status also prints the values for the <code>mysql</code> variables that affect your queries. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; system <i>command</i>, \! <i>command</i> </p>
<p> Execute the given command using your default command interpreter. </p>
<p> Prior to MySQL 8.0.19, the system command works only in Unix. As of 8.0.19, it also works on Windows. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; tee [<i>file_name</i>], \T [<i>file_name</i>] </p>
<p> By using the <code>--tee</code> option when you invoke <code>mysql</code>, you can log statements and their output. All the data displayed on the screen is appended into a given file. This can be very useful for debugging purposes also. <code>mysql</code> flushes results to the file after each statement, just before it prints its next prompt. Tee functionality works only in interactive mode. </p>
<p> You can enable this feature interactively with the tee command. Without a parameter, the previous file is used. The tee file can be disabled with the notee command. Executing tee again re-enables logging. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; use <i>db_name</i>, \u <i>db_name</i> </p>
<p> Use <i>db_name</i> as the default database. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; warnings, \W </p>
<p> Enable display of warnings after each statement (if there are any). </p>
 </dd></dl>
<p> Here are a few tips about the pager command: </p>
<dl>
<dd> <p> &bull; You can use it to write to a file and the results go only to the file: </p>
 </dd>
<dl>
<dd> <pre><code>mysql&gt; pager cat &gt; /tmp/log.txt 
</code></pre>
 </dd></dl>
<p> You can also pass any options for the program that you want to use as your pager: </p>
<dl>
<dd> <pre><code>mysql&gt; pager less -n -i -S 
</code></pre>
 </dd></dl>
</dl>
<dl>
<dd> <p> &bull; In the preceding example, note the <code>-S</code> option. You may find it very useful for browsing wide query results. Sometimes a very wide result set is difficult to read on the screen. The <code>-S</code> option to <code>less</code> can make the result set much more readable because you can scroll it horizontally using the left-arrow and right-arrow keys. You can also use <code>-S</code> interactively within <code>less</code> to switch the horizontal-browse mode on and off. For more information, read the <code>less</code> manual page: </p>
 </dd>
<dl>
<dd> <pre><code>shell&gt; man less 
</code></pre>
 </dd></dl>
</dl>
<dl>
<dd> <p> &bull; The <code>-F</code> and <code>-X</code> options may be used with <code>less</code> to cause it to exit if output fits on one screen, which is convenient when no scrolling is necessary: </p>
 </dd>
<dl>
<dd> <pre><code>mysql&gt; pager less -n -i -S -F -X 
</code></pre>
 </dd></dl>
</dl>
<dl>
<dd> <p> &bull; You can specify very complex pager commands for handling query output: </p>
 </dd>
<dl>
<dd> <pre><code>mysql&gt; pager cat | tee /dr1/tmp/res.txt \  | tee /dr2/tmp/res2.txt | less -n -i -S 
</code></pre>
 </dd></dl>
<p> In this example, the command would send query results to two files in two different directories on two different file systems mounted on /dr1 and /dr2, yet still display the results onscreen using <code>less</code>. </dl>
 </p>
<p> You can also combine the tee and pager functions. Have a tee file enabled and pager set to <code>less</code>, and you are able to browse the results using the <code>less</code> program and still have everything appended into a file the same time. The difference between the Unix tee used with the pager command and the <code>mysql</code> built-in tee command is that the built-in tee works even if you do not have the Unix <code>tee</code> available. The built-in tee also logs everything that is printed on the screen, whereas the Unix <code>tee</code> used with pager does not log quite that much. Additionally, tee file logging can be turned on and off interactively from within <code>mysql</code>. This is useful when you want to log some queries to a file, but not others. </p>
<p> The prompt command reconfigures the default mysql&gt; prompt. The string for defining the prompt can contain the following special sequences. </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Option </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> C </td>
<td> The current connection identifier 
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td> A counter that increments for each statement you issue 
</td>
</tr>
<tr VALIGN=top>
<td> D </td>
<td> The full current date 
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td> The default database 
</td>
</tr>
<tr VALIGN=top>
<td> The server host T} T{ <hr />
The current delimiter T} T{ m T}:T{ Minutes of the current time T} T{ T}:T{ A newline character T} T{ O T}:T{ The current month in three-letter format (Jan, Feb, ...) T} T{ The current month in numeric format T} T{ P T}:T{ am/pm T} T{  T}:T{ The current TCP/IP port or socket file T} T{ R T}:T{ The current time, in 24-hour military time (0-23) T} T{ T}:T{ The current time, standard 12-hour time (1-12) T} T{ S T}:T{ Semicolon T} T{ T}:T{ Seconds of the current time T} T{ T}:T{ A tab character T} T{ U T}:T{  Your full <i>user_name</i>@<i>host_name</i> account name T} T{ T}:T{ Your user name T} T{ The server version T} T{ The current day of the week in three-letter format (Mon, Tue, ...) T} T{ Y T}:T{ The current year, four digits T} T{ y T}:T{ The current year, two digits T} T{ _ T}:T{ A space T} T{ \ T}:T{ A space (a space follows the backslash) T} T{ &#8216; T}:T{ Single quote T} T{ T}:T{ Double quote T} T{ \ T}:T{ A literal &nbsp;backslash character T} T{ \fIx T}:T{  <p> <i>x</i>, for any "<i>x</i>" not listed above T} </p>
 You can set the prompt in several ways: <dl>
<dd>  &bull; <i>Use an environment variable.</i> You can set the MYSQL_PS1 environment variable to a prompt string. For example:  </dd>
<dl>
<dd>  <pre><code>shell&gt; export MYSQL_PS1=&quot;(\u@\h) [\d]&gt; &quot; 
</code></pre>
  </dd></dl>
 </dl>
 <dl>
<dd>  &bull; <i>Use a command-line option.</i> You can set the <code>--prompt</code> option on the command line to <code>mysql</code>. For example:  </dd>
<dl>
<dd>  <pre><code>shell&gt; mysql --prompt=&quot;(\u@\h) [\d]&gt; &quot; (user [at] host) [database]&gt;
</code></pre>
  </dd></dl>
 </dl>
 <dl>
<dd>  &bull; <i>Use an option file.</i> You can set the prompt option in the [mysql] group of any MySQL option file, such as /etc/my.cnf or the .my.cnf file in your home directory. For example:  </dd>
<dl>
<dd>  <pre><code>[mysql]
prompt=(\\u@\\h) [\\d]&gt;\\_
</code></pre>
  </dd></dl>
  In this example, note that the backslashes are doubled. If you set the prompt using the prompt option in an option file, it is advisable to double the backslashes when using the special prompt options. There is some overlap in the set of permissible prompt options and the set of special escape sequences that are recognized in option files. (The rules for escape sequences in option files are listed in Section 4.2.2.2, "Using Option Files".) The overlap may cause you problems if you use single backslashes. For example, \s is interpreted as a space rather than as the current seconds value. The following example shows how to define a prompt within an option file to include the current time in <i>hh:mm:ss</i>&gt; format: <dl>
<dd>  <pre><code>[mysql]
prompt=&quot;\\r:\\m:\\s&gt; &quot;
</code></pre>
  </dd></dl>
 </dl>
 <dl>
<dd>  &bull; <i>Set the prompt interactively.</i> You can change your prompt interactively by using the prompt (or \R) command. For example:  </dd>
<dl>
<dd>  <pre><code>mysql&gt; prompt (\u@\h) [\d]&gt;\_ PROMPT set to '(\u@\h) [\d]&gt;\_'
( user @ host ) [ database ]&gt;
( user @ host ) [ database ]&gt; prompt
Returning to default PROMPT of mysql&gt;
mysql&gt;
</code></pre>
  </dd></dl>
 </dl>
  <h2>MYSQL CLIENT LOGGING</h2>
  The <code>mysql</code> client can do these types of logging for statements executed interactively: <dl>
<dd>  &bull; On Unix, <code>mysql</code> writes the statements to a history file. By default, this file is named .mysql_history in your home directory. To specify a different file, set the value of the MYSQL_HISTFILE environment variable.  </dd></dl>
 <dl>
<dd>  &bull; On all platforms, if the <code>--syslog</code> option is given, <code>mysql</code> writes the statements to the system logging facility. On Unix, this is syslog; on Windows, it is the Windows Event Log. The destination where logged messages appear is system dependent. On Linux, the destination is often the /var/log/messages file.  </dd></dl>
  The following discussion describes characteristics that apply to all logging types and provides information specific to each logging type. <dl>
<dd>  &bull; How Logging Occurs  </dd></dl>
 <dl>
<dd>  &bull; Controlling the History File  </dd></dl>
 <dl>
<dd>  &bull; syslog Logging Characteristics  </dd></dl>
 How Logging Occurs  For each enabled logging destination, statement logging occurs as follows: <dl>
<dd>  &bull; Statements are logged only when executed interactively. Statements are noninteractive, for example, when read from a file or a pipe. It is also possible to suppress statement logging by using the <code>--batch</code> or <code>--execute</code> option.  </dd></dl>
 <dl>
<dd>  &bull; Statements are ignored and not logged if they match any pattern in the "ignore" list. This list is described later.  </dd></dl>
 <dl>
<dd>  &bull; <code>mysql</code> logs each nonignored, nonempty statement line individually.  </dd></dl>
 <dl>
<dd>  &bull; If a nonignored statement spans multiple lines (not including the terminating delimiter), <code>mysql</code> concatenates the lines to form the complete statement, maps newlines to spaces, and logs the result, plus a delimiter.  </dd></dl>
  Consequently, an input statement that spans multiple lines can be logged twice. Consider this input: <dl>
<dd>  <pre><code>mysql&gt; SELECT     -&gt; 'Today is'     -&gt; ,     -&gt; CURDATE()     -&gt; ; 
</code></pre>
  </dd></dl>
  In this case, <code>mysql</code> logs the "SELECT", "&#8216;Today is&#8217;", ",", "CURDATE()", and ";" lines as it reads them. It also logs the complete statement, after mapping SELECT\n&#8217;Today is&#8217;\n,\nCURDATE() to SELECT &#8216;Today is&#8217; , CURDATE(), plus a delimiter. Thus, these lines appear in logged output: <dl>
<dd>  <pre><code>SELECT
'Today is'
,
CURDATE()
;
SELECT 'Today is' , CURDATE();
</code></pre>
  </dd></dl>
  <p> <code>mysql</code> ignores for logging purposes statements that match any pattern in the "ignore" list. By default, the pattern list is &quot;*IDENTIFIED*:*PASSWORD*&quot;, to ignore statements that refer to passwords. Pattern matching is not case-sensitive. Within patterns, two characters are special: </p>
<dl>
<dd>  &bull; ? matches any single character.  </dd></dl>
 <dl>
<dd>  &bull; * matches any sequence of zero or more characters.  </dd></dl>
  To specify additional patterns, use the <code>--histignore</code> option or set the MYSQL_HISTIGNORE environment variable. (If both are specified, the option value takes precedence.) The value should be a list of one or more colon-separated patterns, which are appended to the default pattern list.  Patterns specified on the command line might need to be quoted or escaped to prevent your command interpreter from treating them specially. For example, to suppress logging for UPDATE and DELETE statements in addition to statements that refer to passwords, invoke <code>mysql</code> like this: <dl>
<dd>  <pre><code>shell&gt; mysql --histignore=&quot;*UPDATE*:*DELETE*&quot; 
</code></pre>
  </dd></dl>
  Controlling the History File  The .mysql_history file should be protected with a restrictive access mode because sensitive information might be written to it, such as the text of SQL statements that contain passwords. See Section 6.1.2.1, "End-User Guidelines for Password Security". Statements in the file are accessible from the <code>mysql</code> client when the up-arrow key is used to recall the history. See Disabling Interactive History.  If you do not want to maintain a history file, first remove .mysql_history if it exists. Then use either of the following techniques to prevent it from being created again: <dl>
<dd>  &bull; Set the MYSQL_HISTFILE environment variable to /dev/null. To cause this setting to take effect each time you log in, put it in one of your shell&#8217;s startup files.  </dd></dl>
 <dl>
<dd>  &bull; Create .mysql_history as a symbolic link to /dev/null; this need be done only once:  </dd>
<dl>
<dd>  <pre><code>shell&gt; ln -s /dev/null $HOME/.mysql_history 
</code></pre>
  </dd></dl>
 </dl>
 syslog Logging Characteristics  If the <code>--syslog</code> option is given, <code>mysql</code> writes interactive statements to the system logging facility. Message logging has the following characteristics.  Logging occurs at the "information" level. This corresponds to the LOG_INFO priority for syslog on Unix/Linux syslog capability and to EVENTLOG_INFORMATION_TYPE for the Windows Event Log. Consult your system documentation for configuration of your logging capability.  Message size is limited to 1024 bytes.  Messages consist of the identifier MysqlClient followed by these values: <dl>
<dd>  &bull; SYSTEM_USER  The operating system user name (login name) or -- if the user is unknown.  </dd></dl>
 <dl>
<dd>  &bull; MYSQL_USER  The MySQL user name (specified with the <code>--user</code> option) or -- if the user is unknown.  </dd></dl>
 <dl>
<dd>  &bull; CONNECTION_ID:  The client connection identifier. This is the same as the CONNECTION_ID() function value within the session.  </dd></dl>
 <dl>
<dd>  &bull; DB_SERVER  The server host or -- if the host is unknown.  </dd></dl>
 <dl>
<dd>  &bull; DB  The default database or -- if no database has been selected.  </dd></dl>
 <dl>
<dd>  &bull; QUERY  The text of the logged statement.  </dd></dl>
  Here is a sample of output generated on Linux by using <code>--syslog</code>. This output is formatted for readability; each logged message actually takes a single line. <dl>
<dd>  <pre><code>Mar 7 12:39:25 myhost MysqlClient[20824]:
  SYSTEM_USER:'oscar', MYSQL_USER:'my_oscar', CONNECTION_ID:23,
  DB_SERVER:'127.0.0.1', DB:'--', QUERY:'USE test;'
Mar 7 12:39:28 myhost MysqlClient[20824]:
  SYSTEM_USER:'oscar', MYSQL_USER:'my_oscar', CONNECTION_ID:23,
  DB_SERVER:'127.0.0.1', DB:'test', QUERY:'SHOW TABLES;'
</code></pre>
  </dd></dl>
  <h2>MYSQL CLIENT SERVER-SIDE HELP</h2>
 <dl>
<dd>  <pre><code>mysql&gt; help  search_string 
</code></pre>
  </dd></dl>
  If you provide an argument to the help command, <code>mysql</code> uses it as a search string to access server-side help from the contents of the MySQL Reference Manual. The proper operation of this command requires that the help tables in the mysql database be initialized with help topic information (see Section 5.1.14, "Server-Side Help Support").  If there is no match for the search string, the search fails: <dl>
<dd>  <pre><code>mysql&gt; help me Nothing found
Please try to run 'help contents' for a list of all accessible topics
</code></pre>
  </dd></dl>
  Use <code>help contents</code> to see a list of the help categories: <dl>
<dd>  <pre><code>mysql&gt; help contents You asked for help about help category: &quot;Contents&quot;
For more information, type 'help &lt;item&gt;', where &lt;item&gt; is one of the
following categories:
   Account Management
   Administration
   Data Definition
   Data Manipulation
   Data Types
   Functions
   Functions and Modifiers for Use with GROUP BY
   Geographic Features
   Language Structure
   Plugins
   Storage Engines
   Stored Routines
   Table Maintenance
   Transactions
   Triggers
</code></pre>
  </dd></dl>
  If the search string matches multiple items, <code>mysql</code> shows a list of matching topics: <dl>
<dd>  <pre><code>mysql&gt; help logs Many help items for your request exist.
To make a more specific request, please type 'help &lt;item&gt;',
where &lt;item&gt; is one of the following topics:
   SHOW
   SHOW BINARY LOGS
   SHOW ENGINE
   SHOW LOGS
</code></pre>
  </dd></dl>
  Use a topic as the search string to see the help entry for that topic: <dl>
<dd>  <pre><code>mysql&gt; help show binary logs Name: 'SHOW BINARY LOGS'
Description:
Syntax:
SHOW BINARY LOGS
SHOW MASTER LOGS
Lists the binary log files on the server. This statement is used as
part of the procedure described in [purge-binary-logs], that shows how
to determine which logs can be purged.
mysql&gt; SHOW BINARY LOGS;
+---------------+-----------+-----------+
| Log_name | File_size | Encrypted |
+---------------+-----------+-----------+
| binlog.000015 | 724935 | Yes |
| binlog.000016 | 733481 | Yes |
+---------------+-----------+-----------+
</code></pre>
  </dd></dl>
  The search string can contain the wildcard characters % and _. These have the same meaning as for pattern-matching operations performed with the LIKE operator. For example, HELP rep% returns a list of topics that begin with rep: <dl>
<dd>  <pre><code>mysql&gt; HELP rep% Many help items for your request exist.
To make a more specific request, please type 'help &lt;item&gt;',
where &lt;item&gt; is one of the following
topics:
   REPAIR TABLE
   REPEAT FUNCTION
   REPEAT LOOP
   REPLACE
   REPLACE FUNCTION
</code></pre>
  </dd></dl>
  <h2>EXECUTING SQL STATEMENTS FROM A TEXT FILE</h2>
  The <code>mysql</code> client typically is used interactively, like this: <dl>
<dd>  <pre><code>shell&gt; mysql  db_name 
</code></pre>
  </dd></dl>
  However, it is also possible to put your SQL statements in a file and then tell <code>mysql</code> to read its input from that file. To do so, create a text file <i>text_file</i> that contains the statements you wish to execute. Then invoke <code>mysql</code> as shown here: <dl>
<dd>  <pre><code>shell&gt; mysql  db_name   &lt;  text_file 
</code></pre>
  </dd></dl>
  If you place a USE <i>db_name</i> statement as the first statement in the file, it is unnecessary to specify the database name on the command line: <dl>
<dd>  <pre><code>shell&gt; mysql &lt; text_file 
</code></pre>
  </dd></dl>
  If you are already running <code>mysql</code>, you can execute an SQL script file using the source command or \. command: <dl>
<dd>  <pre><code>mysql&gt; source  file_name mysql&gt; \.  file_name 
</code></pre>
  </dd></dl>
  Sometimes you may want your script to display progress information to the user. For this you can insert statements like this: <dl>
<dd>  <pre><code>SELECT '&lt;info_to_display&gt;' AS ' ';
</code></pre>
  </dd></dl>
  The statement shown outputs &lt;info_to_display&gt;.  You can also invoke <code>mysql</code> with the <code>--verbose</code> option, which causes each statement to be displayed before the result that it produces.  <p> <code>mysql</code> ignores Unicode byte order mark (BOM) characters at the beginning of input files. Previously, it read them and sent them to the server, resulting in a syntax error. Presence of a BOM does not cause <code>mysql</code> to change its default character set. To do that, invoke <code>mysql</code> with an option such as <code>--default-character-set=utf8</code>. </p>
 For more information about batch mode, see Section 3.5, "Using mysql in Batch Mode".  <h2>MYSQL CLIENT TIPS</h2>
  This section provides information about techniques for more effective use of <code>mysql</code> and about <code>mysql</code> operational behavior. <dl>
<dd>  &bull; Input-Line Editing  </dd></dl>
 <dl>
<dd>  &bull; Disabling Interactive History  </dd></dl>
 <dl>
<dd>  &bull; Unicode Support on Windows  </dd></dl>
 <dl>
<dd>  &bull; Displaying Query Results Vertically  </dd></dl>
 <dl>
<dd>  &bull; Using Safe-Updates Mode (--safe-updates)  </dd></dl>
 <dl>
<dd>  &bull; Disabling mysql Auto-Reconnect  </dd></dl>
 <dl>
<dd>  &bull; mysql Client Parser Versus Server Parser  </dd></dl>
 Input-Line Editing  <p> <code>mysql</code> supports input-line editing, which enables you to modify the current input line in place or recall previous input lines. For example, the left-arrow and right-arrow keys move horizontally within the current input line, and the up-arrow and down-arrow keys move up and down through the set of previously entered lines. Backspace deletes the character before the cursor and typing new characters enters them at the cursor position. To enter the line, press Enter. </p>
 On Windows, the editing key sequences are the same as supported for command editing in console windows. On Unix, the key sequences depend on the input library used to build <code>mysql</code> (for example, the libedit or readline library).  Documentation for the libedit and readline libraries is available online. To change the set of key sequences permitted by a given input library, define key bindings in the library startup file. This is a file in your home directory: .editrc for libedit and .inputrc for readline.  For example, in libedit, Control+W deletes everything before the current cursor position and Control+U deletes the entire line. In readline, Control+W deletes the word before the cursor and Control+U deletes everything before the current cursor position. If <code>mysql</code> was built using libedit, a user who prefers the readline behavior for these two keys can put the following lines in the .editrc file (creating the file if necessary): <dl>
<dd>  <pre><code>bind &quot;^W&quot; ed-delete-prev-word
bind &quot;^U&quot; vi-kill-line-prev
</code></pre>
  </dd></dl>
  To see the current set of key bindings, temporarily put a line that says only bind at the end of .editrc. <code>mysql</code> will show the bindings when it starts. Disabling Interactive History  The up-arrow key enables you to recall input lines from current and previous sessions. In cases where a console is shared, this behavior may be unsuitable. <code>mysql</code> supports disabling the interactive history partially or fully, depending on the host platform.  On Windows, the history is stored in memory. Alt+F7 deletes all input lines stored in memory for the current history buffer. It also deletes the list of sequential numbers in front of the input lines displayed with F7 and recalled (by number) with F9. New input lines entered after you press Alt+F7 repopulate the current history buffer. Clearing the buffer does not prevent logging to the Windows Event Viewer, if the <code>--syslog</code> option was used to start <code>mysql</code>. Closing the console window also clears the current history buffer.  To disable interactive history on Unix, first delete the .mysql_history file, if it exists (previous entries are recalled otherwise). Then start <code>mysql</code> with the --histignore=&quot;*&quot; option to ignore all new input lines. To re-enable the recall (and logging) behavior, restart <code>mysql</code> without the option.  If you prevent the .mysql_history file from being created (see Controlling the History File) and use --histignore=&quot;*&quot; to start the <code>mysql</code> client, the interactive history recall facility is disabled fully. Alternatively, if you omit the <code>--histignore</code> option, you can recall the input lines entered during the current session. Unicode Support on Windows  Windows provides APIs based on UTF-16LE for reading from and writing to the console; the <code>mysql</code> client for Windows is able to use these APIs. The Windows installer creates an item in the MySQL menu named MySQL command line client - Unicode. This item invokes the <code>mysql</code> client with properties set to communicate through the console to the MySQL server using Unicode.  To take advantage of this support manually, run <code>mysql</code> within a console that uses a compatible Unicode font and set the default character set to a Unicode character set that is supported for communication with the server: <dl>
<dd>  1. Open a console window.  </dd></dl>
 <dl>
<dd>  2. Go to the console window properties, select the font tab, and choose Lucida Console or some other compatible Unicode font. This is necessary because console windows start by default using a DOS raster font that is inadequate for Unicode.  </dd></dl>
 <dl>
<dd>  3. Execute <code>mysql.exe</code> with the <code>--default-character-set=utf8</code> (or utf8mb4) option. This option is necessary because utf16le is one of the character sets that cannot be used as the client character set. See the section called "Impermissible Client Character Sets".  </dd></dl>
  With those changes, <code>mysql</code> will use the Windows APIs to communicate with the console using UTF-16LE, and communicate with the server using UTF-8. (The menu item mentioned previously sets the font and character set as just described.)  To avoid those steps each time you run <code>mysql</code>, you can create a shortcut that invokes <code>mysql.exe</code>. The shortcut should set the console font to Lucida Console or some other compatible Unicode font, and pass the <code>--default-character-set=utf8</code> (or utf8mb4) option to <code>mysql.exe</code>.  Alternatively, create a shortcut that only sets the console font, and set the character set in the [mysql] group of your my.ini file: <dl>
<dd>  <pre><code>[mysql]
default-character-set=utf8
</code></pre>
  </dd></dl>
  Displaying Query Results Vertically  Some query results are much more readable when displayed vertically, instead of in the usual horizontal table format. Queries can be displayed vertically by terminating the query with \G instead of a semicolon. For example, longer text values that include newlines often are much easier to read with vertical output: <dl>
<dd>  <pre><code>mysql&gt; SELECT * FROM mails WHERE LENGTH(txt) &lt; 300 LIMIT 300,1\G *************************** 1. row ***************************
  msg_nro: 3068
     date: 2000-03-01 23:29:50
time_zone: +0200
mail_from: Jones
    reply: jones [at] example.com
  mail_to: &quot;John Smith&quot; &lt;smith [at] example.com&gt;
      sbj: UTF-8
      txt: &gt;&gt;&gt;&gt;&gt; &quot;John&quot; == John Smith writes:
John&gt; Hi. I think this is a good idea. Is anyone familiar
John&gt; with UTF-8 or Unicode? Otherwise, I'll put this on my
John&gt; TODO list and see what happens.
Yes, please do that.
Regards,
Jones
     file: inbox-jani-1
     hash: 190402944
1 row in set (0.09 sec)
</code></pre>
  </dd></dl>
  Using Safe-Updates Mode (--safe-updates)  For beginners, a useful startup option is <code>--safe-updates</code> (or <code>--i-am-a-dummy</code>, which has the same effect). Safe-updates mode is helpful for cases when you might have issued an UPDATE or DELETE statement but forgotten the WHERE clause indicating which rows to modify. Normally, such statements update or delete all rows in the table. With <code>--safe-updates</code>, you can modify rows only by specifying the key values that identify them, or a LIMIT clause, or both. This helps prevent accidents. Safe-updates mode also restricts SELECT statements that produce (or are estimated to produce) very large result sets.  The <code>--safe-updates</code> option causes <code>mysql</code> to execute the following statement when it connects to the MySQL server, to set the session values of the sql_safe_updates, sql_select_limit, and max_join_size system variables: <dl>
<dd>  <pre><code>SET sql_safe_updates=1, sql_select_limit=1000, max_join_size=1000000;
</code></pre>
  </dd></dl>
  The SET statement affects statement processing as follows: <dl>
<dd>  &bull; Enabling sql_safe_updates causes UPDATE and DELETE statements to produce an error if they do not specify a key constraint in the WHERE clause, or provide a LIMIT clause, or both. For example:  </dd>
<dl>
<dd>  <pre><code>UPDATE tbl_name  SET not_key_column = val  WHERE key_column = val ;
UPDATE tbl_name  SET not_key_column = val  LIMIT 1;
</code></pre>
  </dd></dl>
 </dl>
 <dl>
<dd>  &bull; Setting sql_select_limit to 1,000 causes the server to limit all SELECT result sets to 1,000 rows unless the statement includes a LIMIT clause.  </dd></dl>
 <dl>
<dd>  &bull; Setting max_join_size to 1,000,000 causes multiple-table SELECT statements to produce an error if the server estimates it must examine more than 1,000,000 row combinations.  </dd></dl>
  To specify result set limits different from 1,000 and 1,000,000, you can override the defaults by using the <code>--select-limit</code> and <code>--max-join-size</code> options when you invoke <code>mysql</code>: <dl>
<dd>  <pre><code>mysql --safe-updates --select-limit=500 --max-join-size=10000
</code></pre>
  </dd></dl>
  It is possible for UPDATE and DELETE statements to produce an error in safe-updates mode even with a key specified in the WHERE clause, if the optimizer decides not to use the index on the key column: <dl>
<dd>  &bull; Range access on the index cannot be used if memory usage exceeds that permitted by the range_optimizer_max_mem_size system variable. The optimizer then falls back to a table scan. See the section called "Limiting Memory Use for Range Optimization".  </dd></dl>
 <dl>
<dd>  &bull; If key comparisons require type conversion, the index may not be used (see Section 8.3.1, "How MySQL Uses Indexes"). Suppose that an indexed string column c1 is compared to a numeric value using WHERE c1 = 2222. For such comparisons, the string value is converted to a number and the operands are compared numerically (see Section 12.2, "Type Conversion in Expression Evaluation"), preventing use of the index. If safe-updates mode is enabled, an error occurs.  </dd></dl>
  As of MySQL 8.0.13, safe-updates mode also includes these behaviors: <dl>
<dd>  &bull; EXPLAIN with UPDATE and DELETE statements does not produce safe-updates errors. This enables use of EXPLAIN plus SHOW WARNINGS to see why an index is not used, which can be helpful in cases such as when a range_optimizer_max_mem_size violation or type conversion occurs and the optimizer does not use an index even though a key column was specified in the WHERE clause.  </dd></dl>
 <dl>
<dd>  &bull; When a safe-updates error occurs, the error message includes the first diagnostic that was produced, to provide information about the reason for failure. For example, the message may indicate that the range_optimizer_max_mem_size value was exceeded or type conversion occurred, either of which can preclude use of an index.  </dd></dl>
 <dl>
<dd>  &bull; For multiple-table deletes and updates, an error is produced with safe updates enabled only if any target table uses a table scan.  </dd></dl>
 Disabling mysql Auto-Reconnect  If the <code>mysql</code> client loses its connection to the server while sending a statement, it immediately and automatically tries to reconnect once to the server and send the statement again. However, even if <code>mysql</code> succeeds in reconnecting, your first connection has ended and all your previous session objects and settings are lost: temporary tables, the autocommit mode, and user-defined and session variables. Also, any current transaction rolls back. This behavior may be dangerous for you, as in the following example where the server was shut down and restarted between the first and second statements without you knowing it: <dl>
<dd>  <pre><code>mysql&gt; SET @a=1; Query OK, 0 rows affected (0.05 sec)
mysql&gt; INSERT INTO t VALUES(@a); ERROR 2006: MySQL server has gone away
No connection. Trying to reconnect...
Connection id: 1
Current database: test
Query OK, 1 row affected (1.30 sec)
mysql&gt; SELECT * FROM t; +------+
| a |
+------+
| NULL |
+------+
1 row in set (0.05 sec)
</code></pre>
  </dd></dl>
  The @a user variable has been lost with the connection, and after the reconnection it is undefined. If it is important to have <code>mysql</code> terminate with an error if the connection has been lost, you can start the <code>mysql</code> client with the <code>--skip-reconnect</code> option.  For more information about auto-reconnect and its effect on state information when a reconnection occurs, see Section 28.7.27, "C API Automatic Reconnection Control". mysql Client Parser Versus Server Parser  The <code>mysql</code> client uses a parser on the client side that is not a duplicate of the complete parser used by the <code>mysqld</code> server on the server side. This can lead to differences in treatment of certain constructs. Examples: <dl>
<dd>  &bull; The server parser treats strings delimited by &quot; characters as identifiers rather than as plain strings if the ANSI_QUOTES SQL mode is enabled.  The <code>mysql</code> client parser does not take the ANSI_QUOTES SQL mode into account. It treats strings delimited by &quot;, &#8216;, and ` characters the same, regardless of whether ANSI_QUOTES is enabled.  </dd></dl>
 <dl>
<dd>  &bull; Within /*! ... */ and /*+ ... */ comments, the <code>mysql</code> client parser interprets short-form <code>mysql</code> commands. The server parser does not interpret them because these commands have no meaning on the server side.  If it is desirable for <code>mysql</code> not to interpret short-form commands within comments, a partial workaround is to use the <code>--binary-mode</code> option, which causes all <code>mysql</code> commands to be disabled except \C and \d in noninteractive mode (for input piped to <code>mysql</code> or loaded using the source command).  </dd></dl>
  <h2>COPYRIGHT</h2>
   Copyright &#169; 1997, 2020, Oracle and/or its affiliates. All rights reserved.  This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License.  This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.  You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> <h2>NOTES</h2>
 <dl>
 <dt> 1.</dt>
<dd>  MySQL Shell 8.0 (part of MySQL 8.0)  </dd>
<dl>
<dd>  <a rel="nofollow" href="https://dev.mysql.com/doc/mysql-shell/8.0/en/">https://dev.mysql.com/doc/mysql-shell/8.0/en/</a>  </dd></dl>
 </dl>
  <h2>SEE ALSO</h2>
 For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a>  <h2>AUTHOR</h2>
 Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>).  
</td>
<td> The server host 
</td>
</tr>
<tr VALIGN=top>
<td> <hr />
The current delimiter T} T{ m T}:T{ Minutes of the current time T} T{ T}:T{ A newline character T} T{ O T}:T{ The current month in three-letter format (Jan, Feb, ...) T} T{ The current month in numeric format T} T{ P T}:T{ am/pm T} T{  T}:T{ The current TCP/IP port or socket file T} T{ R T}:T{ The current time, in 24-hour military time (0-23) T} T{ T}:T{ The current time, standard 12-hour time (1-12) T} T{ S T}:T{ Semicolon T} T{ T}:T{ Seconds of the current time T} T{ T}:T{ A tab character T} T{ U T}:T{  Your full <i>user_name</i>@<i>host_name</i> account name T} T{ T}:T{ Your user name T} T{ The server version T} T{ The current day of the week in three-letter format (Mon, Tue, ...) T} T{ Y T}:T{ The current year, four digits T} T{ y T}:T{ The current year, two digits T} T{ _ T}:T{ A space T} T{ \ T}:T{ A space (a space follows the backslash) T} T{ &#8216; T}:T{ Single quote T} T{ T}:T{ Double quote T} T{ \ T}:T{ A literal &nbsp;backslash character T} T{ \fIx T}:T{  <p> <i>x</i>, for any "<i>x</i>" not listed above T} </p>
 You can set the prompt in several ways: <dl>
<dd>  &bull; <i>Use an environment variable.</i> You can set the MYSQL_PS1 environment variable to a prompt string. For example:  </dd>
<dl>
<dd>  <pre><code>shell&gt; export MYSQL_PS1=&quot;(\u@\h) [\d]&gt; &quot; 
</code></pre>
  </dd></dl>
 </dl>
 <dl>
<dd>  &bull; <i>Use a command-line option.</i> You can set the <code>--prompt</code> option on the command line to <code>mysql</code>. For example:  </dd>
<dl>
<dd>  <pre><code>shell&gt; mysql --prompt=&quot;(\u@\h) [\d]&gt; &quot; (user [at] host) [database]&gt;
</code></pre>
  </dd></dl>
 </dl>
 <dl>
<dd>  &bull; <i>Use an option file.</i> You can set the prompt option in the [mysql] group of any MySQL option file, such as /etc/my.cnf or the .my.cnf file in your home directory. For example:  </dd>
<dl>
<dd>  <pre><code>[mysql]
prompt=(\\u@\\h) [\\d]&gt;\\_
</code></pre>
  </dd></dl>
  In this example, note that the backslashes are doubled. If you set the prompt using the prompt option in an option file, it is advisable to double the backslashes when using the special prompt options. There is some overlap in the set of permissible prompt options and the set of special escape sequences that are recognized in option files. (The rules for escape sequences in option files are listed in Section 4.2.2.2, "Using Option Files".) The overlap may cause you problems if you use single backslashes. For example, \s is interpreted as a space rather than as the current seconds value. The following example shows how to define a prompt within an option file to include the current time in <i>hh:mm:ss</i>&gt; format: <dl>
<dd>  <pre><code>[mysql]
prompt=&quot;\\r:\\m:\\s&gt; &quot;
</code></pre>
  </dd></dl>
 </dl>
 <dl>
<dd>  &bull; <i>Set the prompt interactively.</i> You can change your prompt interactively by using the prompt (or \R) command. For example:  </dd>
<dl>
<dd>  <pre><code>mysql&gt; prompt (\u@\h) [\d]&gt;\_ PROMPT set to '(\u@\h) [\d]&gt;\_'
( user @ host ) [ database ]&gt;
( user @ host ) [ database ]&gt; prompt
Returning to default PROMPT of mysql&gt;
mysql&gt;
</code></pre>
  </dd></dl>
 </dl>
  <h2>MYSQL CLIENT LOGGING</h2>
  The <code>mysql</code> client can do these types of logging for statements executed interactively: <dl>
<dd>  &bull; On Unix, <code>mysql</code> writes the statements to a history file. By default, this file is named .mysql_history in your home directory. To specify a different file, set the value of the MYSQL_HISTFILE environment variable.  </dd></dl>
 <dl>
<dd>  &bull; On all platforms, if the <code>--syslog</code> option is given, <code>mysql</code> writes the statements to the system logging facility. On Unix, this is syslog; on Windows, it is the Windows Event Log. The destination where logged messages appear is system dependent. On Linux, the destination is often the /var/log/messages file.  </dd></dl>
  The following discussion describes characteristics that apply to all logging types and provides information specific to each logging type. <dl>
<dd>  &bull; How Logging Occurs  </dd></dl>
 <dl>
<dd>  &bull; Controlling the History File  </dd></dl>
 <dl>
<dd>  &bull; syslog Logging Characteristics  </dd></dl>
 How Logging Occurs  For each enabled logging destination, statement logging occurs as follows: <dl>
<dd>  &bull; Statements are logged only when executed interactively. Statements are noninteractive, for example, when read from a file or a pipe. It is also possible to suppress statement logging by using the <code>--batch</code> or <code>--execute</code> option.  </dd></dl>
 <dl>
<dd>  &bull; Statements are ignored and not logged if they match any pattern in the "ignore" list. This list is described later.  </dd></dl>
 <dl>
<dd>  &bull; <code>mysql</code> logs each nonignored, nonempty statement line individually.  </dd></dl>
 <dl>
<dd>  &bull; If a nonignored statement spans multiple lines (not including the terminating delimiter), <code>mysql</code> concatenates the lines to form the complete statement, maps newlines to spaces, and logs the result, plus a delimiter.  </dd></dl>
  Consequently, an input statement that spans multiple lines can be logged twice. Consider this input: <dl>
<dd>  <pre><code>mysql&gt; SELECT     -&gt; 'Today is'     -&gt; ,     -&gt; CURDATE()     -&gt; ; 
</code></pre>
  </dd></dl>
  In this case, <code>mysql</code> logs the "SELECT", "&#8216;Today is&#8217;", ",", "CURDATE()", and ";" lines as it reads them. It also logs the complete statement, after mapping SELECT\n&#8217;Today is&#8217;\n,\nCURDATE() to SELECT &#8216;Today is&#8217; , CURDATE(), plus a delimiter. Thus, these lines appear in logged output: <dl>
<dd>  <pre><code>SELECT
'Today is'
,
CURDATE()
;
SELECT 'Today is' , CURDATE();
</code></pre>
  </dd></dl>
  <p> <code>mysql</code> ignores for logging purposes statements that match any pattern in the "ignore" list. By default, the pattern list is &quot;*IDENTIFIED*:*PASSWORD*&quot;, to ignore statements that refer to passwords. Pattern matching is not case-sensitive. Within patterns, two characters are special: </p>
<dl>
<dd>  &bull; ? matches any single character.  </dd></dl>
 <dl>
<dd>  &bull; * matches any sequence of zero or more characters.  </dd></dl>
  To specify additional patterns, use the <code>--histignore</code> option or set the MYSQL_HISTIGNORE environment variable. (If both are specified, the option value takes precedence.) The value should be a list of one or more colon-separated patterns, which are appended to the default pattern list.  Patterns specified on the command line might need to be quoted or escaped to prevent your command interpreter from treating them specially. For example, to suppress logging for UPDATE and DELETE statements in addition to statements that refer to passwords, invoke <code>mysql</code> like this: <dl>
<dd>  <pre><code>shell&gt; mysql --histignore=&quot;*UPDATE*:*DELETE*&quot; 
</code></pre>
  </dd></dl>
  Controlling the History File  The .mysql_history file should be protected with a restrictive access mode because sensitive information might be written to it, such as the text of SQL statements that contain passwords. See Section 6.1.2.1, "End-User Guidelines for Password Security". Statements in the file are accessible from the <code>mysql</code> client when the up-arrow key is used to recall the history. See Disabling Interactive History.  If you do not want to maintain a history file, first remove .mysql_history if it exists. Then use either of the following techniques to prevent it from being created again: <dl>
<dd>  &bull; Set the MYSQL_HISTFILE environment variable to /dev/null. To cause this setting to take effect each time you log in, put it in one of your shell&#8217;s startup files.  </dd></dl>
 <dl>
<dd>  &bull; Create .mysql_history as a symbolic link to /dev/null; this need be done only once:  </dd>
<dl>
<dd>  <pre><code>shell&gt; ln -s /dev/null $HOME/.mysql_history 
</code></pre>
  </dd></dl>
 </dl>
 syslog Logging Characteristics  If the <code>--syslog</code> option is given, <code>mysql</code> writes interactive statements to the system logging facility. Message logging has the following characteristics.  Logging occurs at the "information" level. This corresponds to the LOG_INFO priority for syslog on Unix/Linux syslog capability and to EVENTLOG_INFORMATION_TYPE for the Windows Event Log. Consult your system documentation for configuration of your logging capability.  Message size is limited to 1024 bytes.  Messages consist of the identifier MysqlClient followed by these values: <dl>
<dd>  &bull; SYSTEM_USER  The operating system user name (login name) or -- if the user is unknown.  </dd></dl>
 <dl>
<dd>  &bull; MYSQL_USER  The MySQL user name (specified with the <code>--user</code> option) or -- if the user is unknown.  </dd></dl>
 <dl>
<dd>  &bull; CONNECTION_ID:  The client connection identifier. This is the same as the CONNECTION_ID() function value within the session.  </dd></dl>
 <dl>
<dd>  &bull; DB_SERVER  The server host or -- if the host is unknown.  </dd></dl>
 <dl>
<dd>  &bull; DB  The default database or -- if no database has been selected.  </dd></dl>
 <dl>
<dd>  &bull; QUERY  The text of the logged statement.  </dd></dl>
  Here is a sample of output generated on Linux by using <code>--syslog</code>. This output is formatted for readability; each logged message actually takes a single line. <dl>
<dd>  <pre><code>Mar 7 12:39:25 myhost MysqlClient[20824]:
  SYSTEM_USER:'oscar', MYSQL_USER:'my_oscar', CONNECTION_ID:23,
  DB_SERVER:'127.0.0.1', DB:'--', QUERY:'USE test;'
Mar 7 12:39:28 myhost MysqlClient[20824]:
  SYSTEM_USER:'oscar', MYSQL_USER:'my_oscar', CONNECTION_ID:23,
  DB_SERVER:'127.0.0.1', DB:'test', QUERY:'SHOW TABLES;'
</code></pre>
  </dd></dl>
  <h2>MYSQL CLIENT SERVER-SIDE HELP</h2>
 <dl>
<dd>  <pre><code>mysql&gt; help  search_string 
</code></pre>
  </dd></dl>
  If you provide an argument to the help command, <code>mysql</code> uses it as a search string to access server-side help from the contents of the MySQL Reference Manual. The proper operation of this command requires that the help tables in the mysql database be initialized with help topic information (see Section 5.1.14, "Server-Side Help Support").  If there is no match for the search string, the search fails: <dl>
<dd>  <pre><code>mysql&gt; help me Nothing found
Please try to run 'help contents' for a list of all accessible topics
</code></pre>
  </dd></dl>
  Use <code>help contents</code> to see a list of the help categories: <dl>
<dd>  <pre><code>mysql&gt; help contents You asked for help about help category: &quot;Contents&quot;
For more information, type 'help &lt;item&gt;', where &lt;item&gt; is one of the
following categories:
   Account Management
   Administration
   Data Definition
   Data Manipulation
   Data Types
   Functions
   Functions and Modifiers for Use with GROUP BY
   Geographic Features
   Language Structure
   Plugins
   Storage Engines
   Stored Routines
   Table Maintenance
   Transactions
   Triggers
</code></pre>
  </dd></dl>
  If the search string matches multiple items, <code>mysql</code> shows a list of matching topics: <dl>
<dd>  <pre><code>mysql&gt; help logs Many help items for your request exist.
To make a more specific request, please type 'help &lt;item&gt;',
where &lt;item&gt; is one of the following topics:
   SHOW
   SHOW BINARY LOGS
   SHOW ENGINE
   SHOW LOGS
</code></pre>
  </dd></dl>
  Use a topic as the search string to see the help entry for that topic: <dl>
<dd>  <pre><code>mysql&gt; help show binary logs Name: 'SHOW BINARY LOGS'
Description:
Syntax:
SHOW BINARY LOGS
SHOW MASTER LOGS
Lists the binary log files on the server. This statement is used as
part of the procedure described in [purge-binary-logs], that shows how
to determine which logs can be purged.
mysql&gt; SHOW BINARY LOGS;
+---------------+-----------+-----------+
| Log_name | File_size | Encrypted |
+---------------+-----------+-----------+
| binlog.000015 | 724935 | Yes |
| binlog.000016 | 733481 | Yes |
+---------------+-----------+-----------+
</code></pre>
  </dd></dl>
  The search string can contain the wildcard characters % and _. These have the same meaning as for pattern-matching operations performed with the LIKE operator. For example, HELP rep% returns a list of topics that begin with rep: <dl>
<dd>  <pre><code>mysql&gt; HELP rep% Many help items for your request exist.
To make a more specific request, please type 'help &lt;item&gt;',
where &lt;item&gt; is one of the following
topics:
   REPAIR TABLE
   REPEAT FUNCTION
   REPEAT LOOP
   REPLACE
   REPLACE FUNCTION
</code></pre>
  </dd></dl>
  <h2>EXECUTING SQL STATEMENTS FROM A TEXT FILE</h2>
  The <code>mysql</code> client typically is used interactively, like this: <dl>
<dd>  <pre><code>shell&gt; mysql  db_name 
</code></pre>
  </dd></dl>
  However, it is also possible to put your SQL statements in a file and then tell <code>mysql</code> to read its input from that file. To do so, create a text file <i>text_file</i> that contains the statements you wish to execute. Then invoke <code>mysql</code> as shown here: <dl>
<dd>  <pre><code>shell&gt; mysql  db_name   &lt;  text_file 
</code></pre>
  </dd></dl>
  If you place a USE <i>db_name</i> statement as the first statement in the file, it is unnecessary to specify the database name on the command line: <dl>
<dd>  <pre><code>shell&gt; mysql &lt; text_file 
</code></pre>
  </dd></dl>
  If you are already running <code>mysql</code>, you can execute an SQL script file using the source command or \. command: <dl>
<dd>  <pre><code>mysql&gt; source  file_name mysql&gt; \.  file_name 
</code></pre>
  </dd></dl>
  Sometimes you may want your script to display progress information to the user. For this you can insert statements like this: <dl>
<dd>  <pre><code>SELECT '&lt;info_to_display&gt;' AS ' ';
</code></pre>
  </dd></dl>
  The statement shown outputs &lt;info_to_display&gt;.  You can also invoke <code>mysql</code> with the <code>--verbose</code> option, which causes each statement to be displayed before the result that it produces.  <p> <code>mysql</code> ignores Unicode byte order mark (BOM) characters at the beginning of input files. Previously, it read them and sent them to the server, resulting in a syntax error. Presence of a BOM does not cause <code>mysql</code> to change its default character set. To do that, invoke <code>mysql</code> with an option such as <code>--default-character-set=utf8</code>. </p>
 For more information about batch mode, see Section 3.5, "Using mysql in Batch Mode".  <h2>MYSQL CLIENT TIPS</h2>
  This section provides information about techniques for more effective use of <code>mysql</code> and about <code>mysql</code> operational behavior. <dl>
<dd>  &bull; Input-Line Editing  </dd></dl>
 <dl>
<dd>  &bull; Disabling Interactive History  </dd></dl>
 <dl>
<dd>  &bull; Unicode Support on Windows  </dd></dl>
 <dl>
<dd>  &bull; Displaying Query Results Vertically  </dd></dl>
 <dl>
<dd>  &bull; Using Safe-Updates Mode (--safe-updates)  </dd></dl>
 <dl>
<dd>  &bull; Disabling mysql Auto-Reconnect  </dd></dl>
 <dl>
<dd>  &bull; mysql Client Parser Versus Server Parser  </dd></dl>
 Input-Line Editing  <p> <code>mysql</code> supports input-line editing, which enables you to modify the current input line in place or recall previous input lines. For example, the left-arrow and right-arrow keys move horizontally within the current input line, and the up-arrow and down-arrow keys move up and down through the set of previously entered lines. Backspace deletes the character before the cursor and typing new characters enters them at the cursor position. To enter the line, press Enter. </p>
 On Windows, the editing key sequences are the same as supported for command editing in console windows. On Unix, the key sequences depend on the input library used to build <code>mysql</code> (for example, the libedit or readline library).  Documentation for the libedit and readline libraries is available online. To change the set of key sequences permitted by a given input library, define key bindings in the library startup file. This is a file in your home directory: .editrc for libedit and .inputrc for readline.  For example, in libedit, Control+W deletes everything before the current cursor position and Control+U deletes the entire line. In readline, Control+W deletes the word before the cursor and Control+U deletes everything before the current cursor position. If <code>mysql</code> was built using libedit, a user who prefers the readline behavior for these two keys can put the following lines in the .editrc file (creating the file if necessary): <dl>
<dd>  <pre><code>bind &quot;^W&quot; ed-delete-prev-word
bind &quot;^U&quot; vi-kill-line-prev
</code></pre>
  </dd></dl>
  To see the current set of key bindings, temporarily put a line that says only bind at the end of .editrc. <code>mysql</code> will show the bindings when it starts. Disabling Interactive History  The up-arrow key enables you to recall input lines from current and previous sessions. In cases where a console is shared, this behavior may be unsuitable. <code>mysql</code> supports disabling the interactive history partially or fully, depending on the host platform.  On Windows, the history is stored in memory. Alt+F7 deletes all input lines stored in memory for the current history buffer. It also deletes the list of sequential numbers in front of the input lines displayed with F7 and recalled (by number) with F9. New input lines entered after you press Alt+F7 repopulate the current history buffer. Clearing the buffer does not prevent logging to the Windows Event Viewer, if the <code>--syslog</code> option was used to start <code>mysql</code>. Closing the console window also clears the current history buffer.  To disable interactive history on Unix, first delete the .mysql_history file, if it exists (previous entries are recalled otherwise). Then start <code>mysql</code> with the --histignore=&quot;*&quot; option to ignore all new input lines. To re-enable the recall (and logging) behavior, restart <code>mysql</code> without the option.  If you prevent the .mysql_history file from being created (see Controlling the History File) and use --histignore=&quot;*&quot; to start the <code>mysql</code> client, the interactive history recall facility is disabled fully. Alternatively, if you omit the <code>--histignore</code> option, you can recall the input lines entered during the current session. Unicode Support on Windows  Windows provides APIs based on UTF-16LE for reading from and writing to the console; the <code>mysql</code> client for Windows is able to use these APIs. The Windows installer creates an item in the MySQL menu named MySQL command line client - Unicode. This item invokes the <code>mysql</code> client with properties set to communicate through the console to the MySQL server using Unicode.  To take advantage of this support manually, run <code>mysql</code> within a console that uses a compatible Unicode font and set the default character set to a Unicode character set that is supported for communication with the server: <dl>
<dd>  1. Open a console window.  </dd></dl>
 <dl>
<dd>  2. Go to the console window properties, select the font tab, and choose Lucida Console or some other compatible Unicode font. This is necessary because console windows start by default using a DOS raster font that is inadequate for Unicode.  </dd></dl>
 <dl>
<dd>  3. Execute <code>mysql.exe</code> with the <code>--default-character-set=utf8</code> (or utf8mb4) option. This option is necessary because utf16le is one of the character sets that cannot be used as the client character set. See the section called "Impermissible Client Character Sets".  </dd></dl>
  With those changes, <code>mysql</code> will use the Windows APIs to communicate with the console using UTF-16LE, and communicate with the server using UTF-8. (The menu item mentioned previously sets the font and character set as just described.)  To avoid those steps each time you run <code>mysql</code>, you can create a shortcut that invokes <code>mysql.exe</code>. The shortcut should set the console font to Lucida Console or some other compatible Unicode font, and pass the <code>--default-character-set=utf8</code> (or utf8mb4) option to <code>mysql.exe</code>.  Alternatively, create a shortcut that only sets the console font, and set the character set in the [mysql] group of your my.ini file: <dl>
<dd>  <pre><code>[mysql]
default-character-set=utf8
</code></pre>
  </dd></dl>
  Displaying Query Results Vertically  Some query results are much more readable when displayed vertically, instead of in the usual horizontal table format. Queries can be displayed vertically by terminating the query with \G instead of a semicolon. For example, longer text values that include newlines often are much easier to read with vertical output: <dl>
<dd>  <pre><code>mysql&gt; SELECT * FROM mails WHERE LENGTH(txt) &lt; 300 LIMIT 300,1\G *************************** 1. row ***************************
  msg_nro: 3068
     date: 2000-03-01 23:29:50
time_zone: +0200
mail_from: Jones
    reply: jones [at] example.com
  mail_to: &quot;John Smith&quot; &lt;smith [at] example.com&gt;
      sbj: UTF-8
      txt: &gt;&gt;&gt;&gt;&gt; &quot;John&quot; == John Smith writes:
John&gt; Hi. I think this is a good idea. Is anyone familiar
John&gt; with UTF-8 or Unicode? Otherwise, I'll put this on my
John&gt; TODO list and see what happens.
Yes, please do that.
Regards,
Jones
     file: inbox-jani-1
     hash: 190402944
1 row in set (0.09 sec)
</code></pre>
  </dd></dl>
  Using Safe-Updates Mode (--safe-updates)  For beginners, a useful startup option is <code>--safe-updates</code> (or <code>--i-am-a-dummy</code>, which has the same effect). Safe-updates mode is helpful for cases when you might have issued an UPDATE or DELETE statement but forgotten the WHERE clause indicating which rows to modify. Normally, such statements update or delete all rows in the table. With <code>--safe-updates</code>, you can modify rows only by specifying the key values that identify them, or a LIMIT clause, or both. This helps prevent accidents. Safe-updates mode also restricts SELECT statements that produce (or are estimated to produce) very large result sets.  The <code>--safe-updates</code> option causes <code>mysql</code> to execute the following statement when it connects to the MySQL server, to set the session values of the sql_safe_updates, sql_select_limit, and max_join_size system variables: <dl>
<dd>  <pre><code>SET sql_safe_updates=1, sql_select_limit=1000, max_join_size=1000000;
</code></pre>
  </dd></dl>
  The SET statement affects statement processing as follows: <dl>
<dd>  &bull; Enabling sql_safe_updates causes UPDATE and DELETE statements to produce an error if they do not specify a key constraint in the WHERE clause, or provide a LIMIT clause, or both. For example:  </dd>
<dl>
<dd>  <pre><code>UPDATE tbl_name  SET not_key_column = val  WHERE key_column = val ;
UPDATE tbl_name  SET not_key_column = val  LIMIT 1;
</code></pre>
  </dd></dl>
 </dl>
 <dl>
<dd>  &bull; Setting sql_select_limit to 1,000 causes the server to limit all SELECT result sets to 1,000 rows unless the statement includes a LIMIT clause.  </dd></dl>
 <dl>
<dd>  &bull; Setting max_join_size to 1,000,000 causes multiple-table SELECT statements to produce an error if the server estimates it must examine more than 1,000,000 row combinations.  </dd></dl>
  To specify result set limits different from 1,000 and 1,000,000, you can override the defaults by using the <code>--select-limit</code> and <code>--max-join-size</code> options when you invoke <code>mysql</code>: <dl>
<dd>  <pre><code>mysql --safe-updates --select-limit=500 --max-join-size=10000
</code></pre>
  </dd></dl>
  It is possible for UPDATE and DELETE statements to produce an error in safe-updates mode even with a key specified in the WHERE clause, if the optimizer decides not to use the index on the key column: <dl>
<dd>  &bull; Range access on the index cannot be used if memory usage exceeds that permitted by the range_optimizer_max_mem_size system variable. The optimizer then falls back to a table scan. See the section called "Limiting Memory Use for Range Optimization".  </dd></dl>
 <dl>
<dd>  &bull; If key comparisons require type conversion, the index may not be used (see Section 8.3.1, "How MySQL Uses Indexes"). Suppose that an indexed string column c1 is compared to a numeric value using WHERE c1 = 2222. For such comparisons, the string value is converted to a number and the operands are compared numerically (see Section 12.2, "Type Conversion in Expression Evaluation"), preventing use of the index. If safe-updates mode is enabled, an error occurs.  </dd></dl>
  As of MySQL 8.0.13, safe-updates mode also includes these behaviors: <dl>
<dd>  &bull; EXPLAIN with UPDATE and DELETE statements does not produce safe-updates errors. This enables use of EXPLAIN plus SHOW WARNINGS to see why an index is not used, which can be helpful in cases such as when a range_optimizer_max_mem_size violation or type conversion occurs and the optimizer does not use an index even though a key column was specified in the WHERE clause.  </dd></dl>
 <dl>
<dd>  &bull; When a safe-updates error occurs, the error message includes the first diagnostic that was produced, to provide information about the reason for failure. For example, the message may indicate that the range_optimizer_max_mem_size value was exceeded or type conversion occurred, either of which can preclude use of an index.  </dd></dl>
 <dl>
<dd>  &bull; For multiple-table deletes and updates, an error is produced with safe updates enabled only if any target table uses a table scan.  </dd></dl>
 Disabling mysql Auto-Reconnect  If the <code>mysql</code> client loses its connection to the server while sending a statement, it immediately and automatically tries to reconnect once to the server and send the statement again. However, even if <code>mysql</code> succeeds in reconnecting, your first connection has ended and all your previous session objects and settings are lost: temporary tables, the autocommit mode, and user-defined and session variables. Also, any current transaction rolls back. This behavior may be dangerous for you, as in the following example where the server was shut down and restarted between the first and second statements without you knowing it: <dl>
<dd>  <pre><code>mysql&gt; SET @a=1; Query OK, 0 rows affected (0.05 sec)
mysql&gt; INSERT INTO t VALUES(@a); ERROR 2006: MySQL server has gone away
No connection. Trying to reconnect...
Connection id: 1
Current database: test
Query OK, 1 row affected (1.30 sec)
mysql&gt; SELECT * FROM t; +------+
| a |
+------+
| NULL |
+------+
1 row in set (0.05 sec)
</code></pre>
  </dd></dl>
  The @a user variable has been lost with the connection, and after the reconnection it is undefined. If it is important to have <code>mysql</code> terminate with an error if the connection has been lost, you can start the <code>mysql</code> client with the <code>--skip-reconnect</code> option.  For more information about auto-reconnect and its effect on state information when a reconnection occurs, see Section 28.7.27, "C API Automatic Reconnection Control". mysql Client Parser Versus Server Parser  The <code>mysql</code> client uses a parser on the client side that is not a duplicate of the complete parser used by the <code>mysqld</code> server on the server side. This can lead to differences in treatment of certain constructs. Examples: <dl>
<dd>  &bull; The server parser treats strings delimited by &quot; characters as identifiers rather than as plain strings if the ANSI_QUOTES SQL mode is enabled.  The <code>mysql</code> client parser does not take the ANSI_QUOTES SQL mode into account. It treats strings delimited by &quot;, &#8216;, and ` characters the same, regardless of whether ANSI_QUOTES is enabled.  </dd></dl>
 <dl>
<dd>  &bull; Within /*! ... */ and /*+ ... */ comments, the <code>mysql</code> client parser interprets short-form <code>mysql</code> commands. The server parser does not interpret them because these commands have no meaning on the server side.  If it is desirable for <code>mysql</code> not to interpret short-form commands within comments, a partial workaround is to use the <code>--binary-mode</code> option, which causes all <code>mysql</code> commands to be disabled except \C and \d in noninteractive mode (for input piped to <code>mysql</code> or loaded using the source command).  </dd></dl>
  <h2>COPYRIGHT</h2>
   Copyright &#169; 1997, 2020, Oracle and/or its affiliates. All rights reserved.  This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License.  This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.  You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> <h2>NOTES</h2>
 <dl>
 <dd>  4 MySQL Shell 8.0 (part of MySQL 8.0)  </dd>
<dl>
<dd>  <a rel="nofollow" href="https://dev.mysql.com/doc/mysql-shell/8.0/en/">https://dev.mysql.com/doc/mysql-shell/8.0/en/</a>  </dd></dl>
 </dl>
  <h2>SEE ALSO</h2>
 For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a>  <h2>AUTHOR</h2>
 Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>).  
</td>
<td> The current delimiter 
</td>
</tr>
<tr VALIGN=top>
<td> m </td>
<td> Minutes of the current time 
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td> A newline character 
</td>
</tr>
<tr VALIGN=top>
<td> O </td>
<td> The current month in three-letter format (Jan, Feb, ...) 
</td>
</tr>
<tr VALIGN=top>
<td> The current month in numeric format T} T{ P T}:T{ am/pm T} T{  T}:T{ The current TCP/IP port or socket file T} T{ R T}:T{ The current time, in 24-hour military time (0-23) T} T{ T}:T{ The current time, standard 12-hour time (1-12) T} T{ S T}:T{ Semicolon T} T{ T}:T{ Seconds of the current time T} T{ T}:T{ A tab character T} T{ U T}:T{  Your full <i>user_name</i>@<i>host_name</i> account name T} T{ T}:T{ Your user name T} T{ The server version T} T{ The current day of the week in three-letter format (Mon, Tue, ...) T} T{ Y T}:T{ The current year, four digits T} T{ y T}:T{ The current year, two digits T} T{ _ T}:T{ A space T} T{ \ T}:T{ A space (a space follows the backslash) T} T{ &#8216; T}:T{ Single quote T} T{ T}:T{ Double quote T} T{ \ T}:T{ A literal &nbsp;backslash character T} T{ \fIx T}:T{  <p> <i>x</i>, for any "<i>x</i>" not listed above T} </p>
 You can set the prompt in several ways: <dl>
<dd>  &bull; <i>Use an environment variable.</i> You can set the MYSQL_PS1 environment variable to a prompt string. For example:  </dd>
<dl>
<dd>  <pre><code>shell&gt; export MYSQL_PS1=&quot;(\u@\h) [\d]&gt; &quot; 
</code></pre>
  </dd></dl>
 </dl>
 <dl>
<dd>  &bull; <i>Use a command-line option.</i> You can set the <code>--prompt</code> option on the command line to <code>mysql</code>. For example:  </dd>
<dl>
<dd>  <pre><code>shell&gt; mysql --prompt=&quot;(\u@\h) [\d]&gt; &quot; (user [at] host) [database]&gt;
</code></pre>
  </dd></dl>
 </dl>
 <dl>
<dd>  &bull; <i>Use an option file.</i> You can set the prompt option in the [mysql] group of any MySQL option file, such as /etc/my.cnf or the .my.cnf file in your home directory. For example:  </dd>
<dl>
<dd>  <pre><code>[mysql]
prompt=(\\u@\\h) [\\d]&gt;\\_
</code></pre>
  </dd></dl>
  In this example, note that the backslashes are doubled. If you set the prompt using the prompt option in an option file, it is advisable to double the backslashes when using the special prompt options. There is some overlap in the set of permissible prompt options and the set of special escape sequences that are recognized in option files. (The rules for escape sequences in option files are listed in Section 4.2.2.2, "Using Option Files".) The overlap may cause you problems if you use single backslashes. For example, \s is interpreted as a space rather than as the current seconds value. The following example shows how to define a prompt within an option file to include the current time in <i>hh:mm:ss</i>&gt; format: <dl>
<dd>  <pre><code>[mysql]
prompt=&quot;\\r:\\m:\\s&gt; &quot;
</code></pre>
  </dd></dl>
 </dl>
 <dl>
<dd>  &bull; <i>Set the prompt interactively.</i> You can change your prompt interactively by using the prompt (or \R) command. For example:  </dd>
<dl>
<dd>  <pre><code>mysql&gt; prompt (\u@\h) [\d]&gt;\_ PROMPT set to '(\u@\h) [\d]&gt;\_'
( user @ host ) [ database ]&gt;
( user @ host ) [ database ]&gt; prompt
Returning to default PROMPT of mysql&gt;
mysql&gt;
</code></pre>
  </dd></dl>
 </dl>
  <h2>MYSQL CLIENT LOGGING</h2>
  The <code>mysql</code> client can do these types of logging for statements executed interactively: <dl>
<dd>  &bull; On Unix, <code>mysql</code> writes the statements to a history file. By default, this file is named .mysql_history in your home directory. To specify a different file, set the value of the MYSQL_HISTFILE environment variable.  </dd></dl>
 <dl>
<dd>  &bull; On all platforms, if the <code>--syslog</code> option is given, <code>mysql</code> writes the statements to the system logging facility. On Unix, this is syslog; on Windows, it is the Windows Event Log. The destination where logged messages appear is system dependent. On Linux, the destination is often the /var/log/messages file.  </dd></dl>
  The following discussion describes characteristics that apply to all logging types and provides information specific to each logging type. <dl>
<dd>  &bull; How Logging Occurs  </dd></dl>
 <dl>
<dd>  &bull; Controlling the History File  </dd></dl>
 <dl>
<dd>  &bull; syslog Logging Characteristics  </dd></dl>
 How Logging Occurs  For each enabled logging destination, statement logging occurs as follows: <dl>
<dd>  &bull; Statements are logged only when executed interactively. Statements are noninteractive, for example, when read from a file or a pipe. It is also possible to suppress statement logging by using the <code>--batch</code> or <code>--execute</code> option.  </dd></dl>
 <dl>
<dd>  &bull; Statements are ignored and not logged if they match any pattern in the "ignore" list. This list is described later.  </dd></dl>
 <dl>
<dd>  &bull; <code>mysql</code> logs each nonignored, nonempty statement line individually.  </dd></dl>
 <dl>
<dd>  &bull; If a nonignored statement spans multiple lines (not including the terminating delimiter), <code>mysql</code> concatenates the lines to form the complete statement, maps newlines to spaces, and logs the result, plus a delimiter.  </dd></dl>
  Consequently, an input statement that spans multiple lines can be logged twice. Consider this input: <dl>
<dd>  <pre><code>mysql&gt; SELECT     -&gt; 'Today is'     -&gt; ,     -&gt; CURDATE()     -&gt; ; 
</code></pre>
  </dd></dl>
  In this case, <code>mysql</code> logs the "SELECT", "&#8216;Today is&#8217;", ",", "CURDATE()", and ";" lines as it reads them. It also logs the complete statement, after mapping SELECT\n&#8217;Today is&#8217;\n,\nCURDATE() to SELECT &#8216;Today is&#8217; , CURDATE(), plus a delimiter. Thus, these lines appear in logged output: <dl>
<dd>  <pre><code>SELECT
'Today is'
,
CURDATE()
;
SELECT 'Today is' , CURDATE();
</code></pre>
  </dd></dl>
  <p> <code>mysql</code> ignores for logging purposes statements that match any pattern in the "ignore" list. By default, the pattern list is &quot;*IDENTIFIED*:*PASSWORD*&quot;, to ignore statements that refer to passwords. Pattern matching is not case-sensitive. Within patterns, two characters are special: </p>
<dl>
<dd>  &bull; ? matches any single character.  </dd></dl>
 <dl>
<dd>  &bull; * matches any sequence of zero or more characters.  </dd></dl>
  To specify additional patterns, use the <code>--histignore</code> option or set the MYSQL_HISTIGNORE environment variable. (If both are specified, the option value takes precedence.) The value should be a list of one or more colon-separated patterns, which are appended to the default pattern list.  Patterns specified on the command line might need to be quoted or escaped to prevent your command interpreter from treating them specially. For example, to suppress logging for UPDATE and DELETE statements in addition to statements that refer to passwords, invoke <code>mysql</code> like this: <dl>
<dd>  <pre><code>shell&gt; mysql --histignore=&quot;*UPDATE*:*DELETE*&quot; 
</code></pre>
  </dd></dl>
  Controlling the History File  The .mysql_history file should be protected with a restrictive access mode because sensitive information might be written to it, such as the text of SQL statements that contain passwords. See Section 6.1.2.1, "End-User Guidelines for Password Security". Statements in the file are accessible from the <code>mysql</code> client when the up-arrow key is used to recall the history. See Disabling Interactive History.  If you do not want to maintain a history file, first remove .mysql_history if it exists. Then use either of the following techniques to prevent it from being created again: <dl>
<dd>  &bull; Set the MYSQL_HISTFILE environment variable to /dev/null. To cause this setting to take effect each time you log in, put it in one of your shell&#8217;s startup files.  </dd></dl>
 <dl>
<dd>  &bull; Create .mysql_history as a symbolic link to /dev/null; this need be done only once:  </dd>
<dl>
<dd>  <pre><code>shell&gt; ln -s /dev/null $HOME/.mysql_history 
</code></pre>
  </dd></dl>
 </dl>
 syslog Logging Characteristics  If the <code>--syslog</code> option is given, <code>mysql</code> writes interactive statements to the system logging facility. Message logging has the following characteristics.  Logging occurs at the "information" level. This corresponds to the LOG_INFO priority for syslog on Unix/Linux syslog capability and to EVENTLOG_INFORMATION_TYPE for the Windows Event Log. Consult your system documentation for configuration of your logging capability.  Message size is limited to 1024 bytes.  Messages consist of the identifier MysqlClient followed by these values: <dl>
<dd>  &bull; SYSTEM_USER  The operating system user name (login name) or -- if the user is unknown.  </dd></dl>
 <dl>
<dd>  &bull; MYSQL_USER  The MySQL user name (specified with the <code>--user</code> option) or -- if the user is unknown.  </dd></dl>
 <dl>
<dd>  &bull; CONNECTION_ID:  The client connection identifier. This is the same as the CONNECTION_ID() function value within the session.  </dd></dl>
 <dl>
<dd>  &bull; DB_SERVER  The server host or -- if the host is unknown.  </dd></dl>
 <dl>
<dd>  &bull; DB  The default database or -- if no database has been selected.  </dd></dl>
 <dl>
<dd>  &bull; QUERY  The text of the logged statement.  </dd></dl>
  Here is a sample of output generated on Linux by using <code>--syslog</code>. This output is formatted for readability; each logged message actually takes a single line. <dl>
<dd>  <pre><code>Mar 7 12:39:25 myhost MysqlClient[20824]:
  SYSTEM_USER:'oscar', MYSQL_USER:'my_oscar', CONNECTION_ID:23,
  DB_SERVER:'127.0.0.1', DB:'--', QUERY:'USE test;'
Mar 7 12:39:28 myhost MysqlClient[20824]:
  SYSTEM_USER:'oscar', MYSQL_USER:'my_oscar', CONNECTION_ID:23,
  DB_SERVER:'127.0.0.1', DB:'test', QUERY:'SHOW TABLES;'
</code></pre>
  </dd></dl>
  <h2>MYSQL CLIENT SERVER-SIDE HELP</h2>
 <dl>
<dd>  <pre><code>mysql&gt; help  search_string 
</code></pre>
  </dd></dl>
  If you provide an argument to the help command, <code>mysql</code> uses it as a search string to access server-side help from the contents of the MySQL Reference Manual. The proper operation of this command requires that the help tables in the mysql database be initialized with help topic information (see Section 5.1.14, "Server-Side Help Support").  If there is no match for the search string, the search fails: <dl>
<dd>  <pre><code>mysql&gt; help me Nothing found
Please try to run 'help contents' for a list of all accessible topics
</code></pre>
  </dd></dl>
  Use <code>help contents</code> to see a list of the help categories: <dl>
<dd>  <pre><code>mysql&gt; help contents You asked for help about help category: &quot;Contents&quot;
For more information, type 'help &lt;item&gt;', where &lt;item&gt; is one of the
following categories:
   Account Management
   Administration
   Data Definition
   Data Manipulation
   Data Types
   Functions
   Functions and Modifiers for Use with GROUP BY
   Geographic Features
   Language Structure
   Plugins
   Storage Engines
   Stored Routines
   Table Maintenance
   Transactions
   Triggers
</code></pre>
  </dd></dl>
  If the search string matches multiple items, <code>mysql</code> shows a list of matching topics: <dl>
<dd>  <pre><code>mysql&gt; help logs Many help items for your request exist.
To make a more specific request, please type 'help &lt;item&gt;',
where &lt;item&gt; is one of the following topics:
   SHOW
   SHOW BINARY LOGS
   SHOW ENGINE
   SHOW LOGS
</code></pre>
  </dd></dl>
  Use a topic as the search string to see the help entry for that topic: <dl>
<dd>  <pre><code>mysql&gt; help show binary logs Name: 'SHOW BINARY LOGS'
Description:
Syntax:
SHOW BINARY LOGS
SHOW MASTER LOGS
Lists the binary log files on the server. This statement is used as
part of the procedure described in [purge-binary-logs], that shows how
to determine which logs can be purged.
mysql&gt; SHOW BINARY LOGS;
+---------------+-----------+-----------+
| Log_name | File_size | Encrypted |
+---------------+-----------+-----------+
| binlog.000015 | 724935 | Yes |
| binlog.000016 | 733481 | Yes |
+---------------+-----------+-----------+
</code></pre>
  </dd></dl>
  The search string can contain the wildcard characters % and _. These have the same meaning as for pattern-matching operations performed with the LIKE operator. For example, HELP rep% returns a list of topics that begin with rep: <dl>
<dd>  <pre><code>mysql&gt; HELP rep% Many help items for your request exist.
To make a more specific request, please type 'help &lt;item&gt;',
where &lt;item&gt; is one of the following
topics:
   REPAIR TABLE
   REPEAT FUNCTION
   REPEAT LOOP
   REPLACE
   REPLACE FUNCTION
</code></pre>
  </dd></dl>
  <h2>EXECUTING SQL STATEMENTS FROM A TEXT FILE</h2>
  The <code>mysql</code> client typically is used interactively, like this: <dl>
<dd>  <pre><code>shell&gt; mysql  db_name 
</code></pre>
  </dd></dl>
  However, it is also possible to put your SQL statements in a file and then tell <code>mysql</code> to read its input from that file. To do so, create a text file <i>text_file</i> that contains the statements you wish to execute. Then invoke <code>mysql</code> as shown here: <dl>
<dd>  <pre><code>shell&gt; mysql  db_name   &lt;  text_file 
</code></pre>
  </dd></dl>
  If you place a USE <i>db_name</i> statement as the first statement in the file, it is unnecessary to specify the database name on the command line: <dl>
<dd>  <pre><code>shell&gt; mysql &lt; text_file 
</code></pre>
  </dd></dl>
  If you are already running <code>mysql</code>, you can execute an SQL script file using the source command or \. command: <dl>
<dd>  <pre><code>mysql&gt; source  file_name mysql&gt; \.  file_name 
</code></pre>
  </dd></dl>
  Sometimes you may want your script to display progress information to the user. For this you can insert statements like this: <dl>
<dd>  <pre><code>SELECT '&lt;info_to_display&gt;' AS ' ';
</code></pre>
  </dd></dl>
  The statement shown outputs &lt;info_to_display&gt;.  You can also invoke <code>mysql</code> with the <code>--verbose</code> option, which causes each statement to be displayed before the result that it produces.  <p> <code>mysql</code> ignores Unicode byte order mark (BOM) characters at the beginning of input files. Previously, it read them and sent them to the server, resulting in a syntax error. Presence of a BOM does not cause <code>mysql</code> to change its default character set. To do that, invoke <code>mysql</code> with an option such as <code>--default-character-set=utf8</code>. </p>
 For more information about batch mode, see Section 3.5, "Using mysql in Batch Mode".  <h2>MYSQL CLIENT TIPS</h2>
  This section provides information about techniques for more effective use of <code>mysql</code> and about <code>mysql</code> operational behavior. <dl>
<dd>  &bull; Input-Line Editing  </dd></dl>
 <dl>
<dd>  &bull; Disabling Interactive History  </dd></dl>
 <dl>
<dd>  &bull; Unicode Support on Windows  </dd></dl>
 <dl>
<dd>  &bull; Displaying Query Results Vertically  </dd></dl>
 <dl>
<dd>  &bull; Using Safe-Updates Mode (--safe-updates)  </dd></dl>
 <dl>
<dd>  &bull; Disabling mysql Auto-Reconnect  </dd></dl>
 <dl>
<dd>  &bull; mysql Client Parser Versus Server Parser  </dd></dl>
 Input-Line Editing  <p> <code>mysql</code> supports input-line editing, which enables you to modify the current input line in place or recall previous input lines. For example, the left-arrow and right-arrow keys move horizontally within the current input line, and the up-arrow and down-arrow keys move up and down through the set of previously entered lines. Backspace deletes the character before the cursor and typing new characters enters them at the cursor position. To enter the line, press Enter. </p>
 On Windows, the editing key sequences are the same as supported for command editing in console windows. On Unix, the key sequences depend on the input library used to build <code>mysql</code> (for example, the libedit or readline library).  Documentation for the libedit and readline libraries is available online. To change the set of key sequences permitted by a given input library, define key bindings in the library startup file. This is a file in your home directory: .editrc for libedit and .inputrc for readline.  For example, in libedit, Control+W deletes everything before the current cursor position and Control+U deletes the entire line. In readline, Control+W deletes the word before the cursor and Control+U deletes everything before the current cursor position. If <code>mysql</code> was built using libedit, a user who prefers the readline behavior for these two keys can put the following lines in the .editrc file (creating the file if necessary): <dl>
<dd>  <pre><code>bind &quot;^W&quot; ed-delete-prev-word
bind &quot;^U&quot; vi-kill-line-prev
</code></pre>
  </dd></dl>
  To see the current set of key bindings, temporarily put a line that says only bind at the end of .editrc. <code>mysql</code> will show the bindings when it starts. Disabling Interactive History  The up-arrow key enables you to recall input lines from current and previous sessions. In cases where a console is shared, this behavior may be unsuitable. <code>mysql</code> supports disabling the interactive history partially or fully, depending on the host platform.  On Windows, the history is stored in memory. Alt+F7 deletes all input lines stored in memory for the current history buffer. It also deletes the list of sequential numbers in front of the input lines displayed with F7 and recalled (by number) with F9. New input lines entered after you press Alt+F7 repopulate the current history buffer. Clearing the buffer does not prevent logging to the Windows Event Viewer, if the <code>--syslog</code> option was used to start <code>mysql</code>. Closing the console window also clears the current history buffer.  To disable interactive history on Unix, first delete the .mysql_history file, if it exists (previous entries are recalled otherwise). Then start <code>mysql</code> with the --histignore=&quot;*&quot; option to ignore all new input lines. To re-enable the recall (and logging) behavior, restart <code>mysql</code> without the option.  If you prevent the .mysql_history file from being created (see Controlling the History File) and use --histignore=&quot;*&quot; to start the <code>mysql</code> client, the interactive history recall facility is disabled fully. Alternatively, if you omit the <code>--histignore</code> option, you can recall the input lines entered during the current session. Unicode Support on Windows  Windows provides APIs based on UTF-16LE for reading from and writing to the console; the <code>mysql</code> client for Windows is able to use these APIs. The Windows installer creates an item in the MySQL menu named MySQL command line client - Unicode. This item invokes the <code>mysql</code> client with properties set to communicate through the console to the MySQL server using Unicode.  To take advantage of this support manually, run <code>mysql</code> within a console that uses a compatible Unicode font and set the default character set to a Unicode character set that is supported for communication with the server: <dl>
<dd>  1. Open a console window.  </dd></dl>
 <dl>
<dd>  2. Go to the console window properties, select the font tab, and choose Lucida Console or some other compatible Unicode font. This is necessary because console windows start by default using a DOS raster font that is inadequate for Unicode.  </dd></dl>
 <dl>
<dd>  3. Execute <code>mysql.exe</code> with the <code>--default-character-set=utf8</code> (or utf8mb4) option. This option is necessary because utf16le is one of the character sets that cannot be used as the client character set. See the section called "Impermissible Client Character Sets".  </dd></dl>
  With those changes, <code>mysql</code> will use the Windows APIs to communicate with the console using UTF-16LE, and communicate with the server using UTF-8. (The menu item mentioned previously sets the font and character set as just described.)  To avoid those steps each time you run <code>mysql</code>, you can create a shortcut that invokes <code>mysql.exe</code>. The shortcut should set the console font to Lucida Console or some other compatible Unicode font, and pass the <code>--default-character-set=utf8</code> (or utf8mb4) option to <code>mysql.exe</code>.  Alternatively, create a shortcut that only sets the console font, and set the character set in the [mysql] group of your my.ini file: <dl>
<dd>  <pre><code>[mysql]
default-character-set=utf8
</code></pre>
  </dd></dl>
  Displaying Query Results Vertically  Some query results are much more readable when displayed vertically, instead of in the usual horizontal table format. Queries can be displayed vertically by terminating the query with \G instead of a semicolon. For example, longer text values that include newlines often are much easier to read with vertical output: <dl>
<dd>  <pre><code>mysql&gt; SELECT * FROM mails WHERE LENGTH(txt) &lt; 300 LIMIT 300,1\G *************************** 1. row ***************************
  msg_nro: 3068
     date: 2000-03-01 23:29:50
time_zone: +0200
mail_from: Jones
    reply: jones [at] example.com
  mail_to: &quot;John Smith&quot; &lt;smith [at] example.com&gt;
      sbj: UTF-8
      txt: &gt;&gt;&gt;&gt;&gt; &quot;John&quot; == John Smith writes:
John&gt; Hi. I think this is a good idea. Is anyone familiar
John&gt; with UTF-8 or Unicode? Otherwise, I'll put this on my
John&gt; TODO list and see what happens.
Yes, please do that.
Regards,
Jones
     file: inbox-jani-1
     hash: 190402944
1 row in set (0.09 sec)
</code></pre>
  </dd></dl>
  Using Safe-Updates Mode (--safe-updates)  For beginners, a useful startup option is <code>--safe-updates</code> (or <code>--i-am-a-dummy</code>, which has the same effect). Safe-updates mode is helpful for cases when you might have issued an UPDATE or DELETE statement but forgotten the WHERE clause indicating which rows to modify. Normally, such statements update or delete all rows in the table. With <code>--safe-updates</code>, you can modify rows only by specifying the key values that identify them, or a LIMIT clause, or both. This helps prevent accidents. Safe-updates mode also restricts SELECT statements that produce (or are estimated to produce) very large result sets.  The <code>--safe-updates</code> option causes <code>mysql</code> to execute the following statement when it connects to the MySQL server, to set the session values of the sql_safe_updates, sql_select_limit, and max_join_size system variables: <dl>
<dd>  <pre><code>SET sql_safe_updates=1, sql_select_limit=1000, max_join_size=1000000;
</code></pre>
  </dd></dl>
  The SET statement affects statement processing as follows: <dl>
<dd>  &bull; Enabling sql_safe_updates causes UPDATE and DELETE statements to produce an error if they do not specify a key constraint in the WHERE clause, or provide a LIMIT clause, or both. For example:  </dd>
<dl>
<dd>  <pre><code>UPDATE tbl_name  SET not_key_column = val  WHERE key_column = val ;
UPDATE tbl_name  SET not_key_column = val  LIMIT 1;
</code></pre>
  </dd></dl>
 </dl>
 <dl>
<dd>  &bull; Setting sql_select_limit to 1,000 causes the server to limit all SELECT result sets to 1,000 rows unless the statement includes a LIMIT clause.  </dd></dl>
 <dl>
<dd>  &bull; Setting max_join_size to 1,000,000 causes multiple-table SELECT statements to produce an error if the server estimates it must examine more than 1,000,000 row combinations.  </dd></dl>
  To specify result set limits different from 1,000 and 1,000,000, you can override the defaults by using the <code>--select-limit</code> and <code>--max-join-size</code> options when you invoke <code>mysql</code>: <dl>
<dd>  <pre><code>mysql --safe-updates --select-limit=500 --max-join-size=10000
</code></pre>
  </dd></dl>
  It is possible for UPDATE and DELETE statements to produce an error in safe-updates mode even with a key specified in the WHERE clause, if the optimizer decides not to use the index on the key column: <dl>
<dd>  &bull; Range access on the index cannot be used if memory usage exceeds that permitted by the range_optimizer_max_mem_size system variable. The optimizer then falls back to a table scan. See the section called "Limiting Memory Use for Range Optimization".  </dd></dl>
 <dl>
<dd>  &bull; If key comparisons require type conversion, the index may not be used (see Section 8.3.1, "How MySQL Uses Indexes"). Suppose that an indexed string column c1 is compared to a numeric value using WHERE c1 = 2222. For such comparisons, the string value is converted to a number and the operands are compared numerically (see Section 12.2, "Type Conversion in Expression Evaluation"), preventing use of the index. If safe-updates mode is enabled, an error occurs.  </dd></dl>
  As of MySQL 8.0.13, safe-updates mode also includes these behaviors: <dl>
<dd>  &bull; EXPLAIN with UPDATE and DELETE statements does not produce safe-updates errors. This enables use of EXPLAIN plus SHOW WARNINGS to see why an index is not used, which can be helpful in cases such as when a range_optimizer_max_mem_size violation or type conversion occurs and the optimizer does not use an index even though a key column was specified in the WHERE clause.  </dd></dl>
 <dl>
<dd>  &bull; When a safe-updates error occurs, the error message includes the first diagnostic that was produced, to provide information about the reason for failure. For example, the message may indicate that the range_optimizer_max_mem_size value was exceeded or type conversion occurred, either of which can preclude use of an index.  </dd></dl>
 <dl>
<dd>  &bull; For multiple-table deletes and updates, an error is produced with safe updates enabled only if any target table uses a table scan.  </dd></dl>
 Disabling mysql Auto-Reconnect  If the <code>mysql</code> client loses its connection to the server while sending a statement, it immediately and automatically tries to reconnect once to the server and send the statement again. However, even if <code>mysql</code> succeeds in reconnecting, your first connection has ended and all your previous session objects and settings are lost: temporary tables, the autocommit mode, and user-defined and session variables. Also, any current transaction rolls back. This behavior may be dangerous for you, as in the following example where the server was shut down and restarted between the first and second statements without you knowing it: <dl>
<dd>  <pre><code>mysql&gt; SET @a=1; Query OK, 0 rows affected (0.05 sec)
mysql&gt; INSERT INTO t VALUES(@a); ERROR 2006: MySQL server has gone away
No connection. Trying to reconnect...
Connection id: 1
Current database: test
Query OK, 1 row affected (1.30 sec)
mysql&gt; SELECT * FROM t; +------+
| a |
+------+
| NULL |
+------+
1 row in set (0.05 sec)
</code></pre>
  </dd></dl>
  The @a user variable has been lost with the connection, and after the reconnection it is undefined. If it is important to have <code>mysql</code> terminate with an error if the connection has been lost, you can start the <code>mysql</code> client with the <code>--skip-reconnect</code> option.  For more information about auto-reconnect and its effect on state information when a reconnection occurs, see Section 28.7.27, "C API Automatic Reconnection Control". mysql Client Parser Versus Server Parser  The <code>mysql</code> client uses a parser on the client side that is not a duplicate of the complete parser used by the <code>mysqld</code> server on the server side. This can lead to differences in treatment of certain constructs. Examples: <dl>
<dd>  &bull; The server parser treats strings delimited by &quot; characters as identifiers rather than as plain strings if the ANSI_QUOTES SQL mode is enabled.  The <code>mysql</code> client parser does not take the ANSI_QUOTES SQL mode into account. It treats strings delimited by &quot;, &#8216;, and ` characters the same, regardless of whether ANSI_QUOTES is enabled.  </dd></dl>
 <dl>
<dd>  &bull; Within /*! ... */ and /*+ ... */ comments, the <code>mysql</code> client parser interprets short-form <code>mysql</code> commands. The server parser does not interpret them because these commands have no meaning on the server side.  If it is desirable for <code>mysql</code> not to interpret short-form commands within comments, a partial workaround is to use the <code>--binary-mode</code> option, which causes all <code>mysql</code> commands to be disabled except \C and \d in noninteractive mode (for input piped to <code>mysql</code> or loaded using the source command).  </dd></dl>
  <h2>COPYRIGHT</h2>
   Copyright &#169; 1997, 2020, Oracle and/or its affiliates. All rights reserved.  This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License.  This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.  You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> <h2>NOTES</h2>
 <dl>
 <dd>  1. 4 MySQL Shell 8.0 (part of MySQL 8.0)  </dd>
<dl>
<dd>  <a rel="nofollow" href="https://dev.mysql.com/doc/mysql-shell/8.0/en/">https://dev.mysql.com/doc/mysql-shell/8.0/en/</a>  </dd></dl>
 </dl>
  <h2>SEE ALSO</h2>
 For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a>  <h2>AUTHOR</h2>
 Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>).  
</td>
<td> The current month in numeric format 
</td>
</tr>
<tr VALIGN=top>
<td> P </td>
<td> am/pm 
</td>
</tr>
<tr VALIGN=top>
<td>  
</td>
<td> The current TCP/IP port or socket file 
</td>
</tr>
<tr VALIGN=top>
<td> R </td>
<td> The current time, in 24-hour military time (0-23) 
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td> The current time, standard 12-hour time (1-12) 
</td>
</tr>
<tr VALIGN=top>
<td> S </td>
<td> Semicolon 
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td> Seconds of the current time 
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td> A tab character 
</td>
</tr>
<tr VALIGN=top>
<td> U </td>
<td>  Your full <i>user_name</i>@<i>host_name</i> account name 
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td> Your user name 
</td>
</tr>
<tr VALIGN=top>
<td> The server version T} T{ The current day of the week in three-letter format (Mon, Tue, ...) T} T{ Y T}:T{ The current year, four digits T} T{ y T}:T{ The current year, two digits T} T{ _ T}:T{ A space T} T{ \ T}:T{ A space (a space follows the backslash) T} T{ &#8216; T}:T{ Single quote T} T{ T}:T{ Double quote T} T{ \ T}:T{ A literal &nbsp;backslash character T} T{ \fIx T}:T{  <p> <i>x</i>, for any "<i>x</i>" not listed above T} </p>
 You can set the prompt in several ways: <dl>
<dd>  &bull; <i>Use an environment variable.</i> You can set the MYSQL_PS1 environment variable to a prompt string. For example:  </dd>
<dl>
<dd>  <pre><code>shell&gt; export MYSQL_PS1=&quot;(\u@\h) [\d]&gt; &quot; 
</code></pre>
  </dd></dl>
 </dl>
 <dl>
<dd>  &bull; <i>Use a command-line option.</i> You can set the <code>--prompt</code> option on the command line to <code>mysql</code>. For example:  </dd>
<dl>
<dd>  <pre><code>shell&gt; mysql --prompt=&quot;(\u@\h) [\d]&gt; &quot; (user [at] host) [database]&gt;
</code></pre>
  </dd></dl>
 </dl>
 <dl>
<dd>  &bull; <i>Use an option file.</i> You can set the prompt option in the [mysql] group of any MySQL option file, such as /etc/my.cnf or the .my.cnf file in your home directory. For example:  </dd>
<dl>
<dd>  <pre><code>[mysql]
prompt=(\\u@\\h) [\\d]&gt;\\_
</code></pre>
  </dd></dl>
  In this example, note that the backslashes are doubled. If you set the prompt using the prompt option in an option file, it is advisable to double the backslashes when using the special prompt options. There is some overlap in the set of permissible prompt options and the set of special escape sequences that are recognized in option files. (The rules for escape sequences in option files are listed in Section 4.2.2.2, "Using Option Files".) The overlap may cause you problems if you use single backslashes. For example, \s is interpreted as a space rather than as the current seconds value. The following example shows how to define a prompt within an option file to include the current time in <i>hh:mm:ss</i>&gt; format: <dl>
<dd>  <pre><code>[mysql]
prompt=&quot;\\r:\\m:\\s&gt; &quot;
</code></pre>
  </dd></dl>
 </dl>
 <dl>
<dd>  &bull; <i>Set the prompt interactively.</i> You can change your prompt interactively by using the prompt (or \R) command. For example:  </dd>
<dl>
<dd>  <pre><code>mysql&gt; prompt (\u@\h) [\d]&gt;\_ PROMPT set to '(\u@\h) [\d]&gt;\_'
( user @ host ) [ database ]&gt;
( user @ host ) [ database ]&gt; prompt
Returning to default PROMPT of mysql&gt;
mysql&gt;
</code></pre>
  </dd></dl>
 </dl>
  <h2>MYSQL CLIENT LOGGING</h2>
  The <code>mysql</code> client can do these types of logging for statements executed interactively: <dl>
<dd>  &bull; On Unix, <code>mysql</code> writes the statements to a history file. By default, this file is named .mysql_history in your home directory. To specify a different file, set the value of the MYSQL_HISTFILE environment variable.  </dd></dl>
 <dl>
<dd>  &bull; On all platforms, if the <code>--syslog</code> option is given, <code>mysql</code> writes the statements to the system logging facility. On Unix, this is syslog; on Windows, it is the Windows Event Log. The destination where logged messages appear is system dependent. On Linux, the destination is often the /var/log/messages file.  </dd></dl>
  The following discussion describes characteristics that apply to all logging types and provides information specific to each logging type. <dl>
<dd>  &bull; How Logging Occurs  </dd></dl>
 <dl>
<dd>  &bull; Controlling the History File  </dd></dl>
 <dl>
<dd>  &bull; syslog Logging Characteristics  </dd></dl>
 How Logging Occurs  For each enabled logging destination, statement logging occurs as follows: <dl>
<dd>  &bull; Statements are logged only when executed interactively. Statements are noninteractive, for example, when read from a file or a pipe. It is also possible to suppress statement logging by using the <code>--batch</code> or <code>--execute</code> option.  </dd></dl>
 <dl>
<dd>  &bull; Statements are ignored and not logged if they match any pattern in the "ignore" list. This list is described later.  </dd></dl>
 <dl>
<dd>  &bull; <code>mysql</code> logs each nonignored, nonempty statement line individually.  </dd></dl>
 <dl>
<dd>  &bull; If a nonignored statement spans multiple lines (not including the terminating delimiter), <code>mysql</code> concatenates the lines to form the complete statement, maps newlines to spaces, and logs the result, plus a delimiter.  </dd></dl>
  Consequently, an input statement that spans multiple lines can be logged twice. Consider this input: <dl>
<dd>  <pre><code>mysql&gt; SELECT     -&gt; 'Today is'     -&gt; ,     -&gt; CURDATE()     -&gt; ; 
</code></pre>
  </dd></dl>
  In this case, <code>mysql</code> logs the "SELECT", "&#8216;Today is&#8217;", ",", "CURDATE()", and ";" lines as it reads them. It also logs the complete statement, after mapping SELECT\n&#8217;Today is&#8217;\n,\nCURDATE() to SELECT &#8216;Today is&#8217; , CURDATE(), plus a delimiter. Thus, these lines appear in logged output: <dl>
<dd>  <pre><code>SELECT
'Today is'
,
CURDATE()
;
SELECT 'Today is' , CURDATE();
</code></pre>
  </dd></dl>
  <p> <code>mysql</code> ignores for logging purposes statements that match any pattern in the "ignore" list. By default, the pattern list is &quot;*IDENTIFIED*:*PASSWORD*&quot;, to ignore statements that refer to passwords. Pattern matching is not case-sensitive. Within patterns, two characters are special: </p>
<dl>
<dd>  &bull; ? matches any single character.  </dd></dl>
 <dl>
<dd>  &bull; * matches any sequence of zero or more characters.  </dd></dl>
  To specify additional patterns, use the <code>--histignore</code> option or set the MYSQL_HISTIGNORE environment variable. (If both are specified, the option value takes precedence.) The value should be a list of one or more colon-separated patterns, which are appended to the default pattern list.  Patterns specified on the command line might need to be quoted or escaped to prevent your command interpreter from treating them specially. For example, to suppress logging for UPDATE and DELETE statements in addition to statements that refer to passwords, invoke <code>mysql</code> like this: <dl>
<dd>  <pre><code>shell&gt; mysql --histignore=&quot;*UPDATE*:*DELETE*&quot; 
</code></pre>
  </dd></dl>
  Controlling the History File  The .mysql_history file should be protected with a restrictive access mode because sensitive information might be written to it, such as the text of SQL statements that contain passwords. See Section 6.1.2.1, "End-User Guidelines for Password Security". Statements in the file are accessible from the <code>mysql</code> client when the up-arrow key is used to recall the history. See Disabling Interactive History.  If you do not want to maintain a history file, first remove .mysql_history if it exists. Then use either of the following techniques to prevent it from being created again: <dl>
<dd>  &bull; Set the MYSQL_HISTFILE environment variable to /dev/null. To cause this setting to take effect each time you log in, put it in one of your shell&#8217;s startup files.  </dd></dl>
 <dl>
<dd>  &bull; Create .mysql_history as a symbolic link to /dev/null; this need be done only once:  </dd>
<dl>
<dd>  <pre><code>shell&gt; ln -s /dev/null $HOME/.mysql_history 
</code></pre>
  </dd></dl>
 </dl>
 syslog Logging Characteristics  If the <code>--syslog</code> option is given, <code>mysql</code> writes interactive statements to the system logging facility. Message logging has the following characteristics.  Logging occurs at the "information" level. This corresponds to the LOG_INFO priority for syslog on Unix/Linux syslog capability and to EVENTLOG_INFORMATION_TYPE for the Windows Event Log. Consult your system documentation for configuration of your logging capability.  Message size is limited to 1024 bytes.  Messages consist of the identifier MysqlClient followed by these values: <dl>
<dd>  &bull; SYSTEM_USER  The operating system user name (login name) or -- if the user is unknown.  </dd></dl>
 <dl>
<dd>  &bull; MYSQL_USER  The MySQL user name (specified with the <code>--user</code> option) or -- if the user is unknown.  </dd></dl>
 <dl>
<dd>  &bull; CONNECTION_ID:  The client connection identifier. This is the same as the CONNECTION_ID() function value within the session.  </dd></dl>
 <dl>
<dd>  &bull; DB_SERVER  The server host or -- if the host is unknown.  </dd></dl>
 <dl>
<dd>  &bull; DB  The default database or -- if no database has been selected.  </dd></dl>
 <dl>
<dd>  &bull; QUERY  The text of the logged statement.  </dd></dl>
  Here is a sample of output generated on Linux by using <code>--syslog</code>. This output is formatted for readability; each logged message actually takes a single line. <dl>
<dd>  <pre><code>Mar 7 12:39:25 myhost MysqlClient[20824]:
  SYSTEM_USER:'oscar', MYSQL_USER:'my_oscar', CONNECTION_ID:23,
  DB_SERVER:'127.0.0.1', DB:'--', QUERY:'USE test;'
Mar 7 12:39:28 myhost MysqlClient[20824]:
  SYSTEM_USER:'oscar', MYSQL_USER:'my_oscar', CONNECTION_ID:23,
  DB_SERVER:'127.0.0.1', DB:'test', QUERY:'SHOW TABLES;'
</code></pre>
  </dd></dl>
  <h2>MYSQL CLIENT SERVER-SIDE HELP</h2>
 <dl>
<dd>  <pre><code>mysql&gt; help  search_string 
</code></pre>
  </dd></dl>
  If you provide an argument to the help command, <code>mysql</code> uses it as a search string to access server-side help from the contents of the MySQL Reference Manual. The proper operation of this command requires that the help tables in the mysql database be initialized with help topic information (see Section 5.1.14, "Server-Side Help Support").  If there is no match for the search string, the search fails: <dl>
<dd>  <pre><code>mysql&gt; help me Nothing found
Please try to run 'help contents' for a list of all accessible topics
</code></pre>
  </dd></dl>
  Use <code>help contents</code> to see a list of the help categories: <dl>
<dd>  <pre><code>mysql&gt; help contents You asked for help about help category: &quot;Contents&quot;
For more information, type 'help &lt;item&gt;', where &lt;item&gt; is one of the
following categories:
   Account Management
   Administration
   Data Definition
   Data Manipulation
   Data Types
   Functions
   Functions and Modifiers for Use with GROUP BY
   Geographic Features
   Language Structure
   Plugins
   Storage Engines
   Stored Routines
   Table Maintenance
   Transactions
   Triggers
</code></pre>
  </dd></dl>
  If the search string matches multiple items, <code>mysql</code> shows a list of matching topics: <dl>
<dd>  <pre><code>mysql&gt; help logs Many help items for your request exist.
To make a more specific request, please type 'help &lt;item&gt;',
where &lt;item&gt; is one of the following topics:
   SHOW
   SHOW BINARY LOGS
   SHOW ENGINE
   SHOW LOGS
</code></pre>
  </dd></dl>
  Use a topic as the search string to see the help entry for that topic: <dl>
<dd>  <pre><code>mysql&gt; help show binary logs Name: 'SHOW BINARY LOGS'
Description:
Syntax:
SHOW BINARY LOGS
SHOW MASTER LOGS
Lists the binary log files on the server. This statement is used as
part of the procedure described in [purge-binary-logs], that shows how
to determine which logs can be purged.
mysql&gt; SHOW BINARY LOGS;
+---------------+-----------+-----------+
| Log_name | File_size | Encrypted |
+---------------+-----------+-----------+
| binlog.000015 | 724935 | Yes |
| binlog.000016 | 733481 | Yes |
+---------------+-----------+-----------+
</code></pre>
  </dd></dl>
  The search string can contain the wildcard characters % and _. These have the same meaning as for pattern-matching operations performed with the LIKE operator. For example, HELP rep% returns a list of topics that begin with rep: <dl>
<dd>  <pre><code>mysql&gt; HELP rep% Many help items for your request exist.
To make a more specific request, please type 'help &lt;item&gt;',
where &lt;item&gt; is one of the following
topics:
   REPAIR TABLE
   REPEAT FUNCTION
   REPEAT LOOP
   REPLACE
   REPLACE FUNCTION
</code></pre>
  </dd></dl>
  <h2>EXECUTING SQL STATEMENTS FROM A TEXT FILE</h2>
  The <code>mysql</code> client typically is used interactively, like this: <dl>
<dd>  <pre><code>shell&gt; mysql  db_name 
</code></pre>
  </dd></dl>
  However, it is also possible to put your SQL statements in a file and then tell <code>mysql</code> to read its input from that file. To do so, create a text file <i>text_file</i> that contains the statements you wish to execute. Then invoke <code>mysql</code> as shown here: <dl>
<dd>  <pre><code>shell&gt; mysql  db_name   &lt;  text_file 
</code></pre>
  </dd></dl>
  If you place a USE <i>db_name</i> statement as the first statement in the file, it is unnecessary to specify the database name on the command line: <dl>
<dd>  <pre><code>shell&gt; mysql &lt; text_file 
</code></pre>
  </dd></dl>
  If you are already running <code>mysql</code>, you can execute an SQL script file using the source command or \. command: <dl>
<dd>  <pre><code>mysql&gt; source  file_name mysql&gt; \.  file_name 
</code></pre>
  </dd></dl>
  Sometimes you may want your script to display progress information to the user. For this you can insert statements like this: <dl>
<dd>  <pre><code>SELECT '&lt;info_to_display&gt;' AS ' ';
</code></pre>
  </dd></dl>
  The statement shown outputs &lt;info_to_display&gt;.  You can also invoke <code>mysql</code> with the <code>--verbose</code> option, which causes each statement to be displayed before the result that it produces.  <p> <code>mysql</code> ignores Unicode byte order mark (BOM) characters at the beginning of input files. Previously, it read them and sent them to the server, resulting in a syntax error. Presence of a BOM does not cause <code>mysql</code> to change its default character set. To do that, invoke <code>mysql</code> with an option such as <code>--default-character-set=utf8</code>. </p>
 For more information about batch mode, see Section 3.5, "Using mysql in Batch Mode".  <h2>MYSQL CLIENT TIPS</h2>
  This section provides information about techniques for more effective use of <code>mysql</code> and about <code>mysql</code> operational behavior. <dl>
<dd>  &bull; Input-Line Editing  </dd></dl>
 <dl>
<dd>  &bull; Disabling Interactive History  </dd></dl>
 <dl>
<dd>  &bull; Unicode Support on Windows  </dd></dl>
 <dl>
<dd>  &bull; Displaying Query Results Vertically  </dd></dl>
 <dl>
<dd>  &bull; Using Safe-Updates Mode (--safe-updates)  </dd></dl>
 <dl>
<dd>  &bull; Disabling mysql Auto-Reconnect  </dd></dl>
 <dl>
<dd>  &bull; mysql Client Parser Versus Server Parser  </dd></dl>
 Input-Line Editing  <p> <code>mysql</code> supports input-line editing, which enables you to modify the current input line in place or recall previous input lines. For example, the left-arrow and right-arrow keys move horizontally within the current input line, and the up-arrow and down-arrow keys move up and down through the set of previously entered lines. Backspace deletes the character before the cursor and typing new characters enters them at the cursor position. To enter the line, press Enter. </p>
 On Windows, the editing key sequences are the same as supported for command editing in console windows. On Unix, the key sequences depend on the input library used to build <code>mysql</code> (for example, the libedit or readline library).  Documentation for the libedit and readline libraries is available online. To change the set of key sequences permitted by a given input library, define key bindings in the library startup file. This is a file in your home directory: .editrc for libedit and .inputrc for readline.  For example, in libedit, Control+W deletes everything before the current cursor position and Control+U deletes the entire line. In readline, Control+W deletes the word before the cursor and Control+U deletes everything before the current cursor position. If <code>mysql</code> was built using libedit, a user who prefers the readline behavior for these two keys can put the following lines in the .editrc file (creating the file if necessary): <dl>
<dd>  <pre><code>bind &quot;^W&quot; ed-delete-prev-word
bind &quot;^U&quot; vi-kill-line-prev
</code></pre>
  </dd></dl>
  To see the current set of key bindings, temporarily put a line that says only bind at the end of .editrc. <code>mysql</code> will show the bindings when it starts. Disabling Interactive History  The up-arrow key enables you to recall input lines from current and previous sessions. In cases where a console is shared, this behavior may be unsuitable. <code>mysql</code> supports disabling the interactive history partially or fully, depending on the host platform.  On Windows, the history is stored in memory. Alt+F7 deletes all input lines stored in memory for the current history buffer. It also deletes the list of sequential numbers in front of the input lines displayed with F7 and recalled (by number) with F9. New input lines entered after you press Alt+F7 repopulate the current history buffer. Clearing the buffer does not prevent logging to the Windows Event Viewer, if the <code>--syslog</code> option was used to start <code>mysql</code>. Closing the console window also clears the current history buffer.  To disable interactive history on Unix, first delete the .mysql_history file, if it exists (previous entries are recalled otherwise). Then start <code>mysql</code> with the --histignore=&quot;*&quot; option to ignore all new input lines. To re-enable the recall (and logging) behavior, restart <code>mysql</code> without the option.  If you prevent the .mysql_history file from being created (see Controlling the History File) and use --histignore=&quot;*&quot; to start the <code>mysql</code> client, the interactive history recall facility is disabled fully. Alternatively, if you omit the <code>--histignore</code> option, you can recall the input lines entered during the current session. Unicode Support on Windows  Windows provides APIs based on UTF-16LE for reading from and writing to the console; the <code>mysql</code> client for Windows is able to use these APIs. The Windows installer creates an item in the MySQL menu named MySQL command line client - Unicode. This item invokes the <code>mysql</code> client with properties set to communicate through the console to the MySQL server using Unicode.  To take advantage of this support manually, run <code>mysql</code> within a console that uses a compatible Unicode font and set the default character set to a Unicode character set that is supported for communication with the server: <dl>
<dd>  1. Open a console window.  </dd></dl>
 <dl>
<dd>  2. Go to the console window properties, select the font tab, and choose Lucida Console or some other compatible Unicode font. This is necessary because console windows start by default using a DOS raster font that is inadequate for Unicode.  </dd></dl>
 <dl>
<dd>  3. Execute <code>mysql.exe</code> with the <code>--default-character-set=utf8</code> (or utf8mb4) option. This option is necessary because utf16le is one of the character sets that cannot be used as the client character set. See the section called "Impermissible Client Character Sets".  </dd></dl>
  With those changes, <code>mysql</code> will use the Windows APIs to communicate with the console using UTF-16LE, and communicate with the server using UTF-8. (The menu item mentioned previously sets the font and character set as just described.)  To avoid those steps each time you run <code>mysql</code>, you can create a shortcut that invokes <code>mysql.exe</code>. The shortcut should set the console font to Lucida Console or some other compatible Unicode font, and pass the <code>--default-character-set=utf8</code> (or utf8mb4) option to <code>mysql.exe</code>.  Alternatively, create a shortcut that only sets the console font, and set the character set in the [mysql] group of your my.ini file: <dl>
<dd>  <pre><code>[mysql]
default-character-set=utf8
</code></pre>
  </dd></dl>
  Displaying Query Results Vertically  Some query results are much more readable when displayed vertically, instead of in the usual horizontal table format. Queries can be displayed vertically by terminating the query with \G instead of a semicolon. For example, longer text values that include newlines often are much easier to read with vertical output: <dl>
<dd>  <pre><code>mysql&gt; SELECT * FROM mails WHERE LENGTH(txt) &lt; 300 LIMIT 300,1\G *************************** 1. row ***************************
  msg_nro: 3068
     date: 2000-03-01 23:29:50
time_zone: +0200
mail_from: Jones
    reply: jones [at] example.com
  mail_to: &quot;John Smith&quot; &lt;smith [at] example.com&gt;
      sbj: UTF-8
      txt: &gt;&gt;&gt;&gt;&gt; &quot;John&quot; == John Smith writes:
John&gt; Hi. I think this is a good idea. Is anyone familiar
John&gt; with UTF-8 or Unicode? Otherwise, I'll put this on my
John&gt; TODO list and see what happens.
Yes, please do that.
Regards,
Jones
     file: inbox-jani-1
     hash: 190402944
1 row in set (0.09 sec)
</code></pre>
  </dd></dl>
  Using Safe-Updates Mode (--safe-updates)  For beginners, a useful startup option is <code>--safe-updates</code> (or <code>--i-am-a-dummy</code>, which has the same effect). Safe-updates mode is helpful for cases when you might have issued an UPDATE or DELETE statement but forgotten the WHERE clause indicating which rows to modify. Normally, such statements update or delete all rows in the table. With <code>--safe-updates</code>, you can modify rows only by specifying the key values that identify them, or a LIMIT clause, or both. This helps prevent accidents. Safe-updates mode also restricts SELECT statements that produce (or are estimated to produce) very large result sets.  The <code>--safe-updates</code> option causes <code>mysql</code> to execute the following statement when it connects to the MySQL server, to set the session values of the sql_safe_updates, sql_select_limit, and max_join_size system variables: <dl>
<dd>  <pre><code>SET sql_safe_updates=1, sql_select_limit=1000, max_join_size=1000000;
</code></pre>
  </dd></dl>
  The SET statement affects statement processing as follows: <dl>
<dd>  &bull; Enabling sql_safe_updates causes UPDATE and DELETE statements to produce an error if they do not specify a key constraint in the WHERE clause, or provide a LIMIT clause, or both. For example:  </dd>
<dl>
<dd>  <pre><code>UPDATE tbl_name  SET not_key_column = val  WHERE key_column = val ;
UPDATE tbl_name  SET not_key_column = val  LIMIT 1;
</code></pre>
  </dd></dl>
 </dl>
 <dl>
<dd>  &bull; Setting sql_select_limit to 1,000 causes the server to limit all SELECT result sets to 1,000 rows unless the statement includes a LIMIT clause.  </dd></dl>
 <dl>
<dd>  &bull; Setting max_join_size to 1,000,000 causes multiple-table SELECT statements to produce an error if the server estimates it must examine more than 1,000,000 row combinations.  </dd></dl>
  To specify result set limits different from 1,000 and 1,000,000, you can override the defaults by using the <code>--select-limit</code> and <code>--max-join-size</code> options when you invoke <code>mysql</code>: <dl>
<dd>  <pre><code>mysql --safe-updates --select-limit=500 --max-join-size=10000
</code></pre>
  </dd></dl>
  It is possible for UPDATE and DELETE statements to produce an error in safe-updates mode even with a key specified in the WHERE clause, if the optimizer decides not to use the index on the key column: <dl>
<dd>  &bull; Range access on the index cannot be used if memory usage exceeds that permitted by the range_optimizer_max_mem_size system variable. The optimizer then falls back to a table scan. See the section called "Limiting Memory Use for Range Optimization".  </dd></dl>
 <dl>
<dd>  &bull; If key comparisons require type conversion, the index may not be used (see Section 8.3.1, "How MySQL Uses Indexes"). Suppose that an indexed string column c1 is compared to a numeric value using WHERE c1 = 2222. For such comparisons, the string value is converted to a number and the operands are compared numerically (see Section 12.2, "Type Conversion in Expression Evaluation"), preventing use of the index. If safe-updates mode is enabled, an error occurs.  </dd></dl>
  As of MySQL 8.0.13, safe-updates mode also includes these behaviors: <dl>
<dd>  &bull; EXPLAIN with UPDATE and DELETE statements does not produce safe-updates errors. This enables use of EXPLAIN plus SHOW WARNINGS to see why an index is not used, which can be helpful in cases such as when a range_optimizer_max_mem_size violation or type conversion occurs and the optimizer does not use an index even though a key column was specified in the WHERE clause.  </dd></dl>
 <dl>
<dd>  &bull; When a safe-updates error occurs, the error message includes the first diagnostic that was produced, to provide information about the reason for failure. For example, the message may indicate that the range_optimizer_max_mem_size value was exceeded or type conversion occurred, either of which can preclude use of an index.  </dd></dl>
 <dl>
<dd>  &bull; For multiple-table deletes and updates, an error is produced with safe updates enabled only if any target table uses a table scan.  </dd></dl>
 Disabling mysql Auto-Reconnect  If the <code>mysql</code> client loses its connection to the server while sending a statement, it immediately and automatically tries to reconnect once to the server and send the statement again. However, even if <code>mysql</code> succeeds in reconnecting, your first connection has ended and all your previous session objects and settings are lost: temporary tables, the autocommit mode, and user-defined and session variables. Also, any current transaction rolls back. This behavior may be dangerous for you, as in the following example where the server was shut down and restarted between the first and second statements without you knowing it: <dl>
<dd>  <pre><code>mysql&gt; SET @a=1; Query OK, 0 rows affected (0.05 sec)
mysql&gt; INSERT INTO t VALUES(@a); ERROR 2006: MySQL server has gone away
No connection. Trying to reconnect...
Connection id: 1
Current database: test
Query OK, 1 row affected (1.30 sec)
mysql&gt; SELECT * FROM t; +------+
| a |
+------+
| NULL |
+------+
1 row in set (0.05 sec)
</code></pre>
  </dd></dl>
  The @a user variable has been lost with the connection, and after the reconnection it is undefined. If it is important to have <code>mysql</code> terminate with an error if the connection has been lost, you can start the <code>mysql</code> client with the <code>--skip-reconnect</code> option.  For more information about auto-reconnect and its effect on state information when a reconnection occurs, see Section 28.7.27, "C API Automatic Reconnection Control". mysql Client Parser Versus Server Parser  The <code>mysql</code> client uses a parser on the client side that is not a duplicate of the complete parser used by the <code>mysqld</code> server on the server side. This can lead to differences in treatment of certain constructs. Examples: <dl>
<dd>  &bull; The server parser treats strings delimited by &quot; characters as identifiers rather than as plain strings if the ANSI_QUOTES SQL mode is enabled.  The <code>mysql</code> client parser does not take the ANSI_QUOTES SQL mode into account. It treats strings delimited by &quot;, &#8216;, and ` characters the same, regardless of whether ANSI_QUOTES is enabled.  </dd></dl>
 <dl>
<dd>  &bull; Within /*! ... */ and /*+ ... */ comments, the <code>mysql</code> client parser interprets short-form <code>mysql</code> commands. The server parser does not interpret them because these commands have no meaning on the server side.  If it is desirable for <code>mysql</code> not to interpret short-form commands within comments, a partial workaround is to use the <code>--binary-mode</code> option, which causes all <code>mysql</code> commands to be disabled except \C and \d in noninteractive mode (for input piped to <code>mysql</code> or loaded using the source command).  </dd></dl>
  <h2>COPYRIGHT</h2>
   Copyright &#169; 1997, 2020, Oracle and/or its affiliates. All rights reserved.  This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License.  This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.  You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> <h2>NOTES</h2>
 <dl>
 <dd>  1. 4 MySQL Shell 8.0 (part of MySQL 8.0)  </dd>
<dl>
<dd>  <a rel="nofollow" href="https://dev.mysql.com/doc/mysql-shell/8.0/en/">https://dev.mysql.com/doc/mysql-shell/8.0/en/</a>  </dd></dl>
 </dl>
  <h2>SEE ALSO</h2>
 For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a>  <h2>AUTHOR</h2>
 Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>).  
</td>
<td> The server version 
</td>
</tr>
<tr VALIGN=top>
<td> The current day of the week in three-letter format (Mon, Tue, ...) T} T{ Y T}:T{ The current year, four digits T} T{ y T}:T{ The current year, two digits T} T{ _ T}:T{ A space T} T{ \ T}:T{ A space (a space follows the backslash) T} T{ &#8216; T}:T{ Single quote T} T{ T}:T{ Double quote T} T{ \ T}:T{ A literal &nbsp;backslash character T} T{ \fIx T}:T{  <p> <i>x</i>, for any "<i>x</i>" not listed above T} </p>
 You can set the prompt in several ways: <dl>
<dd>  &bull; <i>Use an environment variable.</i> You can set the MYSQL_PS1 environment variable to a prompt string. For example:  </dd>
<dl>
<dd>  <pre><code>shell&gt; export MYSQL_PS1=&quot;(\u@\h) [\d]&gt; &quot; 
</code></pre>
  </dd></dl>
 </dl>
 <dl>
<dd>  &bull; <i>Use a command-line option.</i> You can set the <code>--prompt</code> option on the command line to <code>mysql</code>. For example:  </dd>
<dl>
<dd>  <pre><code>shell&gt; mysql --prompt=&quot;(\u@\h) [\d]&gt; &quot; (user [at] host) [database]&gt;
</code></pre>
  </dd></dl>
 </dl>
 <dl>
<dd>  &bull; <i>Use an option file.</i> You can set the prompt option in the [mysql] group of any MySQL option file, such as /etc/my.cnf or the .my.cnf file in your home directory. For example:  </dd>
<dl>
<dd>  <pre><code>[mysql]
prompt=(\\u@\\h) [\\d]&gt;\\_
</code></pre>
  </dd></dl>
  In this example, note that the backslashes are doubled. If you set the prompt using the prompt option in an option file, it is advisable to double the backslashes when using the special prompt options. There is some overlap in the set of permissible prompt options and the set of special escape sequences that are recognized in option files. (The rules for escape sequences in option files are listed in Section 4.2.2.2, "Using Option Files".) The overlap may cause you problems if you use single backslashes. For example, \s is interpreted as a space rather than as the current seconds value. The following example shows how to define a prompt within an option file to include the current time in <i>hh:mm:ss</i>&gt; format: <dl>
<dd>  <pre><code>[mysql]
prompt=&quot;\\r:\\m:\\s&gt; &quot;
</code></pre>
  </dd></dl>
 </dl>
 <dl>
<dd>  &bull; <i>Set the prompt interactively.</i> You can change your prompt interactively by using the prompt (or \R) command. For example:  </dd>
<dl>
<dd>  <pre><code>mysql&gt; prompt (\u@\h) [\d]&gt;\_ PROMPT set to '(\u@\h) [\d]&gt;\_'
( user @ host ) [ database ]&gt;
( user @ host ) [ database ]&gt; prompt
Returning to default PROMPT of mysql&gt;
mysql&gt;
</code></pre>
  </dd></dl>
 </dl>
  <h2>MYSQL CLIENT LOGGING</h2>
  The <code>mysql</code> client can do these types of logging for statements executed interactively: <dl>
<dd>  &bull; On Unix, <code>mysql</code> writes the statements to a history file. By default, this file is named .mysql_history in your home directory. To specify a different file, set the value of the MYSQL_HISTFILE environment variable.  </dd></dl>
 <dl>
<dd>  &bull; On all platforms, if the <code>--syslog</code> option is given, <code>mysql</code> writes the statements to the system logging facility. On Unix, this is syslog; on Windows, it is the Windows Event Log. The destination where logged messages appear is system dependent. On Linux, the destination is often the /var/log/messages file.  </dd></dl>
  The following discussion describes characteristics that apply to all logging types and provides information specific to each logging type. <dl>
<dd>  &bull; How Logging Occurs  </dd></dl>
 <dl>
<dd>  &bull; Controlling the History File  </dd></dl>
 <dl>
<dd>  &bull; syslog Logging Characteristics  </dd></dl>
 How Logging Occurs  For each enabled logging destination, statement logging occurs as follows: <dl>
<dd>  &bull; Statements are logged only when executed interactively. Statements are noninteractive, for example, when read from a file or a pipe. It is also possible to suppress statement logging by using the <code>--batch</code> or <code>--execute</code> option.  </dd></dl>
 <dl>
<dd>  &bull; Statements are ignored and not logged if they match any pattern in the "ignore" list. This list is described later.  </dd></dl>
 <dl>
<dd>  &bull; <code>mysql</code> logs each nonignored, nonempty statement line individually.  </dd></dl>
 <dl>
<dd>  &bull; If a nonignored statement spans multiple lines (not including the terminating delimiter), <code>mysql</code> concatenates the lines to form the complete statement, maps newlines to spaces, and logs the result, plus a delimiter.  </dd></dl>
  Consequently, an input statement that spans multiple lines can be logged twice. Consider this input: <dl>
<dd>  <pre><code>mysql&gt; SELECT     -&gt; 'Today is'     -&gt; ,     -&gt; CURDATE()     -&gt; ; 
</code></pre>
  </dd></dl>
  In this case, <code>mysql</code> logs the "SELECT", "&#8216;Today is&#8217;", ",", "CURDATE()", and ";" lines as it reads them. It also logs the complete statement, after mapping SELECT\n&#8217;Today is&#8217;\n,\nCURDATE() to SELECT &#8216;Today is&#8217; , CURDATE(), plus a delimiter. Thus, these lines appear in logged output: <dl>
<dd>  <pre><code>SELECT
'Today is'
,
CURDATE()
;
SELECT 'Today is' , CURDATE();
</code></pre>
  </dd></dl>
  <p> <code>mysql</code> ignores for logging purposes statements that match any pattern in the "ignore" list. By default, the pattern list is &quot;*IDENTIFIED*:*PASSWORD*&quot;, to ignore statements that refer to passwords. Pattern matching is not case-sensitive. Within patterns, two characters are special: </p>
<dl>
<dd>  &bull; ? matches any single character.  </dd></dl>
 <dl>
<dd>  &bull; * matches any sequence of zero or more characters.  </dd></dl>
  To specify additional patterns, use the <code>--histignore</code> option or set the MYSQL_HISTIGNORE environment variable. (If both are specified, the option value takes precedence.) The value should be a list of one or more colon-separated patterns, which are appended to the default pattern list.  Patterns specified on the command line might need to be quoted or escaped to prevent your command interpreter from treating them specially. For example, to suppress logging for UPDATE and DELETE statements in addition to statements that refer to passwords, invoke <code>mysql</code> like this: <dl>
<dd>  <pre><code>shell&gt; mysql --histignore=&quot;*UPDATE*:*DELETE*&quot; 
</code></pre>
  </dd></dl>
  Controlling the History File  The .mysql_history file should be protected with a restrictive access mode because sensitive information might be written to it, such as the text of SQL statements that contain passwords. See Section 6.1.2.1, "End-User Guidelines for Password Security". Statements in the file are accessible from the <code>mysql</code> client when the up-arrow key is used to recall the history. See Disabling Interactive History.  If you do not want to maintain a history file, first remove .mysql_history if it exists. Then use either of the following techniques to prevent it from being created again: <dl>
<dd>  &bull; Set the MYSQL_HISTFILE environment variable to /dev/null. To cause this setting to take effect each time you log in, put it in one of your shell&#8217;s startup files.  </dd></dl>
 <dl>
<dd>  &bull; Create .mysql_history as a symbolic link to /dev/null; this need be done only once:  </dd>
<dl>
<dd>  <pre><code>shell&gt; ln -s /dev/null $HOME/.mysql_history 
</code></pre>
  </dd></dl>
 </dl>
 syslog Logging Characteristics  If the <code>--syslog</code> option is given, <code>mysql</code> writes interactive statements to the system logging facility. Message logging has the following characteristics.  Logging occurs at the "information" level. This corresponds to the LOG_INFO priority for syslog on Unix/Linux syslog capability and to EVENTLOG_INFORMATION_TYPE for the Windows Event Log. Consult your system documentation for configuration of your logging capability.  Message size is limited to 1024 bytes.  Messages consist of the identifier MysqlClient followed by these values: <dl>
<dd>  &bull; SYSTEM_USER  The operating system user name (login name) or -- if the user is unknown.  </dd></dl>
 <dl>
<dd>  &bull; MYSQL_USER  The MySQL user name (specified with the <code>--user</code> option) or -- if the user is unknown.  </dd></dl>
 <dl>
<dd>  &bull; CONNECTION_ID:  The client connection identifier. This is the same as the CONNECTION_ID() function value within the session.  </dd></dl>
 <dl>
<dd>  &bull; DB_SERVER  The server host or -- if the host is unknown.  </dd></dl>
 <dl>
<dd>  &bull; DB  The default database or -- if no database has been selected.  </dd></dl>
 <dl>
<dd>  &bull; QUERY  The text of the logged statement.  </dd></dl>
  Here is a sample of output generated on Linux by using <code>--syslog</code>. This output is formatted for readability; each logged message actually takes a single line. <dl>
<dd>  <pre><code>Mar 7 12:39:25 myhost MysqlClient[20824]:
  SYSTEM_USER:'oscar', MYSQL_USER:'my_oscar', CONNECTION_ID:23,
  DB_SERVER:'127.0.0.1', DB:'--', QUERY:'USE test;'
Mar 7 12:39:28 myhost MysqlClient[20824]:
  SYSTEM_USER:'oscar', MYSQL_USER:'my_oscar', CONNECTION_ID:23,
  DB_SERVER:'127.0.0.1', DB:'test', QUERY:'SHOW TABLES;'
</code></pre>
  </dd></dl>
  <h2>MYSQL CLIENT SERVER-SIDE HELP</h2>
 <dl>
<dd>  <pre><code>mysql&gt; help  search_string 
</code></pre>
  </dd></dl>
  If you provide an argument to the help command, <code>mysql</code> uses it as a search string to access server-side help from the contents of the MySQL Reference Manual. The proper operation of this command requires that the help tables in the mysql database be initialized with help topic information (see Section 5.1.14, "Server-Side Help Support").  If there is no match for the search string, the search fails: <dl>
<dd>  <pre><code>mysql&gt; help me Nothing found
Please try to run 'help contents' for a list of all accessible topics
</code></pre>
  </dd></dl>
  Use <code>help contents</code> to see a list of the help categories: <dl>
<dd>  <pre><code>mysql&gt; help contents You asked for help about help category: &quot;Contents&quot;
For more information, type 'help &lt;item&gt;', where &lt;item&gt; is one of the
following categories:
   Account Management
   Administration
   Data Definition
   Data Manipulation
   Data Types
   Functions
   Functions and Modifiers for Use with GROUP BY
   Geographic Features
   Language Structure
   Plugins
   Storage Engines
   Stored Routines
   Table Maintenance
   Transactions
   Triggers
</code></pre>
  </dd></dl>
  If the search string matches multiple items, <code>mysql</code> shows a list of matching topics: <dl>
<dd>  <pre><code>mysql&gt; help logs Many help items for your request exist.
To make a more specific request, please type 'help &lt;item&gt;',
where &lt;item&gt; is one of the following topics:
   SHOW
   SHOW BINARY LOGS
   SHOW ENGINE
   SHOW LOGS
</code></pre>
  </dd></dl>
  Use a topic as the search string to see the help entry for that topic: <dl>
<dd>  <pre><code>mysql&gt; help show binary logs Name: 'SHOW BINARY LOGS'
Description:
Syntax:
SHOW BINARY LOGS
SHOW MASTER LOGS
Lists the binary log files on the server. This statement is used as
part of the procedure described in [purge-binary-logs], that shows how
to determine which logs can be purged.
mysql&gt; SHOW BINARY LOGS;
+---------------+-----------+-----------+
| Log_name | File_size | Encrypted |
+---------------+-----------+-----------+
| binlog.000015 | 724935 | Yes |
| binlog.000016 | 733481 | Yes |
+---------------+-----------+-----------+
</code></pre>
  </dd></dl>
  The search string can contain the wildcard characters % and _. These have the same meaning as for pattern-matching operations performed with the LIKE operator. For example, HELP rep% returns a list of topics that begin with rep: <dl>
<dd>  <pre><code>mysql&gt; HELP rep% Many help items for your request exist.
To make a more specific request, please type 'help &lt;item&gt;',
where &lt;item&gt; is one of the following
topics:
   REPAIR TABLE
   REPEAT FUNCTION
   REPEAT LOOP
   REPLACE
   REPLACE FUNCTION
</code></pre>
  </dd></dl>
  <h2>EXECUTING SQL STATEMENTS FROM A TEXT FILE</h2>
  The <code>mysql</code> client typically is used interactively, like this: <dl>
<dd>  <pre><code>shell&gt; mysql  db_name 
</code></pre>
  </dd></dl>
  However, it is also possible to put your SQL statements in a file and then tell <code>mysql</code> to read its input from that file. To do so, create a text file <i>text_file</i> that contains the statements you wish to execute. Then invoke <code>mysql</code> as shown here: <dl>
<dd>  <pre><code>shell&gt; mysql  db_name   &lt;  text_file 
</code></pre>
  </dd></dl>
  If you place a USE <i>db_name</i> statement as the first statement in the file, it is unnecessary to specify the database name on the command line: <dl>
<dd>  <pre><code>shell&gt; mysql &lt; text_file 
</code></pre>
  </dd></dl>
  If you are already running <code>mysql</code>, you can execute an SQL script file using the source command or \. command: <dl>
<dd>  <pre><code>mysql&gt; source  file_name mysql&gt; \.  file_name 
</code></pre>
  </dd></dl>
  Sometimes you may want your script to display progress information to the user. For this you can insert statements like this: <dl>
<dd>  <pre><code>SELECT '&lt;info_to_display&gt;' AS ' ';
</code></pre>
  </dd></dl>
  The statement shown outputs &lt;info_to_display&gt;.  You can also invoke <code>mysql</code> with the <code>--verbose</code> option, which causes each statement to be displayed before the result that it produces.  <p> <code>mysql</code> ignores Unicode byte order mark (BOM) characters at the beginning of input files. Previously, it read them and sent them to the server, resulting in a syntax error. Presence of a BOM does not cause <code>mysql</code> to change its default character set. To do that, invoke <code>mysql</code> with an option such as <code>--default-character-set=utf8</code>. </p>
 For more information about batch mode, see Section 3.5, "Using mysql in Batch Mode".  <h2>MYSQL CLIENT TIPS</h2>
  This section provides information about techniques for more effective use of <code>mysql</code> and about <code>mysql</code> operational behavior. <dl>
<dd>  &bull; Input-Line Editing  </dd></dl>
 <dl>
<dd>  &bull; Disabling Interactive History  </dd></dl>
 <dl>
<dd>  &bull; Unicode Support on Windows  </dd></dl>
 <dl>
<dd>  &bull; Displaying Query Results Vertically  </dd></dl>
 <dl>
<dd>  &bull; Using Safe-Updates Mode (--safe-updates)  </dd></dl>
 <dl>
<dd>  &bull; Disabling mysql Auto-Reconnect  </dd></dl>
 <dl>
<dd>  &bull; mysql Client Parser Versus Server Parser  </dd></dl>
 Input-Line Editing  <p> <code>mysql</code> supports input-line editing, which enables you to modify the current input line in place or recall previous input lines. For example, the left-arrow and right-arrow keys move horizontally within the current input line, and the up-arrow and down-arrow keys move up and down through the set of previously entered lines. Backspace deletes the character before the cursor and typing new characters enters them at the cursor position. To enter the line, press Enter. </p>
 On Windows, the editing key sequences are the same as supported for command editing in console windows. On Unix, the key sequences depend on the input library used to build <code>mysql</code> (for example, the libedit or readline library).  Documentation for the libedit and readline libraries is available online. To change the set of key sequences permitted by a given input library, define key bindings in the library startup file. This is a file in your home directory: .editrc for libedit and .inputrc for readline.  For example, in libedit, Control+W deletes everything before the current cursor position and Control+U deletes the entire line. In readline, Control+W deletes the word before the cursor and Control+U deletes everything before the current cursor position. If <code>mysql</code> was built using libedit, a user who prefers the readline behavior for these two keys can put the following lines in the .editrc file (creating the file if necessary): <dl>
<dd>  <pre><code>bind &quot;^W&quot; ed-delete-prev-word
bind &quot;^U&quot; vi-kill-line-prev
</code></pre>
  </dd></dl>
  To see the current set of key bindings, temporarily put a line that says only bind at the end of .editrc. <code>mysql</code> will show the bindings when it starts. Disabling Interactive History  The up-arrow key enables you to recall input lines from current and previous sessions. In cases where a console is shared, this behavior may be unsuitable. <code>mysql</code> supports disabling the interactive history partially or fully, depending on the host platform.  On Windows, the history is stored in memory. Alt+F7 deletes all input lines stored in memory for the current history buffer. It also deletes the list of sequential numbers in front of the input lines displayed with F7 and recalled (by number) with F9. New input lines entered after you press Alt+F7 repopulate the current history buffer. Clearing the buffer does not prevent logging to the Windows Event Viewer, if the <code>--syslog</code> option was used to start <code>mysql</code>. Closing the console window also clears the current history buffer.  To disable interactive history on Unix, first delete the .mysql_history file, if it exists (previous entries are recalled otherwise). Then start <code>mysql</code> with the --histignore=&quot;*&quot; option to ignore all new input lines. To re-enable the recall (and logging) behavior, restart <code>mysql</code> without the option.  If you prevent the .mysql_history file from being created (see Controlling the History File) and use --histignore=&quot;*&quot; to start the <code>mysql</code> client, the interactive history recall facility is disabled fully. Alternatively, if you omit the <code>--histignore</code> option, you can recall the input lines entered during the current session. Unicode Support on Windows  Windows provides APIs based on UTF-16LE for reading from and writing to the console; the <code>mysql</code> client for Windows is able to use these APIs. The Windows installer creates an item in the MySQL menu named MySQL command line client - Unicode. This item invokes the <code>mysql</code> client with properties set to communicate through the console to the MySQL server using Unicode.  To take advantage of this support manually, run <code>mysql</code> within a console that uses a compatible Unicode font and set the default character set to a Unicode character set that is supported for communication with the server: <dl>
<dd>  1. Open a console window.  </dd></dl>
 <dl>
<dd>  2. Go to the console window properties, select the font tab, and choose Lucida Console or some other compatible Unicode font. This is necessary because console windows start by default using a DOS raster font that is inadequate for Unicode.  </dd></dl>
 <dl>
<dd>  3. Execute <code>mysql.exe</code> with the <code>--default-character-set=utf8</code> (or utf8mb4) option. This option is necessary because utf16le is one of the character sets that cannot be used as the client character set. See the section called "Impermissible Client Character Sets".  </dd></dl>
  With those changes, <code>mysql</code> will use the Windows APIs to communicate with the console using UTF-16LE, and communicate with the server using UTF-8. (The menu item mentioned previously sets the font and character set as just described.)  To avoid those steps each time you run <code>mysql</code>, you can create a shortcut that invokes <code>mysql.exe</code>. The shortcut should set the console font to Lucida Console or some other compatible Unicode font, and pass the <code>--default-character-set=utf8</code> (or utf8mb4) option to <code>mysql.exe</code>.  Alternatively, create a shortcut that only sets the console font, and set the character set in the [mysql] group of your my.ini file: <dl>
<dd>  <pre><code>[mysql]
default-character-set=utf8
</code></pre>
  </dd></dl>
  Displaying Query Results Vertically  Some query results are much more readable when displayed vertically, instead of in the usual horizontal table format. Queries can be displayed vertically by terminating the query with \G instead of a semicolon. For example, longer text values that include newlines often are much easier to read with vertical output: <dl>
<dd>  <pre><code>mysql&gt; SELECT * FROM mails WHERE LENGTH(txt) &lt; 300 LIMIT 300,1\G *************************** 1. row ***************************
  msg_nro: 3068
     date: 2000-03-01 23:29:50
time_zone: +0200
mail_from: Jones
    reply: jones [at] example.com
  mail_to: &quot;John Smith&quot; &lt;smith [at] example.com&gt;
      sbj: UTF-8
      txt: &gt;&gt;&gt;&gt;&gt; &quot;John&quot; == John Smith writes:
John&gt; Hi. I think this is a good idea. Is anyone familiar
John&gt; with UTF-8 or Unicode? Otherwise, I'll put this on my
John&gt; TODO list and see what happens.
Yes, please do that.
Regards,
Jones
     file: inbox-jani-1
     hash: 190402944
1 row in set (0.09 sec)
</code></pre>
  </dd></dl>
  Using Safe-Updates Mode (--safe-updates)  For beginners, a useful startup option is <code>--safe-updates</code> (or <code>--i-am-a-dummy</code>, which has the same effect). Safe-updates mode is helpful for cases when you might have issued an UPDATE or DELETE statement but forgotten the WHERE clause indicating which rows to modify. Normally, such statements update or delete all rows in the table. With <code>--safe-updates</code>, you can modify rows only by specifying the key values that identify them, or a LIMIT clause, or both. This helps prevent accidents. Safe-updates mode also restricts SELECT statements that produce (or are estimated to produce) very large result sets.  The <code>--safe-updates</code> option causes <code>mysql</code> to execute the following statement when it connects to the MySQL server, to set the session values of the sql_safe_updates, sql_select_limit, and max_join_size system variables: <dl>
<dd>  <pre><code>SET sql_safe_updates=1, sql_select_limit=1000, max_join_size=1000000;
</code></pre>
  </dd></dl>
  The SET statement affects statement processing as follows: <dl>
<dd>  &bull; Enabling sql_safe_updates causes UPDATE and DELETE statements to produce an error if they do not specify a key constraint in the WHERE clause, or provide a LIMIT clause, or both. For example:  </dd>
<dl>
<dd>  <pre><code>UPDATE tbl_name  SET not_key_column = val  WHERE key_column = val ;
UPDATE tbl_name  SET not_key_column = val  LIMIT 1;
</code></pre>
  </dd></dl>
 </dl>
 <dl>
<dd>  &bull; Setting sql_select_limit to 1,000 causes the server to limit all SELECT result sets to 1,000 rows unless the statement includes a LIMIT clause.  </dd></dl>
 <dl>
<dd>  &bull; Setting max_join_size to 1,000,000 causes multiple-table SELECT statements to produce an error if the server estimates it must examine more than 1,000,000 row combinations.  </dd></dl>
  To specify result set limits different from 1,000 and 1,000,000, you can override the defaults by using the <code>--select-limit</code> and <code>--max-join-size</code> options when you invoke <code>mysql</code>: <dl>
<dd>  <pre><code>mysql --safe-updates --select-limit=500 --max-join-size=10000
</code></pre>
  </dd></dl>
  It is possible for UPDATE and DELETE statements to produce an error in safe-updates mode even with a key specified in the WHERE clause, if the optimizer decides not to use the index on the key column: <dl>
<dd>  &bull; Range access on the index cannot be used if memory usage exceeds that permitted by the range_optimizer_max_mem_size system variable. The optimizer then falls back to a table scan. See the section called "Limiting Memory Use for Range Optimization".  </dd></dl>
 <dl>
<dd>  &bull; If key comparisons require type conversion, the index may not be used (see Section 8.3.1, "How MySQL Uses Indexes"). Suppose that an indexed string column c1 is compared to a numeric value using WHERE c1 = 2222. For such comparisons, the string value is converted to a number and the operands are compared numerically (see Section 12.2, "Type Conversion in Expression Evaluation"), preventing use of the index. If safe-updates mode is enabled, an error occurs.  </dd></dl>
  As of MySQL 8.0.13, safe-updates mode also includes these behaviors: <dl>
<dd>  &bull; EXPLAIN with UPDATE and DELETE statements does not produce safe-updates errors. This enables use of EXPLAIN plus SHOW WARNINGS to see why an index is not used, which can be helpful in cases such as when a range_optimizer_max_mem_size violation or type conversion occurs and the optimizer does not use an index even though a key column was specified in the WHERE clause.  </dd></dl>
 <dl>
<dd>  &bull; When a safe-updates error occurs, the error message includes the first diagnostic that was produced, to provide information about the reason for failure. For example, the message may indicate that the range_optimizer_max_mem_size value was exceeded or type conversion occurred, either of which can preclude use of an index.  </dd></dl>
 <dl>
<dd>  &bull; For multiple-table deletes and updates, an error is produced with safe updates enabled only if any target table uses a table scan.  </dd></dl>
 Disabling mysql Auto-Reconnect  If the <code>mysql</code> client loses its connection to the server while sending a statement, it immediately and automatically tries to reconnect once to the server and send the statement again. However, even if <code>mysql</code> succeeds in reconnecting, your first connection has ended and all your previous session objects and settings are lost: temporary tables, the autocommit mode, and user-defined and session variables. Also, any current transaction rolls back. This behavior may be dangerous for you, as in the following example where the server was shut down and restarted between the first and second statements without you knowing it: <dl>
<dd>  <pre><code>mysql&gt; SET @a=1; Query OK, 0 rows affected (0.05 sec)
mysql&gt; INSERT INTO t VALUES(@a); ERROR 2006: MySQL server has gone away
No connection. Trying to reconnect...
Connection id: 1
Current database: test
Query OK, 1 row affected (1.30 sec)
mysql&gt; SELECT * FROM t; +------+
| a |
+------+
| NULL |
+------+
1 row in set (0.05 sec)
</code></pre>
  </dd></dl>
  The @a user variable has been lost with the connection, and after the reconnection it is undefined. If it is important to have <code>mysql</code> terminate with an error if the connection has been lost, you can start the <code>mysql</code> client with the <code>--skip-reconnect</code> option.  For more information about auto-reconnect and its effect on state information when a reconnection occurs, see Section 28.7.27, "C API Automatic Reconnection Control". mysql Client Parser Versus Server Parser  The <code>mysql</code> client uses a parser on the client side that is not a duplicate of the complete parser used by the <code>mysqld</code> server on the server side. This can lead to differences in treatment of certain constructs. Examples: <dl>
<dd>  &bull; The server parser treats strings delimited by &quot; characters as identifiers rather than as plain strings if the ANSI_QUOTES SQL mode is enabled.  The <code>mysql</code> client parser does not take the ANSI_QUOTES SQL mode into account. It treats strings delimited by &quot;, &#8216;, and ` characters the same, regardless of whether ANSI_QUOTES is enabled.  </dd></dl>
 <dl>
<dd>  &bull; Within /*! ... */ and /*+ ... */ comments, the <code>mysql</code> client parser interprets short-form <code>mysql</code> commands. The server parser does not interpret them because these commands have no meaning on the server side.  If it is desirable for <code>mysql</code> not to interpret short-form commands within comments, a partial workaround is to use the <code>--binary-mode</code> option, which causes all <code>mysql</code> commands to be disabled except \C and \d in noninteractive mode (for input piped to <code>mysql</code> or loaded using the source command).  </dd></dl>
  <h2>COPYRIGHT</h2>
   Copyright &#169; 1997, 2020, Oracle and/or its affiliates. All rights reserved.  This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License.  This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.  You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> <h2>NOTES</h2>
 <dl>
 <dd>  1. 4 MySQL Shell 8.0 (part of MySQL 8.0)  </dd>
<dl>
<dd>  <a rel="nofollow" href="https://dev.mysql.com/doc/mysql-shell/8.0/en/">https://dev.mysql.com/doc/mysql-shell/8.0/en/</a>  </dd></dl>
 </dl>
  <h2>SEE ALSO</h2>
 For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a>  <h2>AUTHOR</h2>
 Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>).  
</td>
<td> The current day of the week in three-letter format (Mon, Tue, ...) 
</td>
</tr>
<tr VALIGN=top>
<td> Y </td>
<td> The current year, four digits 
</td>
</tr>
<tr VALIGN=top>
<td> y </td>
<td> The current year, two digits 
</td>
</tr>
<tr VALIGN=top>
<td> _ </td>
<td> A space 
</td>
</tr>
<tr VALIGN=top>
<td> \ </td>
<td> A space (a space follows the backslash) 
</td>
</tr>
<tr VALIGN=top>
<td> &#8216; </td>
<td> Single quote 
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td> Double quote 
</td>
</tr>
<tr VALIGN=top>
<td> \ </td>
<td> A literal &nbsp;backslash character 
</td>
</tr>
<tr VALIGN=top>
<td> \fIx </td>
<td>  <p> <i>x</i>, for any "<i>x</i>" not listed above 
</td>
</tr>
 </table>
 </p>
<p> You can set the prompt in several ways: </p>
<dl>
<dd> <p> &bull; <i>Use an environment variable.</i> You can set the MYSQL_PS1 environment variable to a prompt string. For example: </p>
 </dd>
<dl>
<dd> <pre><code>shell&gt; export MYSQL_PS1=&quot;(\u@\h) [\d]&gt; &quot; 
</code></pre>
 </dd></dl>
</dl>
<dl>
<dd> <p> &bull; <i>Use a command-line option.</i> You can set the <code>--prompt</code> option on the command line to <code>mysql</code>. For example: </p>
 </dd>
<dl>
<dd> <pre><code>shell&gt; mysql --prompt=&quot;(\u@\h) [\d]&gt; &quot; (user [at] host) [database]&gt;
</code></pre>
 </dd></dl>
</dl>
<dl>
<dd> <p> &bull; <i>Use an option file.</i> You can set the prompt option in the [mysql] group of any MySQL option file, such as /etc/my.cnf or the .my.cnf file in your home directory. For example: </p>
 </dd>
<dl>
<dd> <pre><code>[mysql]
prompt=(\\u@\\h) [\\d]&gt;\\_
</code></pre>
 </dd></dl>
<p> In this example, note that the backslashes are doubled. If you set the prompt using the prompt option in an option file, it is advisable to double the backslashes when using the special prompt options. There is some overlap in the set of permissible prompt options and the set of special escape sequences that are recognized in option files. (The rules for escape sequences in option files are listed in Section 4.2.2.2, "Using Option Files".) The overlap may cause you problems if you use single backslashes. For example, \s is interpreted as a space rather than as the current seconds value. The following example shows how to define a prompt within an option file to include the current time in <i>hh:mm:ss</i>&gt; format: </p>
<dl>
<dd> <pre><code>[mysql]
prompt=&quot;\\r:\\m:\\s&gt; &quot;
</code></pre>
 </dd></dl>
</dl>
<dl>
<dd> <p> &bull; <i>Set the prompt interactively.</i> You can change your prompt interactively by using the prompt (or \R) command. For example: </p>
 </dd>
<dl>
<dd> <pre><code>mysql&gt; prompt (\u@\h) [\d]&gt;\_ PROMPT set to '(\u@\h) [\d]&gt;\_'
( user @ host ) [ database ]&gt;
( user @ host ) [ database ]&gt; prompt
Returning to default PROMPT of mysql&gt;
mysql&gt;
</code></pre>
 </dd></dl>
</dl>
<h2>MYSQL CLIENT LOGGING</h2>
<p> The <code>mysql</code> client can do these types of logging for statements executed interactively: </p>
<dl>
<dd> <p> &bull; On Unix, <code>mysql</code> writes the statements to a history file. By default, this file is named .mysql_history in your home directory. To specify a different file, set the value of the MYSQL_HISTFILE environment variable. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; On all platforms, if the <code>--syslog</code> option is given, <code>mysql</code> writes the statements to the system logging facility. On Unix, this is syslog; on Windows, it is the Windows Event Log. The destination where logged messages appear is system dependent. On Linux, the destination is often the /var/log/messages file. </p>
 </dd></dl>
<p> The following discussion describes characteristics that apply to all logging types and provides information specific to each logging type. </p>
<dl>
<dd> <p> &bull; How Logging Occurs </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Controlling the History File </p>
 </dd></dl>
<dl>
<dd> <p> &bull; syslog Logging Characteristics </p>
 </dd></dl>
<p> How Logging Occurs </p>
<p> For each enabled logging destination, statement logging occurs as follows: </p>
<dl>
<dd> <p> &bull; Statements are logged only when executed interactively. Statements are noninteractive, for example, when read from a file or a pipe. It is also possible to suppress statement logging by using the <code>--batch</code> or <code>--execute</code> option. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Statements are ignored and not logged if they match any pattern in the "ignore" list. This list is described later. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>mysql</code> logs each nonignored, nonempty statement line individually. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; If a nonignored statement spans multiple lines (not including the terminating delimiter), <code>mysql</code> concatenates the lines to form the complete statement, maps newlines to spaces, and logs the result, plus a delimiter. </p>
 </dd></dl>
<p> Consequently, an input statement that spans multiple lines can be logged twice. Consider this input: </p>
<dl>
<dd> <pre><code>mysql&gt; SELECT     -&gt; 'Today is'     -&gt; ,     -&gt; CURDATE()     -&gt; ; 
</code></pre>
 </dd></dl>
<p> In this case, <code>mysql</code> logs the "SELECT", "&#8216;Today is&#8217;", ",", "CURDATE()", and ";" lines as it reads them. It also logs the complete statement, after mapping SELECT\n&#8217;Today is&#8217;\n,\nCURDATE() to SELECT &#8216;Today is&#8217; , CURDATE(), plus a delimiter. Thus, these lines appear in logged output: </p>
<dl>
<dd> <pre><code>SELECT
'Today is'
,
CURDATE()
;
SELECT 'Today is' , CURDATE();
</code></pre>
 </dd></dl>
<p> <code>mysql</code> ignores for logging purposes statements that match any pattern in the "ignore" list. By default, the pattern list is &quot;*IDENTIFIED*:*PASSWORD*&quot;, to ignore statements that refer to passwords. Pattern matching is not case-sensitive. Within patterns, two characters are special: </p>
<dl>
<dd> <p> &bull; ? matches any single character. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; * matches any sequence of zero or more characters. </p>
 </dd></dl>
<p> To specify additional patterns, use the <code>--histignore</code> option or set the MYSQL_HISTIGNORE environment variable. (If both are specified, the option value takes precedence.) The value should be a list of one or more colon-separated patterns, which are appended to the default pattern list. </p>
<p> Patterns specified on the command line might need to be quoted or escaped to prevent your command interpreter from treating them specially. For example, to suppress logging for UPDATE and DELETE statements in addition to statements that refer to passwords, invoke <code>mysql</code> like this: </p>
<dl>
<dd> <pre><code>shell&gt; mysql --histignore=&quot;*UPDATE*:*DELETE*&quot; 
</code></pre>
 </dd></dl>
<p> Controlling the History File </p>
<p> The .mysql_history file should be protected with a restrictive access mode because sensitive information might be written to it, such as the text of SQL statements that contain passwords. See Section 6.1.2.1, "End-User Guidelines for Password Security". Statements in the file are accessible from the <code>mysql</code> client when the up-arrow key is used to recall the history. See Disabling Interactive History. </p>
<p> If you do not want to maintain a history file, first remove .mysql_history if it exists. Then use either of the following techniques to prevent it from being created again: </p>
<dl>
<dd> <p> &bull; Set the MYSQL_HISTFILE environment variable to /dev/null. To cause this setting to take effect each time you log in, put it in one of your shell&#8217;s startup files. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Create .mysql_history as a symbolic link to /dev/null; this need be done only once: </p>
 </dd>
<dl>
<dd> <pre><code>shell&gt; ln -s /dev/null $HOME/.mysql_history 
</code></pre>
 </dd></dl>
</dl>
<p> syslog Logging Characteristics </p>
<p> If the <code>--syslog</code> option is given, <code>mysql</code> writes interactive statements to the system logging facility. Message logging has the following characteristics. </p>
<p> Logging occurs at the "information" level. This corresponds to the LOG_INFO priority for syslog on Unix/Linux syslog capability and to EVENTLOG_INFORMATION_TYPE for the Windows Event Log. Consult your system documentation for configuration of your logging capability. </p>
<p> Message size is limited to 1024 bytes. </p>
<p> Messages consist of the identifier MysqlClient followed by these values: </p>
<dl>
<dd> <p> &bull; SYSTEM_USER </p>
<p> The operating system user name (login name) or -- if the user is unknown. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; MYSQL_USER </p>
<p> The MySQL user name (specified with the <code>--user</code> option) or -- if the user is unknown. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; CONNECTION_ID: </p>
<p> The client connection identifier. This is the same as the CONNECTION_ID() function value within the session. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; DB_SERVER </p>
<p> The server host or -- if the host is unknown. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; DB </p>
<p> The default database or -- if no database has been selected. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; QUERY </p>
<p> The text of the logged statement. </p>
 </dd></dl>
<p> Here is a sample of output generated on Linux by using <code>--syslog</code>. This output is formatted for readability; each logged message actually takes a single line. </p>
<dl>
<dd> <pre><code>Mar 7 12:39:25 myhost MysqlClient[20824]:
  SYSTEM_USER:'oscar', MYSQL_USER:'my_oscar', CONNECTION_ID:23,
  DB_SERVER:'127.0.0.1', DB:'--', QUERY:'USE test;'
Mar 7 12:39:28 myhost MysqlClient[20824]:
  SYSTEM_USER:'oscar', MYSQL_USER:'my_oscar', CONNECTION_ID:23,
  DB_SERVER:'127.0.0.1', DB:'test', QUERY:'SHOW TABLES;'
</code></pre>
 </dd></dl>
<h2>MYSQL CLIENT SERVER-SIDE HELP</h2>
<dl>
<dd> <pre><code>mysql&gt; help  search_string 
</code></pre>
 </dd></dl>
<p> If you provide an argument to the help command, <code>mysql</code> uses it as a search string to access server-side help from the contents of the MySQL Reference Manual. The proper operation of this command requires that the help tables in the mysql database be initialized with help topic information (see Section 5.1.14, "Server-Side Help Support"). </p>
<p> If there is no match for the search string, the search fails: </p>
<dl>
<dd> <pre><code>mysql&gt; help me Nothing found
Please try to run 'help contents' for a list of all accessible topics
</code></pre>
 </dd></dl>
<p> Use <code>help contents</code> to see a list of the help categories: </p>
<dl>
<dd> <pre><code>mysql&gt; help contents You asked for help about help category: &quot;Contents&quot;
For more information, type 'help &lt;item&gt;', where &lt;item&gt; is one of the
following categories:
   Account Management
   Administration
   Data Definition
   Data Manipulation
   Data Types
   Functions
   Functions and Modifiers for Use with GROUP BY
   Geographic Features
   Language Structure
   Plugins
   Storage Engines
   Stored Routines
   Table Maintenance
   Transactions
   Triggers
</code></pre>
 </dd></dl>
<p> If the search string matches multiple items, <code>mysql</code> shows a list of matching topics: </p>
<dl>
<dd> <pre><code>mysql&gt; help logs Many help items for your request exist.
To make a more specific request, please type 'help &lt;item&gt;',
where &lt;item&gt; is one of the following topics:
   SHOW
   SHOW BINARY LOGS
   SHOW ENGINE
   SHOW LOGS
</code></pre>
 </dd></dl>
<p> Use a topic as the search string to see the help entry for that topic: </p>
<dl>
<dd> <pre><code>mysql&gt; help show binary logs Name: 'SHOW BINARY LOGS'
Description:
Syntax:
SHOW BINARY LOGS
SHOW MASTER LOGS
Lists the binary log files on the server. This statement is used as
part of the procedure described in [purge-binary-logs], that shows how
to determine which logs can be purged.
mysql&gt; SHOW BINARY LOGS;
+---------------+-----------+-----------+
| Log_name | File_size | Encrypted |
+---------------+-----------+-----------+
| binlog.000015 | 724935 | Yes |
| binlog.000016 | 733481 | Yes |
+---------------+-----------+-----------+
</code></pre>
 </dd></dl>
<p> The search string can contain the wildcard characters % and _. These have the same meaning as for pattern-matching operations performed with the LIKE operator. For example, HELP rep% returns a list of topics that begin with rep: </p>
<dl>
<dd> <pre><code>mysql&gt; HELP rep% Many help items for your request exist.
To make a more specific request, please type 'help &lt;item&gt;',
where &lt;item&gt; is one of the following
topics:
   REPAIR TABLE
   REPEAT FUNCTION
   REPEAT LOOP
   REPLACE
   REPLACE FUNCTION
</code></pre>
 </dd></dl>
<h2>EXECUTING SQL STATEMENTS FROM A TEXT FILE</h2>
<p> The <code>mysql</code> client typically is used interactively, like this: </p>
<dl>
<dd> <pre><code>shell&gt; mysql  db_name 
</code></pre>
 </dd></dl>
<p> However, it is also possible to put your SQL statements in a file and then tell <code>mysql</code> to read its input from that file. To do so, create a text file <i>text_file</i> that contains the statements you wish to execute. Then invoke <code>mysql</code> as shown here: </p>
<dl>
<dd> <pre><code>shell&gt; mysql  db_name   &lt;  text_file 
</code></pre>
 </dd></dl>
<p> If you place a USE <i>db_name</i> statement as the first statement in the file, it is unnecessary to specify the database name on the command line: </p>
<dl>
<dd> <pre><code>shell&gt; mysql &lt; text_file 
</code></pre>
 </dd></dl>
<p> If you are already running <code>mysql</code>, you can execute an SQL script file using the source command or \. command: </p>
<dl>
<dd> <pre><code>mysql&gt; source  file_name mysql&gt; \.  file_name 
</code></pre>
 </dd></dl>
<p> Sometimes you may want your script to display progress information to the user. For this you can insert statements like this: </p>
<dl>
<dd> <pre><code>SELECT '&lt;info_to_display&gt;' AS ' ';
</code></pre>
 </dd></dl>
<p> The statement shown outputs &lt;info_to_display&gt;. </p>
<p> You can also invoke <code>mysql</code> with the <code>--verbose</code> option, which causes each statement to be displayed before the result that it produces. </p>
<p> <code>mysql</code> ignores Unicode byte order mark (BOM) characters at the beginning of input files. Previously, it read them and sent them to the server, resulting in a syntax error. Presence of a BOM does not cause <code>mysql</code> to change its default character set. To do that, invoke <code>mysql</code> with an option such as <code>--default-character-set=utf8</code>. </p>
<p> For more information about batch mode, see Section 3.5, "Using mysql in Batch Mode".  </p>
<h2>MYSQL CLIENT TIPS</h2>
<p> This section provides information about techniques for more effective use of <code>mysql</code> and about <code>mysql</code> operational behavior. </p>
<dl>
<dd> <p> &bull; Input-Line Editing </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Disabling Interactive History </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Unicode Support on Windows </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Displaying Query Results Vertically </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Using Safe-Updates Mode (--safe-updates) </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Disabling mysql Auto-Reconnect </p>
 </dd></dl>
<dl>
<dd> <p> &bull; mysql Client Parser Versus Server Parser </p>
 </dd></dl>
<p> Input-Line Editing </p>
<p> <code>mysql</code> supports input-line editing, which enables you to modify the current input line in place or recall previous input lines. For example, the left-arrow and right-arrow keys move horizontally within the current input line, and the up-arrow and down-arrow keys move up and down through the set of previously entered lines. Backspace deletes the character before the cursor and typing new characters enters them at the cursor position. To enter the line, press Enter. </p>
<p> On Windows, the editing key sequences are the same as supported for command editing in console windows. On Unix, the key sequences depend on the input library used to build <code>mysql</code> (for example, the libedit or readline library). </p>
<p> Documentation for the libedit and readline libraries is available online. To change the set of key sequences permitted by a given input library, define key bindings in the library startup file. This is a file in your home directory: .editrc for libedit and .inputrc for readline. </p>
<p> For example, in libedit, Control+W deletes everything before the current cursor position and Control+U deletes the entire line. In readline, Control+W deletes the word before the cursor and Control+U deletes everything before the current cursor position. If <code>mysql</code> was built using libedit, a user who prefers the readline behavior for these two keys can put the following lines in the .editrc file (creating the file if necessary): </p>
<dl>
<dd> <pre><code>bind &quot;^W&quot; ed-delete-prev-word
bind &quot;^U&quot; vi-kill-line-prev
</code></pre>
 </dd></dl>
<p> To see the current set of key bindings, temporarily put a line that says only bind at the end of .editrc. <code>mysql</code> will show the bindings when it starts. Disabling Interactive History </p>
<p> The up-arrow key enables you to recall input lines from current and previous sessions. In cases where a console is shared, this behavior may be unsuitable. <code>mysql</code> supports disabling the interactive history partially or fully, depending on the host platform. </p>
<p> On Windows, the history is stored in memory. Alt+F7 deletes all input lines stored in memory for the current history buffer. It also deletes the list of sequential numbers in front of the input lines displayed with F7 and recalled (by number) with F9. New input lines entered after you press Alt+F7 repopulate the current history buffer. Clearing the buffer does not prevent logging to the Windows Event Viewer, if the <code>--syslog</code> option was used to start <code>mysql</code>. Closing the console window also clears the current history buffer. </p>
<p> To disable interactive history on Unix, first delete the .mysql_history file, if it exists (previous entries are recalled otherwise). Then start <code>mysql</code> with the --histignore=&quot;*&quot; option to ignore all new input lines. To re-enable the recall (and logging) behavior, restart <code>mysql</code> without the option. </p>
<p> If you prevent the .mysql_history file from being created (see Controlling the History File) and use --histignore=&quot;*&quot; to start the <code>mysql</code> client, the interactive history recall facility is disabled fully. Alternatively, if you omit the <code>--histignore</code> option, you can recall the input lines entered during the current session. Unicode Support on Windows </p>
<p> Windows provides APIs based on UTF-16LE for reading from and writing to the console; the <code>mysql</code> client for Windows is able to use these APIs. The Windows installer creates an item in the MySQL menu named MySQL command line client - Unicode. This item invokes the <code>mysql</code> client with properties set to communicate through the console to the MySQL server using Unicode. </p>
<p> To take advantage of this support manually, run <code>mysql</code> within a console that uses a compatible Unicode font and set the default character set to a Unicode character set that is supported for communication with the server: </p>
<dl>
<dd> <p> 1. Open a console window. </p>
 </dd></dl>
<dl>
<dd> <p> 2. Go to the console window properties, select the font tab, and choose Lucida Console or some other compatible Unicode font. This is necessary because console windows start by default using a DOS raster font that is inadequate for Unicode. </p>
 </dd></dl>
<dl>
<dd> <p> 3. Execute <code>mysql.exe</code> with the <code>--default-character-set=utf8</code> (or utf8mb4) option. This option is necessary because utf16le is one of the character sets that cannot be used as the client character set. See the section called "Impermissible Client Character Sets". </p>
 </dd></dl>
<p> With those changes, <code>mysql</code> will use the Windows APIs to communicate with the console using UTF-16LE, and communicate with the server using UTF-8. (The menu item mentioned previously sets the font and character set as just described.) </p>
<p> To avoid those steps each time you run <code>mysql</code>, you can create a shortcut that invokes <code>mysql.exe</code>. The shortcut should set the console font to Lucida Console or some other compatible Unicode font, and pass the <code>--default-character-set=utf8</code> (or utf8mb4) option to <code>mysql.exe</code>. </p>
<p> Alternatively, create a shortcut that only sets the console font, and set the character set in the [mysql] group of your my.ini file: </p>
<dl>
<dd> <pre><code>[mysql]
default-character-set=utf8
</code></pre>
 </dd></dl>
<p> Displaying Query Results Vertically </p>
<p> Some query results are much more readable when displayed vertically, instead of in the usual horizontal table format. Queries can be displayed vertically by terminating the query with \G instead of a semicolon. For example, longer text values that include newlines often are much easier to read with vertical output: </p>
<dl>
<dd> <pre><code>mysql&gt; SELECT * FROM mails WHERE LENGTH(txt) &lt; 300 LIMIT 300,1\G *************************** 1. row ***************************
  msg_nro: 3068
     date: 2000-03-01 23:29:50
time_zone: +0200
mail_from: Jones
    reply: jones [at] example.com
  mail_to: &quot;John Smith&quot; &lt;smith [at] example.com&gt;
      sbj: UTF-8
      txt: &gt;&gt;&gt;&gt;&gt; &quot;John&quot; == John Smith writes:
John&gt; Hi. I think this is a good idea. Is anyone familiar
John&gt; with UTF-8 or Unicode? Otherwise, I'll put this on my
John&gt; TODO list and see what happens.
Yes, please do that.
Regards,
Jones
     file: inbox-jani-1
     hash: 190402944
1 row in set (0.09 sec)
</code></pre>
 </dd></dl>
<p> Using Safe-Updates Mode (--safe-updates) </p>
<p> For beginners, a useful startup option is <code>--safe-updates</code> (or <code>--i-am-a-dummy</code>, which has the same effect). Safe-updates mode is helpful for cases when you might have issued an UPDATE or DELETE statement but forgotten the WHERE clause indicating which rows to modify. Normally, such statements update or delete all rows in the table. With <code>--safe-updates</code>, you can modify rows only by specifying the key values that identify them, or a LIMIT clause, or both. This helps prevent accidents. Safe-updates mode also restricts SELECT statements that produce (or are estimated to produce) very large result sets. </p>
<p> The <code>--safe-updates</code> option causes <code>mysql</code> to execute the following statement when it connects to the MySQL server, to set the session values of the sql_safe_updates, sql_select_limit, and max_join_size system variables: </p>
<dl>
<dd> <pre><code>SET sql_safe_updates=1, sql_select_limit=1000, max_join_size=1000000;
</code></pre>
 </dd></dl>
<p> The SET statement affects statement processing as follows: </p>
<dl>
<dd> <p> &bull; Enabling sql_safe_updates causes UPDATE and DELETE statements to produce an error if they do not specify a key constraint in the WHERE clause, or provide a LIMIT clause, or both. For example: </p>
 </dd>
<dl>
<dd> <pre><code>UPDATE tbl_name  SET not_key_column = val  WHERE key_column = val ;
UPDATE tbl_name  SET not_key_column = val  LIMIT 1;
</code></pre>
 </dd></dl>
</dl>
<dl>
<dd> <p> &bull; Setting sql_select_limit to 1,000 causes the server to limit all SELECT result sets to 1,000 rows unless the statement includes a LIMIT clause. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Setting max_join_size to 1,000,000 causes multiple-table SELECT statements to produce an error if the server estimates it must examine more than 1,000,000 row combinations. </p>
 </dd></dl>
<p> To specify result set limits different from 1,000 and 1,000,000, you can override the defaults by using the <code>--select-limit</code> and <code>--max-join-size</code> options when you invoke <code>mysql</code>: </p>
<dl>
<dd> <pre><code>mysql --safe-updates --select-limit=500 --max-join-size=10000
</code></pre>
 </dd></dl>
<p> It is possible for UPDATE and DELETE statements to produce an error in safe-updates mode even with a key specified in the WHERE clause, if the optimizer decides not to use the index on the key column: </p>
<dl>
<dd> <p> &bull; Range access on the index cannot be used if memory usage exceeds that permitted by the range_optimizer_max_mem_size system variable. The optimizer then falls back to a table scan. See the section called "Limiting Memory Use for Range Optimization". </p>
 </dd></dl>
<dl>
<dd> <p> &bull; If key comparisons require type conversion, the index may not be used (see Section 8.3.1, "How MySQL Uses Indexes"). Suppose that an indexed string column c1 is compared to a numeric value using WHERE c1 = 2222. For such comparisons, the string value is converted to a number and the operands are compared numerically (see Section 12.2, "Type Conversion in Expression Evaluation"), preventing use of the index. If safe-updates mode is enabled, an error occurs. </p>
 </dd></dl>
<p> As of MySQL 8.0.13, safe-updates mode also includes these behaviors: </p>
<dl>
<dd> <p> &bull; EXPLAIN with UPDATE and DELETE statements does not produce safe-updates errors. This enables use of EXPLAIN plus SHOW WARNINGS to see why an index is not used, which can be helpful in cases such as when a range_optimizer_max_mem_size violation or type conversion occurs and the optimizer does not use an index even though a key column was specified in the WHERE clause. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; When a safe-updates error occurs, the error message includes the first diagnostic that was produced, to provide information about the reason for failure. For example, the message may indicate that the range_optimizer_max_mem_size value was exceeded or type conversion occurred, either of which can preclude use of an index. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; For multiple-table deletes and updates, an error is produced with safe updates enabled only if any target table uses a table scan. </p>
 </dd></dl>
<p> Disabling mysql Auto-Reconnect </p>
<p> If the <code>mysql</code> client loses its connection to the server while sending a statement, it immediately and automatically tries to reconnect once to the server and send the statement again. However, even if <code>mysql</code> succeeds in reconnecting, your first connection has ended and all your previous session objects and settings are lost: temporary tables, the autocommit mode, and user-defined and session variables. Also, any current transaction rolls back. This behavior may be dangerous for you, as in the following example where the server was shut down and restarted between the first and second statements without you knowing it: </p>
<dl>
<dd> <pre><code>mysql&gt; SET @a=1; Query OK, 0 rows affected (0.05 sec)
mysql&gt; INSERT INTO t VALUES(@a); ERROR 2006: MySQL server has gone away
No connection. Trying to reconnect...
Connection id: 1
Current database: test
Query OK, 1 row affected (1.30 sec)
mysql&gt; SELECT * FROM t; +------+
| a |
+------+
| NULL |
+------+
1 row in set (0.05 sec)
</code></pre>
 </dd></dl>
<p> The @a user variable has been lost with the connection, and after the reconnection it is undefined. If it is important to have <code>mysql</code> terminate with an error if the connection has been lost, you can start the <code>mysql</code> client with the <code>--skip-reconnect</code> option. </p>
<p> For more information about auto-reconnect and its effect on state information when a reconnection occurs, see Section 28.7.27, "C API Automatic Reconnection Control". mysql Client Parser Versus Server Parser </p>
<p> The <code>mysql</code> client uses a parser on the client side that is not a duplicate of the complete parser used by the <code>mysqld</code> server on the server side. This can lead to differences in treatment of certain constructs. Examples: </p>
<dl>
<dd> <p> &bull; The server parser treats strings delimited by &quot; characters as identifiers rather than as plain strings if the ANSI_QUOTES SQL mode is enabled. </p>
<p> The <code>mysql</code> client parser does not take the ANSI_QUOTES SQL mode into account. It treats strings delimited by &quot;, &#8216;, and ` characters the same, regardless of whether ANSI_QUOTES is enabled. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Within /*! ... */ and /*+ ... */ comments, the <code>mysql</code> client parser interprets short-form <code>mysql</code> commands. The server parser does not interpret them because these commands have no meaning on the server side. </p>
<p> If it is desirable for <code>mysql</code> not to interpret short-form commands within comments, a partial workaround is to use the <code>--binary-mode</code> option, which causes all <code>mysql</code> commands to be disabled except \C and \d in noninteractive mode (for input piped to <code>mysql</code> or loaded using the source command). </p>
 </dd></dl>
<h2>COPYRIGHT</h2>
<p> <br />
 </p>
<p> Copyright &#169; 1997, 2020, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>NOTES</h2>
<dl>
<dd> <p> 1. 4 MySQL Shell 8.0 (part of MySQL 8.0) </p>
 </dd>
<dl>
<dd> <p> <a rel="nofollow" href="https://dev.mysql.com/doc/mysql-shell/8.0/en/">https://dev.mysql.com/doc/mysql-shell/8.0/en/</a> </p>
 </dd></dl>
</dl>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a>  </p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
