---
title: "ndb_drop_table(1)"
name: "ndb_drop_table"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndb_drop_table/"
description: "ndb_drop_table – drop an NDB table"
---

<h2 class="name">NAME</h2>
<p> ndb_drop_table &#8211; drop an NDB table </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ndb_drop_table </code><i>options</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>ndb_drop_table</code></p>
<dd>drops the specified NDB table. (If you try to use this on a table created with a storage engine other than NDB, it fails with the error 723: No such table exists.) This operation is extremely fast &#8212; in some cases, it can be an order of magnitude faster than using DROP TABLE on an NDB table from MySQL. </p>
<p> <code>Usage</code>: </p>
<dl>
<dt>
<dd>
<pre>
ndb_drop_table -c <i>connect_string</i> <i>tbl_name</i> -d <i>db_name</i>
</pre>
</dl>
<p> <code>Additional Options</code>: None.</p>
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
