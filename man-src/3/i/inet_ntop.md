---
title: "inet_ntop(3)"
name: "inet_ntop"
section: "3"
letter: "i"
url: "/docs/linux/man/3-inet_ntop/"
description: "inet_ntop – convert IPv4 and IPv6 addresses from binary to text form"
---

<h2 class="name">NAME</h2>
<p> inet_ntop &#8211; convert IPv4 and IPv6 addresses from binary to text form </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;arpa/inet.h&gt;
const char *inet_ntop(int af, const void *src,
                      char *dst, socklen_t size);
</code></pre>
<h2>DESCRIPTION</h2>
<p> This function converts the network address structure <i>src</i> in the <i>af</i> address family into a character string. The resulting string is copied to the buffer pointed to by <i>dst</i>, which must be a non-null pointer. The caller specifies the number of bytes available in this buffer in the argument <i>size</i>. </p>
<p> <code>inet_ntop</code>() extends the <code><a href="/docs/linux/man/3-inet_ntoa/">inet_ntoa</a></code>(3) function to support multiple address families, <code><a href="/docs/linux/man/3-inet_ntoa/">inet_ntoa</a></code>(3) is now considered to be deprecated in favor of <code>inet_ntop</code>(). The following address families are currently supported:</p>
<dl>
<dt><code>AF_INET</code></p>
<dd> <i>src</i> points to a <i>struct in_addr</i> (in network byte order) which is converted to an IPv4 network address in the dotted-decimal format, &quot;<i>ddd.ddd.ddd.ddd</i>&quot;. The buffer <i>dst</i> must be at least <code>INET_ADDRSTRLEN</code> bytes long.</p>
<dt><code>AF_INET6</code></p>
<dd> <i>src</i> points to a <i>struct in6_addr</i> (in network byte order) which is converted to a representation of this address in the most appropriate IPv6 network address format for this address. The buffer <i>dst</i> must be at least <code>INET6_ADDRSTRLEN</code> bytes long.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>inet_ntop</code>() returns a non-null pointer to <i>dst</i>. NULL is returned if there was an error, with <i>errno</i> set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAFNOSUPPORT</code></p>
<dd> <i>af</i> was not a valid address family.</p>
<dt><code>ENOSPC</code></p>
<dd> The converted address string would exceed the size given by <i>size</i>.</dl>
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
<td> <code>inet_ntop</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008. Note that RFC 2553 defines a prototype where the last argument <i>size</i> is of type <i>size_t</i>. Many systems follow RFC 2553. Glibc 2.0 and 2.1 have <i>size_t</i>, but 2.2 and later have <i>socklen_t</i>.</p>
<h2>BUGS</h2>
<p> <code>AF_INET6</code> converts IPv4-mapped IPv6 addresses into an IPv6 format.</p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/3-inet_pton/">inet_pton</a></code>(3).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getnameinfo/">getnameinfo</a></code>(3), <code><a href="/docs/linux/man/3-inet/">inet</a></code>(3), <code><a href="/docs/linux/man/3-inet_pton/">inet_pton</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
