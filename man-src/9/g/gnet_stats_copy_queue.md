---
title: "gnet_stats_copy_queue(9)"
name: "gnet_stats_copy_queue"
section: "9"
letter: "g"
url: "/docs/linux/man/9-gnet_stats_copy_queue/"
description: "gnet_stats_copy_queue – copy queue statistics into statistics TLV"
---

<p>gnet_stats_copy_queue &#8211; copy queue statistics into statistics TLV</p>
<h2>Synopsis</h2>
<pre><code>int gnet_stats_copy_queue(struct gnet_dump *d, struct gnet_stats_queue __percpu *cpu_q, struct gnet_stats_queue *q, __u32 qlen);</code></pre>
<h2>Arguments</h2>
<p><i>d</i></p>
<dl>
<dd>
<dd>dumping handle</dl>
<p> <i>cpu_q</i></p>
<dl>
<dd>per cpu queue statistics</dl>
<p> <i>q</i></p>
<dl>
<dd>queue statistics</dl>
<p> <i>qlen</i></p>
<dl>
<dd>queue length statistics</dl>
<h2>Description</h2>
<p>Appends the queue statistics to the top level TLV created by <code>gnet_stats_start_copy</code>. Using per cpu queue statistics if they are available. </p>
<p> Returns 0 on success or -1 with the statistic lock released if the room in the socket buffer was not sufficient.</p>
<h2>Copyright</h2>
