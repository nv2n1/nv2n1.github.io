---
title: "netdev_sent_queue(9)"
name: "netdev_sent_queue"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_sent_queue/"
description: "netdev_sent_queue – report the number of bytes queued to hardware"
---

<p>netdev_sent_queue &#8211; report the number of bytes queued to hardware</p>
<h2>Synopsis</h2>
<pre><code>void netdev_sent_queue(struct net_device *dev, unsigned int bytes);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>network device</dl>
<p> <i>bytes</i></p>
<dl>
<dd>number of bytes queued to the hardware device queue</dl>
<h2>Description</h2>
<p>Report the number of bytes queued for sending/completion to the network device hardware queue. <i>bytes</i> should be a good approximation and should exactly match <code>netdev_completed_queue</code><i>bytes</i></p>
<h2>Copyright</h2>
