---
title: "mysqlaccess(1)"
name: "mysqlaccess"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqlaccess/"
description: "mysqlaccess – client for checking access privileges"
---

<h2 class="name">NAME</h2>
<p> mysqlaccess &#8211; client for checking access privileges </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqlaccess [</code><i>host_name</i><code> [</code><i>user_name</i><code> [</code><i>db_name</i><code>]]] [</code><i>options</i><code>]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>mysqlaccess</code></p>
<dd>is a diagnostic tool written by Yves Carlier. It checks the access privileges for a host name, user name, and database combination. Note that <code>mysqlaccess</code> checks access using only the user, db, and host tables. It does not check table, column, or routine privileges specified in the tables_priv, columns_priv, or procs_priv tables. </p>
<p> Invoke <code>mysqlaccess</code> like this: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; mysqlaccess[host_name[user_name[db_name]]][options]
</code></pre>
</dl>
<p> <code>mysqlaccess</code> supports the following options. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;brief</code>, <code>-b</code> </p>
<p> Generate reports in single-line tabular format.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;commit</code> </p>
<p> Copy the new access privileges from the temporary tables to the original grant tables. The grant tables must be flushed for the new privileges to take effect. (For example, execute a <code>mysqladmin reload</code> command.)</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;copy</code> </p>
<p> Reload the temporary grant tables from original ones.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;db=</code><i>db_name</i>, <code>-d </code><i>db_name</i> </p>
<p> Specify the database name.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug=</code><i>N</i> </p>
<p> Specify the debug level. <i>N</i> can be an integer from 0 to 3.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;host=</code><i>host_name</i>, <code>-h </code><i>host_name</i> </p>
<p> The host name to use in the access privileges.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;howto</code> </p>
<p> Display some examples that show how to use <code>mysqlaccess</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;old_server</code> </p>
<p> Connect to a very old MySQL server (before MySQL 3.21) that does not know how to handle full WHERE clauses.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;password[=</code><i>password</i><code>]</code>, <code>-p[</code><i>password</i><code>]</code> </p>
<p> The password to use when connecting to the server. If you omit the <i>password</i> value following the <code>&#8211;password</code> or <code>-p</code> option on the command line, <code>mysqlaccess</code> prompts for one. </p>
<p> Specifying a password on the command line should be considered insecure. See Section 5.3.2.2, &#8220;End-User Guidelines for Password Security&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;plan</code> </p>
<p> Display suggestions and ideas for future releases.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;preview</code> </p>
<p> Show the privilege differences after making changes to the temporary grant tables.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;relnotes</code> </p>
<p> Display the release notes.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;rhost=</code><i>host_name</i>, <code>-H </code><i>host_name</i> </p>
<p> Connect to the MariaDB server on the given host.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;rollback</code> </p>
<p> Undo the most recent changes to the temporary grant tables.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;spassword[=</code><i>password</i><code>]</code>, <code>-P[</code><i>password</i><code>]</code> </p>
<p> The password to use when connecting to the server as the superuser. If you omit the <i>password</i> value following the <code>&#8211;spassword</code> or <code>-p</code> option on the command line, <code>mysqlaccess</code> prompts for one. </p>
<p> Specifying a password on the command line should be considered insecure. See Section 5.3.2.2, &#8220;End-User Guidelines for Password Security&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;superuser=</code><i>user_name</i>, <code>-U </code><i>user_name</i> </p>
<p> Specify the user name for connecting as the superuser.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;table</code>, <code>-t</code> </p>
<p> Generate reports in table format.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;user=</code><i>user_name</i>, <code>-u </code><i>user_name</i> </p>
<p> The user name to use in the access privileges.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code>, <code>-v</code> </p>
<p> Display version information and exit.</dl>
<p> If your MariaDB distribution is installed in some non-standard location, you must change the location where <code>mysqlaccess</code> expects to find the <code>mysql</code> client. Edit the mysqlaccess script at approximately line 18. Search for a line that looks like this: </p>
<dl>
<dt>
<dd>
<pre>
$MYSQL     = '/usr/local/bin/mysql';    # path to mysql executable
</pre>
</dl>
<p> Change the path to reflect the location where <code>mysql</code> actually is stored on your system. If you do not do this, a Broken pipe error will occur when you run <code>mysqlaccess</code>.</p>
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
