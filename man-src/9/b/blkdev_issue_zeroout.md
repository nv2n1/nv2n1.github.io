---
title: "blkdev_issue_zeroout(9)"
name: "blkdev_issue_zeroout"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blkdev_issue_zeroout/"
description: "blkdev_issue_zeroout – zero-fill a block range"
---

<p>blkdev_issue_zeroout &#8211; zero-fill a block range</p>
<h2>Synopsis</h2>
<pre><code>int blkdev_issue_zeroout(struct block_device *bdev, sector_t sector, sector_t nr_sects, gfp_t gfp_mask, bool discard);</code></pre>
<h2>Arguments</h2>
<p><i>bdev</i></p>
<dl>
<dd>
<dd>blockdev to write</dl>
<p> <i>sector</i></p>
<dl>
<dd>start sector</dl>
<p> <i>nr_sects</i></p>
<dl>
<dd>number of sectors to write</dl>
<p> <i>gfp_mask</i></p>
<dl>
<dd>memory allocation flags (for bio_alloc)</dl>
<p> <i>discard</i></p>
<dl>
<dd>whether to discard the block range</dl>
<h2>Description</h2>
<p>Zero-fill a block range. If the discard flag is set and the block device guarantees that subsequent READ operations to the block range in question will return zeroes, the blocks will be discarded. Should the discard request fail, if the discard flag is not set, or if discard_zeroes_data is not supported, this function will resort to zeroing the blocks manually, thus provisioning (allocating, anchoring) them. If the block device supports the WRITE SAME command <code>blkdev_issue_zeroout</code> will use it to optimize the process of clearing the block range. Otherwise the zeroing will be performed using regular WRITE calls.</p>
<h2>Copyright</h2>
