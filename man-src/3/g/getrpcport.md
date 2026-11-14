---
title: "getrpcport(3)"
name: "getrpcport"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getrpcport/"
description: "getrpcport – get RPC port number"
---

<h2 class="name">NAME</h2>
<p> getrpcport &#8211; get RPC port number </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;rpc/rpc.h&gt;
int getrpcport(const char *host, unsigned long prognum,
               unsigned long versnum, unsigned proto);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>getrpcport</code>() returns the port number for version <i>versnum</i> of the RPC program <i>prognum</i> running on <i>host</i> and using protocol <i>proto</i>. It returns 0 if it cannot contact the portmapper, or if <i>prognum</i> is not registered. If <i>prognum</i> is registered but not with version <i>versnum</i>, it will still return a port number (for some version of the program) indicating that the program is indeed registered. The version mismatch will be detected upon the first call to the service.</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>getrpcport</code>() </td>
<td>Thread safety</td>
<td>MT-Safe env locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> Not in POSIX.1. Present on the BSDs, Solaris, and many other systems.</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
