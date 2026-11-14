---
title: "trace_block_rq_remap(9)"
name: "trace_block_rq_remap"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_block_rq_remap/"
description: "trace_block_rq_remap – map request for a block operation request"
---

<p>trace_block_rq_remap &#8211; map request for a block operation request</p>
<h2>Synopsis</h2>
<pre><code>void trace_block_rq_remap(struct request_queue *q, struct request *rq, dev_t dev, sector_t from);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>queue holding the operation</dl>
<p> <i>rq</i></p>
<dl>
<dd>block IO operation request</dl>
<p> <i>dev</i></p>
<dl>
<dd>device for the operation</dl>
<p> <i>from</i></p>
<dl>
<dd>original sector for the operation</dl>
<h2>Description</h2>
<p>The block operation request <i>rq</i> in <i>q</i> has been remapped. The block operation request <i>rq</i> holds the current information and <i>from</i> hold the original sector.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
