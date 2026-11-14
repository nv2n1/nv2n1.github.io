---
title: "bdev_direct_access(9)"
name: "bdev_direct_access"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bdev_direct_access/"
description: "bdev_direct_access – Get the address for directly-accessibly memory"
---

<p>bdev_direct_access &#8211; Get the address for directly-accessibly memory</p>
<h2>Synopsis</h2>
<pre><code>long bdev_direct_access(struct block_device *bdev, struct blk_dax_ctl *dax);</code></pre>
<h2>Arguments</h2>
<p><i>bdev</i></p>
<dl>
<dd>
<dd>The device containing the memory</dl>
<p> <i>dax</i></p>
<dl>
<dd>control and output parameters for -&gt;direct_access</dl>
<h2>Description</h2>
<p>If a block device is made up of directly addressable memory, this function will tell the caller the PFN and the address of the memory. The address may be directly dereferenced within the kernel without the need to call <code>ioremap</code>, <code>kmap</code> or similar. The PFN is suitable for inserting into page tables.</p>
<h2>Return</h2>
<p>negative errno if an error occurs, otherwise the number of bytes accessible at this address.</p>
<h2>Copyright</h2>
