---
title: "infadd(1)"
name: "infadd"
section: "1"
letter: "i"
url: "/docs/linux/man/1-infadd/"
description: "infadd – infinite additions to LDAP server"
---

<h2 class="name">NAME</h2>
<p> infadd &#8211; infinite additions to LDAP server </p>
<h2>SYNOPSIS</h2>
<p> <code>infadd</code> <i>-s suffix -u bindDN -w password </i>[<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> infadd is used to measure performance of the add operation. It can span multiple threads in order to test the performance under heavy locking. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h hostname</code></p>
<dd> hostname (default: localhost)</p>
<dt><code>-p port</code></p>
<dd> port (default: 389)</p>
<dt><code>-t threads</code></p>
<dd> number of threads to spin (default: 1)</p>
<dt><code>-d</code></p>
<dd> use TCP no-delay</p>
<dt><code>-q</code></p>
<dd> quiet mode (no status updates)</p>
<dt><code>-v</code></p>
<dd> verbose mode (give per-thread statistics)</p>
<dt><code>-I num</code></p>
<dd> first uid (default: 0)</p>
<dt><code>-l count</code></p>
<dd> limit count; stops when the total count exceeds &lt;count&gt;</p>
<dt><code>-i msec</code></p>
<dd> sample interval in milliseconds (default: 10000)</p>
<dt><code>-R size</code></p>
<dd> generate &lt;size&gt; random names instead of using data files</p>
<dt><code>-z size</code></p>
<dd> add binary blob of average size of &lt;size&gt; bytes</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rsearch/">rsearch</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> infadd was written by the 389 Project.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001 Sun Microsystems, Inc. Used by permission.<br />
 Copyright &#169; 2008 Red Hat, Inc.<br />
 This manual page was written by Michele Baldessari &lt;michele [at] pupazzo.org&gt;, for the Debian project (but may be used by others).<br />
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. This license is essentially the GNU General Public License version 2 with an exception for plug-in distribution. </p>
<h2>Index</h2>
