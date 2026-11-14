---
title: "thaw_bdev(9)"
name: "thaw_bdev"
section: "9"
letter: "t"
url: "/docs/linux/man/9-thaw_bdev/"
description: "thaw_bdev – – unlock filesystem"
---

<p>thaw_bdev &#8211; &#8211; unlock filesystem</p>
<h2>Synopsis</h2>
<pre><code>int thaw_bdev(struct block_device *bdev, struct super_block *sb);</code></pre>
<h2>Arguments</h2>
<p><i>bdev</i></p>
<dl>
<dd>
<dd>blockdevice to unlock</dl>
<p> <i>sb</i></p>
<dl>
<dd>associated superblock</dl>
<h2>Description</h2>
<p>Unlocks the filesystem and marks it writeable again after <code>freeze_bdev</code>.</p>
<h2>Copyright</h2>
