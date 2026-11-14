---
title: "mysqld(8)"
name: "mysqld"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mysqld/"
description: "mysqld – the MySQL server"
---

<p>mysqld &#8211; the MySQL server</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>mysqld [</code><i>options</i><code>]</code></dl>
<h2>Description</h2>
<p><code>mysqld</code>, also known as MySQL Server, is the main program that does most of the work in a MySQL installation. MySQL Server manages access to the MySQL data directory that contains databases and tables. The data directory is also the default location for other information such as log files and status files.</p>
<dl>
<dd>
<dd><font SIZE="+1"> <code>Note</code> </font></p>
<dd>
<dd>Some installation packages contain a debugging version of the server named <code>mysqld-debug</code>. Invoke this version instead of <code>mysqld</code> for debugging support, memory allocation checking, and trace file support (see Section 28.5.1.2, &#8220;Creating Trace Files&#8221;).  When MySQL server starts, it listens for network connections from client programs and manages access to databases on behalf of those clients. The <code>mysqld</code> program has many options that can be specified at startup. For a complete list of options, run this command:</p>
<dl>
<dd>
<pre>shell&gt; <code>mysqld --verbose --help</code></pre>
</dl>
<p> MySQL Server also has a set of system variables that affect its operation as it runs. System variables can be set at server startup, and many of them can be changed at runtime to effect dynamic server reconfiguration. MySQL Server also has a set of status variables that provide information about its operation. You can monitor these status variables to access runtime performance characteristics. For a full description of MySQL Server command options, system variables, and status variables, see Section 5.1, &#8220;The MySQL Server&#8221;. For information about installing MySQL and setting up the initial configuration, see Chapter 2, Installing and Upgrading MySQL.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 1997, 2019, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a></p>
<h2>See Also</h2>
<p>For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a></p>
<h2>Author</h2>
<p>Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>).</p>
