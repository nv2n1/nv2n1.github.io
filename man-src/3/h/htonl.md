---
title: "htonl(3)"
name: "htonl"
section: "3"
letter: "h"
url: "/docs/linux/man/3-htonl/"
description: "htonl, htons, ntohl, ntohs – convert values between host and network byte order"
---

<h2 class="name">NAME</h2>
<p> htonl, htons, ntohl, ntohs &#8211; convert values between host and network byte order </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;arpa/inet.h&gt;
uint32_t htonl(uint32_t hostlong);
uint16_t htons(uint16_t hostshort);
uint32_t ntohl(uint32_t netlong);
uint16_t ntohs(uint16_t netshort);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>htonl</code>() function converts the unsigned integer <i>hostlong</i> from host byte order to network byte order. </p>
<p> The <code>htons</code>() function converts the unsigned short integer <i>hostshort</i> from host byte order to network byte order. </p>
<p> The <code>ntohl</code>() function converts the unsigned integer <i>netlong</i> from network byte order to host byte order. </p>
<p> The <code>ntohs</code>() function converts the unsigned short integer <i>netshort</i> from network byte order to host byte order. </p>
<p> On the i386 the host byte order is Least Significant Byte first, whereas the network byte order, as used on the Internet, is Most Significant Byte first.</p>
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
<td> <code>htonl</code>(), <code>htons</code>(), <code>ntohl</code>(), <code>ntohs</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008. </p>
<p> Some systems require the inclusion of <i>&lt;netinet/in.h&gt;</i> instead of <i>&lt;arpa/inet.h&gt;</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bswap/">bswap</a></code>(3), <code><a href="/docs/linux/man/3-endian/">endian</a></code>(3), <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3), <code><a href="/docs/linux/man/3-getservent/">getservent</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
