---
title: "trace_block_bio_bounce(9)"
name: "trace_block_bio_bounce"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_block_bio_bounce/"
description: "trace_block_bio_bounce – used bounce buffer when processing block operation"
---

<p>trace_block_bio_bounce &#8211; used bounce buffer when processing block operation</p>
<h2>Synopsis</h2>
<pre><code>void trace_block_bio_bounce(struct request_queue *q, struct bio *bio);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>queue holding the block operation</dl>
<p> <i>bio</i></p>
<dl>
<dd>block operation</dl>
<h2>Description</h2>
<p>A bounce buffer was used to handle the block operation <i>bio</i> in <i>q</i>. This occurs when hardware limitations prevent a direct transfer of data between the <i>bio</i> data memory area and the IO device. Use of a bounce buffer requires extra copying of data and decreases performance.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
