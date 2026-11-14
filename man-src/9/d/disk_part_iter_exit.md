---
title: "disk_part_iter_exit(9)"
name: "disk_part_iter_exit"
section: "9"
letter: "d"
url: "/docs/linux/man/9-disk_part_iter_exit/"
---

disk_part_iter_exit - finish up partition iteration

<h2>Synopsis</h2>

<pre><code>void disk_part_iter_exit(struct disk_part_iter *piter);</code></pre>

<h2>Arguments</h2>

<i>piter</i>
<dl><dd><dd>iter of interest</dl>

<h2>Description</h2>

Called when iteration is over. Cleans up <i>piter</i>.

<h2>Context</h2>

Don't care.

<h2>Copyright</h2>


