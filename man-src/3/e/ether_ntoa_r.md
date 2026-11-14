---
title: "ether_ntoa_r(3)"
name: "ether_ntoa_r"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ether_ntoa_r/"
description: "ether_aton, ether_ntoa, ether_ntohost, ether_hostton, ether_line, ether_ntoa_r, ether_aton_r – Ethernet address manipulation routines"
---

<h2 class="name">NAME</h2>
<p> ether_aton, ether_ntoa, ether_ntohost, ether_hostton, ether_line, ether_ntoa_r, ether_aton_r &#8211; Ethernet address manipulation routines </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;netinet/ether.h&gt;
char *ether_ntoa(const struct ether_addr *addr);
struct ether_addr *ether_aton(const char *asc);
int ether_ntohost(char *hostname, const struct ether_addr *addr);
int ether_hostton(const char *hostname, struct ether_addr *addr);
int ether_line(const char *line, struct ether_addr *addr,
               char *hostname);
/* GNU extensions */

char *ether_ntoa_r(const struct ether_addr *addr, char *buf);
struct ether_addr *ether_aton_r(const char *asc,
                                struct ether_addr *addr);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ether_aton</code>() converts the 48-bit Ethernet host address <i>asc</i> from the standard hex-digits-and-colons notation into binary data in network byte order and returns a pointer to it in a statically allocated buffer, which subsequent calls will overwrite. <code>ether_aton</code>() returns NULL if the address is invalid. </p>
<p> The <code>ether_ntoa</code>() function converts the Ethernet host address <i>addr</i> given in network byte order to a string in standard hex-digits-and-colons notation, omitting leading zeros. The string is returned in a statically allocated buffer, which subsequent calls will overwrite. </p>
<p> The <code>ether_ntohost</code>() function maps an Ethernet address to the corresponding hostname in <i>/etc/ethers</i> and returns nonzero if it cannot be found. </p>
<p> The <code>ether_hostton</code>() function maps a hostname to the corresponding Ethernet address in <i>/etc/ethers</i> and returns nonzero if it cannot be found. </p>
<p> The <code>ether_line</code>() function parses a line in <i>/etc/ethers</i> format (ethernet address followed by whitespace followed by hostname; &#8216;#&#8217; introduces a comment) and returns an address and hostname pair, or nonzero if it cannot be parsed. The buffer pointed to by <i>hostname</i> must be sufficiently long, for example, have the same length as <i>line</i>. </p>
<p> The functions <code>ether_ntoa_r</code>() and <code>ether_aton_r</code>() are reentrant thread-safe versions of <code>ether_ntoa</code>() and <code>ether_aton</code>() respectively, and do not use static buffers. </p>
<p> The structure <i>ether_addr</i> is defined in <i>&lt;net/ethernet.h&gt;</i> as: </p>
<p> struct ether_addr {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint8_t ether_addr_octet[6]; }</p>
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
<td> <code>ether_aton</code>(), <code>ether_ntoa</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe
</td>
</tr>
<tr VALIGN=top>
<td> <code>ether_ntohost</code>(), <code>ether_hostton</code>(), <code>ether_line</code>(), <code>ether_ntoa_r</code>(), <code>ether_aton_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> 4.3BSD, SunOS.</p>
<h2>BUGS</h2>
<p> In glibc 2.2.5 and earlier, the implementation of <code>ether_line</code>() is broken.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-ethers/">ethers</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
