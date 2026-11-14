---
title: "blkdev_get_by_dev(9)"
name: "blkdev_get_by_dev"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blkdev_get_by_dev/"
description: "blkdev_get_by_dev – open a block device by device number"
---

<p>blkdev_get_by_dev &#8211; open a block device by device number</p>
<h2>Synopsis</h2>
<pre><code>struct block_device *blkdev_get_by_dev(dev_t dev, fmode_t mode, void *holder);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device number of block device to open</dl>
<p> <i>mode</i></p>
<dl>
<dd>FMODE_* mask</dl>
<p> <i>holder</i></p>
<dl>
<dd>exclusive holder identifier</dl>
<h2>Description</h2>
<p>Open the blockdevice described by device number <i>dev</i>. <i>mode</i> and <i>holder</i> are identical to <code>blkdev_get</code>. </p>
<p> Use it ONLY if you really do not have anything better &#8211; i.e. when you are behind a truly sucky interface and all you are given is a device number. _Never_ to be used for internal purposes. If you ever need it &#8211; reconsider your API. </p>
<p> On success, the returned block_device has reference count of one.</p>
<h2>Context</h2>
<p>Might sleep.</p>
<h2>Return</h2>
<p>Pointer to block_device on success, ERR_PTR(-errno) on failure.</p>
<h2>Copyright</h2>
