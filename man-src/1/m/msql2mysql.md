---
title: "msql2mysql(1)"
name: "msql2mysql"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msql2mysql/"
description: "msql2mysql – convert mSQL programs for use with MySQL"
---

<h2 class="name">NAME</h2>
<p> msql2mysql &#8211; convert mSQL programs for use with MySQL </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>msql2mysql</code><i>C-source-file</i><code> &#8230;</code></dl>
<h2>DESCRIPTION</h2>
<dd>Initially, the MySQL C API was developed to be very similar to that for the mSQL database system. Because of this, mSQL programs often can be converted relatively easily for use with MySQL by changing the names of the C API functions. </p>
<p> The <code>msql2mysql</code> utility performs the conversion of mSQL C API function calls to their MySQL equivalents. <code>msql2mysql</code> converts the input file in place, so make a copy of the original before converting it. For example, use <code>msql2mysql</code> like this: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>cp client-prog.c client-prog.c.orig</code>
shell&gt; <code>msql2mysql client-prog.c</code>
client-prog.c converted
</pre>
</dl>
<p> Then examine client-prog.c and make any post-conversion revisions that may be necessary. </p>
<p> <code>msql2mysql</code> uses the <code>replace</code> utility to make the function name substitutions. See <code><a href="/docs/linux/man/1-replace/">replace</a></code>(1).</p>
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
