---
title: "blk_end_request(9)"
name: "blk_end_request"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_end_request/"
description: "blk_end_request – Helper function for drivers to complete the request."
---

<p>blk_end_request &#8211; Helper function for drivers to complete the request.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool blk_end_request(struct request&nbsp;<wbr>*&nbsp;<wbr></code><i>rq</i><code>, int&nbsp;<wbr></code><i>error</i><code>, unsigned int&nbsp;<wbr></code><i>nr_bytes</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>rq</i></p>
<dl>
<dd>
<dd>the request being processed</dl>
<p> <i>error</i></p>
<dl>
<dd><code>0</code> for success, &lt; <code>0</code> for error</dl>
<p> <i>nr_bytes</i></p>
<dl>
<dd>number of bytes to complete</dl>
<h2>Description</h2>
<p>Ends I/O on a number of bytes attached to <i>rq</i>. If <i>rq</i> has leftover, sets it up for the next range of segments.</p>
<h2>Return</h2>
<p><code>false</code> &#8211; we are done with this request <code>true</code> &#8211; still buffers pending for this request</p>
<h2>Copyright</h2>
