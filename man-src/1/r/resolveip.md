---
title: "resolveip(1)"
name: "resolveip"
section: "1"
letter: "r"
url: "/docs/linux/man/1-resolveip/"
description: "resolveip – resolve host name to IP address or vice versa"
---

<h2 class="name">NAME</h2>
<p> resolveip &#8211; resolve host name to IP address or vice versa </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>resolveip [</code><i>options</i><code>] {</code><i>host_name</i><code>|</code><i>ip-addr</i><code>} &#8230;</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>resolveip</code> utility resolves host names to IP addresses and vice versa. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> <code>resolveip</code> is deprecated and is removed in MySQL 8.0. <code>nslookup</code>, <code>host</code>, or <code>dig</code> can be used instead. </p>
</dl>
<p> Invoke <code>resolveip</code> like this: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; resolveip[options]{host_name | ip - addr}...
</code></pre>
</dl>
<p> <code>resolveip</code> supports the following options. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>&#8211;info</code>, <code>-?</code>, <code>-I</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;silent</code>, <code>-s</code> </p>
<p> Silent mode. Produce less output.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code>, <code>-V</code> </p>
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
