---
title: "mysql_zap(1)"
name: "mysql_zap"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysql_zap/"
description: "mysql_zap – kill processes that match a pattern"
---

<h2 class="name">NAME</h2>
<p> mysql_zap &#8211; kill processes that match a pattern </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysql_zap [-</code><i>signal</i><code>] [-?Ift] </code><i>pattern</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>mysql_zap</code></p>
<dd>kills processes that match a pattern. It uses the <code>ps</code> command and Unix signals, so it runs on Unix and Unix-like systems. </p>
<p> Invoke <code>mysql_zap</code> like this: </p>
<dl>
<dt>
<dd>
<pre><code>
shell&gt; mysql_zap [-signal] [-?Ift] pattern
</code></pre>
</dl>
<p> A process matches if its output line from the <code>ps</code> command contains the pattern. By default, <code>mysql_zap</code> asks for confirmation for each process. Respond y to kill the process, or q to exit <code>mysql_zap</code>. For any other response, <code>mysql_zap</code> does not attempt to kill the process. </p>
<p> If the <code>&#8211;</code><i>signal</i> option is given, it specifies the name or number of the signal to send to each process. Otherwise, <code>mysql_zap</code> tries first with TERM (signal 15) and then with KILL (signal 9). </p>
<p> <code>mysql_zap</code> supports the following additional options: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code>, <code>-I</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>-f</code> </p>
<p> Force mode. <code>mysql_zap</code> attempts to kill each process without confirmation.</dl>
<dl>
<dt>
<dd> &bull; <code>-t</code> </p>
<p> Test mode. Display information about each process but do not kill it.</dl>
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
