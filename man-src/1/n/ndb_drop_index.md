---
title: "ndb_drop_index(1)"
name: "ndb_drop_index"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndb_drop_index/"
description: "ndb_drop_index – drop index from an NDB table"
---

<h2 class="name">NAME</h2>
<p> ndb_drop_index &#8211; drop index from an NDB table </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ndb_drop_index </code><i>options</i></dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>ndb_drop_index</code></p>
<dd>drops the specified index from an NDB table. <i>It is recommended that you use this utility only as an example for writing NDB API applications</i> &#8212; see the Warning later in this section for details. </dd>
<p> <code>Usage</code>: </p>
<dl>
<dt>
</dt><dd>
<pre>
ndb_drop_index -c <i>connect_string</i> <i>table_name</i> <i>index</i> -d <i>db_name</i>
</pre>
</dd></dl>
<p> The statement shown above drops the index named <i>index</i> from the <i>table</i> in the <i>database</i>. </p>
<p> <code>Additional Options</code>: None that are specific to this application. </p>
<dl>
<dt>
</dt><dd>
 <font SIZE="+1"> <code>Warning</code> </font> </dd>
<p> <i>Operations performed on Cluster table indexes using the NDB API are not visible to MySQL and make the table unusable by a MySQL server</i>. If you use this program to drop an index, then try to access the table from an SQL node, an error results, as shown here: </p>
</dl>
<dl>
<dt>
</dt><dd>
<pre><code>
shell&gt; ./ndb_drop_index -c localhost dogs ix -d ctest1
Dropping index dogs/idx...OK
NDBT_ProgramExit: 0 - OK
shell&gt; ./mysql -u jon -p ctest1
Enter password: *******
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 7 to server version: 5.1.44-ndb-7.1.4
Type 'help;' or '\h' for help. Type '</code>\c' to clear the buffer.
mysql&gt; SHOW TABLES; +------------------+
| Tables_in_ctest1 |
+------------------+
| a |
| bt1 |
| bt2 |
| dogs |
| employees |
| fish |
+------------------+
6 rows in set (0.00 sec)
mysql&gt; SELECT * FROM dogs; ERROR 1296 (HY000): Got error 4243 'Index not found' from NDBCLUSTER
</code></pre>
</dl>
<p> In such a case, your <i>only</i> option for making the table available to MySQL again is to drop the table and re-create it. You can use either the SQL statementDROP TABLE or the <code>ndb_drop_table</code> utility (see <code><a href="/docs/linux/man/1-ndb_drop_table/">ndb_drop_table</a></code>(1)) to drop the table.  </p>
<h2>COPYRIGHT</h2>
<p> <br />
 </p>
<p> Copyright &#169; 2008, 2010, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a>  </p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
