---
title: "blk_lld_busy(9)"
name: "blk_lld_busy"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_lld_busy/"
description: "blk_lld_busy – Check if underlying low-level drivers of a device are busy"
---

<p>blk_lld_busy &#8211; Check if underlying low-level drivers of a device are busy</p>
<h2>Synopsis</h2>
<pre><code>int blk_lld_busy(struct request_queue *q);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>the queue of the device being checked</dl>
<h2>Description</h2>
<p>Check if underlying low-level drivers of a device are busy. If the drivers want to export their busy state, they must set own exporting function using <code>blk_queue_lld_busy</code> first. </p>
<p> Basically, this function is used only by request stacking drivers to stop dispatching requests to underlying devices when underlying devices are busy. This behavior helps more I/O merging on the queue of the request stacking driver and prevents I/O throughput regression on burst I/O load.</p>
<h2>Return</h2>
<p>0 &#8211; Not busy (The request stacking driver should dispatch request) 1 &#8211; Busy (The request stacking driver should stop dispatching request)</p>
<h2>Copyright</h2>
