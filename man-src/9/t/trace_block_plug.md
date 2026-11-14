---
title: "trace_block_plug(9)"
name: "trace_block_plug"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_block_plug/"
description: "trace_block_plug – keep operations requests in request queue"
---

<p>trace_block_plug &#8211; keep operations requests in request queue</p>
<h2>Synopsis</h2>
<pre><code>void trace_block_plug(struct request_queue *q);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>request queue to plug</dl>
<h2>Description</h2>
<p>Plug the request queue <i>q</i>. Do not allow block operation requests to be sent to the device driver. Instead, accumulate requests in the queue to improve throughput performance of the block device.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
