---
title: "bio_map_kern(9)"
name: "bio_map_kern"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bio_map_kern/"
---

bio_map_kern - map kernel address into bio

<h2>Synopsis</h2>

<pre><code>struct bio *bio_map_kern(struct request_queue *q, void *data, unsigned int len, gfp_t gfp_mask);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the struct request_queue for the bio</dl>
 

 <i>data</i>
<dl><dd>pointer to buffer to map</dl>
 

 <i>len</i>
<dl><dd>length in bytes</dl>
 

 <i>gfp_mask</i>
<dl><dd>allocation flags for bio allocation</dl>

<h2>Description</h2>

Map the kernel address into a bio suitable for io to a block device. Returns an error pointer in case of error.

<h2>Copyright</h2>


