---
title: "ares_inet_pton(3)"
name: "ares_inet_pton"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_inet_pton/"
description: "ares_inet_pton – convert an IPv4 or IPv6 address from text to binary form"
---

<h2>NAME</h2>
<p> ares_inet_pton &#8211; convert an IPv4 or IPv6 address from text to binary form</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
const char *ares_inet_pton(int af, const char *src, void *dst);
</code></pre>
<h2>DESCRIPTION</h2>
<p> This is a portable version with the identical functionality of the commonly available <i>inet_pton</i>. </p>
<p> The ares_inet_pton() function converts the address in its standard text presentation form into its numeric binary form. The <code>af</code> argument shall specify the family of the address. The AF_INET and AF_INET6 address families shall be supported. The <code>src</code> argument points to the string being passed in. The <code>dst</code> argument points to a buffer into which the function stores the numeric address; this shall be large enough to hold the numeric address (32 bits for AF_INET, 128 bits for AF_INET6).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_init/">ares_init</a>(3),</code> <code><a href="/docs/linux/man/3-ares_inet_ntop/">ares_inet_ntop</a>(3)</code></p>
<h2>AVAILABILITY</h2>
<p> made properly publicly available in c-ares for real in version 1.10.0</p>
<h2>AUTHOR</h2>
<p> Daniel Stenberg </p>
<h2>Index</h2>
