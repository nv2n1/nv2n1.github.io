---
title: "bio_trim(9)"
name: "bio_trim"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bio_trim/"
---

bio_trim - trim a bio

<h2>Synopsis</h2>

<pre><code>void bio_trim(struct bio *bio, int offset, int size);</code></pre>

<h2>Arguments</h2>

<i>bio</i>
<dl><dd><dd>bio to trim</dl>
 

 <i>offset</i>
<dl><dd>number of sectors to trim from the front of <i>bio</i></dl>
 

 <i>size</i>
<dl><dd>size we want to trim <i>bio</i> to, in sectors</dl>

<h2>Copyright</h2>


