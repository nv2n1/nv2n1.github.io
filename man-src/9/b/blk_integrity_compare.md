---
title: "blk_integrity_compare(9)"
name: "blk_integrity_compare"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_integrity_compare/"
---

blk_integrity_compare - Compare integrity profile of two disks

<h2>Synopsis</h2>

<pre><code>int blk_integrity_compare(struct gendisk *gd1, struct gendisk *gd2);</code></pre>

<h2>Arguments</h2>

<i>gd1</i>
<dl><dd><dd>Disk to compare</dl>
 

 <i>gd2</i>
<dl><dd>Disk to compare</dl>

<h2>Description</h2>

Meta-devices like DM and MD need to verify that all sub-devices use the same integrity format before advertising to upper layers that they can send/receive integrity metadata. This function can be used to check whether two gendisk devices have compatible integrity formats.

<h2>Copyright</h2>


