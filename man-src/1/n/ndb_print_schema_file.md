---
title: "ndb_print_schema_file(1)"
name: "ndb_print_schema_file"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndb_print_schema_file/"
description: "ndb_print_schema_file – print NDB schema file contents"
---

<h2 class="name">NAME</h2>
<p> ndb_print_schema_file &#8211; print NDB schema file contents </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ndb_print_schema_file </code><i>file_name</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>ndb_print_schema_file</code></p>
<dd>obtains diagnostic information from a cluster schema file. </p>
<p> <code>Usage</code>: </p>
<dl>
<dt>
<dd>
<pre>
ndb_print_schema_file <i>file_name</i>
</pre>
</dl>
<p> <i>file_name</i> is the name of a cluster schema file. For more information about cluster schema files, see m[blue]<code>Cluster Data Node FileSystemDir Files</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> Like <code>ndb_print_backup_file</code> and <code>ndb_print_sys_file</code> (and unlike most of the other NDB utilities that are intended to be run on a management server host or to connect to a management server) <code>ndb_schema_backup_file</code> must be run on a cluster data node, since it accesses the data node file system directly. Because it does not make use of the management server, this utility can be used when the management server is not running, and even when the cluster has been completely shut down. </p>
<p> <code>Additional Options</code>: None.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008, 2010, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Cluster Data Node FileSystemDir Files</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://dev.mysql.com/doc/ndbapi/en/ndb-internals-ndbd-filesystemdir-files.html">http://dev.mysql.com/doc/ndbapi/en/ndb-internals-ndbd-filesystemdir-files.html</a></dl>
</dl>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
