---
title: "ipsec_goodmask(3)"
name: "ipsec_goodmask"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ipsec_goodmask/"
description: "ipsec_goodmask, ipsec_masktobits, ipsec_bitstomask – check if Internet subnet mask is valid, convert Internet subnet mask to bit count, convert bit count to Internet subnet mask"
---

<h2>NAME</h2>
<p> ipsec_goodmask, ipsec_masktobits, ipsec_bitstomask &#8211; check if Internet subnet mask is valid, convert Internet subnet mask to bit count, convert bit count to Internet subnet mask</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libreswan.h&gt;</code> </p>
<p> <code>int goodmask(struct in_addr mask);</code><br />
 <code>int masktobits(struct in_addr mask);</code><br />
 <code>struct in_addr bitstomask(int n);</code></p>
<h2>DESCRIPTION</h2>
<p> These functions are obsolete; see <i><a href="/docs/linux/man/3-ipsec_masktocount/">ipsec_masktocount</a></i>(3) for a partial replacement. </p>
<p> <i>Goodmask</i> reports whether the subnet <i>mask</i> is a valid one, i.e. consists of a (possibly empty) sequence of <code>1</code>s followed by a (possibly empty) sequence of <code>0</code>s. <i>Masktobits</i> takes a (valid) subnet mask and returns the number of <code>1</code> bits in it. <i>Bitstomask</i> reverses this, returning the subnet mask corresponding to bit count <i>n</i>. </p>
<p> All masks are in network byte order.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-inet/">inet</a>(3), <a href="/docs/linux/man/3-ipsec_atosubnet/">ipsec_atosubnet</a>(3)</p>
<h2>DIAGNOSTICS</h2>
<p> <i>Masktobits</i> returns <code>-1</code> for an invalid mask. <i>Bitstomask</i> returns an all-zeros mask for a negative or out-of-range <i>n</i>.</p>
<h2>HISTORY</h2>
<p> Written for the FreeS/WAN project by Henry Spencer.</p>
<h2>BUGS</h2>
<p> The error-reporting convention of <i>bitstomask</i> is less than ideal; zero is sometimes a legitimate mask. </p>
<h2>Index</h2>
