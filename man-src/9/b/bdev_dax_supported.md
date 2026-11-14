---
title: "bdev_dax_supported(9)"
name: "bdev_dax_supported"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bdev_dax_supported/"
---

bdev_dax_supported - Check if the device supports dax for filesystem

<h2>Synopsis</h2>

<pre><code>int bdev_dax_supported(struct super_block *sb, int blocksize);</code></pre>

<h2>Arguments</h2>

<i>sb</i>
<dl><dd><dd>The superblock of the device</dl>
 

 <i>blocksize</i>
<dl><dd>The block size of the device</dl>

<h2>Description</h2>

This is a library function for filesystems to check if the block device can be mounted with dax option.

<h2>Return</h2>

negative errno if unsupported, 0 if supported.

<h2>Copyright</h2>


