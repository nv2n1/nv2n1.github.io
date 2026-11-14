---
title: "blk_rq_map_integrity_sg(9)"
name: "blk_rq_map_integrity_sg"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_rq_map_integrity_sg/"
description: "blk_rq_map_integrity_sg – Map integrity metadata into a scatterlist"
---

<p>blk_rq_map_integrity_sg &#8211; Map integrity metadata into a scatterlist</p>
<h2>Synopsis</h2>
<pre><code>int blk_rq_map_integrity_sg(struct request_queue *q, struct bio *bio, struct scatterlist *sglist);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>request queue</dl>
<p> <i>bio</i></p>
<dl>
<dd>bio with integrity metadata attached</dl>
<p> <i>sglist</i></p>
<dl>
<dd>target scatterlist</dl>
<h2>Description</h2>
<p>Map the integrity vectors in request into a scatterlist. The scatterlist must be big enough to hold all elements. I.e. sized using <code>blk_rq_count_integrity_sg</code>.</p>
<h2>Copyright</h2>
