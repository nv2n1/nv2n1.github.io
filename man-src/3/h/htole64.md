---
title: "htole64(3)"
name: "htole64"
section: "3"
letter: "h"
url: "/docs/linux/man/3-htole64/"
description: "htobe16, htole16, be16toh, le16toh, htobe32, htole32, be32toh, le32toh, htobe64, htole64, be64toh, le64toh – convert values between host and big-/little-endian byte order"
---

<h2 class="name">NAME</h2>
<p> htobe16, htole16, be16toh, le16toh, htobe32, htole32, be32toh, le32toh, htobe64, htole64, be64toh, le64toh &#8211; convert values between host and big-/little-endian byte order </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;endian.h&gt;
uint16_t htobe16(uint16_t host_16bits);
uint16_t htole16(uint16_t host_16bits);
uint16_t be16toh(uint16_t big_endian_16bits);
uint16_t le16toh(uint16_t little_endian_16bits);
uint32_t htobe32(uint32_t host_32bits);
uint32_t htole32(uint32_t host_32bits);
uint32_t be32toh(uint32_t big_endian_32bits);
uint32_t le32toh(uint32_t little_endian_32bits);
uint64_t htobe64(uint64_t host_64bits);
uint64_t htole64(uint64_t host_64bits);
uint64_t be64toh(uint64_t big_endian_64bits);
uint64_t le64toh(uint64_t little_endian_64bits);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>htobe16</code>(), <code>htole16</code>(), <code>be16toh</code>(), <code>le16toh</code>(), <code>htobe32</code>(), <code>htole32</code>(), <code>be32toh</code>(), <code>le32toh</code>(), <code>htobe64</code>(), <code>htole64</code>(), <code>be64toh</code>(), <code>le64toh</code>(): </p>
<pre>
    Since glibc 2.19:
        _DEFAULT_SOURCE
    In glibc up to and including 2.19:
        _BSD_SOURCE
</pre>
<h2>DESCRIPTION</h2>
<p> These functions convert the byte encoding of integer values from the byte order that the current CPU (the &quot;host&quot;) uses, to and from little-endian and big-endian byte order. </p>
<p> The number, <i>nn</i>, in the name of each function indicates the size of integer handled by the function, either 16, 32, or 64 bits. </p>
<p> The functions with names of the form &quot;htobe<i>nn</i>&quot; convert from host byte order to big-endian order. </p>
<p> The functions with names of the form &quot;htole<i>nn</i>&quot; convert from host byte order to little-endian order. </p>
<p> The functions with names of the form &quot;be<i>nn</i>toh&quot; convert from big-endian order to host byte order. </p>
<p> The functions with names of the form &quot;le<i>nn</i>toh&quot; convert from little-endian order to host byte order.</p>
<h2>VERSIONS</h2>
<p> These functions were added to glibc in version 2.9.</p>
<h2>CONFORMING TO</h2>
<p> These functions are nonstandard. Similar functions are present on the BSDs, where the required header file is <i>&lt;sys/endian.h&gt;</i> instead of <i>&lt;endian.h&gt;</i>. Unfortunately, NetBSD, FreeBSD, and glibc haven&#8217;t followed the original OpenBSD naming convention for these functions, whereby the <i>nn</i> component always appears at the end of the function name (thus, for example, in NetBSD, FreeBSD, and glibc, the equivalent of OpenBSDs &quot;betoh32&quot; is &quot;be32toh&quot;).</p>
<h2>NOTES</h2>
<p> These functions are similar to the older <code><a href="/docs/linux/man/3-byteorder/">byteorder</a></code>(3) family of functions. For example, <code>be32toh</code>() is identical to <code>ntohl</code>(). </p>
<p> The advantage of the <code><a href="/docs/linux/man/3-byteorder/">byteorder</a></code>(3) functions is that they are standard functions available on all UNIX systems. On the other hand, the fact that they were designed for use in the context of TCP/IP means that they lack the 64-bit and little-endian variants described in this page.</p>
<h2>EXAMPLES</h2>
<p> The program below display the results of converting an integer from host byte order to both little-endian and big-endian byte order. Since host byte order is either little-endian or big-endian, only one of these conversions will have an effect. When we run this program on a little-endian system such as x86-32, we see the following: </p>
<p> $ <code>./a.out</code> x.u32 = 0x44332211 htole32(x.u32) = 0x44332211 htobe32(x.u32) = 0x11223344</p>
<h3>Program source</h3>
<p> #include &lt;endian.h&gt; #include &lt;stdint.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t u32;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint8_t arr[4];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;x; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x.arr[0]&nbsp;=&nbsp;0x11;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>/*&nbsp;Lowest-address byte&nbsp;*/</p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x.arr[1]&nbsp;=&nbsp;0x22;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x.arr[2]&nbsp;=&nbsp;0x33;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x.arr[3]&nbsp;=&nbsp;0x44;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>/*&nbsp;Highest-address byte&nbsp;*/</p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;x.u32&nbsp;=&nbsp;%#x
&quot;, x.u32);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;htole32(x.u32)&nbsp;=&nbsp;%#x
&quot;, htole32(x.u32));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;htobe32(x.u32)&nbsp;=&nbsp;%#x
&quot;, htobe32(x.u32)); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bswap/">bswap</a></code>(3), <code><a href="/docs/linux/man/3-byteorder/">byteorder</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
