---
title: "ipsec_trap_sendcount(5)"
name: "ipsec_trap_sendcount"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ipsec_trap_sendcount/"
description: "ipsec_trap_sendcount – KLIPS statistic on number of successful ACQUIREs"
---

<p>ipsec_trap_sendcount &#8211; KLIPS statistic on number of successful ACQUIREs</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>cat</code> <i>/proc/net/ipsec/stats/trap_sendcount</i></dl>
<h2>Obsolete</h2>
<dd>Note that trap_sendcount is only supported on the classic KLIPS stack. It is not supported on any other stack and will be completely removed in future versions. A replacement command still needs to be designed</p>
<h2>Description</h2>
<p>/proc/net/ipsec/stats/trap_sendcount is a read-only file. It contains a hexadecimal number which records the number of successful PF_ACQUIRE messages that were sent.</p>
<h2>Files</h2>
<p>/proc/net/ipsec/stats/trap_sendcount</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ipsec/">ipsec</a></code>(8), <code><a href="/docs/linux/man/5-ipsec_pf_key/">ipsec_pf_key</a></code>(5), <code><a href="/docs/linux/man/5-trap_count/">trap_count</a></code>(5), <code><a href="/docs/linux/man/8-pluto/">pluto</a></code>(8)</p>
<h2>History</h2>
<p>Written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org/">http://www.freeswan.org/</a></code>m[]&gt; by Michael C. Richardson &lt;mcr [at] freeswan.org&gt;</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
