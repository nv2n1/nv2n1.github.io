---
title: "bio_put(9)"
name: "bio_put"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bio_put/"
---

bio_put - release a reference to a bio

<h2>Synopsis</h2>

<pre><code>void bio_put(struct bio *bio);</code></pre>

<h2>Arguments</h2>

<i>bio</i>
<dl><dd><dd>bio to release reference to</dl>

<h2>Description</h2>

Put a reference to a struct bio, either one you have gotten with bio_alloc, bio_get or bio_clone. The last put of a bio will free it.

<h2>Copyright</h2>


