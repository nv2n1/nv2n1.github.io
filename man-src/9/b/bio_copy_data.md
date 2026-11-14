---
title: "bio_copy_data(9)"
name: "bio_copy_data"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bio_copy_data/"
---

bio_copy_data - copy contents of data buffers from one chain of bios to another

<h2>Synopsis</h2>

<pre><code>void bio_copy_data(struct bio *dst, struct bio *src);</code></pre>

<h2>Arguments</h2>

<i>dst</i>
<dl><dd><dd>destination bio list</dl>
 

 <i>src</i>
<dl><dd>source bio list</dl>

<h2>Description</h2>

If <i>src</i> and <i>dst</i> are single bios, bi_next must be NULL - otherwise, treats <i>src</i> and <i>dst</i> as linked lists of bios. 

 Stops when it reaches the end of either <i>src</i> or <i>dst</i> - that is, copies min(src-&gt;bi_size, dst-&gt;bi_size) bytes (or the equivalent for lists of bios).

<h2>Copyright</h2>


