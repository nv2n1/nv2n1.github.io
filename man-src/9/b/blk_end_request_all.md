---
title: "blk_end_request_all(9)"
name: "blk_end_request_all"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_end_request_all/"
description: "blk_end_request_all – Helper function for drives to finish the request."
---

<p>blk_end_request_all &#8211; Helper function for drives to finish the request.</p>
<h2>Synopsis</h2>
<pre><code>void blk_end_request_all(struct request *rq, int error);</code></pre>
<h2>Arguments</h2>
<p><i>rq</i></p>
<dl>
<dd>
<dd>the request to finish</dl>
<p> <i>error</i></p>
<dl>
<dd><code>0</code> for success, &lt; <code>0</code> for error</dl>
<h2>Description</h2>
<p>Completely finish <i>rq</i>.</p>
<h2>Copyright</h2>
