---
title: "trace_block_bio_frontmerge(9)"
name: "trace_block_bio_frontmerge"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_block_bio_frontmerge/"
description: "trace_block_bio_frontmerge – merging block operation to the beginning of an existing operation"
---

<p>trace_block_bio_frontmerge &#8211; merging block operation to the beginning of an existing operation</p>
<h2>Synopsis</h2>
<pre><code>void trace_block_bio_frontmerge(struct request_queue *q, struct request *rq, struct bio *bio);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>queue holding operation</dl>
<p> <i>rq</i></p>
<dl>
<dd>request bio is being merged into</dl>
<p> <i>bio</i></p>
<dl>
<dd>new block operation to merge</dl>
<h2>Description</h2>
<p>Merging block IO operation <i>bio</i> to the beginning of an existing block operation in queue <i>q</i>.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
