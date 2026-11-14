---
title: "zlib_decompress(1)"
name: "zlib_decompress"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zlib_decompress/"
description: "zlib_decompress – decompress mysqlpump ZLIB-compressed output"
---

<h2 class="name">NAME</h2>
<p> zlib_decompress &#8211; decompress mysqlpump ZLIB-compressed output </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>zlib_decompress </code><i>input_file</i><i>output_file</i></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>zlib_decompress</code> utility decompresses <code>mysqlpump</code> output that was created using ZLIB compression. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> If MySQL was configured with the <code>-DWITH_ZLIB=system</code> option, <code>zlib_decompress</code> is not built. In this case, the system <code>openssl zlib</code> command can be used instead. </p>
</dl>
<p> Invoke <code>zlib_decompress</code> like this: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>zlib_decompress </code><i>input_file</i><i>output_file</i>
</pre>
</dl>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysqlpump --compress-output=ZLIB &gt; dump.zlib</code>
shell&gt; <code>zlib_decompress dump.zlib dump.txt</code>
</pre>
</dl>
<p> To see a help message, invoke <code>zlib_decompress</code> with no arguments. </p>
<p> To decompress <code>mysqlpump</code> LZ4-compressed output, use <code>lz4_decompress</code>. See <code><a href="/docs/linux/man/1-lz4_decompress/">lz4_decompress</a></code>(1).</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1997, 2020, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
