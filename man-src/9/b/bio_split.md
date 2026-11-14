---
title: "bio_split(9)"
name: "bio_split"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bio_split/"
---

bio_split - split a bio

<h2>Synopsis</h2>

<pre><code>struct bio *bio_split(struct bio *bio, int sectors, gfp_t gfp, struct bio_set *bs);</code></pre>

<h2>Arguments</h2>

<i>bio</i>
<dl><dd><dd>bio to split</dl>
 

 <i>sectors</i>
<dl><dd>number of sectors to split from the front of <i>bio</i></dl>
 

 <i>gfp</i>
<dl><dd>gfp mask</dl>
 

 <i>bs</i>
<dl><dd>bio set to allocate from</dl>

<h2>Description</h2>

Allocates and returns a new bio which represents <i>sectors</i> from the start of <i>bio</i>, and updates <i>bio</i> to represent the remaining sectors. 

 Unless this is a discard request the newly allocated bio will point to <i>bio</i>'s bi_io_vec; it is the caller's responsibility to ensure that <i>bio</i> is not freed before the split.

<h2>Copyright</h2>


