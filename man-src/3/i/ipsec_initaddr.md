---
title: "ipsec_initaddr(3)"
name: "ipsec_initaddr"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ipsec_initaddr/"
description: "ipsec_initaddr, ipsec_addrtypeof, ipsec_addrlenof, ipsec_addrbytesof, ipsec_addrbytesptr – initialize an ip_address, get address type of an ip_address, get length of address within an ip_address, g..."
---

<h2>NAME</h2>
<p> ipsec_initaddr, ipsec_addrtypeof, ipsec_addrlenof, ipsec_addrbytesof, ipsec_addrbytesptr &#8211; initialize an ip_address, get address type of an ip_address, get length of address within an ip_address, get copy of address within an ip_address, get pointer to address within an ip_address</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libreswan.h&gt;</code> </p>
<p> <code>const char *initaddr(const char *src, size_t srclen,</code><br />
 &nbsp;<wbr> <code>int af, ip_address *dst);</code><br />
 <code>int addrtypeof(const ip_address *src);</code><br />
 <code>size_t addrlenof(const ip_address *src);</code><br />
 <code>size_t addrbytesof(const ip_address *src,</code><br />
 &nbsp;<wbr> <code>unsigned char *dst, size_t dstlen);</code><br />
 <code>size_t addrbytesptr(const ip_address *src,</code><br />
 &nbsp;<wbr> <code>const unsigned char **dst);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>&lt;libreswan.h&gt;</code> library uses an internal type <i>ip_address</i> to contain one of the (currently two) types of IP address. These functions provide basic tools for creating and examining this type. </p>
<p> <i>Initaddr</i> initializes a variable <i>*dst</i> of type <i>ip_address</i> from an address (in network byte order, indicated by a pointer <i>src</i> and a length <i>srclen</i>) and an address family <i>af</i> (typically <code>AF_INET</code> or <code>AF_INET6</code>). The length must be consistent with the address family. </p>
<p> <i>Addrtypeof</i> returns the address type of an address, normally <code>AF_INET</code> or <code>AF_INET6</code>. (The <code>&lt;libreswan.h&gt;</code> header file arranges to include the necessary headers for these names to be known.) </p>
<p> <i>Addrlenof</i> returns the size (in bytes) of the address within an <i>ip_address</i>, to permit storage allocation etc. </p>
<p> <i>Addrbytesof</i> copies the address within the <i>ip_address</i> <i>src</i> to the buffer indicated by the pointer <i>dst</i> and the length <i>dstlen</i>, and returns the address length (in bytes). If the address will not fit, as many bytes as will fit are copied; the returned length is still the full length. It is the caller&#8217;s responsibility to check the returned value to ensure that there was enough room. </p>
<p> <i>Addrbytesptr</i> sets <i>*dst</i> to a pointer to the internal address within the <i>ip_address</i>, and returns the address length (in bytes). If <i>dst</i> is <code>NULL</code>, it just returns the address length. The pointer points to <code>const</code> to discourage misuse. </p>
<p> <i>Initaddr</i> returns <code>NULL</code> for success and a pointer to a string-literal error message for failure; see DIAGNOSTICS. </p>
<p> The functions which return <i>size_t</i> return <code>0</code> for a failure.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-inet/">inet</a>(3), <a href="/docs/linux/man/3-ipsec_ttoaddr/">ipsec_ttoaddr</a>(3)</p>
<h2>DIAGNOSTICS</h2>
<p> An unknown address family is a fatal error for any of these functions except <i>addrtypeof</i>. An address-size mismatch is a fatal error for <i>initaddr</i>.</p>
<h2>HISTORY</h2>
<p> Written for the FreeS/WAN project by Henry Spencer.</p>
<h2>BUGS</h2>
<p> <i>Addrtypeof</i> should probably have been named <i>addrfamilyof</i>. </p>
<h2>Index</h2>
