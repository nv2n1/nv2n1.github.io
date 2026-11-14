---
title: "blk_rq_count_integrity_sg(9)"
name: "blk_rq_count_integrity_sg"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_rq_count_integrity_sg/"
---

blk_rq_count_integrity_sg - Count number of integrity scatterlist elements

<h2>Synopsis</h2>

<pre><code>int blk_rq_count_integrity_sg(struct request_queue *q, struct bio *bio);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>request queue</dl>
 

 <i>bio</i>
<dl><dd>bio with integrity metadata attached</dl>

<h2>Description</h2>

Returns the number of elements required in a scatterlist corresponding to the integrity metadata in a bio.

<h2>Copyright</h2>


