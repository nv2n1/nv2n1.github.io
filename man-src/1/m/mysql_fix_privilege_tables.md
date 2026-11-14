---
title: "mysql_fix_privilege_tables(1)"
name: "mysql_fix_privilege_tables"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysql_fix_privilege_tables/"
description: "mysql_fix_privilege_tables – upgrade MySQL system tables"
---

<h2 class="name">NAME</h2>
<p> mysql_fix_privilege_tables &#8211; upgrade MySQL system tables </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysql_fix_privilege_tables &#8211;password=</code><i>root_password</i></dl>
<h2>DESCRIPTION</h2>
<dl>
<dt>
<dd>
<dd> <font SIZE="+1"> <code>Note</code> </font></p>
<dd>
<dd>In MySQL 5.1.7, <code>mysql_fix_privilege_tables</code> was superseded by <code>mysql_upgrade</code>, which should be used instead. See <code><a href="/docs/linux/man/1-mysql_upgrade/">mysql_upgrade</a></code>(1). </p>
</dl>
<p> Some releases of MySQL introduce changes to the structure of the system tables in the mysql database to add new privileges or support new features. When you update to a new version of MySQL, you should update your system tables as well to make sure that their structure is up to date. Otherwise, there might be capabilities that you cannot take advantage of. </p>
<p> <code>mysql_fix_privilege_tables</code> is an older script that previously was used to uprade the system tables in the mysql database after a MySQL upgrade. </p>
<p> Before running <code>mysql_fix_privilege_tables</code>, make a backup of your mysql database. </p>
<p> On Unix or Unix-like systems, update the system tables by running the <code>mysql_fix_privilege_tables</code> script: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql_fix_privilege_tables</code>
</pre>
</dl>
<p> You must run this script while the server is running. It attempts to connect to the server running on the local host as root. If your root account requires a password, indicate the password on the command line like this: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql_fix_privilege_tables --password=</code><i>root_password</i>
</pre>
</dl>
<p> The <code>mysql_fix_privilege_tables</code> script performs any actions necessary to convert your system tables to the current format. You might see some Duplicate column name warnings as it runs; you can ignore them. </p>
<p> After running the script, stop the server and restart it so that any changes made to the system tables take effect. </p>
<p> On Windows systems, MySQL distributions include a mysql_fix_privilege_tables.sql SQL script that you can run using the <code>mysql</code> client. For example, if your MySQL installation is located at C:\Program Files\MySQL\MySQL Server 5.1, the commands look like this: </p>
<dl>
<dt>
<dd>
<pre>
C:\&gt; <code>cd &quot;C:\Program Files\MySQL\MySQL Server 5.1&quot;</code>
C:\&gt; <code>bin\mysql -u root -p mysql</code>
mysql&gt; <code>SOURCE share/mysql_fix_privilege_tables.sql</code>
</pre>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> Prior to version 5.1.17, the mysql_fix_privilege_tables.sql script is found in the scripts directory. </p>
</dl>
<p> The <code>mysql</code> command will prompt you for the root password; enter it when prompted. </p>
<p> If your installation is located in some other directory, adjust the path names appropriately. </p>
<p> As with the Unix procedure, you might see some Duplicate column name warnings as <code>mysql</code> processes the statements in the mysql_fix_privilege_tables.sql script; you can ignore them. </p>
<p> After running the script, stop the server and restart it.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008, 2010, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
