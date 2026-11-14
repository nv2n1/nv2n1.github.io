---
title: "mysql_client_test(1)"
name: "mysql_client_test"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysql_client_test/"
description: "mysql_client_test – test client API mysql_client_test_embedded – test client API for embedded server"
---

<h2 class="name">NAME</h2>
<p> mysql_client_test &#8211; test client API<br />
 mysql_client_test_embedded &#8211; test client API for embedded server </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysql_client_test [</code><i>options</i><code>] [</code><i>test_name</i><code>] &#8230;</code></p>
<dt> <code>mysql_client_test_embedded [</code><i>options</i><code>] [</code><i>test_name</i><code>] &#8230;</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>mysql_client_test</code> program is used for testing aspects of the MariaDB client API that cannot be tested using <code>mysqltest</code> and its test language. <code>mysql_client_test_embedded</code> is similar but used for testing the embedded server. Both programs are run as part of the test suite. </p>
<p> The source code for the programs can be found in in tests/mysql_client_test.c in a source distribution. The program serves as a good source of examples illustrating how to use various features of the client API. </p>
<p> <code>mysql_client_test</code> is used in a test by the same name in the main tests suite of <code>mysql-test-run.pl</code> but may also be run directly. Unlike the other programs listed here, it does not read an external description of what tests to run. Instead, all tests are coded into the program, which is written to cover all aspects of the C language API. </p>
<p> <code>mysql_client_test</code> supports the following options: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;basedir=</code><i>dir_name</i>, <code>-b </code><i>dir_name</i> </p>
<p> The base directory for the tests.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;count=</code><i>count</i>, <code>-t </code><i>count</i> </p>
<p> The number of times to execute the tests.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;database=</code><i>db_name</i>, <code>-D </code><i>db_name</i> </p>
<p> The database to use.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug[=</code><i>debug_options</i><code>]</code>, <code>-#[</code><i>debug_options</i><code>]</code> </p>
<p> Write a debugging log if MariaDB is built with debugging support. The default <i>debug_options</i> value is &#8216;d:t:o,/tmp/mysql_client_test.trace&#8217;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;getopt-ll-test=</code><i>option</i>, <code>-g </code><i>option</i> </p>
<p> Option to use for testing bugs in the getopt library.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;host=</code><i>host_name</i>, <code>-h </code><i>host_name</i> </p>
<p> Connect to the MariaDB server on the given host.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;password[=</code><i>password</i><code>]</code>, <code>-p[</code><i>password</i><code>]</code> </p>
<p> The password to use when connecting to the server. If you use the short option form (<code>-p</code>), you <i>cannot</i> have a space between the option and the password. If you omit the <i>password</i> value following the <code>&#8211;password</code> or <code>-p</code> option on the command line, you are prompted for one.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;port=</code><i>port_num</i>, <code>-P </code><i>port_num</i> </p>
<p> The TCP/IP port number to use for the connection.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;server-arg=</code><i>arg</i>, <code>-A </code><i>arg</i> </p>
<p> Argument to send to the embedded server.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;show-tests</code>, <code>-T</code> </p>
<p> Show all test names.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;silent</code>, <code>-s</code> </p>
<p> Be more silent.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;socket=</code><i>path</i>, <code>-S </code><i>path</i> </p>
<p> The socket file to use when connecting to localhost (which is the default host).</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;testcase</code>, <code>-c</code> </p>
<p> The option is used when called from <code>mysql-test-run.pl</code>, so that <code>mysql_client_test</code> may optionally behave in a different way than if called manually, for example by skipping some tests. Currently, there is no difference in behavior but the option is included in order to make this possible.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;user=</code><i>user_name</i>, <code>-u </code><i>user_name</i> </p>
<p> The MariaDB user name to use when connecting to the server.</dl>
<dl>
<dt>
<dd> &bull; <code>-v </code><i>dir_name</i>, <code>&#8211;vardir=</code><i>dir_name</i> </p>
<p> The data directory for tests. The default is mysql-test/var.</dl>
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
