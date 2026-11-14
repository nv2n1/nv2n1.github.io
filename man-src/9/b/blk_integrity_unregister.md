---
title: "blk_integrity_unregister(9)"
name: "blk_integrity_unregister"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_integrity_unregister/"
---

blk_integrity_unregister - Unregister block integrity profile

<h2>Synopsis</h2>

<pre><code>void blk_integrity_unregister(struct gendisk *disk);</code></pre>

<h2>Arguments</h2>

<i>disk</i>
<dl><dd><dd>disk whose integrity profile to unregister</dl>

<h2>Description</h2>

This function unregisters the integrity capability from a block device.

<h2>Copyright</h2>


