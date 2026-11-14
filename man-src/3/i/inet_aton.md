---
title: "inet_aton(3)"
name: "inet_aton"
section: "3"
letter: "i"
url: "/docs/linux/man/3-inet_aton/"
description: "inet_aton, inet_addr, inet_network, inet_ntoa, inet_makeaddr, inet_lnaof, inet_netof – Internet address manipulation routines"
---

<h2 class="name">NAME</h2>
<p> inet_aton, inet_addr, inet_network, inet_ntoa, inet_makeaddr, inet_lnaof, inet_netof &#8211; Internet address manipulation routines </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;arpa/inet.h&gt;
#include &lt;netinet/in.h&gt;
#include &lt;sys/socket.h&gt;
int inet_aton(const char *cp, struct in_addr *inp);
in_addr_t inet_addr(const char *cp);
in_addr_t inet_network(const char *cp);
char *inet_ntoa(struct in_addr in);
struct in_addr inet_makeaddr(in_addr_t net, in_addr_t host);
in_addr_t inet_lnaof(struct in_addr in);
in_addr_t inet_netof(struct in_addr in);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>inet_aton</code>(), <code>inet_ntoa</code>(): </p>
<pre>
    Since glibc 2.19:
        _DEFAULT_SOURCE
    In glibc up to and including 2.19:
        _BSD_SOURCE || _BSD_SOURCE
</pre>
<h2>DESCRIPTION</h2>
<p> <code>inet_aton</code>() converts the Internet host address <i>cp</i> from the IPv4 numbers-and-dots notation into binary form (in network byte order) and stores it in the structure that <i>inp</i> points to. <code>inet_aton</code>() returns nonzero if the address is valid, zero if not. The address supplied in <i>cp</i> can have one of the following forms:</p>
<dl>
<dt><i>a.b.c.d</i></p>
<dd> Each of the four numeric parts specifies a byte of the address; the bytes are assigned in left-to-right order to produce the binary address.</p>
<dt><i>a.b.c</i></p>
<dd> Parts <i>a</i> and <i>b</i> specify the first two bytes of the binary address. Part <i>c</i> is interpreted as a 16-bit value that defines the rightmost two bytes of the binary address. This notation is suitable for specifying (outmoded) Class B network addresses.</p>
<dt><i>a.b</i></p>
<dd> Part <i>a</i> specifies the first byte of the binary address. Part <i>b</i> is interpreted as a 24-bit value that defines the rightmost three bytes of the binary address. This notation is suitable for specifying (outmoded) Class A network addresses.</p>
<dt><i>a</i></p>
<dd> The value <i>a</i> is interpreted as a 32-bit value that is stored directly into the binary address without any byte rearrangement.</dl>
<p> In all of the above forms, components of the dotted address can be specified in decimal, octal (with a leading <i>0</i>), or hexadecimal, with a leading <i>0X</i>). Addresses in any of these forms are collectively termed <i>IPV4 numbers-and-dots notation</i>. The form that uses exactly four decimal numbers is referred to as <i>IPv4 dotted-decimal notation</i> (or sometimes: <i>IPv4 dotted-quad notation</i>). </p>
<p> <code>inet_aton</code>() returns 1 if the supplied string was successfully interpreted, or 0 if the string is invalid (<code>errno</code> is <i>not</i> set on error). </p>
<p> The <code>inet_addr</code>() function converts the Internet host address <i>cp</i> from IPv4 numbers-and-dots notation into binary data in network byte order. If the input is invalid, <code>INADDR_NONE</code> (usually -1) is returned. Use of this function is problematic because -1 is a valid address (255.255.255.255). Avoid its use in favor of <code>inet_aton</code>(), <code><a href="/docs/linux/man/3-inet_pton/">inet_pton</a></code>(3), or <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3), which provide a cleaner way to indicate error return. </p>
<p> The <code>inet_network</code>() function converts <i>cp</i>, a string in IPv4 numbers-and-dots notation, into a number in host byte order suitable for use as an Internet network address. On success, the converted address is returned. If the input is invalid, -1 is returned. </p>
<p> The <code>inet_ntoa</code>() function converts the Internet host address <i>in</i>, given in network byte order, to a string in IPv4 dotted-decimal notation. The string is returned in a statically allocated buffer, which subsequent calls will overwrite. </p>
<p> The <code>inet_lnaof</code>() function returns the local network address part of the Internet address <i>in</i>. The returned value is in host byte order. </p>
<p> The <code>inet_netof</code>() function returns the network number part of the Internet address <i>in</i>. The returned value is in host byte order. </p>
<p> The <code>inet_makeaddr</code>() function is the converse of <code>inet_netof</code>() and <code>inet_lnaof</code>(). It returns an Internet host address in network byte order, created by combining the network number <i>net</i> with the local address <i>host</i>, both in host byte order. </p>
<p> The structure <i>in_addr</i> as used in <code>inet_ntoa</code>(), <code>inet_makeaddr</code>(), <code>inet_lnaof</code>(), and <code>inet_netof</code>() is defined in <i>&lt;netinet/in.h&gt;</i> as: </p>
<p> typedef uint32_t in_addr_t; </p>
<p> struct in_addr {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in_addr_t s_addr; };</p>
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
<td> <code>inet_aton</code>(), <code>inet_addr</code>(),<br />
 <code>inet_network</code>(), <code>inet_ntoa</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>inet_makeaddr</code>(), <code>inet_lnaof</code>(),<br />
 <code>inet_netof</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>inet_addr</code>(), <code>inet_ntoa</code>(): POSIX.1-2001, POSIX.1-2008, 4.3BSD. </p>
