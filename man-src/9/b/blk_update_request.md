---
title: "blk_update_request(9)"
name: "blk_update_request"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_update_request/"
description: "blk_update_request – Special helper function for request stacking drivers"
---

<p>blk_update_request &#8211; Special helper function for request stacking drivers</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool blk_update_request(struct request&nbsp;<wbr>*&nbsp;<wbr></code><i>req</i><code>, int&nbsp;<wbr></code><i>error</i><code>, unsigned int&nbsp;<wbr></code><i>nr_bytes</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>the request being processed</dl>
<p> <i>error</i></p>
<dl>
<dd><code>0</code> for success, &lt; <code>0</code> for error</dl>
<p> <i>nr_bytes</i></p>
<dl>
<dd>number of bytes to complete <i>req</i></dl>
<h2>Description</h2>
<p>Ends I/O on a number of bytes attached to <i>req</i>, but doesn&#8217;t complete the request structure even if <i>req</i> doesn&#8217;t have leftover. If <i>req</i> has leftover, sets it up for the next range of segments. </p>
<p> This special helper function is only for request stacking drivers (e.g. request-based dm) so that they can handle partial completion. Actual device drivers should use blk_end_request instead. </p>
<p> Passing the result of <code>blk_rq_bytes</code> as <i>nr_bytes</i> guarantees <code>false</code> return from this function.</p>
<h2>Return</h2>
<p><code>false</code> &#8211; this request doesn&#8217;t have any more data <code>true</code> &#8211; this request has more data</p>
<h2>Copyright</h2>
