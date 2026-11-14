---
title: "lwres_inetntop(3)"
name: "lwres_inetntop"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lwres_inetntop/"
description: "lwres_net_ntop – lightweight resolver IP address presentation"
---

<h2 class="name">NAME</h2>
<p> lwres_net_ntop &#8211; lightweight resolver IP address presentation </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;lwres/net.h&gt;
</code></pre>
<dl>
<dt> <code>const char * lwres_net_ntop(int&nbsp;<wbr></code><i>af</i><code>, const void&nbsp;<wbr>*</code><i>src</i><code>, char&nbsp;<wbr>*</code><i>dst</i><code>, size_t&nbsp;<wbr></code><i>size</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>lwres_net_ntop()</code></p>
<dd>converts an IP address of protocol family <i>af</i> &#8212; IPv4 or IPv6 &#8212; at location <i>src</i> from network format to its conventional representation as a string. For IPv4 addresses, that string would be a dotted-decimal. An IPv6 address would be represented in colon notation as described in RFC1884. </p>
<p> The generated string is copied to <i>dst</i> provided <i>size</i> indicates it is long enough to store the ASCII representation of the address.</p>
<h2>RETURN VALUES</h2>
<p> If successful, the function returns <i>dst</i>: a pointer to a string containing the presentation format of the address. <code>lwres_net_ntop()</code> returns <code>NULL</code> and sets the global variable <code>errno</code> to <code>EAFNOSUPPORT</code> if the protocol family given in <i>af</i> is not supported.</p>
<h2>SEE ALSO</h2>
<p> <code>RFC1884</code>(), <code><a href="/docs/linux/man/3-inet_ntop/">inet_ntop</a></code>(3), <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3).</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004, 2005, 2007 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000, 2001 Internet Software Consortium. </p>
<h2>Index</h2>
