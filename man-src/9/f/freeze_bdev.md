---
title: "freeze_bdev(9)"
name: "freeze_bdev"
section: "9"
letter: "f"
url: "/docs/linux/man/9-freeze_bdev/"
description: "freeze_bdev – – lock a filesystem and force it into a consistent state"
---

<p>freeze_bdev &#8211; &#8211; lock a filesystem and force it into a consistent state</p>
<h2>Synopsis</h2>
<pre><code>struct super_block *freeze_bdev(struct block_device *bdev);</code></pre>
<h2>Arguments</h2>
<p><i>bdev</i></p>
<dl>
<dd>
<dd>blockdevice to lock</dl>
<h2>Description</h2>
<p>If a superblock is found on this device, we take the s_umount semaphore on it to make sure nobody unmounts until the snapshot creation is done. The reference counter (bd_fsfreeze_count) guarantees that only the last unfreeze process can unfreeze the frozen filesystem actually when multiple freeze requests arrive simultaneously. It counts up in <code>freeze_bdev</code> and count down in <code>thaw_bdev</code>. When it becomes 0, <code>thaw_bdev</code> will unfreeze actually.</p>
<h2>Copyright</h2>
