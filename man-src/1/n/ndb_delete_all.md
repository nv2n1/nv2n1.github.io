---
title: "ndb_delete_all(1)"
name: "ndb_delete_all"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndb_delete_all/"
description: "ndb_delete_all – delete all rows from an NDB table"
---

<h2 class="name">NAME</h2>
<p> ndb_delete_all &#8211; delete all rows from an NDB table </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ndb_delete_all </code><i>options</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>ndb_delete_all</code></p>
<dd>deletes all rows from the given NDB table. In some cases, this can be much faster than DELETE or even TRUNCATE TABLE. </p>
<p> <code>Usage</code>: </p>
<dl>
<dt>
<dd>
<pre>
ndb_delete_all -c <i>connect_string</i> <i>tbl_name</i> -d <i>db_name</i>
</pre>
</dl>
<p> This deletes all rows from the table named <i>tbl_name</i> in the database named <i>db_name</i>. It is exactly equivalent to executing TRUNCATE <i>db_name</i>.<i>tbl_name</i> in MySQL. </p>
<p> <code>Additional Options</code>: </p>
<dl>
<dt>
<dd> * <code>&#8211;transactional</code>, <code>-t</code> </p>
<p> Use of this option causes the delete operation to be performed as a single transaction. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Warning</code> </font><br />
 With very large tables, using this option may cause the number of operations available to the cluster to be exceeded. </p>
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
