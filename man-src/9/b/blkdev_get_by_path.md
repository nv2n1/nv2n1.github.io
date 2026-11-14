---
title: "blkdev_get_by_path(9)"
name: "blkdev_get_by_path"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blkdev_get_by_path/"
description: "blkdev_get_by_path – open a block device by name"
---

<p>blkdev_get_by_path &#8211; open a block device by name</p>
<h2>Synopsis</h2>
<pre><code>struct block_device *blkdev_get_by_path(const char *path, fmode_t mode, void *holder);</code></pre>
<h2>Arguments</h2>
<p><i>path</i></p>
<dl>
<dd>
<dd>path to the block device to open</dl>
<p> <i>mode</i></p>
<dl>
<dd>FMODE_* mask</dl>
<p> <i>holder</i></p>
<dl>
<dd>exclusive holder identifier</dl>
<h2>Description</h2>
<p>Open the blockdevice described by the device file at <i>path</i>. <i>mode</i> and <i>holder</i> are identical to <code>blkdev_get</code>. </p>
<p> On success, the returned block_device has reference count of one.</p>
<h2>Context</h2>
<p>Might sleep.</p>
<h2>Return</h2>
<p>Pointer to block_device on success, ERR_PTR(-errno) on failure.</p>
<h2>Copyright</h2>
