---
title: "blkdev_issue_discard(9)"
name: "blkdev_issue_discard"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blkdev_issue_discard/"
---

blkdev_issue_discard - queue a discard

<h2>Synopsis</h2>

<pre><code>int blkdev_issue_discard(struct block_device *bdev, sector_t sector, sector_t nr_sects, gfp_t gfp_mask, unsigned long flags);</code></pre>

<h2>Arguments</h2>

<i>bdev</i>
<dl><dd><dd>blockdev to issue discard for</dl>
 

 <i>sector</i>
<dl><dd>start sector</dl>
 

 <i>nr_sects</i>
<dl><dd>number of sectors to discard</dl>
 

 <i>gfp_mask</i>
<dl><dd>memory allocation flags (for bio_alloc)</dl>
 

 <i>flags</i>
<dl><dd>BLKDEV_IFL_* flags to control behaviour</dl>

<h2>Description</h2>

Issue a discard request for the sectors in question.

<h2>Copyright</h2>


