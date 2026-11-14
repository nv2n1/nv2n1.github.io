---
title: "bio_add_page(9)"
name: "bio_add_page"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bio_add_page/"
---

bio_add_page - attempt to add page to bio

<h2>Synopsis</h2>

<pre><code>int bio_add_page(struct bio *bio, struct page *page, unsigned int len, unsigned int offset);</code></pre>

<h2>Arguments</h2>

<i>bio</i>
<dl><dd><dd>destination bio</dl>
 

 <i>page</i>
<dl><dd>page to add</dl>
 

 <i>len</i>
<dl><dd>vec entry length</dl>
 

 <i>offset</i>
<dl><dd>vec entry offset</dl>

<h2>Description</h2>

Attempt to add a page to the bio_vec maplist. This will only fail if either bio-&gt;bi_vcnt == bio-&gt;bi_max_vecs or it's a cloned bio.

<h2>Copyright</h2>


