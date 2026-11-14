---
title: "disk_unblock_events(9)"
name: "disk_unblock_events"
section: "9"
letter: "d"
url: "/docs/linux/man/9-disk_unblock_events/"
description: "disk_unblock_events – unblock disk event checking"
---

<p>disk_unblock_events &#8211; unblock disk event checking</p>
<h2>Synopsis</h2>
<pre><code>void disk_unblock_events(struct gendisk *disk);</code></pre>
<h2>Arguments</h2>
<p><i>disk</i></p>
<dl>
<dd>
<dd>disk to unblock events for</dl>
<h2>Description</h2>
<p>Undo <code>disk_block_events</code>. When the block count reaches zero, it starts events polling if configured.</p>
<h2>Context</h2>
<p>Don&#8217;t care. Safe to call from irq context.</p>
<h2>Copyright</h2>
