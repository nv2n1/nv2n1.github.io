---
title: "check_disk_size_change(9)"
name: "check_disk_size_change"
section: "9"
letter: "c"
url: "/docs/linux/man/9-check_disk_size_change/"
---

check_disk_size_change - checks for disk size change and adjusts bdev size.

<h2>Synopsis</h2>

<pre><code>void check_disk_size_change(struct gendisk *disk, struct block_device *bdev);</code></pre>

<h2>Arguments</h2>

<i>disk</i>
<dl><dd><dd>struct gendisk to check</dl>
 

 <i>bdev</i>
<dl><dd>struct bdev to adjust.</dl>

<h2>Description</h2>

This routine checks to see if the bdev size does not match the disk size and adjusts it if it differs.

<h2>Copyright</h2>


