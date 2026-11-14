---
title: "eth_header_cache_update(9)"
name: "eth_header_cache_update"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eth_header_cache_update/"
---

eth_header_cache_update - update cache entry

<h2>Synopsis</h2>

<pre><code>void eth_header_cache_update(struct hh_cache *hh, const struct net_device *dev, const unsigned char *haddr);</code></pre>

<h2>Arguments</h2>

<i>hh</i>
<dl><dd><dd>destination cache entry</dl>
 

 <i>dev</i>
<dl><dd>network device</dl>
 

 <i>haddr</i>
<dl><dd>new hardware address</dl>

<h2>Description</h2>

Called by Address Resolution module to notify changes in address.

<h2>Copyright</h2>


