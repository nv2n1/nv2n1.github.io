---
title: "rio_enable_rx_tx_port(9)"
name: "rio_enable_rx_tx_port"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_enable_rx_tx_port/"
description: "rio_enable_rx_tx_port – enable input receiver and output transmitter of given port"
---

<p>rio_enable_rx_tx_port &#8211; enable input receiver and output transmitter of given port</p>
<h2>Synopsis</h2>
<pre><code>int rio_enable_rx_tx_port(struct rio_mport *port, int local, u16 destid, u8 hopcount, u8 port_num);</code></pre>
<h2>Arguments</h2>
<p><i>port</i></p>
<dl>
<dd>
<dd>Master port associated with the RIO network</dl>
<p> <i>local</i></p>
<dl>
<dd>local=1 select local port otherwise a far device is reached</dl>
<p> <i>destid</i></p>
<dl>
<dd>Destination ID of the device to check host bit</dl>
<p> <i>hopcount</i></p>
<dl>
<dd>Number of hops to reach the target</dl>
<p> <i>port_num</i></p>
<dl>
<dd>Port (-number on switch) to enable on a far end device</dl>
<h2>Description</h2>
<p>Returns 0 or 1 from on General Control Command and Status Register (EXT_PTR+0x3C)</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
