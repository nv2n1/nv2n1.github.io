---
title: "bio_advance(9)"
name: "bio_advance"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bio_advance/"
---

bio_advance - increment/complete a bio by some number of bytes

<h2>Synopsis</h2>

<pre><code>void bio_advance(struct bio *bio, unsigned bytes);</code></pre>

<h2>Arguments</h2>

<i>bio</i>
<dl><dd><dd>bio to advance</dl>
 

 <i>bytes</i>
<dl><dd>number of bytes to complete</dl>

<h2>Description</h2>

This updates bi_sector, bi_size and bi_idx; if the number of bytes to complete doesn't align with a bvec boundary, then bv_len and bv_offset will be updated on the last bvec as well. 

 <i>bio</i> will then represent the remaining, uncompleted portion of the io.

<h2>Copyright</h2>


