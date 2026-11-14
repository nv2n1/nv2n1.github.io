---
title: "blk_add_trace_bio_remap(9)"
name: "blk_add_trace_bio_remap"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_add_trace_bio_remap/"
---

blk_add_trace_bio_remap - Add a trace for a bio-remap operation

<h2>Synopsis</h2>

<pre><code>void blk_add_trace_bio_remap(void *ignore, struct request_queue *q, struct bio *bio, dev_t dev, sector_t from);</code></pre>

<h2>Arguments</h2>

<i>ignore</i>
<dl><dd><dd>trace callback data parameter (not used)</dl>
 

 <i>q</i>
<dl><dd>queue the io is for</dl>
 

 <i>bio</i>
<dl><dd>the source bio</dl>
 

 <i>dev</i>
<dl><dd>target device</dl>
 

 <i>from</i>
<dl><dd>source sector</dl>

<h2>Description</h2>

Device mapper or raid target sometimes need to split a bio because it spans a stripe (or similar). Add a trace for that action.

<h2>Copyright</h2>


