---
title: "blkdev_issue_write_same(9)"
name: "blkdev_issue_write_same"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blkdev_issue_write_same/"
---

blkdev_issue_write_same - queue a write same operation

<h2>Synopsis</h2>

<pre><code>int blkdev_issue_write_same(struct block_device *bdev, sector_t sector, sector_t nr_sects, gfp_t gfp_mask, struct page *page);</code></pre>

<h2>Arguments</h2>

<i>bdev</i>
<dl><dd><dd>target blockdev</dl>
 

 <i>sector</i>
<dl><dd>start sector</dl>
 

 <i>nr_sects</i>
<dl><dd>number of sectors to write</dl>
 

 <i>gfp_mask</i>
<dl><dd>memory allocation flags (for bio_alloc)</dl>
 

 <i>page</i>
<dl><dd>page containing data to write</dl>

<h2>Description</h2>

Issue a write same request for the sectors in question.

<h2>Copyright</h2>


