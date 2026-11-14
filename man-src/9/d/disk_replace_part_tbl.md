---
title: "disk_replace_part_tbl(9)"
name: "disk_replace_part_tbl"
section: "9"
letter: "d"
url: "/docs/linux/man/9-disk_replace_part_tbl/"
---

disk_replace_part_tbl - replace disk-&gt;part_tbl in RCU-safe way

<h2>Synopsis</h2>

<pre><code>void disk_replace_part_tbl(struct gendisk *disk, struct disk_part_tbl *new_ptbl);</code></pre>

<h2>Arguments</h2>

<i>disk</i>
<dl><dd><dd>disk to replace part_tbl for</dl>
 

 <i>new_ptbl</i>
<dl><dd>new part_tbl to install</dl>

<h2>Description</h2>

Replace disk-&gt;part_tbl with <i>new_ptbl</i> in RCU-safe way. The original ptbl is freed using RCU callback. 

 LOCKING: Matching bd_mutx locked.

<h2>Copyright</h2>


