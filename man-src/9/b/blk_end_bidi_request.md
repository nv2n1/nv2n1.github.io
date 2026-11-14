---
title: "blk_end_bidi_request(9)"
name: "blk_end_bidi_request"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_end_bidi_request/"
description: "blk_end_bidi_request – Complete a bidi request"
---

<p>blk_end_bidi_request &#8211; Complete a bidi request</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool blk_end_bidi_request(struct request&nbsp;<wbr>*&nbsp;<wbr></code><i>rq</i><code>, int&nbsp;<wbr></code><i>error</i><code>, unsigned int&nbsp;<wbr></code><i>nr_bytes</i><code>, unsigned int&nbsp;<wbr></code><i>bidi_bytes</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>rq</i></p>
<dl>
<dd>
<dd>the request to complete</dl>
<p> <i>error</i></p>
<dl>
<dd><code>0</code> for success, &lt; <code>0</code> for error</dl>
<p> <i>nr_bytes</i></p>
<dl>
<dd>number of bytes to complete <i>rq</i></dl>
<p> <i>bidi_bytes</i></p>
<dl>
<dd>number of bytes to complete <i>rq</i>-&gt;next_rq</dl>
<h2>Description</h2>
<p>Ends I/O on a number of bytes attached to <i>rq</i> and <i>rq</i>-&gt;next_rq. Drivers that supports bidi can safely call this member for any type of request, bidi or uni. In the later case <i>bidi_bytes</i> is just ignored.</p>
<h2>Return</h2>
<p><code>false</code> &#8211; we are done with this request <code>true</code> &#8211; still buffers pending for this request</p>
<h2>Copyright</h2>
