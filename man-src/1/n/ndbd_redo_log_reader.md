---
title: "ndbd_redo_log_reader(1)"
name: "ndbd_redo_log_reader"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndbd_redo_log_reader/"
description: "ndbd_redo_log_reader – check and print content of cluster redo log"
---

<h2 class="name">NAME</h2>
<p> ndbd_redo_log_reader &#8211; check and print content of cluster redo log </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ndbd_redo_log_reader </code><i>file_name</i><code> [</code><i>options</i><code>]</code></dl>
<h2>DESCRIPTION</h2>
<dd>Reads a redo log file, checking it for errors, printing its contents in a human-readable format, or both. <code>ndbd_redo_log_reader</code> is intended for use primarily by MySQL developers and support personnel in debugging and diagnosing problems. </p>
<p> This utility was made available as part of default builds beginning with MySQL Cluster NDB 6.1.3. It remains under development, and its syntax and behavior are subject to change in future releases. For this reason, it should be considered experimental at this time. </p>
<p> The C++ source files for <code>ndbd_redo_log_reader</code> can be found in the directory /storage/ndb/src/kernel/blocks/dblqh/redoLogReader. </p>
<p> The following table includes options that are specific to the MySQL Cluster program <code>ndbd_redo_log_reader</code>. Additional descriptions follow the table. For options common to all MySQL Cluster programs, see Section 17.4.2, lqOptions Common to MySQL Cluster Programsrq. </p>
<p> <code>Usage</code>: </p>
<dl>
<dt>
<dd>
<pre>
ndbd_redo_log_reader <i>file_name</i> [<i>options</i>]
</pre>
</dl>
<p> <i>file_name</i> is the name of a cluster REDO log file. REDO log files are located in the numbered directories under the data node&#8217;s data directory (DataDir); the path under this directory to the REDO log files matches the pattern ndb_<i>#</i>_fs/D<i>#</i>/LCP/<i>#</i>/T<i>#</i>F<i>#</i>.Data. In each case, the <i>#</i> represents a number (not necessarily the same number). For more information, see m[blue]<code>Cluster Data Node FileSystemDir Files</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> The name of the file to be read may be followed by one or more of the options listed here: </p>
<dl>
<dt>
<dd> * </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> -noprint
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> boolean </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> FALSE </td>
</tr>
</table>
<p> <code>-noprint</code>: Do not print the contents of the log file.</dl>
<dl>
<dt>
<dd> * </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> -nocheck
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> boolean </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> FALSE </td>
</tr>
</table>
<p> <code>-nocheck</code>: Do not check the log file for errors.</dl>
<p> Like <code>ndb_print_backup_file</code> and <code>ndb_print_schema_file</code> (and unlike most of the NDB utilities that are intended to be run on a management server host or to connect to a management server) <code>ndbd_redo_log_reader</code> must be run on a cluster data node, since it accesses the data node file system directly. Because it does not make use of the management server, this utility can be used when the management server is not running, and even when the cluster has been completely shut down.</p>
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
