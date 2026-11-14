---
title: "bio_chain(9)"
name: "bio_chain"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bio_chain/"
---

bio_chain - chain bio completions

<h2>Synopsis</h2>

<pre><code>void bio_chain(struct bio *bio, struct bio *parent);</code></pre>

<h2>Arguments</h2>

<i>bio</i>
<dl><dd><dd>the target bio</dl>
 

 <i>parent</i>
<dl><dd>the <i>bio</i>'s parent bio</dl>

<h2>Description</h2>

The caller won't have a bi_end_io called when <i>bio</i> completes - instead, <i>parent</i>'s bi_end_io won't be called until both <i>parent</i> and <i>bio</i> have completed; the chained bio will also be freed when it completes. 

 The caller must not set bi_private or bi_end_io in <i>bio</i>.

<h2>Copyright</h2>


