---
title: "blk_queue_max_write_same_sectors(9)"
name: "blk_queue_max_write_same_sectors"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_max_write_same_sectors/"
---

blk_queue_max_write_same_sectors - set max sectors for a single write same

<h2>Synopsis</h2>

<pre><code>void blk_queue_max_write_same_sectors(struct request_queue *q, unsigned int max_write_same_sectors);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the request queue for the device</dl>
 

 <i>max_write_same_sectors</i>
<dl><dd>maximum number of sectors to write per command</dl>

<h2>Copyright</h2>


