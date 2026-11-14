---
title: "trace_block_rq_abort(9)"
name: "trace_block_rq_abort"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_block_rq_abort/"
description: "trace_block_rq_abort – abort block operation request"
---

<p>trace_block_rq_abort &#8211; abort block operation request</p>
<h2>Synopsis</h2>
<pre><code>void trace_block_rq_abort(struct request_queue *q, struct request *rq);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>queue containing the block operation request</dl>
<p> <i>rq</i></p>
<dl>
<dd>block IO operation request</dl>
<h2>Description</h2>
<p>Called immediately after pending block IO operation request <i>rq</i> in queue <i>q</i> is aborted. The fields in the operation request <i>rq</i> can be examined to determine which device and sectors the pending operation would access.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
