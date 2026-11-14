---
title: "blk_end_request_err(9)"
name: "blk_end_request_err"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_end_request_err/"
description: "blk_end_request_err – Finish a request till the next failure boundary."
---

<p>blk_end_request_err &#8211; Finish a request till the next failure boundary.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool blk_end_request_err(struct request&nbsp;<wbr>*&nbsp;<wbr></code><i>rq</i><code>, int&nbsp;<wbr></code><i>error</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>rq</i></p>
<dl>
<dd>
<dd>the request to finish till the next failure boundary for</dl>
<p> <i>error</i></p>
<dl>
<dd>must be negative errno</dl>
<h2>Description</h2>
<p>Complete <i>rq</i> till the next failure boundary.</p>
<h2>Return</h2>
<p><code>false</code> &#8211; we are done with this request <code>true</code> &#8211; still buffers pending for this request</p>
<h2>Copyright</h2>
