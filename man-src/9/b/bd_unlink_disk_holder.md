---
title: "bd_unlink_disk_holder(9)"
name: "bd_unlink_disk_holder"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bd_unlink_disk_holder/"
description: "bd_unlink_disk_holder – destroy symlinks created by bd_link_disk_holder"
---

<p>bd_unlink_disk_holder &#8211; destroy symlinks created by <code>bd_link_disk_holder</code></p>
<h2>Synopsis</h2>
<pre><code>void bd_unlink_disk_holder(struct block_device *bdev, struct gendisk *disk);</code></pre>
<h2>Arguments</h2>
<p><i>bdev</i></p>
<dl>
<dd>
<dd>the calimed slave bdev</dl>
<p> <i>disk</i></p>
<dl>
<dd>the holding disk</dl>
<h2>Description</h2>
<p>DON&#8217;T USE THIS UNLESS YOU&#8217;RE ALREADY USING IT.</p>
<h2>Context</h2>
<p>Might sleep.</p>
<h2>Copyright</h2>
