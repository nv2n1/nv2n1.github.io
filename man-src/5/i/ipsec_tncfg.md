---
title: "ipsec_tncfg(5)"
name: "ipsec_tncfg"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ipsec_tncfg/"
description: "ipsec_tncfg – lists IPSEC virtual interfaces attached to real interfaces"
---

<p>ipsec_tncfg &#8211; lists IPSEC virtual interfaces attached to real interfaces</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> <i>tncfg</i></p>
<dd><i>cat/proc/net/ipsec_tncfg</i></dl>
<h2>Klips</h2>
<dd>Note that tncfg is only supported on the KLIPS stack which uses ipsecX interfaces bound to physical interfaces</p>
<h2>Description</h2>
<p>/proc/net/ipsec_tncfg is a read-only file which lists which IPSEC virtual interfaces are attached to which real interfaces, through which packets will be forwarded once processed by IPSEC. </p>
<p> Each line lists one ipsec I/F. A table entry consists of: </p>
<p> +</p>
<dl>
<dd>an ipsec virtual I/F name</dl>
<p> +</p>
<dl>
<dd>a visual and machine parsable separator &#8216;-&gt;&#8217;, separating the virtual I/F and the physical I/F,</dl>
<p> +</p>
<dl>
<dd>a physical I/F name, to which the ipsec virtual I/F is attached or NULL if it is not attached,</dl>
<p> +</p>
<dl>
<dd>the keyword <code>mtu=</code>,</dl>
<p> +</p>
<dl>
<dd>the MTU of the ipsec virtual I/F,</dl>
<p> +</p>
<dl>
<dd>the automatically adjusted effective MTU for PMTU discovery, in brackets,</dl>
<p> +</p>
<dl>
<dd>a visual and machine parsable separator &#8216;-&gt;&#8217;, separating the virtual I/F MTU and the physical I/F MTU,</dl>
<p> +</p>
<dl>
<dd>the MTU of the attached physical I/F.</dl>
<h2>Examples</h2>
<p><code>ipsec2 -&gt; eth3 mtu=16260(1443) -&gt; 1500</code></p>
<dl>
<dd></dl>
<p> shows that virtual device <code>ipsec2</code> with an MTU of 16260 is connected to physical device <code>eth3</code> with an MTU of 1500 and that the effective MTU as a result of PMTU discovery has been automatically set to 1443. </p>
<p> <code>ipsec0 -&gt; wvlan0 mtu=1400(16260) -&gt; 1500</code></p>
<dl>
<dd></dl>
<p> shows that virtual device <code>ipsec0</code> with an MTU of 1400 is connected to physical device <code>wvlan0</code> with an MTU of 1500 and no PMTU packets have gotten far enough to bump down the effective MTU from its default of 16260. </p>
<p> <code>ipsec3 -&gt; NULL mtu=0(0) -&gt; 0</code></p>
<dl>
<dd></dl>
<p> shows that virtual device <code>ipsec3</code> is not connected to any physical device.</p>
<h2>Files</h2>
<p>/proc/net/ipsec_tncfg, /usr/local/bin/ipsec</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipsec/">ipsec</a>(8), <a href="/docs/linux/man/5-ipsec_eroute/">ipsec_eroute</a>(5), <a href="/docs/linux/man/5-ipsec_spi/">ipsec_spi</a>(5), <a href="/docs/linux/man/5-ipsec_spigrp/">ipsec_spigrp</a>(5), <a href="/docs/linux/man/5-ipsec_klipsdebug/">ipsec_klipsdebug</a>(5), <a href="/docs/linux/man/8-ipsec_tncfg/">ipsec_tncfg</a>(8), <a href="/docs/linux/man/5-ipsec_version/">ipsec_version</a>(5), <a href="/docs/linux/man/5-ipsec_pf_key/">ipsec_pf_key</a>(5)</p>
<h2>History</h2>
<p>Written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org/">http://www.freeswan.org/</a></code>m[]&gt; by Richard Guy Briggs.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
