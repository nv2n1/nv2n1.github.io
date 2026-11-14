---
title: "dev_fill_metadata_dst(9)"
name: "dev_fill_metadata_dst"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_fill_metadata_dst/"
---

dev_fill_metadata_dst - Retrieve tunnel egress information.

<h2>Synopsis</h2>

<pre><code>int dev_fill_metadata_dst(struct net_device *dev, struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>targeted interface</dl>
 

 <i>skb</i>
<dl><dd>The packet.</dl>

<h2>Description</h2>

For better visibility of tunnel traffic OVS needs to retrieve egress tunnel information for a packet. Following API allows user to get this info.

<h2>Copyright</h2>


