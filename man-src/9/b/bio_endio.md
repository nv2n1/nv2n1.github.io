---
title: "bio_endio(9)"
name: "bio_endio"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bio_endio/"
description: "bio_endio – end I/O on a bio"
---

<p>bio_endio &#8211; end I/O on a bio</p>
<h2>Synopsis</h2>
<pre><code>void bio_endio(struct bio *bio);</code></pre>
<h2>Arguments</h2>
<p><i>bio</i></p>
<dl>
<dd>
<dd>bio</dl>
<h2>Description</h2>
<p><code>bio_endio</code> will end I/O on the whole bio. <code>bio_endio</code> is the preferred way to end I/O on a bio. No one should call <code>bi_end_io</code> directly on a bio unless they own it and thus know that it has an end_io function.</p>
<h2>Copyright</h2>
