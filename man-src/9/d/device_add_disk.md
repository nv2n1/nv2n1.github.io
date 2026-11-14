---
title: "device_add_disk(9)"
name: "device_add_disk"
section: "9"
letter: "d"
url: "/docs/linux/man/9-device_add_disk/"
---

device_add_disk - add partitioning information to kernel list

<h2>Synopsis</h2>

<pre><code>void device_add_disk(struct device *parent, struct gendisk *disk);</code></pre>

<h2>Arguments</h2>

<i>parent</i>
<dl><dd><dd>parent device for the disk</dl>
 

 <i>disk</i>
<dl><dd>per-device partitioning information</dl>

<h2>Description</h2>

This function registers the partitioning information in <i>disk</i> with the kernel. 

 FIXME: error handling

<h2>Copyright</h2>


