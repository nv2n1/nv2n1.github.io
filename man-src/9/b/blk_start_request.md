---
title: "blk_start_request(9)"
name: "blk_start_request"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_start_request/"
description: "blk_start_request – start request processing on the driver"
---

<p>blk_start_request &#8211; start request processing on the driver</p>
<h2>Synopsis</h2>
<pre><code>void blk_start_request(struct request *req);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>request to dequeue</dl>
<h2>Description</h2>
<p>Dequeue <i>req</i> and start timeout timer on it. This hands off the request to the driver. </p>
<p> Block internal functions which don&#8217;t want to start timer should call <code>blk_dequeue_request</code>.</p>
<h2>Context</h2>
<p>queue_lock must be held.</p>
<h2>Copyright</h2>
