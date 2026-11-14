---
title: "revalidate_disk(9)"
name: "revalidate_disk"
section: "9"
letter: "r"
url: "/docs/linux/man/9-revalidate_disk/"
---

revalidate_disk - wrapper for lower-level driver's revalidate_disk call-back

<h2>Synopsis</h2>

<pre><code>int revalidate_disk(struct gendisk *disk);</code></pre>

<h2>Arguments</h2>

<i>disk</i>
<dl><dd><dd>struct gendisk to be revalidated</dl>

<h2>Description</h2>

This routine is a wrapper for lower-level driver's revalidate_disk call-backs. It is used to do common pre and post operations needed for all revalidate_disk operations.

<h2>Copyright</h2>


