---
title: "blk_start_queue(9)"
name: "blk_start_queue"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_start_queue/"
description: "blk_start_queue – restart a previously stopped queue"
---

<p>blk_start_queue &#8211; restart a previously stopped queue</p>
<h2>Synopsis</h2>
<pre><code>void blk_start_queue(struct request_queue *q);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>The struct request_queue in question</dl>
<h2>Description</h2>
<p><code>blk_start_queue</code> will clear the stop flag on the queue, and call the request_fn for the queue if it was in a stopped state when entered. Also see <code>blk_stop_queue</code>. Queue lock must be held.</p>
<h2>Copyright</h2>
