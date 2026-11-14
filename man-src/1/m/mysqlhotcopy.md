---
title: "mysqlhotcopy(1)"
name: "mysqlhotcopy"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqlhotcopy/"
description: "mysqlhotcopy – a database backup program"
---

<h2 class="name">NAME</h2>
<p> mysqlhotcopy &#8211; a database backup program </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqlhotcopy </code><i>arguments</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>mysqlhotcopy</code></p>
<dd>is a Perl script that was originally written and contributed by Tim Bunce. It uses FLUSH TABLES, LOCK TABLES, and cp or scp to make a database backup. It is a fast way to make a backup of the database or single tables, but it can be run only on the same machine where the database directories are located. <code>mysqlhotcopy</code> works only for backing up MyISAM and ARCHIVE tables. It runs on Unix and NetWare. </p>
<p> To use <code>mysqlhotcopy</code>, you must have read access to the files for the tables that you are backing up, the SELECT privilege for those tables, the RELOAD privilege (to be able to execute FLUSH TABLES), and the LOCK TABLES privilege (to be able to lock the tables). </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlhotcopy </code><i>db_name</i><code> [</code><i>/path/to/new_directory</i><code>]</code>
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlhotcopy </code><i>db_name_1</i><code> ... </code><i>db_name_n</i><i>/path/to/new_directory</i>
</pre>
</dl>
<p> Back up tables in the given database that match a regular expression: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlhotcopy </code><i>db_name</i><code>./</code><i>regex</i><code>/</code>
</pre>
</dl>
<p> The regular expression for the table name can be negated by prefixing it with a tilde (&#8220;~&#8221;): </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlhotcopy </code><i>db_name</i><code>./~</code><i>regex</i><code>/</code>
</pre>
</dl>
<p> <code>mysqlhotcopy</code> supports the following options, which can be specified on the command line or in the [mysqlhotcopy] and [client] option file groups. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;addtodest</code> </p>
<p> Do not rename target directory (if it exists); merely add files to it.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;allowold</code> </p>
<p> Do not abort if a target exists; rename it by adding an _old suffix.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;checkpoint=</code><i>db_name</i><code>.</code><i>tbl_name</i> </p>
<p> Insert checkpoint entries into the specified database <i>db_name</i> and table <i>tbl_name</i>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;chroot=</code><i>path</i> </p>
<p> Base directory of the <code>chroot</code> jail in which <code>mysqld</code> operates. The <i>path</i> value should match that of the <code>&#8211;chroot</code> option given to <code>mysqld</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;debug</code> </p>
<p> Enable debug output.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;dryrun</code>, <code>-n</code> </p>
<p> Report actions without performing them.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;flushlog</code> </p>
<p> Flush logs after all tables are locked.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;host=</code><i>host_name</i>, <code>-h </code><i>host_name</i> </p>
<p> The host name of the local host to use for making a TCP/IP connection to the local server. By default, the connection is made to localhost using a Unix socket file.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;keepold</code> </p>
<p> Do not delete previous (renamed) target when done.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;method=</code><i>command</i> </p>
<p> The method for copying files (cp or scp). The default is cp.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;noindices</code> </p>
<p> Do not include full index files for MyISAM tables in the backup. This makes the backup smaller and faster. The indexes for reloaded tables can be reconstructed later with <code>myisamchk -rq</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;old-server</code> </p>
<p> Connect to old MySQL-server (before v5.5) which doesn&#8217;t have FLUSH TABLES WITH READ LOCK fully implemented..</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;password=</code><i>password</i>, <code>-p</code><i>password</i> </p>
<p> The password to use when connecting to the server. The password value is not optional for this option, unlike for other MariaDB programs. </p>
<p> Specifying a password on the command line should be considered insecure. You can use an option file to avoid giving the password on the command line.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;port=</code><i>port_num</i>, <code>-P </code><i>port_num</i> </p>
<p> The TCP/IP port number to use when connecting to the local server.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;quiet</code>, <code>-q</code> </p>
<p> Be silent except for errors.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;record_log_pos=</code><i>db_name</i><code>.</code><i>tbl_name</i> </p>
<p> Record master and slave status in the specified database <i>db_name</i> and table <i>tbl_name</i>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;regexp=</code><i>expr</i> </p>
<p> Copy all databases with names that match the given regular expression.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;resetmaster</code> </p>
<p> Reset the binary log after locking all the tables.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;resetslave</code> </p>
<p> Reset the master.info file after locking all the tables.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;socket=</code><i>path</i>, <code>-S </code><i>path</i> </p>
<p> The Unix socket file to use for connections to localhost.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;suffix=</code><i>str</i> </p>
<p> The suffix to use for names of copied databases.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;tmpdir=</code><i>path</i> </p>
<p> The temporary directory. The default is /tmp.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;user=</code><i>user_name</i>, <code>-u </code><i>user_name</i> </p>
<p> The MariaDB user name to use when connecting to the server.</dl>
<p> Use perldoc for additional <code>mysqlhotcopy</code> documentation, including information about the structure of the tables needed for the <code>&#8211;checkpoint</code> and <code>&#8211;record_log_pos</code> options: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>perldoc mysqlhotcopy</code>
</pre>
</dl>
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
