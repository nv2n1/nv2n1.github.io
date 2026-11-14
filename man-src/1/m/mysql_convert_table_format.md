---
title: "mysql_convert_table_format(1)"
name: "mysql_convert_table_format"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysql_convert_table_format/"
description: "mysql_convert_table_format – convert tables to use a given storage engine"
---

<h2 class="name">NAME</h2>
<p> mysql_convert_table_format &#8211; convert tables to use a given storage engine </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysql_convert_table_format [</code><i>options</i><code>] </code><i>db_name</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>mysql_convert_table_format</code></p>
<dd>converts the tables in a database to use a particular storage engine (MyISAM by default). <code>mysql_convert_table_format</code> is written in Perl and requires that the DBI and DBD::mysql Perl modules be installed (see Section 2.15, &#8220;Perl Installation Notes&#8221;). </p>
<p> Invoke <code>mysql_convert_table_format</code> like this: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql_convert_table_format [</code><i>options</i><code>]</code><i>db_name</i>
</pre>
</dl>
<p> The <i>db_name</i> argument indicates the database containing the tables to be converted. </p>
<p> <code>mysql_convert_table_format</code> supports the options described in the following list. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;force</code> </p>
<p> Continue even if errors occur.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;host=</code><i>host_name</i> </p>
<p> Connect to the MariaDB server on the given host.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;password=</code><i>password</i> </p>
<p> The password to use when connecting to the server. Note that the password value is not optional for this option, unlike for other MariaDB programs. </p>
<p> Specifying a password on the command line should be considered insecure. You can use an option file to avoid giving the password on the command line.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;port=</code><i>port_num</i> </p>
<p> The TCP/IP port number to use for the connection.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;socket=</code><i>path</i> </p>
<p> For connections to localhost, the Unix socket file to use.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;type=</code><i>engine_name</i> </p>
<p> Specify the storage engine that the tables should be converted to use. The default is MyISAM if this option is not given.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;user=</code><i>user_name</i> </p>
<p> The MariaDB user name to use when connecting to the server.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;verbose</code> </p>
<p> Verbose mode. Print more information about what the program does.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code> </p>
<p> Display version information and exit.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright 2007-2008 MySQL AB, 2008-2010 Sun Microsystems, Inc., 2010-2015 MariaDB Foundation </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MariaDB Knowledge Base, available online at <a rel="nofollow" href="https://mariadb.com/kb/">https://mariadb.com/kb/</a></p>
<h2>AUTHOR</h2>
<p> MariaDB Foundation (<a rel="nofollow" href="http://www.mariadb.org/">http://www.mariadb.org/</a>). </p>
<h2>Index</h2>
