---
title: "mysql_upgrade(1)"
name: "mysql_upgrade"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysql_upgrade/"
description: "mysql_upgrade – check and upgrade MySQL tables"
---

<h2 class="name">NAME</h2>
<p> mysql_upgrade &#8211; check and upgrade MySQL tables </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysql_upgrade [</code><i>options</i><code>]</code></dl>
<h2>DESCRIPTION</h2>
<dl>
<dt>
<dd>
<dd> <font SIZE="+1"> <code>Note</code> </font></p>
<dd>
<dd>As of MySQL 8.0.16, the MySQL server performs the upgrade tasks previously handled by <code>mysql_upgrade</code> (for details, see Section 2.11.3, &#8220;What the MySQL Upgrade Process Upgrades&#8221;). Consequently, <code>mysql_upgrade</code> is unneeded and is deprecated as of that version, and will be removed in a future MySQL version. Because <code>mysql_upgrade</code> no longer performs upgrade tasks, it exits with status 0 unconditionally. </p>
</dl>
<p> Each time you upgrade MySQL, you should execute <code>mysql_upgrade</code>, which looks for incompatibilities with the upgraded MySQL server: </p>
<dl>
<dt>
<dd> &bull; It upgrades the system tables in the mysql schema so that you can take advantage of new privileges or capabilities that might have been added.</dl>
<dl>
<dt>
<dd> &bull; It upgrades the Performance Schema, INFORMATION_SCHEMA, and sys schema.</dl>
<dl>
<dt>
<dd> &bull; It examines user schemas.</dl>
<p> If <code>mysql_upgrade</code> finds that a table has a possible incompatibility, it performs a table check and, if problems are found, attempts a table repair. If the table cannot be repaired, see Section 2.11.13, &#8220;Rebuilding or Repairing Tables or Indexes&#8221; for manual table repair strategies. </p>
<p> <code>mysql_upgrade</code> communicates directly with the MySQL server, sending it the SQL statements required to perform an upgrade. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Caution</code> </font> </p>
<p> You should always back up your current MySQL installation <i>before</i> performing an upgrade. See Section 7.2, &#8220;Database Backup Methods&#8221;. </p>
<p> Some upgrade incompatibilities may require special handling <i>before</i> upgrading your MySQL installation and running <code>mysql_upgrade</code>. See Section 2.11, &#8220;Upgrading MySQL&#8221;, for instructions on determining whether any such incompatibilities apply to your installation and how to handle them. </p>
</dl>
<p> Use <code>mysql_upgrade</code> like this: </p>
<dl>
<dt>
<dd> 1. Ensure that the server is running.</dl>
<dl>
<dt>
<dd> 2. Invoke <code>mysql_upgrade</code> to upgrade the system tables in the mysql schema and check and repair tables in other schemas: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql_upgrade [</code><i>options</i><code>]</code>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> 3. Stop the server and restart it so that any system table changes take effect.</dl>
<p> If you have multiple MySQL server instances to upgrade, invoke <code>mysql_upgrade</code> with connection parameters appropriate for connecting to each of the desired servers. For example, with servers running on the local host on parts 3306 through 3308, upgrade each of them by connecting to the appropriate port: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; mysql_upgrade-- protocol = tcp - P 3306 [other_options] shell &gt; mysql_upgrade-- protocol = tcp - P 3307 [other_options] shell &gt; mysql_upgrade-- protocol = tcp - P 3308 [other_options]
</code></pre>
</dl>
<p> For local host connections on Unix, the <code>&#8211;protocol=tcp</code> option forces a connection using TCP/IP rather than the Unix socket file. </p>
<p> By default, <code>mysql_upgrade</code> runs as the MySQL root user. If the root password is expired when you run <code>mysql_upgrade</code>, you will see a message that your password is expired and that <code>mysql_upgrade</code> failed as a result. To correct this, reset the root password to unexpire it and run <code>mysql_upgrade</code> again. First, connect to the server as root: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql -u root -p</code>
Enter password: <code>****</code>  &lt;- enter root password here
</pre>
</dl>
<p> Reset the password using ALTER USER: </p>
<dl>
<dt>
<dd>
<pre>
mysql&gt; <code>ALTER USER USER() IDENTIFIED BY '</code><i>root-password</i><code>';</code>
</pre>
</dl>
<p> Then exit <code>mysql</code> and run <code>mysql_upgrade</code> again: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql_upgrade [</code><i>options</i><code>]</code>
</pre>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> If you run the server with the disabled_storage_engines system variable set to disable certain storage engines (for example, MyISAM), <code>mysql_upgrade</code> might fail with an error like this: </p>
<dl>
<dt>
<dd>
<pre>
mysql_upgrade: [ERROR] 3161: Storage engine MyISAM is disabled
(Table creation is disallowed).
</pre>
</dl>
<p> To handle this, restart the server with disabled_storage_engines disabled. Then you should be able to run <code>mysql_upgrade</code> successfully. After that, restart the server with disabled_storage_engines set to its original value. </p>
</dl>
<p> Unless invoked with the <code>&#8211;upgrade-system-tables</code> option, <code>mysql_upgrade</code> processes all tables in all user schemas as necessary. Table checking might take a long time to complete. Each table is locked and therefore unavailable to other sessions while it is being processed. Check and repair operations can be time-consuming, particularly for large tables. Table checking uses the FOR UPGRADE option of the CHECK TABLE statement. For details about what this option entails, see Section 13.7.3.2, &#8220;CHECK TABLE Statement&#8221;. </p>
<p> <code>mysql_upgrade</code> marks all checked and repaired tables with the current MySQL version number. This ensures that the next time you run <code>mysql_upgrade</code> with the same version of the server, it can be determined whether there is any need to check or repair a given table again. </p>
<p> <code>mysql_upgrade</code> saves the MySQL version number in a file named mysql_upgrade_info in the data directory. This is used to quickly check whether all tables have been checked for this release so that table-checking can be skipped. To ignore this file and perform the check regardless, use the <code>&#8211;force</code> option. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> The mysql_upgrade_info file is deprecated and will be removed in a future MySQL version. </p>
</dl>
<p> <code>mysql_upgrade</code> checks mysql.user system table rows and, for any row with an empty plugin column, sets that column to &#8216;mysql_native_password&#8217; if the credentials use a hash format compatible with that plugin. Rows with a pre-4.1 password hash must be upgraded manually. </p>
<p> <code>mysql_upgrade</code> does not upgrade the contents of the time zone tables or help tables. For upgrade instructions, see Section 5.1.13, &#8220;MySQL Server Time Zone Support&#8221;, and Section 5.1.14, &#8220;Server-Side Help Support&#8221;. </p>
<p> Unless invoked with the <code>&#8211;skip-sys-schema</code> option, <code>mysql_upgrade</code> installs the sys schema if it is not installed, and upgrades it to the current version otherwise. An error occurs if a sys schema exists but has no version view, on the assumption that its absence indicates a user-created schema: </p>
<dl>
<dt>
<dd>
<pre>
A sys schema exists with no sys.version view. If
you have a user created sys schema, this must be renamed for the
upgrade to succeed.
</pre>
</dl>
<p> To upgrade in this case, remove or rename the existing sys schema first. </p>
<p> <code>mysql_upgrade</code> supports the following options, which can be specified on the command line or in the [mysql_upgrade] and [client] groups of an option file. For information about option files used by MySQL programs, see Section 4.2.2.2, &#8220;Using Option Files&#8221;. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code> </p>
<p> Display a short help message and exit.</dl>
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
<dd> &bull; <code>&#8211;debug[=</code><i>debug_options</i><code>]</code>, <code>-# [</code><i>debug_options</i><code>]</code> </p>
<p> Write a debugging log. A typical <i>debug_options</i> string is d:t:o,<i>file_name</i>. The default is d:t:O,/tmp/mysql_upgrade.trace.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug-check</code> </p>
<p> Print some debugging information when the program exits.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug-info</code>, <code>-T</code> </p>
<p> Print debugging information and memory and CPU usage statistics when the program exits.</dl>
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
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;defaults-group-suffix=</code><i>str</i> </p>
<p> Read not only the usual option groups, but also groups with the usual names and a suffix of <i>str</i>. For example, <code>mysql_upgrade</code> normally reads the [client] and [mysql_upgrade] groups. If the <code>&#8211;defaults-group-suffix=_other</code> option is given, <code>mysql_upgrade</code> also reads the [client_other] and [mysql_upgrade_other] groups. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;force</code> </p>
<p> Ignore the mysql_upgrade_info file and force execution even if <code>mysql_upgrade</code> has already been executed for the current version of MySQL.</dl>
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
<dd> &bull; <code>&#8211;max-allowed-packet=</code><i>value</i> </p>
<p> The maximum size of the buffer for client/server communication. The default value is 24MB. The minimum and maximum values are 4KB and 2GB.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;net-buffer-length=</code><i>value</i> </p>
<p> The initial size of the buffer for client/server communication. The default value is 1MB − 1KB. The minimum and maximum values are 4KB and 16MB.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-defaults</code> </p>
<p> Do not read any option files. If program startup fails due to reading unknown options from an option file, <code>&#8211;no-defaults</code> can be used to prevent them from being read. </p>
<p> The exception is that the .mylogin.cnf file, if it exists, is read in all cases. This permits passwords to be specified in a safer way than on the command line even when <code>&#8211;no-defaults</code> is used. (.mylogin.cnf is created by the <code>mysql_config_editor</code> utility. See <code><a href="/docs/linux/man/1-mysql_config_editor/">mysql_config_editor</a></code>(1).) </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;password[=</code><i>password</i><code>]</code>, <code>-p[</code><i>password</i><code>]</code> </p>
<p> The password of the MySQL account used for connecting to the server. The password value is optional. If not given, <code>mysql_upgrade</code> prompts for one. If given, there must be <i>no space</i> between <code>&#8211;password=</code> or <code>-p</code> and the password following it. If no password option is specified, the default is to send no password. </p>
<p> Specifying a password on the command line should be considered insecure. To avoid giving the password on the command line, use an option file. See Section 6.1.2.1, &#8220;End-User Guidelines for Password Security&#8221;. </p>
<p> To explicitly specify that there is no password and that <code>mysql_upgrade</code> should not prompt for one, use the <code>&#8211;skip-password</code> option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;pipe</code>, <code>-W</code> </p>
<p> On Windows, connect to the server using a named pipe. This option applies only if the server was started with the named_pipe system variable enabled to support named-pipe connections. In addition, the user making the connection must be a member of the Windows group specified by the named_pipe_full_access_group system variable.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;plugin-dir=</code><i>dir_name</i> </p>
<p> The directory in which to look for plugins. Specify this option if the <code>&#8211;default-auth</code> option is used to specify an authentication plugin but <code>mysql_upgrade</code> does not find it. See Section 6.2.17, &#8220;Pluggable Authentication&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;port=</code><i>port_num</i>, <code>-P </code><i>port_num</i> </p>
<p> For TCP/IP connections, the port number to use.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;print-defaults</code> </p>
<p> Print the program name and all options that it gets from option files.</dl>
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
<dd> &bull; <code>&#8211;shared-memory-base-name=</code><i>name</i> </p>
<p> On Windows, the shared-memory name to use for connections made using shared memory to a local server. The default value is MYSQL. The shared-memory name is case-sensitive. </p>
<p> This option applies only if the server was started with the shared_memory system variable enabled to support shared-memory connections.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;skip-sys-schema</code> </p>
<p> By default, <code>mysql_upgrade</code> installs the sys schema if it is not installed, and upgrades it to the current version otherwise. The <code>&#8211;skip-sys-schema</code> option suppresses this behavior.</dl>
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
<dd> &bull; <code>&#8211;upgrade-system-tables</code>, <code>-s</code> </p>
<p> Upgrade only the system tables in the mysql schema, do not upgrade user schemas.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;user=</code><i>user_name</i>, <code>-u </code><i>user_name</i> </p>
<p> The user name of the MySQL account to use for connecting to the server. The default user name is root.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;verbose</code> </p>
<p> Verbose mode. Print more information about what the program does.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version-check</code>, <code>-k</code> </p>
<p> Check the version of the server to which <code>mysql_upgrade</code> is connecting to verify that it is the same as the version for which <code>mysql_upgrade</code> was built. If not, <code>mysql_upgrade</code> exits. This option is enabled by default; to disable the check, use <code>&#8211;skip-version-check</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;write-binlog</code> </p>
<p> By default, binary logging by <code>mysql_upgrade</code> is disabled. Invoke the program with <code>&#8211;write-binlog</code> if you want its actions to be written to the binary log. </p>
<p> When the server is running with global transaction identifiers (GTIDs) enabled (gtid_mode=ON), do not enable binary logging by <code>mysql_upgrade</code>.</dl>
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
