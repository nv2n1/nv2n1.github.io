---
title: "bio_clone_fast(9)"
name: "bio_clone_fast"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bio_clone_fast/"
---

bio_clone_fast - clone a bio that shares the original bio's biovec

<h2>Synopsis</h2>

<pre><code>struct bio *bio_clone_fast(struct bio *bio, gfp_t gfp_mask, struct bio_set *bs);</code></pre>

<h2>Arguments</h2>

<i>bio</i>
<dl><dd><dd>bio to clone</dl>
 

 <i>gfp_mask</i>
<dl><dd>allocation priority</dl>
 

 <i>bs</i>
<dl><dd>bio_set to allocate from</dl>

<h2>Description</h2>

Like __bio_clone_fast, only also allocates the returned bio

<h2>Copyright</h2>


