---
title: "blk_stop_queue(9)"
name: "blk_stop_queue"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_stop_queue/"
description: "blk_stop_queue – stop a queue"
---

<p>blk_stop_queue &#8211; stop a queue</p>
<h2>Synopsis</h2>
<pre><code>void blk_stop_queue(struct request_queue *q);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>The struct request_queue in question</dl>
<h2>Description</h2>
<p>The Linux block layer assumes that a block driver will consume all entries on the request queue when the request_fn strategy is called. Often this will not happen, because of hardware limitations (queue depth settings). If a device driver gets a &#8216;queue full&#8217; response, or if it simply chooses not to queue more I/O at one point, it can call this function to prevent the request_fn from being called until the driver has signalled it&#8217;s ready to go again. This happens by calling <code>blk_start_queue</code> to restart queue operations. Queue lock must be held.</p>
<h2>Copyright</h2>
