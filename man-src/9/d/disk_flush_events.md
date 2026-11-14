---
title: "disk_flush_events(9)"
name: "disk_flush_events"
section: "9"
letter: "d"
url: "/docs/linux/man/9-disk_flush_events/"
---

disk_flush_events - schedule immediate event checking and flushing

<h2>Synopsis</h2>

<pre><code>void disk_flush_events(struct gendisk *disk, unsigned int mask);</code></pre>

<h2>Arguments</h2>

<i>disk</i>
<dl><dd><dd>disk to check and flush events for</dl>
 

 <i>mask</i>
<dl><dd>events to flush</dl>

<h2>Description</h2>

Schedule immediate event checking on <i>disk</i> if not blocked. Events in <i>mask</i> are scheduled to be cleared from the driver. Note that this doesn't clear the events from <i>disk</i>-&gt;ev.

<h2>Context</h2>

If <i>mask</i> is non-zero must be called with bdev-&gt;bd_mutex held.

<h2>Copyright</h2>


