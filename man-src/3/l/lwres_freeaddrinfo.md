---
title: "lwres_freeaddrinfo(3)"
name: "lwres_freeaddrinfo"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lwres_freeaddrinfo/"
description: "lwres_getaddrinfo, lwres_freeaddrinfo – socket address structure to host and service name"
---

<h2 class="name">NAME</h2>
<p> lwres_getaddrinfo, lwres_freeaddrinfo &#8211; socket address structure to host and service name </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;lwres/netdb.h&gt;
</code></pre>
<dl>
<dt> <code>int lwres_getaddrinfo(const char&nbsp;<wbr>*</code><i>hostname</i><code>, const char&nbsp;<wbr>*</code><i>servname</i><code>, const struct addrinfo&nbsp;<wbr>*</code><i>hints</i><code>, struct addrinfo&nbsp;<wbr>**</code><i>res</i><code>);</code></p>
<dt> <code>void lwres_freeaddrinfo(struct addrinfo&nbsp;<wbr>*</code><i>ai</i><code>);</code></dl>
<dd>If the operating system does not provide a <code>struct addrinfo</code>, the following structure is used: </p>
<dl>
<dt>
<dd>
<pre><code>
struct addrinfo {
    int ai_flags;             /* AI_PASSIVE, AI_CANONNAME */
    int ai_family;            /* PF_xxx */
    int ai_socktype;          /* SOCK_xxx */
    int ai_protocol;          /* 0 or IPPROTO_xxx for IPv4 and IPv6 */
    size_t ai_addrlen;        /* length of ai_addr */
    char *ai_canonname;       /* canonical name for hostname */
    struct sockaddr *ai_addr; /* binary address */
    struct addrinfo *ai_next; /* next structure in linked list */
};
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>lwres_getaddrinfo()</code> is used to get a list of IP addresses and port numbers for host <i>hostname</i> and service <i>servname</i>. The function is the lightweight resolver&#8217;s implementation of <code>getaddrinfo()</code> as defined in RFC2133. <i>hostname</i> and <i>servname</i> are pointers to null-terminated strings or <code>NULL</code>. <i>hostname</i> is either a host name or a numeric host address string: a dotted decimal IPv4 address or an IPv6 address. <i>servname</i> is either a decimal port number or a service name as listed in <i>/etc/services</i>. </p>
<p> <i>hints</i> is an optional pointer to a <code>struct addrinfo</code>. This structure can be used to provide hints concerning the type of socket that the caller supports or wishes to use. The caller can supply the following structure elements in <i>*hints</i>: </p>
<p> <code>ai_family</code></p>
<dl>
<dt>
<dd> The protocol family that should be used. When <code>ai_family</code> is set to <code>PF_UNSPEC</code>, it means the caller will accept any protocol family supported by the operating system.</dl>
<p> <code>ai_socktype</code></p>
<dl>
<dt>
<dd> denotes the type of socket &#8212; <code>SOCK_STREAM</code>, <code>SOCK_DGRAM</code> or <code>SOCK_RAW</code> &#8212; that is wanted. When <code>ai_socktype</code> is zero the caller will accept any socket type.</dl>
<p> <code>ai_protocol</code></p>
<dl>
<dt>
<dd> indicates which transport protocol is wanted: IPPROTO_UDP or IPPROTO_TCP. If <code>ai_protocol</code> is zero the caller will accept any protocol.</dl>
<p> <code>ai_flags</code></p>
<dl>
<dt>
<dd> Flag bits. If the <code>AI_CANONNAME</code> bit is set, a successful call to <code>lwres_getaddrinfo()</code> will return a null-terminated string containing the canonical name of the specified hostname in <code>ai_canonname</code> of the first <code>addrinfo</code> structure returned. Setting the <code>AI_PASSIVE</code> bit indicates that the returned socket address structure is intended for used in a call to <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2). In this case, if the hostname argument is a <code>NULL</code> pointer, then the IP address portion of the socket address structure will be set to <code>INADDR_ANY</code> for an IPv4 address or <code>IN6ADDR_ANY_INIT</code> for an IPv6 address. </p>
<p> When <code>ai_flags</code> does not set the <code>AI_PASSIVE</code> bit, the returned socket address structure will be ready for use in a call to <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) for a connection-oriented protocol or <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2), or <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) if a connectionless protocol was chosen. The IP address portion of the socket address structure will be set to the loopback address if <i>hostname</i> is a <code>NULL</code> pointer and <code>AI_PASSIVE</code> is not set in <code>ai_flags</code>. </p>
<p> If <code>ai_flags</code> is set to <code>AI_NUMERICHOST</code> it indicates that <i>hostname</i> should be treated as a numeric string defining an IPv4 or IPv6 address and no name resolution should be attempted.</dl>
<p> All other elements of the <code>struct addrinfo</code> passed via <i>hints</i> must be zero. </p>
<p> A <i>hints</i> of <code>NULL</code> is treated as if the caller provided a <code>struct addrinfo</code> initialized to zero with <code>ai_family</code>set to <code>PF_UNSPEC</code>. </p>
<p> After a successful call to <code>lwres_getaddrinfo()</code>, <i>*res</i> is a pointer to a linked list of one or more <code>addrinfo</code> structures. Each <code>struct addrinfo</code> in this list cn be processed by following the <code>ai_next</code> pointer, until a <code>NULL</code> pointer is encountered. The three members <code>ai_family</code>, <code>ai_socktype</code>, and <code>ai_protocol</code> in each returned <code>addrinfo</code> structure contain the corresponding arguments for a call to <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2). For each <code>addrinfo</code> structure in the list, the <code>ai_addr</code> member points to a filled-in socket address structure of length <code>ai_addrlen</code>. </p>
<p> All of the information returned by <code>lwres_getaddrinfo()</code> is dynamically allocated: the addrinfo structures, and the socket address structures and canonical host name strings pointed to by the <code>addrinfo</code>structures. Memory allocated for the dynamically allocated structures created by a successful call to <code>lwres_getaddrinfo()</code> is released by <code>lwres_freeaddrinfo()</code>. <i>ai</i> is a pointer to a <code>struct addrinfo</code> created by a call to <code>lwres_getaddrinfo()</code>.</p>
<h2>RETURN VALUES</h2>
<p> <code>lwres_getaddrinfo()</code> returns zero on success or one of the error codes listed in <code><a href="/docs/linux/man/3-gai_strerror/">gai_strerror</a></code>(3) if an error occurs. If both <i>hostname</i> and <i>servname</i> are <code>NULL</code> <code>lwres_getaddrinfo()</code> returns <code>EAI_NONAME</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-lwres/">lwres</a></code>(3), <code><a href="/docs/linux/man/3-lwres_getaddrinfo/">lwres_getaddrinfo</a></code>(3), <code><a href="/docs/linux/man/3-lwres_freeaddrinfo/">lwres_freeaddrinfo</a></code>(3), <code><a href="/docs/linux/man/3-lwres_gai_strerror/">lwres_gai_strerror</a></code>(3), <code>RFC2133</code>(), <code><a href="/docs/linux/man/3-getservbyname/">getservbyname</a></code>(3), <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2), <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2).</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004, 2005, 2007 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000, 2001, 2003 Internet Software Consortium. </p>
<h2>Index</h2>
