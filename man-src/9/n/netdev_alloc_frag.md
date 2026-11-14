---
title: "netdev_alloc_frag(9)"
name: "netdev_alloc_frag"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_alloc_frag/"
---

netdev_alloc_frag - allocate a page fragment

<h2>Synopsis</h2>

<pre><code>void *netdev_alloc_frag(unsigned int fragsz);</code></pre>

<h2>Arguments</h2>

<i>fragsz</i>
<dl><dd><dd>fragment size</dl>

<h2>Description</h2>

Allocates a frag from a page for receive buffer. Uses GFP_ATOMIC allocations.

<h2>Copyright</h2>


