---
title: "ipsec_initsubnet(3)"
name: "ipsec_initsubnet"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ipsec_initsubnet/"
description: "ipsec_initsubnet, ipsec_addrtosubnet, ipsec_subnettypeof, ipsec_masktocount, ipsec_networkof, ipsec_maskof – initialize an ip_subnet, initialize a singleton ip_subnet, get address type of an ip_sub..."
---

<h2>NAME</h2>
<p> ipsec_initsubnet, ipsec_addrtosubnet, ipsec_subnettypeof, ipsec_masktocount, ipsec_networkof, ipsec_maskof &#8211; initialize an ip_subnet, initialize a singleton ip_subnet, get address type of an ip_subnet, convert subnet mask to bit count, get base address of an ip_subnet, get subnet mask of an ip_subnet</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libreswan.h&gt;</code> </p>
<p> <code>const char *initsubnet(const ip_address *addr,</code><br />
 &nbsp;<wbr> <code>int maskbits, int clash, ip_subnet *dst);</code><br />
 <code>const char *addrtosubnet(const ip_address *addr,</code><br />
 &nbsp;<wbr> <code>ip_subnet *dst);</code> </p>
<p> <code>int subnettypeof(const ip_subnet *src);</code><br />
 <code>int masktocount(const ip_address *src);</code><br />
 <code>void networkof(const ip_subnet *src, ip_address *dst);</code><br />
 <code>void maskof(const ip_subnet *src, ip_address *dst);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>&lt;libreswan.h&gt;</code> library uses an internal type <i>ip_subnet</i> to contain a description of an IP subnet (base address plus mask). These functions provide basic tools for creating and examining this type. </p>
<p> <i>Initsubnet</i> initializes a variable <i>*dst</i> of type <i>ip_subnet</i> from a base address and a count of mask bits. The <i>clash</i> parameter specifies what to do if the base address includes <code>1</code> bits outside the prefix specified by the mask (that is, in the &#8220;host number&#8221; part of the address):</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8216;0&#8217;</p>
<dd> zero out host-number bits</p>
<dt>&#8216;x&#8217;</p>
<dd> non-zero host-number bits are an error</dl>
</dl>
<p> <i>Initsubnet</i> returns <code>NULL</code> for success and a pointer to a string-literal error message for failure; see DIAGNOSTICS. </p>
<p> <i>Addrtosubnet</i> initializes an <i>ip_subnet</i> variable <i>*dst</i> to a &#8220;singleton subnet&#8221; containing the single address <i>*addr</i>. It returns <code>NULL</code> for success and a pointer to a string-literal error message for failure. </p>
<p> <i>Subnettypeof</i> returns the address type of a subnet, normally <code>AF_INET</code> or <code>AF_INET6</code>. (The <code>&lt;libreswan.h&gt;</code> header file arranges to include the necessary headers for these names to be known.) </p>
<p> <i>Masktocount</i> converts a subnet mask, expressed as an address, to a bit count suitable for use with <i>initsubnet</i>. It returns <code>-1</code> for error; see DIAGNOSTICS. </p>
<p> <i>Networkof</i> fills in <i>*dst</i> with the base address of subnet <i>src</i>. </p>
<p> <i>Maskof</i> fills in <i>*dst</i> with the subnet mask of subnet <i>src</i>, expressed as an address.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-inet/">inet</a>(3), <a href="/docs/linux/man/3-ipsec_ttosubnet/">ipsec_ttosubnet</a>(3), <a href="/docs/linux/man/3-ipsec_rangetosubnet/">ipsec_rangetosubnet</a>(3)</p>
<h2>DIAGNOSTICS</h2>
<p> Fatal errors in <i>initsubnet</i> are: unknown address family; unknown <i>clash</i> value; impossible mask bit count; non-zero host-number bits and <i>clash</i> is <code>&#8216;x&#8217;</code>. Fatal errors in <i>addrtosubnet</i> are: unknown address family. Fatal errors in <i>masktocount</i> are: unknown address family; mask bits not contiguous.</p>
<h2>HISTORY</h2>
<p> Written for the FreeS/WAN project by Henry Spencer. </p>
<h2>Index</h2>
