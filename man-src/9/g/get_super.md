---
title: "get_super(9)"
name: "get_super"
section: "9"
letter: "g"
url: "/docs/linux/man/9-get_super/"
description: "get_super – get the superblock of a device"
---

<p>get_super &#8211; get the superblock of a device</p>
<h2>Synopsis</h2>
<pre><code>struct super_block *get_super(struct block_device *bdev);</code></pre>
<h2>Arguments</h2>
<p><i>bdev</i></p>
<dl>
<dd>
<dd>device to get the superblock for </p>
<p> Scans the superblock list and finds the superblock of the file system mounted on the device given. <code>NULL</code> is returned if no match is found.</dl>
<h2>Copyright</h2>
