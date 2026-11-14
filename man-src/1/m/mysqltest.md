---
title: "mysqltest(1)"
name: "mysqltest"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqltest/"
description: "mysqltest – program to run test cases mysqltest_embedded – program to run embedded test cases"
---

<h2 class="name">NAME</h2>
<p> mysqltest &#8211; program to run test cases<br />
 mysqltest_embedded &#8211; program to run embedded test cases </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqltest [</code><i>options</i><code>] [</code><i>db_name</i><code>]</code></p>
<dt> <code>mysqltest_embedded [</code><i>options</i><code>] [</code><i>db_name</i><code>]</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>mysqltest</code> program runs a test case against a MariaDB server and optionally compares the output with a result file. This program reads input written in a special test language. Typically, you invoke <code>mysqltest</code> via <code>mysql-test-run.pl</code> rather than invoking it directly. </p>
<p> <code>mysqltest_embedded</code> is similar but is built with support for the libmysqld embedded server. </p>
<p> Features of <code>mysqltest</code>: </p>
<dl>
<dt>
<dd> &bull; Can send SQL statements to MariaDB servers for execution</dl>
<dl>
<dt>
<dd> &bull; Can execute external shell commands</dl>
<dl>
<dt>
<dd> &bull; Can test whether the result from an SQL statement or shell command is as expected</dl>
<dl>
<dt>
<dd> &bull; Can connect to one or more standalone <code>mysqld</code> servers and switch between connections</dl>
<dl>
<dt>
<dd> &bull; Can connect to an embedded server (libmysqld), if MariaDB is compiled with support for libmysqld. (In this case, the executable is named <code>mysqltest_embedded</code> rather than <code>mysqltest</code>.)</dl>
<p> By default, <code>mysqltest</code> reads the test case on the standard input. To run <code>mysqltest</code> this way, you normally invoke it like this: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; mysqltest[options][db_name] &lt; test_file
</code></pre>
</dl>
<p> You can also name the test case file with a <code>&#8211;test-file=</code><i>file_name</i> option. </p>
<p> The exit value from <code>mysqltest</code> is 0 for success, 1 for failure, and 62 if it skips the test case (for example, if after checking some preconditions it decides not to run the test). </p>
<p> <code>mysqltest</code> supports the following options: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;basedir=</code><i>dir_name</i>, <code>-b </code><i>dir_name</i> </p>
<p> The base directory for tests.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;character-sets-dir=</code><i>path</i> </p>
<p> The directory where character sets are installed.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;compress</code>, <code>-C</code> </p>
<p> Compress all information sent between the client and the server if both support compression.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;connect-timeout=</code><i>num</i> </p>
<p> This can be used to set the MYSQL_OPT_CONNECT_TIMEOUT parameter of mysql_options to change the number of seconds before an unsuccessful connection attempt times out.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;continue-on-error</code> </p>
<p> Continue test even if we got an error. This is mostly useful when testing a storage engine to see what from a test file it can execute, or to find all syntax errors in a newly created big test file.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;cursor-protocol</code> </p>
<p> Use cursors for prepared statements.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;database=</code><i>db_name</i>, <code>-D </code><i>db_name</i> </p>
<p> The default database to use.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug[=</code><i>debug_options</i><code>]</code>, <code>-#[</code><i>debug_options</i><code>]</code> </p>
<p> Write a debugging log if MariaDB is built with debugging support. The default <i>debug_options</i> value is &#8216;d:t:S:i:O,/tmp/mysqltest.trace&#8217;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug-check</code> </p>
<p> Print some debugging information when the program exits.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug-info</code> </p>
<p> Print debugging information and memory and CPU usage statistics when the program exits.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;host=</code><i>host_name</i>, <code>-h </code><i>host_name</i> </p>
<p> Connect to the MariaDB server on the given host.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;logdir=</code><i>dir_name</i> </p>
<p> The directory to use for log files.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;mark-progress</code> </p>
<p> Write the line number and elapsed time to <i>test_file</i>.progress.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;max-connect-retries=</code><i>num</i> </p>
<p> The maximum number of connection attempts when connecting to server.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;max-connections=</code><i>num</i> </p>
<p> The maximum number of simultaneous server connections per client (that is, per test). If not set, the maximum is 128. Minimum allowed limit is 8, maximum is 5120.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-defaults</code> </p>
<p> Do not read default options from any option files. If used, this must be the first option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;non-blocking-api</code> </p>
<p> Use the non-blocking client API for communication.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;overlay-dir=</code><i>dir_name</i> </p>
<p> Overlay directory.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;password[=</code><i>password</i><code>]</code>, <code>-p[</code><i>password</i><code>]</code> </p>
<p> The password to use when connecting to the server. If you use the short option form (<code>-p</code>), you <i>cannot</i> have a space between the option and the password. If you omit the <i>password</i> value following the <code>&#8211;password</code> or <code>-p</code> option on the command line, you are prompted for one.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;plugin-dir=</code><i>dir_name</i> </p>
<p> Directory for client-side plugins.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;port=</code><i>port_num</i>, <code>-P </code><i>port_num</i> </p>
<p> The TCP/IP port number to use for the connection or 0 for default to, in order of preference, my.cnf, $MYSQL_TCP_PORT, /etc/services, built-in default (3306).</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;prologue=</code><i>name</i> </p>
<p> Include the contents of the given file before processing the contents of the test file. The included file should have the same format as other <code>mysqltest</code> test files. This option has the same effect as putting a &#8211;source <i>file_name</i> command as the first line of the test file.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;protocol={TCP|SOCKET|PIPE|MEMORY}</code> </p>
<p> The connection protocol to use for connecting to the server. It is useful when the other connection parameters normally would cause a protocol to be used other than the one you want.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;ps-protocol</code> </p>
<p> Use the prepared-statement protocol for communication.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;quiet</code> </p>
<p> Suppress all normal output. This is a synonym for <code>&#8211;silent</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;record</code>, <code>-r</code> </p>
<p> Record the output that results from running the test file into the file named by the <code>&#8211;result-file</code> option, if that option is given. It is an error to use this option without also using <code>&#8211;result-file</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;result-file=</code><i>file_name</i>, <code>-R </code><i>file_name</i> </p>
<p> This option specifies the file for test case expected results. <code>&#8211;result-file</code>, together with <code>&#8211;record</code>, determines how <code>mysqltest</code> treats the test actual and expected results for a test case: </p>
<dl>
<dt>
<dd> &bull; If the test produces no results, <code>mysqltest</code> exits with an error message to that effect, unless <code>&#8211;result-file</code> is given and the named file is an empty file.</dl>
<dl>
<dt>
<dd> &bull; Otherwise, if <code>&#8211;result-file</code> is not given, <code>mysqltest</code> sends test results to the standard output.</dl>
<dl>
<dt>
<dd> &bull; With <code>&#8211;result-file</code> but not <code>&#8211;record</code>, <code>mysqltest</code> reads the expected results from the given file and compares them with the actual results. If the results do not match, <code>mysqltest</code> writes a .reject file in the same directory as the result file, outputs a diff of the two files, and exits with an error.</dl>
<dl>
<dt>
<dd> &bull; With both <code>&#8211;result-file</code> and <code>&#8211;record</code>, <code>mysqltest</code> updates the given file by writing the actual test results to it.</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;result-format-version=</code><i>#</i> </p>
<p> Version of the result file format to use.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;server-arg=</code><i>value</i>, <code>-A </code><i>value</i> </p>
<p> Pass the argument as an argument to the embedded server. For example, <code>&#8211;server-arg=&#8211;tmpdir=/tmp</code> or <code>&#8211;server-arg=&#8211;core</code>. Up to 64 arguments can be given.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;server-file=</code><i>file_name</i>, <code>-F </code><i>file_name</i> </p>
<p> Read arguments for the embedded server from the given file. The file should contain one argument per line.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;silent</code>, <code>-s</code> </p>
<p> Suppress all normal output.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;sleep=</code><i>num</i>, <code>-T </code><i>num</i> </p>
<p> Cause all sleep commands in the test case file to sleep <i>num</i> seconds. This option does not affect real_sleep commands. </p>
<p> An option value of 0 can be used, which effectively disables sleep commands in the test case.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;socket=</code><i>path</i>, <code>-S </code><i>path</i> </p>
<p> The socket file to use when connecting to localhost (which is the default host).</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;sp-protocol</code> </p>
<p> Execute DML statements within a stored procedure. For every DML statement, <code>mysqltest</code> creates and invokes a stored procedure that executes the statement rather than executing the statement directly.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;ssl</code> </p>
<p> Enable SSL for connection (automatically enabled with other flags). Disable with <code>&#8211;skip-ssl</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;ssl-ca=</code><i>name</i> </p>
<p> CA file in PEM format (check OpenSSL docs, implies <code>&#8211;ssl</code>).</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;ssl-capath=</code><i>name</i> </p>
<p> CA directory (check OpenSSL docs, implies <code>&#8211;ssl</code>).</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;ssl-cert=</code><i>name</i> </p>
<p> X509 cert in PEM format (check OpenSSL docs, implies <code>&#8211;ssl</code>).</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;ssl-cipher=</code><i>name</i> </p>
<p> SSL cipher to use (check OpenSSL docs, implies <code>&#8211;ssl</code>).</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;ssl-key=</code><i>name</i> </p>
<p> X509 key in PEM format (check OpenSSL docs, implies <code>&#8211;ssl</code>).</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;ssl-crl=</code><i>name</i> </p>
<p> Certificate revocation list (check OpenSSL docs, implies <code>&#8211;ssl</code>).</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;ssl-crlpath=</code><i>name</i> </p>
<p> Certificate revocation list path (check OpenSSL docs, implies <code>&#8211;ssl</code>).</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;ssl-verify-server-cert</code> </p>
<p> Verify server&#8217;s &quot;Common Name&quot; in its cert against hostname used when connecting. This option is disabled by default.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;suite-dir=</code><i>dir_name</i> </p>
<p> Suite directory.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;tail-lines=</code><i>nn</i> </p>
<p> Specify how many lines of the result to include in the output if the test fails because an SQL statement fails. The default is 0, meaning no lines of result printed.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;test-file=</code><i>file_name</i>, <code>-x </code><i>file_name</i> </p>
<p> Read test input from this file. The default is to read from the standard input.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;timer-file=</code><i>file_name</i>, <code>-m </code><i>file_name</i> </p>
<p> If given, the number of microseconds spent running the test will be written to this file. This is used by <code>mysql-test-run.pl</code> for its reporting.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;tmpdir=</code><i>dir_name</i>, <code>-t </code><i>dir_name</i> </p>
<p> The temporary directory where socket files are created.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;user=</code><i>user_name</i>, <code>-u </code><i>user_name</i> </p>
<p> The MariaDB user name to use when connecting to the server.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;verbose</code>, <code>-v</code> </p>
<p> Verbose mode. Print out more information about what the program does.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code>, <code>-V</code> </p>
<p> Display version information and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;view-protocol</code> </p>
<p> Every SELECT statement is wrapped inside a view.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2007, 2010, Oracle and/or its affiliates, 2010-2015 MariaDB Foundation </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MariaDB Knowledge Base, available online at <a rel="nofollow" href="https://mariadb.com/kb/">https://mariadb.com/kb/</a></p>
<h2>AUTHOR</h2>
<p> MariaDB Foundation (<a rel="nofollow" href="http://www.mariadb.org/">http://www.mariadb.org/</a>). </p>
<h2>Index</h2>
