---
title: "ndb_error_reporter(1)"
name: "ndb_error_reporter"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndb_error_reporter/"
description: "ndb_error_reporter – NDB error-reporting utility"
---

<h2 class="name">NAME</h2>
<p> ndb_error_reporter &#8211; NDB error-reporting utility </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ndb_error_reporter </code><i>options</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>ndb_error_reporter</code></p>
<dd>creates an archive from data node and management node log files that can be used to help diagnose bugs or other problems with a cluster. <i>It is highly recommended that you make use of this utility when filing reports of bugs in MySQL Cluster</i>. </p>
<p> <code>Usage</code>: </p>
<dl>
<dt>
<dd>
<pre><code>
ndb_error_reporter path / to / config - file[username][--fs]
</code></pre>
</dl>
<p> This utility is intended for use on a management node host, and requires the path to the management host configuration file (config.ini). Optionally, you can supply the name of a user that is able to access the cluster&#8217;s data nodes via SSH, in order to copy the data node log files. ndb_error_reporter then includes all of these files in archive that is created in the same directory in which it is run. The archive is named ndb_error_report_<i>YYYYMMDDHHMMSS</i>.tar.bz2, where <i>YYYYMMDDHHMMSS</i> is a datetime string. </p>
<p> If the <code>&#8211;fs</code> is used, then the data node file systems are also copied to the management host and included in the archive that is produced by this script. As data node file systems can be extremely large even after being compressed, we ask that you please do <i>not</i> send archives created using this option to Sun Microsystems, Inc. unless you are specifically requested to do so. </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;fs
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
