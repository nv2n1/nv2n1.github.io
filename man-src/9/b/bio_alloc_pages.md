---
title: "bio_alloc_pages(9)"
name: "bio_alloc_pages"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bio_alloc_pages/"
---

bio_alloc_pages - allocates a single page for each bvec in a bio

<h2>Synopsis</h2>

<pre><code>int bio_alloc_pages(struct bio *bio, gfp_t gfp_mask);</code></pre>

<h2>Arguments</h2>

<i>bio</i>
<dl><dd><dd>bio to allocate pages for</dl>
 

 <i>gfp_mask</i>
<dl><dd>flags for allocation</dl>

<h2>Description</h2>

Allocates pages up to <i>bio</i>-&gt;bi_vcnt. 

 Returns 0 on success, -ENOMEM on failure. On failure, any allocated pages are freed.

<h2>Copyright</h2>


