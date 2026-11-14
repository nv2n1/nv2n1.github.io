---
title: "mysql_find_rows(1)"
name: "mysql_find_rows"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysql_find_rows/"
description: "mysql_find_rows – extract SQL statements from files"
---

<h2 class="name">NAME</h2>
<p> mysql_find_rows &#8211; extract SQL statements from files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysql_find_rows [</code><i>options</i><code>] [</code><i>file_name</i><code> &#8230;]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>mysql_find_rows</code></p>
<dd>reads files containing SQL statements and extracts statements that match a given regular expression or that contain USE <i>db_name</i> or SET statements. The utility was written for use with update log files (as used prior to MySQL 5.0) and as such expects statements to be terminated with semicolon (;) characters. It may be useful with other files that contain SQL statements as long as statements are terminated with semicolons. </p>
<p> Invoke <code>mysql_find_rows</code> like this: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; mysql_find_rows[options][file_name...]
</code></pre>
</dl>
<p> Each <i>file_name</i> argument should be the name of file containing SQL statements. If no file names are given, <code>mysql_find_rows</code> reads the standard input. </p>
<p> Examples: </p>
<dl>
<dt>
<dd>
<pre>
mysql_find_rows --regexp=problem_table --rows=20 &lt; update.log
mysql_find_rows --regexp=problem_table  update-log.1 update-log.2
</pre>
</dl>
<p> <code>mysql_find_rows</code> supports the following options: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>&#8211;Information</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;regexp=</code><i>pattern</i> </p>
<p> Display queries that match the pattern.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;rows=</code><i>N</i> </p>
<p> Quit after displaying <i>N</i> queries.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;skip-use-db</code> </p>
<p> Do not include USE <i>db_name</i> statements in the output.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;start_row=</code><i>N</i> </p>
<p> Start output from this row.</dl>
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
