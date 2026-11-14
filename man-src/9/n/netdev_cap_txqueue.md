---
title: "netdev_cap_txqueue(9)"
name: "netdev_cap_txqueue"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_cap_txqueue/"
description: "netdev_cap_txqueue – check if selected tx queue exceeds device queues"
---

<p>netdev_cap_txqueue &#8211; check if selected tx queue exceeds device queues</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u16 netdev_cap_txqueue(struct net_device&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>, u16&nbsp;<wbr></code><i>queue_index</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>network device</dl>
<p> <i>queue_index</i></p>
<dl>
<dd>given tx queue index</dl>
<h2>Description</h2>
<p>Returns 0 if given tx queue index &gt;= number of device tx queues, otherwise returns the originally passed tx queue index.</p>
<h2>Copyright</h2>
