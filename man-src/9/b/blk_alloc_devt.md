---
title: "blk_alloc_devt(9)"
name: "blk_alloc_devt"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_alloc_devt/"
---

blk_alloc_devt - allocate a dev_t for a partition

<h2>Synopsis</h2>

<pre><code>int blk_alloc_devt(struct hd_struct *part, dev_t *devt);</code></pre>

<h2>Arguments</h2>

<i>part</i>
<dl><dd><dd>partition to allocate dev_t for</dl>
 

 <i>devt</i>
<dl><dd>out parameter for resulting dev_t</dl>

<h2>Description</h2>

Allocate a dev_t for block device.

<h2>Return</h2>

0 on success, allocated dev_t is returned in *<i>devt</i>. -errno on failure.

<h2>Context</h2>

Might sleep.

<h2>Copyright</h2>


