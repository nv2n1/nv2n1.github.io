---
title: "blk_queue_write_cache(9)"
name: "blk_queue_write_cache"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_write_cache/"
---

blk_queue_write_cache - configure queue's write cache

<h2>Synopsis</h2>

<pre><code>void blk_queue_write_cache(struct request_queue *q, bool wc, bool fua);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the request queue for the device</dl>
 

 <i>wc</i>
<dl><dd>write back cache on or off</dl>
 

 <i>fua</i>
<dl><dd>device supports FUA writes, if true</dl>

<h2>Description</h2>

Tell the block layer about the write cache of <i>q</i>.

<h2>Copyright</h2>


