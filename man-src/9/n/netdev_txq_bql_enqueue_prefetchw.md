---
title: "netdev_txq_bql_enqueue_prefetchw(9)"
name: "netdev_txq_bql_enqueue_prefetchw"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_txq_bql_enqueue_prefetchw/"
description: "netdev_txq_bql_enqueue_prefetchw – prefetch bql data for write"
---

<p>netdev_txq_bql_enqueue_prefetchw &#8211; prefetch bql data for write</p>
<h2>Synopsis</h2>
<pre><code>void netdev_txq_bql_enqueue_prefetchw(struct netdev_queue *dev_queue);</code></pre>
<h2>Arguments</h2>
<p><i>dev_queue</i></p>
<dl>
<dd>
<dd>pointer to transmit queue</dl>
<h2>Description</h2>
<p>BQL enabled drivers might use this helper in their <code>ndo_start_xmit</code>, to give appropriate hint to the CPU.</p>
<h2>Copyright</h2>
