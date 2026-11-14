---
title: "netdev_completed_queue(9)"
name: "netdev_completed_queue"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_completed_queue/"
description: "netdev_completed_queue – report bytes and packets completed by device"
---

<p>netdev_completed_queue &#8211; report bytes and packets completed by device</p>
<h2>Synopsis</h2>
<pre><code>void netdev_completed_queue(struct net_device *dev, unsigned int pkts, unsigned int bytes);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>network device</dl>
<p> <i>pkts</i></p>
<dl>
<dd>actual number of packets sent over the medium</dl>
<p> <i>bytes</i></p>
<dl>
<dd>actual number of bytes sent over the medium</dl>
<h2>Description</h2>
<p>Report the number of bytes and packets transmitted by the network device hardware queue over the physical medium, <i>bytes</i> must exactly match the <i>bytes</i> amount passed to <code>netdev_sent_queue</code></p>
<h2>Copyright</h2>
