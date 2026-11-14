---
title: "mysqlanalyze(1)"
name: "mysqlanalyze"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqlanalyze/"
description: "mysqlcheck – a table maintenance program"
---

<h2 class="name">NAME</h2>
<p> mysqlcheck &#8211; a table maintenance program </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqlcheck [</code><i>options</i><code>] [</code><i>db_name</i><code> [</code><i>tbl_name</i><code> &#8230;]]</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>mysqlcheck</code> client performs table maintenance: It checks, repairs, optimizes, or analyzes tables. </p>
<p> Each table is locked and therefore unavailable to other sessions while it is being processed, although for check operations, the table is locked with a READ lock only (see Section 13.3.6, &#8220;LOCK TABLES and UNLOCK TABLES Statements&#8221;, for more information about READ and WRITE locks). Table maintenance operations can be time-consuming, particularly for large tables. If you use the <code>&#8211;databases</code> or <code>&#8211;all-databases</code> option to process all tables in one or more databases, an invocation of <code>mysqlcheck</code> might take a long time. (This is also true for the MySQL upgrade procedure if it determines that table checking is needed because it processes tables the same way.) </p>
<p> <code>mysqlcheck</code> must be used when the <code>mysqld</code> server is running, which means that you do not have to stop the server to perform table maintenance. </p>
<p> <code>mysqlcheck</code> uses the SQL statements CHECK TABLE, REPAIR TABLE, ANALYZE TABLE, and OPTIMIZE TABLE in a convenient way for the user. It determines which statements to use for the operation you want to perform, and then sends the statements to the server to be executed. For details about which storage engines each statement works with, see the descriptions for those statements in Section 13.7.3, &#8220;Table Maintenance Statements&#8221;. </p>
<p> All storage engines do not necessarily support all four maintenance operations. In such cases, an error message is displayed. For example, if test.t is an MEMORY table, an attempt to check it produces this result: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlcheck test t</code>
test.t
note     : The storage engine for the table doesn't support check
</pre>
</dl>
<p> If <code>mysqlcheck</code> is unable to repair a table, see Section 2.11.13, &#8220;Rebuilding or Repairing Tables or Indexes&#8221; for manual table repair strategies. This will be the case, for example, for InnoDB tables, which can be checked with CHECK TABLE, but not repaired with REPAIR TABLE. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Caution</code> </font> </p>
<p> It is best to make a backup of a table before performing a table repair operation; under some circumstances the operation might cause data loss. Possible causes include but are not limited to file system errors. </p>
</dl>
<p> There are three general ways to invoke <code>mysqlcheck</code>: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; mysqlcheck[options] db_name[tbl_name...] shell &gt; mysqlcheck[options]-- databases db_name... shell &gt; mysqlcheck[options]-- all - databases
</code></pre>
</dl>
<p> If you do not name any tables following <i>db_name</i> or if you use the <code>&#8211;databases</code> or <code>&#8211;all-databases</code> option, entire databases are checked. </p>
<p> <code>mysqlcheck</code> has a special feature compared to other client programs. The default behavior of checking tables (<code>&#8211;check</code>) can be changed by renaming the binary. If you want to have a tool that repairs tables by default, you should just make a copy of <code>mysqlcheck</code> named <code>mysqlrepair</code>, or make a symbolic link to <code>mysqlcheck</code> named <code>mysqlrepair</code>. If you invoke <code>mysqlrepair</code>, it repairs tables. </p>
<p> The names shown in the following table can be used to change <code>mysqlcheck</code> default behavior. </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Command </code></td>
<td><code> Meaning </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>mysqlrepair</code> </td>
<td> The default option is <code>&#8211;repair</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>mysqlanalyze</code> </td>
<td> The default option is <code>&#8211;analyze</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>mysqloptimize</code> </td>
<td> The default option is <code>&#8211;optimize</code>
</td>
</tr>
</table>
<p> <code>mysqlcheck</code> supports the following options, which can be specified on the command line or in the [mysqlcheck] and [client] groups of an option file. For information about option files used by MySQL programs, see Section 4.2.2.2, &#8220;Using Option Files&#8221;. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;all-databases</code>, <code>-A</code> </p>
<p> Check all tables in all databases. This is the same as using the <code>&#8211;databases</code> option and naming all the databases on the command line, except that the INFORMATION_SCHEMA and performance_schema databases are not checked. They can be checked by explicitly naming them with the <code>&#8211;databases</code> option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;all-in-1</code>, <code>-1</code> </p>
<p> Instead of issuing a statement for each table, execute a single statement for each database that names all the tables from that database to be processed.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;analyze</code>, <code>-a</code> </p>
<p> Analyze the tables.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;auto-repair</code> </p>
<p> If a checked table is corrupted, automatically fix it. Any necessary repairs are done after all tables have been checked.</dl>
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
<dd> &bull; <code>&#8211;check</code>, <code>-c</code> </p>
<p> Check the tables for errors. This is the default operation.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;check-only-changed</code>, <code>-C</code> </p>
<p> Check only tables that have changed since the last check or that have not been closed properly.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;check-upgrade</code>, <code>-g</code> </p>
<p> Invoke CHECK TABLE with the FOR UPGRADE option to check tables for incompatibilities with the current version of the server.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;compress</code> </p>
<p> Compress all information sent between the client and the server if possible. See Section 4.2.6, &#8220;Connection Compression Control&#8221;. </p>
<p> As of MySQL 8.0.18, this option is deprecated. It will be removed in a future MySQL version. See the section called &#8220;Legacy Connection Compression Configuration&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;compression-algorithms=</code><i>value</i> The permitted compression algorithms for connections to the server. The available algorithms are the same as for the protocol_compression_algorithms system variable. The default value is uncompressed. </p>
<p> For more information, see Section 4.2.6, &#8220;Connection Compression Control&#8221;. </p>
<p> This option was added in MySQL 8.0.18.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;databases</code>, <code>-B</code> </p>
<p> Process all tables in the named databases. Normally, <code>mysqlcheck</code> treats the first name argument on the command line as a database name and any following names as table names. With this option, it treats all name arguments as database names.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug[=</code><i>debug_options</i><code>]</code>, <code>-# [</code><i>debug_options</i><code>]</code> </p>
<p> Write a debugging log. A typical <i>debug_options</i> string is d:t:o,<i>file_name</i>. The default is d:t:o. </p>
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
<p> Read not only the usual option groups, but also groups with the usual names and a suffix of <i>str</i>. For example, <code>mysqlcheck</code> normally reads the [client] and [mysqlcheck] groups. If the <code>&#8211;defaults-group-suffix=_other</code> option is given, <code>mysqlcheck</code> also reads the [client_other] and [mysqlcheck_other] groups. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;extended</code>, <code>-e</code> </p>
<p> If you are using this option to check tables, it ensures that they are 100% consistent but takes a long time. </p>
<p> If you are using this option to repair tables, it runs an extended repair that may not only take a long time to execute, but may produce a lot of garbage rows also!</dl>
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
<dd> &bull; <code>&#8211;fast</code>, <code>-F</code> </p>
<p> Check only tables that have not been closed properly.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;force</code>, <code>-f</code> </p>
<p> Continue even if an SQL error occurs.</dl>
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
<dd> &bull; <code>&#8211;medium-check</code>, <code>-m</code> </p>
<p> Do a check that is faster than an <code>&#8211;extended</code> operation. This finds only 99.99% of all errors, which should be good enough in most cases.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-defaults</code> </p>
<p> Do not read any option files. If program startup fails due to reading unknown options from an option file, <code>&#8211;no-defaults</code> can be used to prevent them from being read. </p>
<p> The exception is that the .mylogin.cnf file, if it exists, is read in all cases. This permits passwords to be specified in a safer way than on the command line even when <code>&#8211;no-defaults</code> is used. (.mylogin.cnf is created by the <code>mysql_config_editor</code> utility. See <code><a href="/docs/linux/man/1-mysql_config_editor/">mysql_config_editor</a></code>(1).) </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;optimize</code>, <code>-o</code> </p>
<p> Optimize the tables.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;password[=</code><i>password</i><code>]</code>, <code>-p[</code><i>password</i><code>]</code> </p>
<p> The password of the MySQL account used for connecting to the server. The password value is optional. If not given, <code>mysqlcheck</code> prompts for one. If given, there must be <i>no space</i> between <code>&#8211;password=</code> or <code>-p</code> and the password following it. If no password option is specified, the default is to send no password. </p>
<p> Specifying a password on the command line should be considered insecure. To avoid giving the password on the command line, use an option file. See Section 6.1.2.1, &#8220;End-User Guidelines for Password Security&#8221;. </p>
<p> To explicitly specify that there is no password and that <code>mysqlcheck</code> should not prompt for one, use the <code>&#8211;skip-password</code> option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;pipe</code>, <code>-W</code> </p>
<p> On Windows, connect to the server using a named pipe. This option applies only if the server was started with the named_pipe system variable enabled to support named-pipe connections. In addition, the user making the connection must be a member of the Windows group specified by the named_pipe_full_access_group system variable.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;plugin-dir=</code><i>dir_name</i> </p>
<p> The directory in which to look for plugins. Specify this option if the <code>&#8211;default-auth</code> option is used to specify an authentication plugin but <code>mysqlcheck</code> does not find it. See Section 6.2.17, &#8220;Pluggable Authentication&#8221;.</dl>
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
<dd> &bull; <code>&#8211;quick</code>, <code>-q</code> </p>
<p> If you are using this option to check tables, it prevents the check from scanning the rows to check for incorrect links. This is the fastest check method. </p>
<p> If you are using this option to repair tables, it tries to repair only the index tree. This is the fastest repair method.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;repair</code>, <code>-r</code> </p>
<p> Perform a repair that can fix almost anything except unique keys that are not unique.</dl>
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
<p> Silent mode. Print only error messages.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;skip-database=</code><i>db_name</i> </p>
<p> Do not include the named database (case-sensitive) in the operations performed by <code>mysqlcheck</code>.</dl>
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
<dd> &bull; <code>&#8211;tables</code> </p>
<p> Override the <code>&#8211;databases</code> or <code>-B</code> option. All name arguments following the option are regarded as table names.</dl>
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
<dd> &bull; <code>&#8211;use-frm</code> </p>
<p> For repair operations on MyISAM tables, get the table structure from the data dictionary so that the table can be repaired even if the .MYI header is corrupted.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;user=</code><i>user_name</i>, <code>-u </code><i>user_name</i> </p>
<p> The user name of the MySQL account to use for connecting to the server.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;verbose</code>, <code>-v</code> </p>
<p> Verbose mode. Print information about the various stages of program operation.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code>, <code>-V</code> </p>
<p> Display version information and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;write-binlog</code> </p>
<p> This option is enabled by default, so that ANALYZE TABLE, OPTIMIZE TABLE, and REPAIR TABLE statements generated by <code>mysqlcheck</code> are written to the binary log. Use <code>&#8211;skip-write-binlog</code> to cause NO_WRITE_TO_BINLOG to be added to the statements so that they are not logged. Use the <code>&#8211;skip-write-binlog</code> when these statements should not be sent to replication slaves or run when using the binary logs for recovery from backup.</dl>
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
