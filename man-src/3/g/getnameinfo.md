---
title: "getnameinfo(3)"
name: "getnameinfo"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getnameinfo/"
description: "getnameinfo – address-to-name translation in protocol-independent manner"
---

<h2 class="name">NAME</h2>
<p> getnameinfo &#8211; address-to-name translation in protocol-independent manner </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;netdb.h&gt;
#include &lt;sys/socket.h&gt;
int getnameinfo(const struct sockaddr *addr, socklen_t addrlen,
                char *host, socklen_t hostlen,
                char *serv, socklen_t servlen, int flags);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getnameinfo</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.22:&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.21 and earlier:&nbsp;_POSIX_C_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>getnameinfo</code>() function is the inverse of <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3): it converts a socket address to a corresponding host and service, in a protocol-independent manner. It combines the functionality of <code><a href="/docs/linux/man/3-gethostbyaddr/">gethostbyaddr</a></code>(3) and <code><a href="/docs/linux/man/3-getservbyport/">getservbyport</a></code>(3), but unlike those functions, <code>getnameinfo</code>() is reentrant and allows programs to eliminate IPv4-versus-IPv6 dependencies. </p>
<p> The <i>addr</i> argument is a pointer to a generic socket address structure (of type <i>sockaddr_in</i> or <i>sockaddr_in6</i>) of size <i>addrlen</i> that holds the input IP address and port number. The arguments <i>host</i> and <i>serv</i> are pointers to caller-allocated buffers (of size <i>hostlen</i> and <i>servlen</i> respectively) into which <code>getnameinfo</code>() places null-terminated strings containing the host and service names respectively. </p>
<p> The caller can specify that no hostname (or no service name) is required by providing a NULL <i>host</i> (or <i>serv</i>) argument or a zero <i>hostlen</i> (or <i>servlen</i>) argument. However, at least one of hostname or service name must be requested. </p>
<p> The <i>flags</i> argument modifies the behavior of <code>getnameinfo</code>() as follows:</p>
<dl>
<dt><code>NI_NAMEREQD</code></p>
<dd> If set, then an error is returned if the hostname cannot be determined.</p>
<dt><code>NI_DGRAM</code></p>
<dd> If set, then the service is datagram (UDP) based rather than stream (TCP) based. This is required for the few ports (512-514) that have different services for UDP and TCP.</p>
<dt><code>NI_NOFQDN</code></p>
<dd> If set, return only the hostname part of the fully qualified domain name for local hosts.</p>
<dt><code>NI_NUMERICHOST</code></p>
<dd> If set, then the numeric form of the hostname is returned. (When not set, this will still happen in case the node&#8217;s name cannot be determined.)</p>
<dt><code>NI_NUMERICSERV</code></p>
<dd> If set, then the numeric form of the service address is returned. (When not set, this will still happen in case the service&#8217;s name cannot be determined.)</dl>
<h3>Extensions to getnameinfo() for Internationalized Domain Names</h3>
<p> Starting with glibc 2.3.4, <code>getnameinfo</code>() has been extended to selectively allow hostnames to be transparently converted to and from the Internationalized Domain Name (IDN) format (see RFC 3490, <i>Internationalizing Domain Names in Applications (IDNA)</i>). Three new flags are defined:</p>
<dl>
<dt><code>NI_IDN</code></p>
<dd> If this flag is used, then the name found in the lookup process is converted from IDN format to the locale&#8217;s encoding if necessary. ASCII-only names are not affected by the conversion, which makes this flag usable in existing programs and environments.</p>
<dt><code>NI_IDN_ALLOW_UNASSIGNED</code>, <code>NI_IDN_USE_STD3_ASCII_RULES</code></p>
<dd> Setting these flags will enable the IDNA_ALLOW_UNASSIGNED (allow unassigned Unicode code points) and IDNA_USE_STD3_ASCII_RULES (check output to make sure it is a STD3 conforming hostname) flags respectively to be used in the IDNA handling.</dl>
<h2>RETURN VALUE</h2>
<p> On success, 0 is returned, and node and service names, if requested, are filled with null-terminated strings, possibly truncated to fit the specified buffer lengths. On error, one of the following nonzero error codes is returned:</p>
<dl>
<dt><code>EAI_AGAIN</code></p>
<dd> The name could not be resolved at this time. Try again later.</p>
<dt><code>EAI_BADFLAGS</code></p>
<dd> The <i>flags</i> argument has an invalid value.</p>
<dt><code>EAI_FAIL</code></p>
<dd> A nonrecoverable error occurred.</p>
<dt><code>EAI_FAMILY</code></p>
<dd> The address family was not recognized, or the address length was invalid for the specified family.</p>
<dt><code>EAI_MEMORY</code></p>
<dd> Out of memory.</p>
<dt><code>EAI_NONAME</code></p>
<dd> The name does not resolve for the supplied arguments. <code>NI_NAMEREQD</code> is set and the host&#8217;s name cannot be located, or neither hostname nor service name were requested.</p>
<dt><code>EAI_OVERFLOW</code></p>
<dd> The buffer pointed to by <i>host</i> or <i>serv</i> was too small.</p>
<dt><code>EAI_SYSTEM</code></p>
<dd> A system error occurred. The error code can be found in <i>errno</i>.</dl>
<p> The <code><a href="/docs/linux/man/3-gai_strerror/">gai_strerror</a></code>(3) function translates these error codes to a human readable string, suitable for error reporting.</p>
<h2>FILES</h2>
<p> <i>/etc/hosts</i><br />
 <i>/etc/nsswitch.conf</i><br />
 <i>/etc/resolv.conf</i></p>
<h2>VERSIONS</h2>
<p> <code>getnameinfo</code>() is provided in glibc since version 2.1.</p>
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
<td> <code>getnameinfo</code>() </td>
<td>Thread safety</td>
<td>MT-Safe env locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, RFC 2553.</p>
<h2>NOTES</h2>
<p> In order to assist the programmer in choosing reasonable sizes for the supplied buffers, <i>&lt;netdb.h&gt;</i> defines the constants </p>
<p> #define NI_MAXHOST 1025 #define NI_MAXSERV 32 </p>
<p> Since glibc 2.8, these definitions are exposed only if suitable feature test macros are defined, namely: <code>_GNU_SOURCE</code>, <code>_DEFAULT_SOURCE</code> (since glibc 2.19), or (in glibc versions up to and including 2.19) <code>_BSD_SOURCE</code> or <code>_SVID_SOURCE</code>. </p>
<p> The former is the constant <code>MAXDNAME</code> in recent versions of BIND&#8217;s <i>&lt;arpa/nameser.h&gt;</i> header file. The latter is a guess based on the services listed in the current Assigned Numbers RFC. </p>
<p> Before glibc version 2.2, the <i>hostlen</i> and <i>servlen</i> arguments were typed as <i>size_t</i>.</p>
<h2>EXAMPLES</h2>
<p> The following code tries to get the numeric hostname and service name, for a given socket address. Note that there is no hardcoded reference to a particular address family. </p>
<p> struct sockaddr *addr; /* input */ socklen_t addrlen; /* input */ char hbuf[NI_MAXHOST], sbuf[NI_MAXSERV]; </p>
<p> if (getnameinfo(addr, addrlen, hbuf, sizeof(hbuf), sbuf,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sizeof(sbuf), NI_NUMERICHOST | NI_NUMERICSERV)&nbsp;==&nbsp;0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;host=%s, serv=%s
&quot;, hbuf, sbuf); </p>
<p> The following version checks if the socket address has a reverse address mapping. </p>
<p> struct sockaddr *addr; /* input */ socklen_t addrlen; /* input */ char hbuf[NI_MAXHOST]; </p>
<p> if (getnameinfo(addr, addrlen, hbuf, sizeof(hbuf),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;NULL, 0, NI_NAMEREQD))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;could not resolve hostname&quot;); else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;host=%s
&quot;, hbuf); </p>
<p> An example program using <code>getnameinfo</code>() can be found in <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2), <code><a href="/docs/linux/man/2-getpeername/">getpeername</a></code>(2), <code><a href="/docs/linux/man/2-getsockname/">getsockname</a></code>(2), <code><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3), <code><a href="/docs/linux/man/3-gethostbyaddr/">gethostbyaddr</a></code>(3), <code><a href="/docs/linux/man/3-getservbyname/">getservbyname</a></code>(3), <code><a href="/docs/linux/man/3-getservbyport/">getservbyport</a></code>(3), <code><a href="/docs/linux/man/3-inet_ntop/">inet_ntop</a></code>(3), <code><a href="/docs/linux/man/5-hosts/">hosts</a></code>(5), <code><a href="/docs/linux/man/5-services/">services</a></code>(5), <code><a href="/docs/linux/man/7-hostname/">hostname</a></code>(7), <code><a href="/docs/linux/man/8-named/">named</a></code>(8) </p>
<p> R. Gilligan, S. Thomson, J. Bound and W. Stevens, <i>Basic Socket Interface Extensions for IPv6</i>, RFC 2553, March 1999. </p>
<p> Tatsuya Jinmei and Atsushi Onoe, <i>An Extension of Format for IPv6 Scoped Addresses</i>, internet draft, work in progress </p>
<p> Craig Metz, <i>Protocol Independence Using the Sockets API</i>, Proceedings of the freenix track: 2000 USENIX annual technical conference, June 2000</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
