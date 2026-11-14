---
title: "trace_block_rq_insert(9)"
name: "trace_block_rq_insert"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_block_rq_insert/"
description: "trace_block_rq_insert – insert block operation request into queue"
---

<p>trace_block_rq_insert &#8211; insert block operation request into queue</p>
<h2>Synopsis</h2>
<pre><code>void trace_block_rq_insert(struct request_queue *q, struct request *rq);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>target queue</dl>
<p> <i>rq</i></p>
<dl>
<dd>block IO operation request</dl>
<h2>Description</h2>
<p>Called immediately before block operation request <i>rq</i> is inserted into queue <i>q</i>. The fields in the operation request <i>rq</i> struct can be examined to determine which device and sectors the pending operation would access.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
