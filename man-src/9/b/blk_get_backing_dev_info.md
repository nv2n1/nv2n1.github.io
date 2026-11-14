---
title: "blk_get_backing_dev_info(9)"
name: "blk_get_backing_dev_info"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_get_backing_dev_info/"
---

blk_get_backing_dev_info - get the address of a queue's backing_dev_info

<h2>Synopsis</h2>

<pre><code>struct backing_dev_info *blk_get_backing_dev_info(struct block_device *bdev);</code></pre>

<h2>Arguments</h2>

<i>bdev</i>
<dl><dd><dd>device</dl>

<h2>Description</h2>

Locates the passed device's request queue and returns the address of its backing_dev_info. This function can only be called if <i>bdev</i> is opened and the return value is never NULL.

<h2>Copyright</h2>


