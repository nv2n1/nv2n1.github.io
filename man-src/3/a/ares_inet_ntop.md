---
title: "ares_inet_ntop(3)"
name: "ares_inet_ntop"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_inet_ntop/"
description: "ares_inet_ntop – convert a network format address to presentation format"
---

<h2>NAME</h2>
<p> ares_inet_ntop &#8211; convert a network format address to presentation format</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
const char *
ares_inet_ntop(int af, const void *src, char *dst, ares_socklen_t size);
</code></pre>
<h2>DESCRIPTION</h2>
<p> This is a portable version with the identical functionality of the commonly available <i>inet_ntop</i>. </p>
<p> The ares_inet_ntop() function converts a numeric address into a text string suitable for presentation. The <code>af</code> argument shall specify the family of the address. This can be AF_INET or AF_INET6. The <code>src</code> argument points to a buffer holding an IPv4 address if the af argument is AF_INET, or an IPv6 address if the af argument is AF_INET6; the address must be in network byte order. The <code>dst</code> argument points to a buffer where the function stores the resulting text string; it shall not be NULL. The <code>size</code> argument specifies the size of this buffer, which shall be large enough to hold the text string (INET_ADDRSTRLEN (16) characters for IPv4, INET6_ADDRSTRLEN (46) characters for IPv6).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_init/">ares_init</a>(3),</code> <code><a href="/docs/linux/man/3-ares_inet_pton/">ares_inet_pton</a>(3)</code></p>
<h2>AVAILABILITY</h2>
<p> made properly publicly available in c-ares for real in version 1.10.0</p>
<h2>AUTHOR</h2>
<p> Daniel Stenberg </p>
<h2>Index</h2>
