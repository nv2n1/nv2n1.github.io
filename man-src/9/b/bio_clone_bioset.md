---
title: "bio_clone_bioset(9)"
name: "bio_clone_bioset"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bio_clone_bioset/"
---

bio_clone_bioset - clone a bio

<h2>Synopsis</h2>

<pre><code>struct bio *bio_clone_bioset(struct bio *bio_src, gfp_t gfp_mask, struct bio_set *bs);</code></pre>

<h2>Arguments</h2>

<i>bio_src</i>
<dl><dd><dd>bio to clone</dl>
 

 <i>gfp_mask</i>
<dl><dd>allocation priority</dl>
 

 <i>bs</i>
<dl><dd>bio_set to allocate from</dl>

<h2>Description</h2>

Clone bio. Caller will own the returned bio, but not the actual data it points to. Reference count of returned bio will be one.

<h2>Copyright</h2>


