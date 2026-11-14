---
title: "if_nametoindex(3)"
name: "if_nametoindex"
section: "3"
letter: "i"
url: "/docs/linux/man/3-if_nametoindex/"
description: "if_nametoindex, if_indextoname – mappings between network interface names and indexes"
---

<h2 class="name">NAME</h2>
<p> if_nametoindex, if_indextoname &#8211; mappings between network interface names and indexes </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;net/if.h&gt;
unsigned int if_nametoindex(const char *ifname);
char *if_indextoname(unsigned int ifindex, char *ifname);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>if_nametoindex</code>() function returns the index of the network interface corresponding to the name <i>ifname</i>. </p>
<p> The <code>if_indextoname</code>() function returns the name of the network interface corresponding to the interface index <i>ifindex</i>. The name is placed in the buffer pointed to by <i>ifname</i>. The buffer must allow for the storage of at least <code>IF_NAMESIZE</code> bytes.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>if_nametoindex</code>() returns the index number of the network interface; on error, 0 is returned and <i>errno</i> is set appropriately. </p>
<p> On success, <code>if_indextoname</code>() returns <i>ifname</i>; on error, NULL is returned and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> <code>if_nametoindex</code>() may fail and set <i>errno</i> if:</p>
<dl>
<dt><code>ENODEV</code></p>
<dd> No interface found with given name.</dl>
<p> <code>if_indextoname</code>() may fail and set <i>errno</i> if:</p>
<dl>
<dt><code>ENXIO</code></p>
<dd> No interface found for the index.</dl>
<p> <code>if_nametoindex</code>() and <code>if_indextoname</code>() may also fail for any of the errors specified for <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2) or <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2).</p>
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
<td> <code>if_nametoindex</code>(), <code>if_indextoname</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, RFC 3493. </p>
<p> This function first appeared in BSDi.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getifaddrs/">getifaddrs</a></code>(3), <code><a href="/docs/linux/man/3-if_nameindex/">if_nameindex</a></code>(3), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
