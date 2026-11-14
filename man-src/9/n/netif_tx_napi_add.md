---
title: "netif_tx_napi_add(9)"
name: "netif_tx_napi_add"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netif_tx_napi_add/"
description: "netif_tx_napi_add – initialize a NAPI context"
---

<p>netif_tx_napi_add &#8211; initialize a NAPI context</p>
<h2>Synopsis</h2>
<pre><code>void netif_tx_napi_add(struct net_device *dev, struct napi_struct *napi, int (*poll)(struct napi_struct *, int), int weight);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>network device</dl>
<p> <i>napi</i></p>
<dl>
<dd>NAPI context</dl>
<p> <i>poll</i></p>
<dl>
<dd>polling function</dl>
<p> <i>weight</i></p>
<dl>
<dd>default weight</dl>
<h2>Description</h2>
<p>This variant of <code>netif_napi_add</code> should be used from drivers using NAPI to exclusively poll a TX queue. This will avoid we add it into napi_hash[], thus polluting this hash table.</p>
<h2>Copyright</h2>
