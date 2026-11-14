---
title: "bioset_create(9)"
name: "bioset_create"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bioset_create/"
---

bioset_create - Create a bio_set

<h2>Synopsis</h2>

<pre><code>struct bio_set *bioset_create(unsigned int pool_size, unsigned int front_pad);</code></pre>

<h2>Arguments</h2>

<i>pool_size</i>
<dl><dd><dd>Number of bio and bio_vecs to cache in the mempool</dl>
 

 <i>front_pad</i>
<dl><dd>Number of bytes to allocate in front of the returned bio</dl>

<h2>Description</h2>

Set up a bio_set to be used with <i>bio_alloc_bioset</i>. Allows the caller to ask for a number of bytes to be allocated in front of the bio. Front pad allocation is useful for embedding the bio inside another structure, to avoid allocating extra data to go with the bio. Note that the bio must be embedded at the END of that structure always, or things will break badly.

<h2>Copyright</h2>


