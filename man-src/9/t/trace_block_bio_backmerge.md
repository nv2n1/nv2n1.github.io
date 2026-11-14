---
title: "trace_block_bio_backmerge(9)"
name: "trace_block_bio_backmerge"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_block_bio_backmerge/"
description: "trace_block_bio_backmerge – merging block operation to the end of an existing operation"
---

<p>trace_block_bio_backmerge &#8211; merging block operation to the end of an existing operation</p>
<h2>Synopsis</h2>
<pre><code>void trace_block_bio_backmerge(struct request_queue *q, struct request *rq, struct bio *bio);</code></pre>
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
<p>Merging block request <i>bio</i> to the end of an existing block request in queue <i>q</i>.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
