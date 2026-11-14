---
title: "lwres_getnameinfo(3)"
name: "lwres_getnameinfo"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lwres_getnameinfo/"
description: "lwres_getnameinfo – lightweight resolver socket address structure to hostname and service name"
---

<h2 class="name">NAME</h2>
<p> lwres_getnameinfo &#8211; lightweight resolver socket address structure to hostname and service name </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;lwres/netdb.h&gt;
</code></pre>
<dl>
<dt> <code>int lwres_getnameinfo(const struct sockaddr&nbsp;<wbr>*</code><i>sa</i><code>, size_t&nbsp;<wbr></code><i>salen</i><code>, char&nbsp;<wbr>*</code><i>host</i><code>, size_t&nbsp;<wbr></code><i>hostlen</i><code>, char&nbsp;<wbr>*</code><i>serv</i><code>, size_t&nbsp;<wbr></code><i>servlen</i><code>, int&nbsp;<wbr></code><i>flags</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>This function is equivalent to the <code><a href="/docs/linux/man/3-getnameinfo/">getnameinfo</a></code>(3) function defined in RFC2133. <code>lwres_getnameinfo()</code> returns the hostname for the <code>struct sockaddr</code> <i>sa</i> which is <i>salen</i> bytes long. The hostname is of length <i>hostlen</i> and is returned via <i>*host.</i> The maximum length of the hostname is 1025 bytes: <code>NI_MAXHOST</code>. </p>
<p> The name of the service associated with the port number in <i>sa</i> is returned in <i>*serv.</i> It is <i>servlen</i> bytes long. The maximum length of the service name is <code>NI_MAXSERV</code> &#8211; 32 bytes. </p>
<p> The <i>flags</i> argument sets the following bits: </p>
<p> <code>NI_NOFQDN</code></p>
<dl>
<dt>
<dd> A fully qualified domain name is not required for local hosts. The local part of the fully qualified domain name is returned instead.</dl>
<p> <code>NI_NUMERICHOST</code></p>
<dl>
<dt>
<dd> Return the address in numeric form, as if calling inet_ntop(), instead of a host name.</dl>
<p> <code>NI_NAMEREQD</code></p>
<dl>
<dt>
<dd> A name is required. If the hostname cannot be found in the DNS and this flag is set, a non-zero error code is returned. If the hostname is not found and the flag is not set, the address is returned in numeric form.</dl>
<p> <code>NI_NUMERICSERV</code></p>
<dl>
<dt>
<dd> The service name is returned as a digit string representing the port number.</dl>
<p> <code>NI_DGRAM</code></p>
<dl>
<dt>
<dd> Specifies that the service being looked up is a datagram service, and causes getservbyport() to be called with a second argument of &quot;udp&quot; instead of its default of &quot;tcp&quot;. This is required for the few ports (512-514) that have different services for UDP and TCP.</dl>
<h2>RETURN VALUES</h2>
<p> <code>lwres_getnameinfo()</code> returns 0 on success or a non-zero error code if an error occurs.</p>
<h2>SEE ALSO</h2>
<p> <code>RFC2133</code>(), <code><a href="/docs/linux/man/3-getservbyport/">getservbyport</a></code>(3), <code><a href="/docs/linux/man/3-lwres/">lwres</a></code>(3), <code><a href="/docs/linux/man/3-lwres_getnameinfo/">lwres_getnameinfo</a></code>(3), <code><a href="/docs/linux/man/3-lwres_getnamebyaddr/">lwres_getnamebyaddr</a></code>(3). <code><a href="/docs/linux/man/3-lwres_net_ntop/">lwres_net_ntop</a></code>(3).</p>
<h2>BUGS</h2>
<p> RFC2133 fails to define what the nonzero return values of <code><a href="/docs/linux/man/3-getnameinfo/">getnameinfo</a></code>(3) are.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004, 2005, 2007 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000, 2001 Internet Software Consortium. </p>
<h2>Index</h2>
