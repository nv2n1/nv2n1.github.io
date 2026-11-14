---
title: "lz4_decompress(1)"
name: "lz4_decompress"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lz4_decompress/"
description: "lz4_decompress – decompress mysqlpump LZ4-compressed output"
---

<h2 class="name">NAME</h2>
<p> lz4_decompress &#8211; decompress mysqlpump LZ4-compressed output </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>lz4_decompress </code><i>input_file</i><i>output_file</i></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>lz4_decompress</code> utility decompresses <code>mysqlpump</code> output that was created using LZ4 compression. <code>lz4_decompress</code> was added in MySQL 5.7.10. </p>
<p> Invoke <code>lz4_decompress</code> like this: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>lz4_decompress </code><i>input_file</i><i>output_file</i>
</pre>
</dl>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlpump --compress-output=LZ4 &gt; dump.lz4</code>
shell&gt; <code>lz4_decompress dump.lz4 dump.txt</code>
</pre>
</dl>
<p> To see a help message, invoke <code>lz4_decompress</code> with no arguments. </p>
<p> To decompress <code>mysqlpump</code> ZLIB-compressed output, use <code>zlib_decompress</code>. See <code><a href="/docs/linux/man/1-zlib_decompress/">zlib_decompress</a></code>(1).</p>
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
