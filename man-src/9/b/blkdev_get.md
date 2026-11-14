---
title: "blkdev_get(9)"
name: "blkdev_get"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blkdev_get/"
description: "blkdev_get – open a block device"
---

<p>blkdev_get &#8211; open a block device</p>
<h2>Synopsis</h2>
<pre><code>int blkdev_get(struct block_device *bdev, fmode_t mode, void *holder);</code></pre>
<h2>Arguments</h2>
<p><i>bdev</i></p>
<dl>
<dd>
<dd>block_device to open</dl>
<p> <i>mode</i></p>
<dl>
<dd>FMODE_* mask</dl>
<p> <i>holder</i></p>
<dl>
<dd>exclusive holder identifier</dl>
<h2>Description</h2>
<p>Open <i>bdev</i> with <i>mode</i>. If <i>mode</i> includes <code>FMODE_EXCL</code>, <i>bdev</i> is open with exclusive access. Specifying <code>FMODE_EXCL</code> with <code>NULL</code><i>holder</i> is invalid. Exclusive opens may nest for the same <i>holder</i>. </p>
<p> On success, the reference count of <i>bdev</i> is unchanged. On failure, <i>bdev</i> is put.</p>
<h2>Context</h2>
<p>Might sleep.</p>
<h2>Return</h2>
<p>0 on success, -errno on failure.</p>
<h2>Copyright</h2>
