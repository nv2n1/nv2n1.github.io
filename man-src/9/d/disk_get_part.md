---
title: "disk_get_part(9)"
name: "disk_get_part"
section: "9"
letter: "d"
url: "/docs/linux/man/9-disk_get_part/"
---

disk_get_part - get partition

<h2>Synopsis</h2>

<pre><code>struct hd_struct *disk_get_part(struct gendisk *disk, int partno);</code></pre>

<h2>Arguments</h2>

<i>disk</i>
<dl><dd><dd>disk to look partition from</dl>
 

 <i>partno</i>
<dl><dd>partition number</dl>

<h2>Description</h2>

Look for partition <i>partno</i> from <i>disk</i>. If found, increment reference count and return it.

<h2>Context</h2>

Don't care.

<h2>Return</h2>

Pointer to the found partition on success, NULL if not found.

<h2>Copyright</h2>


