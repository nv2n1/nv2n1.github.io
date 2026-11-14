---
title: "mysql_fix_extensions(1)"
name: "mysql_fix_extensions"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysql_fix_extensions/"
description: "mysql_fix_extensions – normalize table file name extensions"
---

<h2 class="name">NAME</h2>
<p> mysql_fix_extensions &#8211; normalize table file name extensions </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysql_fix_extensions </code><i>data_dir</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>mysql_fix_extensions</code></p>
<dd>converts the extensions for MyISAM (or ISAM) table files to their canonical forms. It looks for files with extensions matching any lettercase variant of .frm, .myd, .myi, .isd, and .ism and renames them to have extensions of .frm, .MYD, .MYI, .ISD, and .ISM, respectively. This can be useful after transferring the files from a system with case-insensitive file names (such as Windows) to a system with case-sensitive file names. </p>
<p> Invoke <code>mysql_fix_extensions</code> like this, where <i>data_dir</i> is the path name to the MySQL data directory. </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql_fix_extensions </code><i>data_dir</i>
</pre>
</dl>
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
