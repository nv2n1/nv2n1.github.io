---
title: "idr_alloc_cyclic(9)"
name: "idr_alloc_cyclic"
section: "9"
letter: "i"
url: "/docs/linux/man/9-idr_alloc_cyclic/"
---

idr_alloc_cyclic - allocate new idr entry in a cyclical fashion

<h2>Synopsis</h2>

<pre><code>int idr_alloc_cyclic(struct idr *idr, void *ptr, int start, int end, gfp_t gfp_mask);</code></pre>

<h2>Arguments</h2>

<i>idr</i>
<dl><dd><dd>the (initialized) idr</dl>
 

 <i>ptr</i>
<dl><dd>pointer to be associated with the new id</dl>
 

 <i>start</i>
<dl><dd>the minimum id (inclusive)</dl>
 

 <i>end</i>
<dl><dd>the maximum id (exclusive, &lt;= 0 for max)</dl>
 

 <i>gfp_mask</i>
<dl><dd>memory allocation flags</dl>

<h2>Description</h2>

Essentially the same as idr_alloc, but prefers to allocate progressively higher ids if it can. If the "cur" counter wraps, then it will start again at the "start" end of the range and allocate one that has already been used.

<h2>Copyright</h2>