<p> <code>inet_aton</code>() is not specified in POSIX.1, but is available on most systems.</p>
<h2>NOTES</h2>
<p> On x86 architectures, the host byte order is Least Significant Byte first (little endian), whereas the network byte order, as used on the Internet, is Most Significant Byte first (big endian). </p>
<p> <code>inet_lnaof</code>(), <code>inet_netof</code>(), and <code>inet_makeaddr</code>() are legacy functions that assume they are dealing with <i>classful network addresses</i>. Classful networking divides IPv4 network addresses into host and network components at byte boundaries, as follows:</p>
<dl>
<dt>Class A</p>
<dd> This address type is indicated by the value 0 in the most significant bit of the (network byte ordered) address. The network address is contained in the most significant byte, and the host address occupies the remaining three bytes.</p>
<dt>Class B</p>
<dd> This address type is indicated by the binary value 10 in the most significant two bits of the address. The network address is contained in the two most significant bytes, and the host address occupies the remaining two bytes.</p>
<dt>Class C</p>
<dd> This address type is indicated by the binary value 110 in the most significant three bits of the address. The network address is contained in the three most significant bytes, and the host address occupies the remaining byte.</dl>
<p> Classful network addresses are now obsolete, having been superseded by Classless Inter-Domain Routing (CIDR), which divides addresses into network and host components at arbitrary bit (rather than byte) boundaries.</p>
<h2>EXAMPLES</h2>
<p> An example of the use of <code>inet_aton</code>() and <code>inet_ntoa</code>() is shown below. Here are some example runs: </p>
<p> $<code> ./a.out 226.000.000.037</code> # Last byte is in octal 226.0.0.31 $<code> ./a.out 0x7f.1 </code> # First byte is in hex 127.0.0.1</p>
<h3>Program source</h3>
<p> #define _BSD_SOURCE #include &lt;arpa/inet.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct in_addr addr; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;%s&nbsp;&lt;dotted-address&gt;
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(inet_aton(argv[1],&nbsp;&amp;addr)&nbsp;==&nbsp;0)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Invalid address
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%s
&quot;, inet_ntoa(addr));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-byteorder/">byteorder</a></code>(3), <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3), <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3), <code><a href="/docs/linux/man/3-getnameinfo/">getnameinfo</a></code>(3), <code><a href="/docs/linux/man/3-getnetent/">getnetent</a></code>(3), <code><a href="/docs/linux/man/3-inet_net_pton/">inet_net_pton</a></code>(3), <code><a href="/docs/linux/man/3-inet_ntop/">inet_ntop</a></code>(3), <code><a href="/docs/linux/man/3-inet_pton/">inet_pton</a></code>(3), <code><a href="/docs/linux/man/5-hosts/">hosts</a></code>(5), <code><a href="/docs/linux/man/5-networks/">networks</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
