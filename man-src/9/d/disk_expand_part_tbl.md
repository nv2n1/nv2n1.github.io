---
title: "disk_expand_part_tbl(9)"
name: "disk_expand_part_tbl"
section: "9"
letter: "d"
url: "/docs/linux/man/9-disk_expand_part_tbl/"
---

disk_expand_part_tbl - expand disk-&gt;part_tbl

<h2>Synopsis</h2>

<pre><code>int disk_expand_part_tbl(struct gendisk *disk, int partno);</code></pre>

<h2>Arguments</h2>

<i>disk</i>
<dl><dd><dd>disk to expand part_tbl for</dl>
 

 <i>partno</i>
<dl><dd>expand such that this partno can fit in</dl>

<h2>Description</h2>

Expand disk-&gt;part_tbl such that <i>partno</i> can fit in. disk-&gt;part_tbl uses RCU to allow unlocked dereferencing for stats and other stuff. 

 LOCKING: Matching bd_mutex locked, might sleep.

<h2>Return</h2>

0 on success, -errno on failure.

<h2>Copyright</h2>


