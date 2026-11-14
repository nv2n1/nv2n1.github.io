---
title: "blk_delay_queue(9)"
name: "blk_delay_queue"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_delay_queue/"
---

blk_delay_queue - restart queueing after defined interval

<h2>Synopsis</h2>

<pre><code>void blk_delay_queue(struct request_queue *q, unsigned long msecs);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>The struct request_queue in question</dl>
 

 <i>msecs</i>
<dl><dd>Delay in msecs</dl>

<h2>Description</h2>

Sometimes queueing needs to be postponed for a little while, to allow resources to come back. This function will make sure that queueing is restarted around the specified time. Queue lock must be held.

<h2>Copyright</h2>


