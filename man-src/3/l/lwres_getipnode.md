---
title: "lwres_getipnode(3)"
name: "lwres_getipnode"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lwres_getipnode/"
description: "lwres_getipnodebyname, lwres_getipnodebyaddr, lwres_freehostent – lightweight resolver nodename / address translation API"
---

<h2 class="name">NAME</h2>
<p> lwres_getipnodebyname, lwres_getipnodebyaddr, lwres_freehostent &#8211; lightweight resolver nodename / address translation API </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;lwres/netdb.h&gt;
</code></pre>
<dl>
<dt> <code>struct hostent * lwres_getipnodebyname(const char&nbsp;<wbr>*</code><i>name</i><code>, int&nbsp;<wbr></code><i>af</i><code>, int&nbsp;<wbr></code><i>flags</i><code>, int&nbsp;<wbr>*</code><i>error_num</i><code>);</code></p>
<dt> <code>struct hostent * lwres_getipnodebyaddr(const void&nbsp;<wbr>*</code><i>src</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>, int&nbsp;<wbr></code><i>af</i><code>, int&nbsp;<wbr>*</code><i>error_num</i><code>);</code></p>
<dt> <code>void lwres_freehostent(struct hostent&nbsp;<wbr>*</code><i>he</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>These functions perform thread safe, protocol independent nodename-to-address and address-to-nodename translation as defined in RFC2553. </p>
<p> They use a <code>struct hostent</code> which is defined in <i>namedb.h</i>: </p>
<dl>
<dt>
<dd>
<pre><code>
struct hostent {
    char *h_name;       /* official name of host */
    char **h_aliases;   /* alias list */
    int h_addrtype;     /* host address type */
    int h_length;       /* length of address */
    char **h_addr_list; /* list of addresses from name server */
};
#define h_addr h_addr_list[0] /* address, for backward compatibility */
</code></pre>
</dl>
<p> The members of this structure are: </p>
<p> <code>h_name</code></p>
<dl>
<dt>
<dd> The official (canonical) name of the host.</dl>
<p> <code>h_aliases</code></p>
<dl>
<dt>
<dd> A NULL-terminated array of alternate names (nicknames) for the host.</dl>
<p> <code>h_addrtype</code></p>
<dl>
<dt>
<dd> The type of address being returned &#8211; usually <code>PF_INET</code> or <code>PF_INET6</code>.</dl>
<p> <code>h_length</code></p>
<dl>
<dt>
<dd> The length of the address in bytes.</dl>
<p> <code>h_addr_list</code></p>
<dl>
<dt>
<dd> A <code>NULL</code> terminated array of network addresses for the host. Host addresses are returned in network byte order.</dl>
<p> <code>lwres_getipnodebyname()</code> looks up addresses of protocol family <i>af</i> for the hostname <i>name</i>. The <i>flags</i> parameter contains ORed flag bits to specify the types of addresses that are searched for, and the types of addresses that are returned. The flag bits are: </p>
<p> <code>AI_V4MAPPED</code></p>
<dl>
<dt>
<dd> This is used with an <i>af</i> of AF_INET6, and causes IPv4 addresses to be returned as IPv4-mapped IPv6 addresses.</dl>
<p> <code>AI_ALL</code></p>
<dl>
<dt>
<dd> This is used with an <i>af</i> of AF_INET6, and causes all known addresses (IPv6 and IPv4) to be returned. If AI_V4MAPPED is also set, the IPv4 addresses are return as mapped IPv6 addresses.</dl>
<p> <code>AI_ADDRCONFIG</code></p>
<dl>
<dt>
<dd> Only return an IPv6 or IPv4 address if here is an active network interface of that type. This is not currently implemented in the BIND 9 lightweight resolver, and the flag is ignored.</dl>
<p> <code>AI_DEFAULT</code></p>
<dl>
<dt>
<dd> This default sets the <code>AI_V4MAPPED</code> and <code>AI_ADDRCONFIG</code> flag bits.</dl>
<p> <code>lwres_getipnodebyaddr()</code> performs a reverse lookup of address <i>src</i> which is <i>len</i> bytes long. <i>af</i> denotes the protocol family, typically <code>PF_INET</code> or <code>PF_INET6</code>. </p>
<p> <code>lwres_freehostent()</code> releases all the memory associated with the <code>struct hostent</code> pointer <i>he</i>. Any memory allocated for the <code>h_name</code>, <code>h_addr_list</code> and <code>h_aliases</code> is freed, as is the memory for the <code>hostent</code> structure itself.</p>
<h2>RETURN VALUES</h2>
<p> If an error occurs, <code>lwres_getipnodebyname()</code> and <code>lwres_getipnodebyaddr()</code> set <i>*error_num</i> to an appropriate error code and the function returns a <code>NULL</code> pointer. The error codes and their meanings are defined in <i>&lt;lwres/netdb.h&gt;</i>: </p>
<p> <code>HOST_NOT_FOUND</code></p>
<dl>
<dt>
<dd> No such host is known.</dl>
<p> <code>NO_ADDRESS</code></p>
<dl>
<dt>
<dd> The server recognised the request and the name but no address is available. Another type of request to the name server for the domain might return an answer.</dl>
<p> <code>TRY_AGAIN</code></p>
<dl>
<dt>
<dd> A temporary and possibly transient error occurred, such as a failure of a server to respond. The request may succeed if retried.</dl>
<p> <code>NO_RECOVERY</code></p>
<dl>
<dt>
<dd> An unexpected failure occurred, and retrying the request is pointless.</dl>
<p> <code><a href="/docs/linux/man/3-lwres_hstrerror/">lwres_hstrerror</a></code>(3) translates these error codes to suitable error messages.</p>
<h2>SEE ALSO</h2>
<p> <code>RFC2553</code>(), <code><a href="/docs/linux/man/3-lwres/">lwres</a></code>(3), <code><a href="/docs/linux/man/3-lwres_gethostent/">lwres_gethostent</a></code>(3), <code><a href="/docs/linux/man/3-lwres_getaddrinfo/">lwres_getaddrinfo</a></code>(3), <code><a href="/docs/linux/man/3-lwres_getnameinfo/">lwres_getnameinfo</a></code>(3), <code><a href="/docs/linux/man/3-lwres_hstrerror/">lwres_hstrerror</a></code>(3).</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004, 2005, 2007 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000, 2001, 2003 Internet Software Consortium. </p>
<h2>Index</h2>
