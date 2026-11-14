---
title: "ipsec_anyaddr(3)"
name: "ipsec_anyaddr"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ipsec_anyaddr/"
description: "ipsec_anyaddr, ipsec_isanyaddr, ipsec_unspecaddr, ipsec_isunspecaddr, ipsec_loopbackaddr, ipsec_isloopbackaddr – get and test for addresses of type \"any\", \"unspecified\" and loopback get \"any\" address"
---

<h2>NAME</h2>
<p> ipsec_anyaddr, ipsec_isanyaddr, ipsec_unspecaddr, ipsec_isunspecaddr, ipsec_loopbackaddr, ipsec_isloopbackaddr &#8211; get and test for addresses of type &quot;any&quot;, &quot;unspecified&quot; and loopback get &quot;any&quot; address</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libreswan.h&gt;</code> </p>
<p> <code>const char *anyaddr(int af, ip_address *dst);</code><br />
 <code>int isanyaddr(const ip_address *src);</code><br />
 <code>const char *unspecaddr(int af, ip_address *dst);</code><br />
 <code>int isunspecaddr(const ip_address *src);</code><br />
 <code>const char *loopbackaddr(int af, ip_address *dst);</code><br />
 <code>int isloopbackaddr(const ip_address *src);</code></p>
<h2>DESCRIPTION</h2>
<p> These functions fill in, and test for, special values of the <i>ip_address</i> type. </p>
<p> <i>Anyaddr</i> fills in the destination <i>*dst</i> with the &#8220;any&#8221; address of address family <i>af</i> (normally <code>AF_INET</code> or <code>AF_INET6</code>). The IPv4 &#8220;any&#8221; address is the one embodied in the old <code>INADDR_ANY</code> macro. </p>
<p> <i>Isanyaddr</i> returns <code>1</code> if the <i>src</i> address equals the &#8220;any&#8221; address, and <code>0</code> otherwise. </p>
<p> Similarly, <i>unspecaddr</i> supplies, and <i>isunspecaddr</i> tests for, the &#8220;unspecified&#8221; address, which may be the same as the &#8220;any&#8221; address. </p>
<p> Similarly, <i>loopbackaddr</i> supplies, and <i>islookbackaddr</i> tests for, the loopback address. </p>
<p> <i>Anyaddr</i>, <i>unspecaddr</i>, and <i>loopbackaddr</i> return <code>NULL</code> for success and a pointer to a string-literal error message for failure; see DIAGNOSTICS.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-inet/">inet</a>(3), <a href="/docs/linux/man/3-ipsec_addrtot/">ipsec_addrtot</a>(3), <a href="/docs/linux/man/3-ipsec_sameaddr/">ipsec_sameaddr</a>(3)</p>
<h2>DIAGNOSTICS</h2>
<p> Fatal errors in the address-supplying functions are: unknown address family.</p>
<h2>HISTORY</h2>
<p> Written for the FreeS/WAN project by Henry Spencer. </p>
<h2>Index</h2>
