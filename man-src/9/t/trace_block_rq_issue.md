---
title: "trace_block_rq_issue(9)"
name: "trace_block_rq_issue"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_block_rq_issue/"
description: "trace_block_rq_issue – issue pending block IO request operation to device driver"
---

<p>trace_block_rq_issue &#8211; issue pending block IO request operation to device driver</p>
<h2>Synopsis</h2>
<pre><code>void trace_block_rq_issue(struct request_queue *q, struct request *rq);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>queue holding operation</dl>
<p> <i>rq</i></p>
<dl>
<dd>block IO operation operation request</dl>
<h2>Description</h2>
<p>Called when block operation request <i>rq</i> from queue <i>q</i> is sent to a device driver for processing.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
