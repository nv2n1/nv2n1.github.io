---
title: "trace_block_rq_complete(9)"
name: "trace_block_rq_complete"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_block_rq_complete/"
description: "trace_block_rq_complete – block IO operation completed by device driver"
---

<p>trace_block_rq_complete &#8211; block IO operation completed by device driver</p>
<h2>Synopsis</h2>
<pre><code>void trace_block_rq_complete(struct request_queue *q, struct request *rq, unsigned int nr_bytes);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>queue containing the block operation request</dl>
<p> <i>rq</i></p>
<dl>
<dd>block operations request</dl>
<p> <i>nr_bytes</i></p>
<dl>
<dd>number of completed bytes</dl>
<h2>Description</h2>
<p>The block_rq_complete tracepoint event indicates that some portion of operation request has been completed by the device driver. If the <i>rq</i>-&gt;bio is <code>NULL</code>, then there is absolutely no additional work to do for the request. If <i>rq</i>-&gt;bio is non-NULL then there is additional work required to complete the request.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
