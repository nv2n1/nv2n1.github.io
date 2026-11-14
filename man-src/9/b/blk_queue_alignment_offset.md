---
title: "blk_queue_alignment_offset(9)"
name: "blk_queue_alignment_offset"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_alignment_offset/"
---

blk_queue_alignment_offset - set physical block alignment offset

<h2>Synopsis</h2>

<pre><code>void blk_queue_alignment_offset(struct request_queue *q, unsigned int offset);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the request queue for the device</dl>
 

 <i>offset</i>
<dl><dd>alignment offset in bytes</dl>

<h2>Description</h2>

Some devices are naturally misaligned to compensate for things like the legacy DOS partition table 63-sector offset. Low-level drivers should call this function for devices whose first sector is not naturally aligned.

<h2>Copyright</h2>


