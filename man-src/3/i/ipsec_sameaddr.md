---
title: "ipsec_sameaddr(3)"
name: "ipsec_sameaddr"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ipsec_sameaddr/"
description: "ipsec_sameaddr, ipsec_addrcmp, ipsec_samesubnet, ipsec_addrinsubnet, ipsec_subnetinsubnet, ipsec_subnetishost, ipsec_samesaid, ipsec_sameaddrtype, ipsec_samesubnettype – do comparisons for addresse..."
---

<h2>NAME</h2>
<p> ipsec_sameaddr, ipsec_addrcmp, ipsec_samesubnet, ipsec_addrinsubnet, ipsec_subnetinsubnet, ipsec_subnetishost, ipsec_samesaid, ipsec_sameaddrtype, ipsec_samesubnettype &#8211; do comparisons for addresses, subnets, SA IDs and address families</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libreswan.h&gt;</code> </p>
<p> <code>int sameaddr(const ip_address *a, const ip_address *b);</code><br />
 <code>int addrcmp(const ip_address *a, const ip_address *b);</code><br />
 <code>int samesubnet(const ip_subnet *a, const ip_subnet *b);</code><br />
 <code>int addrinsubnet(const ip_address *a, const ip_subnet *s);</code><br />
 <code>int subnetinsubnet(const ip_subnet *a, const ip_subnet *b);</code><br />
 <code>int subnetishost(const ip_subnet *s);</code><br />
 <code>int samesaid(const ip_said *a, const ip_said *b);</code><br />
 <code>int sameaddrtype(const ip_address *a, const ip_address *b);</code><br />
 <code>int samesubnettype(const ip_subnet *a, const ip_subnet *b);</code></p>
<h2>DESCRIPTION</h2>
<p> These functions do various comparisons and tests on the <i>ip_address</i> type and <i>ip_subnet</i> types. </p>
<p> <i>Sameaddr</i> returns non-zero if addresses <i>a</i> and <i>b</i> are identical, and <code>0</code> otherwise. Addresses of different families are never identical. </p>
<p> <i>Addrcmp</i> returns <code>-1</code>, <code>0</code>, or <code>1</code> respectively if address <i>a</i> is less than, equal to, or greater than <i>b</i>. If they are not of the same address family, they are never equal; the ordering reported in this case is arbitrary (and probably not useful) but consistent. </p>
<p> <i>Samesubnet</i> returns non-zero if subnets <i>a</i> and <i>b</i> are identical, and <code>0</code> otherwise. Subnets of different address families are never identical. </p>
<p> <i>Addrinsubnet</i> returns non-zero if address <i>a</i> is within subnet <i>s</i> and <code>0</code> otherwise. An address is never within a subnet of a different address family. </p>
<p> <i>Subnetinsubnet</i> returns non-zero if subnet <i>a</i> is a subset of subnet <i>b</i> and <code>0</code> otherwise. A subnet is deemed to be a subset of itself. A subnet is never a subset of another subnet if their address families differ. </p>
<p> <i>Subnetishost</i> returns non-zero if subnet <i>s</i> is in fact only a single host, and <code>0</code> otherwise. </p>
<p> <i>Samesaid</i> returns non-zero if SA IDs <i>a</i> and <i>b</i> are identical, and <code>0</code> otherwise. </p>
<p> <i>Sameaddrtype</i> returns non-zero if addresses <i>a</i> and <i>b</i> are of the same address family, and <code>0</code> otherwise. </p>
<p> <i>Samesubnettype</i> returns non-zero if subnets <i>a</i> and <i>b</i> are of the same address family, and <code>0</code> otherwise.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-inet/">inet</a>(3), <a href="/docs/linux/man/3-ipsec_initaddr/">ipsec_initaddr</a>(3)</p>
<h2>HISTORY</h2>
<p> Written for the FreeS/WAN project by Henry Spencer. </p>
<h2>Index</h2>
