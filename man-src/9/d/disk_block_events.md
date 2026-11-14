---
title: "disk_block_events(9)"
name: "disk_block_events"
section: "9"
letter: "d"
url: "/docs/linux/man/9-disk_block_events/"
description: "disk_block_events – block and flush disk event checking"
---

<p>disk_block_events &#8211; block and flush disk event checking</p>
<h2>Synopsis</h2>
<pre><code>void disk_block_events(struct gendisk *disk);</code></pre>
<h2>Arguments</h2>
<p><i>disk</i></p>
<dl>
<dd>
<dd>disk to block events for</dl>
<h2>Description</h2>
<p>On return from this function, it is guaranteed that event checking isn&#8217;t in progress and won&#8217;t happen until unblocked by <code>disk_unblock_events</code>. Events blocking is counted and the actual unblocking happens after the matching number of unblocks are done. </p>
<p> Note that this intentionally does not block event checking from <code>disk_clear_events</code>.</p>
<h2>Context</h2>
<p>Might sleep.</p>
<h2>Copyright</h2>
