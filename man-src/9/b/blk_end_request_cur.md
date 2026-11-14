---
title: "blk_end_request_cur(9)"
name: "blk_end_request_cur"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_end_request_cur/"
description: "blk_end_request_cur – Helper function to finish the current request chunk."
---

<p>blk_end_request_cur &#8211; Helper function to finish the current request chunk.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool blk_end_request_cur(struct request&nbsp;<wbr>*&nbsp;<wbr></code><i>rq</i><code>, int&nbsp;<wbr></code><i>error</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>rq</i></p>
<dl>
<dd>
<dd>the request to finish the current chunk for</dl>
<p> <i>error</i></p>
<dl>
<dd><code>0</code> for success, &lt; <code>0</code> for error</dl>
<h2>Description</h2>
<p>Complete the current consecutively mapped chunk from <i>rq</i>.</p>
<h2>Return</h2>
<p><code>false</code> &#8211; we are done with this request <code>true</code> &#8211; still buffers pending for this request</p>
<h2>Copyright</h2>
