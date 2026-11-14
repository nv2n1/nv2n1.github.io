---
title: "trace_block_rq_requeue(9)"
name: "trace_block_rq_requeue"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_block_rq_requeue/"
description: "trace_block_rq_requeue – place block IO request back on a queue"
---

<p>trace_block_rq_requeue &#8211; place block IO request back on a queue</p>
<h2>Synopsis</h2>
<pre><code>void trace_block_rq_requeue(struct request_queue *q, struct request *rq);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>queue holding operation</dl>
<p> <i>rq</i></p>
<dl>
<dd>block IO operation request</dl>
<h2>Description</h2>
<p>The block operation request <i>rq</i> is being placed back into queue <i>q</i>. For some reason the request was not completed and needs to be put back in the queue.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
