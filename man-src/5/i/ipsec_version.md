---
title: "ipsec_version(5)"
name: "ipsec_version"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ipsec_version/"
description: "ipsec_version – lists KLIPS version information"
---

<p>ipsec_version &#8211; lists KLIPS version information</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>cat</code> <i>/proc/net/ipsec_version</i></dl>
<h2>Obsolete</h2>
<dd>Note that ipsec_version is only supported on the classic KLIPS stack. It is not supported on any other stack.</p>
<h2>Description</h2>
<p>/proc/net/ipsec_version is a read-only file which lists the currently running KLIPS version information.</p>
<h2>Examples</h2>
<p><code>FreeS/WAN version: 1.4</code></p>
<dl>
<dd></dl>
<p> shows that the currently loaded <code>KLIPS</code> is from <code>FreeS/WAN 1.4.</code></p>
<h2>Files</h2>
<p>/proc/net/ipsec_version</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipsec/">ipsec</a>(8), <a href="/docs/linux/man/5-ipsec_eroute/">ipsec_eroute</a>(5), <a href="/docs/linux/man/5-ipsec_spi/">ipsec_spi</a>(5), <a href="/docs/linux/man/5-ipsec_spigrp/">ipsec_spigrp</a>(5), <a href="/docs/linux/man/5-ipsec_klipsdebug/">ipsec_klipsdebug</a>(5), <a href="/docs/linux/man/8-ipsec_tncfg/">ipsec_tncfg</a>(8), <a href="/docs/linux/man/5-ipsec_pf_key/">ipsec_pf_key</a>(5)</p>
<h2>History</h2>
<p>Written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org/">http://www.freeswan.org/</a></code>m[]&gt; by Richard Guy Briggs.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
