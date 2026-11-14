---
title: "resolve_stack_dump(1)"
name: "resolve_stack_dump"
section: "1"
letter: "r"
url: "/docs/linux/man/1-resolve_stack_dump/"
description: "resolve_stack_dump – resolve numeric stack trace dump to symbols"
---

<h2 class="name">NAME</h2>
<p> resolve_stack_dump &#8211; resolve numeric stack trace dump to symbols </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>resolve_stack_dump [</code><i>options</i><code>] </code><i>symbols_file</i><code> [</code><i>numeric_dump_file</i><code>]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>resolve_stack_dump</code></p>
<dd>resolves a numeric stack dump to symbols. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> <code>resolve_stack_dump</code> is deprecated and is removed in MySQL 8.0. Stack traces from official MySQL builds are always symbolized, so there is no need to use <code>resolve_stack_dump</code>. </p>
</dl>
<p> Invoke <code>resolve_stack_dump</code> like this: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; resolve_stack_dump[options] symbols_file[numeric_dump_file]
</code></pre>
</dl>
<p> The symbols file should include the output from the <code>nm &#8211;numeric-sort mysqld</code> command. The numeric dump file should contain a numeric stack track from <code>mysqld</code>. If no numeric dump file is named on the command line, the stack trace is read from the standard input. </p>
<p> <code>resolve_stack_dump</code> supports the following options. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-h</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;numeric-dump-file=</code><i>file_name</i>, <code>-n </code><i>file_name</i> </p>
<p> Read the stack trace from the given file.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;symbols-file=</code><i>file_name</i>, <code>-s </code><i>file_name</i> </p>
<p> Use the given symbols file.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code>, <code>-V</code> </p>
<p> Display version information and exit.</dl>
<p> For more information, see Section 28.5.1.5, &#8220;Using a Stack Trace&#8221;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1997, 2019, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
