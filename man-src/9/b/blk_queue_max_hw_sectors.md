---
title: "blk_queue_max_hw_sectors(9)"
name: "blk_queue_max_hw_sectors"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_max_hw_sectors/"
---

blk_queue_max_hw_sectors - set max sectors for a request for this queue

<h2>Synopsis</h2>

<pre><code>void blk_queue_max_hw_sectors(struct request_queue *q, unsigned int max_hw_sectors);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the request queue for the device</dl>
 

 <i>max_hw_sectors</i>
<dl><dd>max hardware sectors in the usual 512b unit</dl>

<h2>Description</h2>

Enables a low level driver to set a hard upper limit, max_hw_sectors, on the size of requests. max_hw_sectors is set by the device driver based upon the capabilities of the I/O controller. 

 max_dev_sectors is a hard limit imposed by the storage device for READ/WRITE requests. It is set by the disk driver. 

 max_sectors is a soft limit imposed by the block layer for filesystem type requests. This value can be overridden on a per-device basis in /sys/block/&lt;device&gt;/queue/max_sectors_kb. The soft limit can not exceed max_hw_sectors.

<h2>Copyright</h2>


