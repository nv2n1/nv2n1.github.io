---
title: "blk_queue_bypass_start(9)"
name: "blk_queue_bypass_start"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_bypass_start/"
description: "blk_queue_bypass_start – enter queue bypass mode"
---

<p>blk_queue_bypass_start &#8211; enter queue bypass mode</p>
<h2>Synopsis</h2>
<pre><code>void blk_queue_bypass_start(struct request_queue *q);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>queue of interest</dl>
<h2>Description</h2>
<p>In bypass mode, only the dispatch FIFO queue of <i>q</i> is used. This function makes <i>q</i> enter bypass mode and drains all requests which were throttled or issued before. On return, it&#8217;s guaranteed that no request is being throttled or has ELVPRIV set and <code>blk_queue_bypass</code><code>true</code> inside queue or RCU read lock.</p>
<h2>Copyright</h2>
