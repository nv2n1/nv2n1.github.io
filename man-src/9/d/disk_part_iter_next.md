---
title: "disk_part_iter_next(9)"
name: "disk_part_iter_next"
section: "9"
letter: "d"
url: "/docs/linux/man/9-disk_part_iter_next/"
---

disk_part_iter_next - proceed iterator to the next partition and return it

<h2>Synopsis</h2>

<pre><code>struct hd_struct *disk_part_iter_next(struct disk_part_iter *piter);</code></pre>

<h2>Arguments</h2>

<i>piter</i>
<dl><dd><dd>iterator of interest</dl>

<h2>Description</h2>

Proceed <i>piter</i> to the next partition and return it.

<h2>Context</h2>

Don't care.

<h2>Copyright</h2>


