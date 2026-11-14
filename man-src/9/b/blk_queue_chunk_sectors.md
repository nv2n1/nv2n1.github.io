---
title: "blk_queue_chunk_sectors(9)"
name: "blk_queue_chunk_sectors"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_chunk_sectors/"
---

blk_queue_chunk_sectors - set size of the chunk for this queue

<h2>Synopsis</h2>

<pre><code>void blk_queue_chunk_sectors(struct request_queue *q, unsigned int chunk_sectors);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the request queue for the device</dl>
 

 <i>chunk_sectors</i>
<dl><dd>chunk sectors in the usual 512b unit</dl>

<h2>Description</h2>

If a driver doesn't want IOs to cross a given chunk size, it can set this limit and prevent merging across chunks. Note that the chunk size must currently be a power-of-2 in sectors. Also note that the block layer must accept a page worth of data at any offset. So if the crossing of chunks is a hard limitation in the driver, it must still be prepared to split single page bios.

<h2>Copyright</h2>


