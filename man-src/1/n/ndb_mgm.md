---
title: "ndb_mgm(1)"
name: "ndb_mgm"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndb_mgm/"
description: "ndb_mgm – the MySQL Cluster management client"
---

<h2 class="name">NAME</h2>
<p> ndb_mgm &#8211; the MySQL Cluster management client </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ndb_mgm </code><i>options</i></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>ndb_mgm</code> management client process is actually not needed to run the cluster. Its value lies in providing a set of commands for checking the cluster&#8217;s status, starting backups, and performing other administrative functions. The management client accesses the management server using a C API. Advanced users can also employ this API for programming dedicated management processes to perform tasks similar to those performed by <code>ndb_mgm</code>. </p>
<p> To start the management client, it is necessary to supply the host name and port number of the management server: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; ndb_mgm[host_name[port_num]]
</code></pre>
</dl>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>ndb_mgm ndb_mgmd.mysql.com 1186</code>
</pre>
</dl>
<p> The default host name and port number are localhost and 1186, respectively. </p>
<p> The following table includes options that are specific to the MySQL Cluster management client program <code>ndb_mgm</code>. Additional descriptions follow the table. For options common to all MySQL Cluster programs, see Section 17.4.2, lqOptions Common to MySQL Cluster Programsrq. </p>
<dl>
<dt>
<dd> * <code>&#8211;try-reconnect=</code><i>number</i> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;try-reconnect=#
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
<td> TRUE </td>
</tr>
</table>
<p> If the connection to the management server is broken, the node tries to reconnect to it every 5 seconds until it succeeds. By using this option, it is possible to limit the number of attempts to <i>number</i> before giving up and reporting an error instead.</dl>
<p> Additional information about using <code>ndb_mgm</code> can be found in Section 17.5.2, lqCommands in the MySQL Cluster Management Clientrq.</p>
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
