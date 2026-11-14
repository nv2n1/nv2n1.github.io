---
title: "disk_clear_events(9)"
name: "disk_clear_events"
section: "9"
letter: "d"
url: "/docs/linux/man/9-disk_clear_events/"
---

disk_clear_events - synchronously check, clear and return pending events

<h2>Synopsis</h2>

<pre><code>unsigned int disk_clear_events(struct gendisk *disk, unsigned int mask);</code></pre>

<h2>Arguments</h2>

<i>disk</i>
<dl><dd><dd>disk to fetch and clear events from</dl>
 

 <i>mask</i>
<dl><dd>mask of events to be fetched and cleared</dl>

<h2>Description</h2>

Disk events are synchronously checked and pending events in <i>mask</i> are cleared and returned. This ignores the block count.

<h2>Context</h2>

Might sleep.

<h2>Copyright</h2>


