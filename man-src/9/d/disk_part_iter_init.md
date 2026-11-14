---
title: "disk_part_iter_init(9)"
name: "disk_part_iter_init"
section: "9"
letter: "d"
url: "/docs/linux/man/9-disk_part_iter_init/"
---

disk_part_iter_init - initialize partition iterator

<h2>Synopsis</h2>

<pre><code>void disk_part_iter_init(struct disk_part_iter *piter, struct gendisk *disk, unsigned int flags);</code></pre>

<h2>Arguments</h2>

<i>piter</i>
<dl><dd><dd>iterator to initialize</dl>
 

 <i>disk</i>
<dl><dd>disk to iterate over</dl>
 

 <i>flags</i>
<dl><dd>DISK_PITER_* flags</dl>

<h2>Description</h2>

Initialize <i>piter</i> so that it iterates over partitions of <i>disk</i>.

<h2>Context</h2>

Don't care.

<h2>Copyright</h2>


