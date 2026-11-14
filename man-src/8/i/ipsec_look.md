---
title: "ipsec_look(8)"
name: "ipsec_look"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_look/"
description: "ipsec_look – get a quick summary of Libreswan status"
---

<p>ipsec_look &#8211; get a quick summary of Libreswan status</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> <i>look</i></dl>
<h2>Description</h2>
<p><i>Look</i></p>
<dd>is used to get a quick overview of what the status of Libreswan is. It is the equivalent to running the commands <i>ipsec eroute</i>, <i>ipsec spigrp</i>, <i>ipsec tncfg</i>, <i>ipsec spi</i> and <i>netstat -rn</i>. However a bit of processing is done to combine the outputs. </p>
<p> Some of the above commands, and therefore <i>ipsec look</i>, are only supported with the KLIPS or MAST stack, and will give errors when used on BSD, Windows or Linux with NETKEY.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ipsec/">ipsec</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_tncfg/">ipsec_tncfg</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_spi/">ipsec_spi</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_spigrp/">ipsec_spigrp</a></code>(8), <code><a href="/docs/linux/man/5-ipsec_eroute/">ipsec_eroute</a></code>(5), <code><a href="/docs/linux/man/8-netstat/">netstat</a></code>(8).</p>
<h2>History</h2>
<p>Man page written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org/">http://www.freeswan.org/</a></code>m[]&gt; by Michael Richardson. Original program written by Henry Spencer.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
