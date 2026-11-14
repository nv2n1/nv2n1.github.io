---
title: "mysqlbug(1)"
name: "mysqlbug"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqlbug/"
description: "mysqlbug – generate bug report"
---

<h2 class="name">NAME</h2>
<p> mysqlbug &#8211; generate bug report </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqlbug</code></dl>
<h2>DESCRIPTION</h2>
<dd>To report MariaDB bugs, see <a rel="nofollow" href="https://mariadb.com/kb/en/mariadb/reporting-bugs/">https://mariadb.com/kb/en/mariadb/reporting-bugs/</a> &#8211; the mysqlbug program has now been deprecated by Oracle, and was never useful for MariaDB. </p>
<p> Originally, the program enabled you to generate a bug report and send it to Oracle Corporation. It is a shell script and runs on Unix. </p>
<p> The normal way to report MySQL bugs is to visit m[blue]<code><a rel="nofollow" href="http://bugs.mysql.com/">http://bugs.mysql.com/</a></code>m[], which is the address for MySQL&#8217;s bugs database. This database is public and can be browsed and searched by anyone. If you log in to the system, you can enter new reports. If you have no Web access, you can generate a bug report by using the <code>mysqlbug</code> script. </p>
<p> <code>mysqlbug</code> helps you generate a report by determining much of the following information automatically, but if something important is missing, please include it with your message. <code>mysqlbug</code> can be found in the scripts directory (source distribution) and in the bin directory under your MySQL installation directory (binary distribution). </p>
<p> Invoke <code>mysqlbug</code> without arguments: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlbug</code>
</pre>
</dl>
<p> The script will place you in an editor with a copy of the report to be sent. Edit the lines near the beginning that indicate the nature of the problem. Then write the file to save your changes, quit the editor, and <code>mysqlbug</code> will send the report by email.</p>
<h2>COPYRIGHT</h2>
<p> Copyright 2007-2008 MySQL AB, 2008-2010 Sun Microsystems, Inc., 2010-2015 MariaDB Foundation </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MariaDB Knowledge Base, available online at <a rel="nofollow" href="https://mariadb.com/kb/">https://mariadb.com/kb/</a></p>
<h2>AUTHOR</h2>
<p> MariaDB Foundation (<a rel="nofollow" href="http://www.mariadb.org/">http://www.mariadb.org/</a>). </p>
<h2>Index</h2>
