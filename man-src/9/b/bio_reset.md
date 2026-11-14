---
title: "bio_reset(9)"
name: "bio_reset"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bio_reset/"
description: "bio_reset – reinitialize a bio"
---

<p>bio_reset &#8211; reinitialize a bio</p>
<h2>Synopsis</h2>
<pre><code>void bio_reset(struct bio *bio);</code></pre>
<h2>Arguments</h2>
<p><i>bio</i></p>
<dl>
<dd>
<dd>bio to reset</dl>
<h2>Description</h2>
<p>After calling <code>bio_reset</code>, <i>bio</i> will be in the same state as a freshly allocated bio returned bio <code>bio_alloc_bioset</code> &#8211; the only fields that are preserved are the ones that are initialized by <code>bio_alloc_bioset</code>. See comment in struct bio.</p>
<h2>Copyright</h2>
