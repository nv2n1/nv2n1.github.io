---
title: "ipsec_klipsdebug(5)"
name: "ipsec_klipsdebug"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ipsec_klipsdebug/"
description: "ipsec_klipsdebug – list KLIPS (kernel IPSEC support) debug features and level"
---

<p>ipsec_klipsdebug &#8211; list KLIPS (kernel IPSEC support) debug features and level</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> <i>klipsdebug</i></p>
<dd><i>cat/proc/net/ipsec_klipsdebug</i></dl>
<h2>Description</h2>
<p>/proc/net/ipsec_klipsdebug</p>
<dd>lists flags that control various parts of the debugging output of KLIPS and MAST, two of the IPsec stacks supported by Libreswan. At this point it is a read-only file. </p>
<p> A table entry consists of: </p>
<p> +</p>
<dl>
<dd>a KLIPS debug variable</dl>
<p> +</p>
<dl>
<dd>a &#8216;=&#8217; separator for visual and automated parsing between the variable name and its current value</dl>
<p> +</p>
<dl>
<dd>hexadecimal bitmap of variable&#8217;s flags.</dl>
<p> The variable names roughly describe the scope of the debugging variable. Currently, no flags are documented or individually accessible yet except tunnel-xmit. </p>
<p> The variable names are: </p>
<p> <code>tunnel</code></p>
<dl>
<dd>tunnelling code</dl>
<p> <code>netlink</code></p>
<dl>
<dd>userspace communication code (obsolete)</dl>
<p> <code>xform</code></p>
<dl>
<dd>transform selection and manipulation code</dl>
<p> <code>eroute</code></p>
<dl>
<dd>eroute table manipulation code</dl>
<p> <code>spi</code></p>
<dl>
<dd>SA table manipulation code</dl>
<p> <code>radij</code></p>
<dl>
<dd>radij tree manipulation code</dl>
<p> <code>esp</code></p>
<dl>
<dd>encryptions transforms code</dl>
<p> <code>ah</code></p>
<dl>
<dd>authentication transforms code</dl>
<p> <code>rcv</code></p>
<dl>
<dd>receive code</dl>
<p> <code>ipcomp</code></p>
<dl>
<dd>ip compression transforms code</dl>
<p> <code>verbose</code></p>
<dl>
<dd>give even more information, beware this will probably trample the 4k kernel printk buffer giving inaccurate output</dl>
<p> All KLIPS debug output appears as <code>kernel.info</code> messages to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8). Most systems are set up to log these messages to /var/log/messages.</p>
<h2>Examples</h2>
<p><code>debug_tunnel=00000010.</code><code>debug_netlink=00000000.</code><code>debug_xform=00000000.</code><code>debug_eroute=00000000.</code><code>debug_spi=00000000.</code><code>debug_radij=00000000.</code><code>debug_esp=00000000.</code><code>debug_ah=00000000.</code><code>debug_rcv=00000000.</code><code>debug_pfkey=ffffffff.</code> </p>
<p> means that one <code>tunnel</code> flag has been set (tunnel-xmit), full <code>pfkey</code> sockets debugging has been set and everything else is not set.</p>
<h2>Files</h2>
<p>/proc/net/ipsec_klipsdebug, /usr/local/bin/ipsec</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipsec/">ipsec</a>(8), <a href="/docs/linux/man/8-ipsec_tncfg/">ipsec_tncfg</a>(8), <a href="/docs/linux/man/8-ipsec_eroute/">ipsec_eroute</a>(8), <a href="/docs/linux/man/8-ipsec_spi/">ipsec_spi</a>(8), <a href="/docs/linux/man/8-ipsec_spigrp/">ipsec_spigrp</a>(8), <a href="/docs/linux/man/5-ipsec_klipsdebug/">ipsec_klipsdebug</a>(5), <a href="/docs/linux/man/5-ipsec_version/">ipsec_version</a>(5), <a href="/docs/linux/man/5-ipsec_pf_key/">ipsec_pf_key</a>(5)</p>
<h2>History</h2>
<p>Written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org/">http://www.freeswan.org/</a></code>m[]&gt; by Richard Guy Briggs.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
