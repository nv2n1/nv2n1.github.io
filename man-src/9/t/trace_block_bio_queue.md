---
title: "trace_block_bio_queue(9)"
name: "trace_block_bio_queue"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_block_bio_queue/"
description: "trace_block_bio_queue – putting new block IO operation in queue"
---

<p>trace_block_bio_queue &#8211; putting new block IO operation in queue</p>
<h2>Synopsis</h2>
<pre><code>void trace_block_bio_queue(struct request_queue *q, struct bio *bio);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>queue holding operation</dl>
<p> <i>bio</i></p>
<dl>
<dd>new block operation</dl>
<h2>Description</h2>
<p>About to place the block IO operation <i>bio</i> into queue <i>q</i>.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
