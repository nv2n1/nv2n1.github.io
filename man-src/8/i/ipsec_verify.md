---
title: "ipsec_verify(8)"
name: "ipsec_verify"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_verify/"
description: "ipsec_verify – see if the IPsec subsystem has been installed correctly"
---

<p>ipsec_verify &#8211; see if the IPsec subsystem has been installed correctly</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> <i>verify</i></dl>
<h2>Description</h2>
<dd>The <i>ipsec verify</i> examines the local system for a number of common system faults and configuration mistakes.</p>
<h2>History</h2>
<p>Written originally for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org">http://www.freeswan.org</a></code>m[]&gt; by Michael Richardson. Rewritten in python by Paul Wouters</p>
<h2>Bugs</h2>
<p><i>Verify</i> was converted from shell to perl to python, and the MASQUERADING/NAT rule tests still need to be ported. The <i>ss</i> command is around in various non-intuitive and buggy versions, causing some false-positives with respect to listening on UDP port 500 and 4500. See <a rel="nofollow" href="https://bugzilla.redhat.com/show_bug.cgi?id=829630">https://bugzilla.redhat.com/show_bug.cgi?id=829630</a></p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
