---
title: "get_super_thawed(9)"
name: "get_super_thawed"
section: "9"
letter: "g"
url: "/docs/linux/man/9-get_super_thawed/"
description: "get_super_thawed – get thawed superblock of a device"
---

<p>get_super_thawed &#8211; get thawed superblock of a device</p>
<h2>Synopsis</h2>
<pre><code>struct super_block *get_super_thawed(struct block_device *bdev);</code></pre>
<h2>Arguments</h2>
<p><i>bdev</i></p>
<dl>
<dd>
<dd>device to get the superblock for</dl>
<h2>Description</h2>
<p>Scans the superblock list and finds the superblock of the file system mounted on the device. The superblock is returned once it is thawed (or immediately if it was not frozen). <code>NULL</code> is returned if no match is found.</p>
<h2>Copyright</h2>
