---
title: "ipsec_portof(3)"
name: "ipsec_portof"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ipsec_portof/"
description: "ipsec_portof, ipsec_setportof, ipsec_sockaddrof, ipsec_sockaddrlenof – get port field of an ip_address, set port field of an ip_address, get pointer to internal sockaddr of an ip_address, get lengt..."
---

<h2>NAME</h2>
<p> ipsec_portof, ipsec_setportof, ipsec_sockaddrof, ipsec_sockaddrlenof &#8211; get port field of an ip_address, set port field of an ip_address, get pointer to internal sockaddr of an ip_address, get length of internal sockaddr of an ip_address</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libreswan.h&gt;</code> </p>
<p> <code>int portof(const ip_address *src);</code><br />
 <code>void setportof(int port, ip_address *dst);</code><br />
 <code>struct sockaddr *sockaddrof(ip_address *src);</code><br />
 <code>size_t sockaddrlenof(const ip_address *src);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>&lt;libreswan.h&gt;</code> internal type <i>ip_address</i> contains one of the <i>sockaddr</i> types internally. <i>Reliance on this feature is discouraged</i>, but it may occasionally be necessary. These functions provide low-level tools for this purpose. </p>
<p> <i>Portof</i> and <i>setportof</i> respectively read and write the port-number field of the internal <i>sockaddr</i>. The values are in network byte order. </p>
<p> <i>Sockaddrof</i> returns a pointer to the internal <i>sockaddr</i>, for passing to other functions. </p>
<p> <i>Sockaddrlenof</i> reports the size of the internal <i>sockaddr</i>, for use in storage allocation.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-inet/">inet</a>(3), <a href="/docs/linux/man/3-ipsec_initaddr/">ipsec_initaddr</a>(3)</p>
<h2>DIAGNOSTICS</h2>
<p> <i>Portof</i> returns <code>-1</code>, <i>sockaddrof</i> returns <code>NULL</code>, and <i>sockaddrlenof</i> returns <code>0</code> if an unknown address family is found within the <i>ip_address</i>.</p>
<h2>HISTORY</h2>
<p> Written for the FreeS/WAN project by Henry Spencer.</p>
<h2>BUGS</h2>
<p> These functions all depend on low-level details of the <i>ip_address</i> type, which are in principle subject to change. Avoid using them unless really necessary. </p>
<h2>Index</h2>
