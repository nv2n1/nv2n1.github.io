---
title: "trace_block_bio_complete(9)"
name: "trace_block_bio_complete"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_block_bio_complete/"
description: "trace_block_bio_complete – completed all work on the block operation"
---

<p>trace_block_bio_complete &#8211; completed all work on the block operation</p>
<h2>Synopsis</h2>
<pre><code>void trace_block_bio_complete(struct request_queue *q, struct bio *bio, int error);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>queue holding the block operation</dl>
<p> <i>bio</i></p>
<dl>
<dd>block operation completed</dl>
<p> <i>error</i></p>
<dl>
<dd>io error value</dl>
<h2>Description</h2>
<p>This tracepoint indicates there is no further work to do on this block IO operation <i>bio</i>.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
