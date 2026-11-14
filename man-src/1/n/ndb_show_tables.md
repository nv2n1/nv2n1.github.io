---
title: "ndb_show_tables(1)"
name: "ndb_show_tables"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndb_show_tables/"
description: "ndb_show_tables – display list of NDB tables"
---

<h2 class="name">NAME</h2>
<p> ndb_show_tables &#8211; display list of NDB tables </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ndb_show_tables [</code><i>options</i><code>]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>ndb_show_tables</code></p>
<dd>displays a list of all NDB database objects in the cluster. By default, this includes not only both user-created tables and NDB system tables, but NDB-specific indexes, internal triggers, and MySQL Cluster Disk Data objects as well. </p>
<p> The following table includes options that are specific to the MySQL Cluster program <code>ndb_show_tables</code>. Additional descriptions follow the table. For options common to all MySQL Cluster programs, see Section 17.4.2, lqOptions Common to MySQL Cluster Programsrq. </p>
<p> <code>Usage</code>: </p>
<dl>
<dt>
<dd>
<pre>
ndb_show_tables [-c <i>connect_string</i>]
</pre>
</dl>
<dl>
<dt>
<dd> * <code>&#8211;database</code>, <code>-d</code> </p>
<p> Specifies the name of the database in which the tables are found.</dl>
<dl>
<dt>
<dd> * <code>&#8211;loops</code>, <code>-l</code> </p>
<p> Specifies the number of times the utility should execute. This is 1 when this option is not specified, but if you do use the option, you must supply an integer argument for it.</dl>
<dl>
<dt>
<dd> * <code>&#8211;parsable</code>, <code>-p</code> </p>
<p> Using this option causes the output to be in a format suitable for use with LOAD DATA INFILE.</dl>
<dl>
<dt>
<dd> * <code>&#8211;show-temp-status</code> </p>
<p> If specified, this causes temporary tables to be displayed.</dl>
<dl>
<dt>
<dd> * <code>&#8211;type</code>, <code>-t</code> </p>
<p> Can be used to restrict the output to one type of object, specified by an integer type code as shown here: </p>
<dl>
<dt>
<dd> * <code>1</code>: System table</dl>
<dl>
<dt>
<dd> * <code>2</code>: User-created table</dl>
<dl>
<dt>
<dd> * <code>3</code>: Unique hash index</dl>
<dl>
<dt>
<dd> Any other value causes all NDB database objects to be listed (the default).</dl>
<dl>
<dt>
<dd> * <code>&#8211;unqualified</code>, <code>-u</code> </p>
<p> If specified, this causes unqualified object names to be displayed.</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> Only user-created Cluster tables may be accessed from MySQL; system tables such as SYSTAB_0 are not visible to <code>mysqld</code>. However, you can examine the contents of system tables using NDB API applications such as <code>ndb_select_all</code> (see <code><a href="/docs/linux/man/1-ndb_select_all/">ndb_select_all</a></code>(1)). </p>
</dl>
</dl>
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
