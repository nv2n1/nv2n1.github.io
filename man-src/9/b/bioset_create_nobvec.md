---
title: "bioset_create_nobvec(9)"
name: "bioset_create_nobvec"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bioset_create_nobvec/"
description: "bioset_create_nobvec – Create a bio_set without bio_vec mempool"
---

<p>bioset_create_nobvec &#8211; Create a bio_set without bio_vec mempool</p>
<h2>Synopsis</h2>
<pre><code>struct bio_set *bioset_create_nobvec(unsigned int pool_size, unsigned int front_pad);</code></pre>
<h2>Arguments</h2>
<p><i>pool_size</i></p>
<dl>
<dd>
<dd>Number of bio to cache in the mempool</dl>
<p> <i>front_pad</i></p>
<dl>
<dd>Number of bytes to allocate in front of the returned bio</dl>
<h2>Description</h2>
<p>Same functionality as <code>bioset_create</code> except that mempool is not created for bio_vecs. Saving some memory for <code>bio_clone_fast</code> users.</p>
<h2>Copyright</h2>
