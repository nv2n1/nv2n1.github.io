---
title: "ipsec_trap_count(5)"
name: "ipsec_trap_count"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ipsec_trap_count/"
description: "ipsec_trap_count – KLIPS statistic on number of ACQUIREs"
---

<p>ipsec_trap_count &#8211; KLIPS statistic on number of ACQUIREs</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>cat</code> <i>/proc/net/ipsec/stats/trap_count</i></dl>
<h2>Obsolete</h2>
<dd>Note that trap_count is only supported on the classic KLIPS stack. It is not supported on any other stack and will be completely removed in future versions. A replacement command still needs to be designed</p>
<h2>Description</h2>
<p>/proc/net/ipsec/stats/trap_count is a read-only file. It contains a hexadecimal number which records the number of attempts to send PF_ACQUIRE messages. Only those recorded by trap_sendcount were actually successfully passed to userland. Note that the userland may still have lost them on its own.</p>
<h2>Files</h2>
<p>/proc/net/ipsec/stats/trap_count</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ipsec/">ipsec</a></code>(8), <code><a href="/docs/linux/man/5-ipsec_pf_key/">ipsec_pf_key</a></code>(5), <code><a href="/docs/linux/man/5-trap_sendcount/">trap_sendcount</a></code>(5), <code><a href="/docs/linux/man/8-pluto/">pluto</a></code>(8)</p>
<h2>History</h2>
<p>Written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org/">http://www.freeswan.org/</a></code>m[]&gt; by Michael C. Richardson &lt;mcr [at] freeswan.org&gt;</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
