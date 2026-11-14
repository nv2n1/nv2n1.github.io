---
title: "netdev_txq_bql_complete_prefetchw(9)"
name: "netdev_txq_bql_complete_prefetchw"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_txq_bql_complete_prefetchw/"
---

netdev_txq_bql_complete_prefetchw - prefetch bql data for write

<h2>Synopsis</h2>

<pre><code>void netdev_txq_bql_complete_prefetchw(struct netdev_queue *dev_queue);</code></pre>

<h2>Arguments</h2>

<i>dev_queue</i>
<dl><dd><dd>pointer to transmit queue</dl>

<h2>Description</h2>

BQL enabled drivers might use this helper in their TX completion path, to give appropriate hint to the CPU.

<h2>Copyright</h2>


