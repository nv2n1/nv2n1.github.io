---
title: "replace(1)"
name: "replace"
section: "1"
letter: "r"
url: "/docs/linux/man/1-replace/"
description: "replace – a string-replacement utility"
---

<h2 class="name">NAME</h2>
<p> replace &#8211; a string-replacement utility </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>replace </code><i>arguments</i></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>replace</code> utility program changes strings in place in files or on the standard input. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> The <code>replace</code> utility is deprecated as of MySQL 5.7.18 and is removed in MySQL 8.0. </p>
</dl>
<p> Invoke <code>replace</code> in one of the following ways: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; replace fromto[fromto]... --file_name[file_name]... shell &gt; replace fromto[fromto]... &lt; file_name
</code></pre>
</dl>
<p> <i>from</i> represents a string to look for and <i>to</i> represents its replacement. There can be one or more pairs of strings. </p>
<p> Use the <code>&#8212;</code> option to indicate where the string-replacement list ends and the file names begin. In this case, any file named on the command line is modified in place, so you may want to make a copy of the original before converting it. <i>replace</i> prints a message indicating which of the input files it actually modifies. </p>
<p> If the <code>&#8212;</code> option is not given, <code>replace</code> reads the standard input and writes to the standard output. </p>
<p> <code>replace</code> uses a finite state machine to match longer strings first. It can be used to swap strings. For example, the following command swaps a and b in the given files, file1 and file2: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>replace a b b a -- file1 file2 ...</code>
</pre>
</dl>
<p> <code>replace</code> supports the following options. </p>
<dl>
<dt>
<dd> &bull; <code>-?</code>, <code>-I</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>-#</code><i>debug_options</i> </p>
<p> Enable debugging.</dl>
<dl>
<dt>
<dd> &bull; <code>-s</code> </p>
<p> Silent mode. Print less information what the program does.</dl>
<dl>
<dt>
<dd> &bull; <code>-v</code> </p>
<p> Verbose mode. Print more information about what the program does.</dl>
<dl>
<dt>
<dd> &bull; <code>-V</code> </p>
<p> Display version information and exit.</dl>
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
