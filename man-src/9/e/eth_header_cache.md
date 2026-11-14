---
title: "eth_header_cache(9)"
name: "eth_header_cache"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eth_header_cache/"
---

eth_header_cache - fill cache entry from neighbour

<h2>Synopsis</h2>

<pre><code>int eth_header_cache(const struct neighbour *neigh, struct hh_cache *hh, __be16 type);</code></pre>

<h2>Arguments</h2>

<i>neigh</i>
<dl><dd><dd>source neighbour</dl>
 

 <i>hh</i>
<dl><dd>destination cache entry</dl>
 

 <i>type</i>
<dl><dd>Ethernet type field</dl>

<h2>Description</h2>

Create an Ethernet header template from the neighbour.

<h2>Copyright</h2>


