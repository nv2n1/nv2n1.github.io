---
title: "mysql_waitpid(1)"
name: "mysql_waitpid"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysql_waitpid/"
description: "mysql_waitpid – kill process and wait for its termination"
---

<h2 class="name">NAME</h2>
<p> mysql_waitpid &#8211; kill process and wait for its termination </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysql_waitpid [</code><i>options</i><code>] </code><i>pid</i><i>wait_time</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>mysql_waitpid</code></p>
<dd>signals a process to terminate and waits for the process to exit. It uses the kill() system call and Unix signals, so it runs on Unix and Unix-like systems. </p>
<p> Invoke <code>mysql_waitpid</code> like this: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql_waitpid [</code><i>options</i><code>] </code><i>pid</i><i>wait_time</i>
</pre>
</dl>
<p> <code>mysql_waitpid</code> sends signal 0 to the process identified by <i>pid</i> and waits up to <i>wait_time</i> seconds for the process to terminate. <i>pid</i> and <i>wait_time</i> must be positive integers. </p>
<p> If process termination occurs within the wait time or the process does not exist, <code>mysql_waitpid</code> returns 0. Otherwise, it returns 1. </p>
<p> If the kill() system call cannot handle signal 0, <code>mysql_waitpid()</code> uses signal 1 instead. </p>
<p> <code>mysql_waitpid</code> supports the following options: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code>, <code>-I</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;verbose</code>, <code>-v</code> </p>
<p> Verbose mode. Display a warning if signal 0 could not be used and signal 1 is used instead.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code>, <code>-V</code> </p>
<p> Display version information and exit.</dl>
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
