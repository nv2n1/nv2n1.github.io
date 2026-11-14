---
title: "trace_block_bio_remap(9)"
name: "trace_block_bio_remap"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_block_bio_remap/"
description: "trace_block_bio_remap – map request for a logical device to the raw device"
---

<p>trace_block_bio_remap &#8211; map request for a logical device to the raw device</p>
<h2>Synopsis</h2>
<pre><code>void trace_block_bio_remap(struct request_queue *q, struct bio *bio, dev_t dev, sector_t from);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>queue holding the operation</dl>
<p> <i>bio</i></p>
<dl>
<dd>revised operation</dl>
<p> <i>dev</i></p>
<dl>
<dd>device for the operation</dl>
<p> <i>from</i></p>
<dl>
<dd>original sector for the operation</dl>
<h2>Description</h2>
<p>An operation for a logical device has been mapped to the raw block device.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
