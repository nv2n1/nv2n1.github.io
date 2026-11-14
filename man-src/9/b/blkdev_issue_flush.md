---
title: "blkdev_issue_flush(9)"
name: "blkdev_issue_flush"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blkdev_issue_flush/"
---

blkdev_issue_flush - queue a flush

<h2>Synopsis</h2>

<pre><code>int blkdev_issue_flush(struct block_device *bdev, gfp_t gfp_mask, sector_t *error_sector);</code></pre>

<h2>Arguments</h2>

<i>bdev</i>
<dl><dd><dd>blockdev to issue flush for</dl>
 

 <i>gfp_mask</i>
<dl><dd>memory allocation flags (for bio_alloc)</dl>
 

 <i>error_sector</i>
<dl><dd>error sector</dl>

<h2>Description</h2>

Issue a flush for the block device in question. Caller can supply room for storing the error offset in case of a flush error, if they wish to. If WAIT flag is not passed then caller may check only what request was pushed in some internal queue for later handling.

<h2>Copyright</h2>


