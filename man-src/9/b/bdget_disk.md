---
title: "bdget_disk(9)"
name: "bdget_disk"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bdget_disk/"
description: "bdget_disk – do bdget by gendisk and partition number"
---

<p>bdget_disk &#8211; do <code>bdget</code> by gendisk and partition number</p>
<h2>Synopsis</h2>
<pre><code>struct block_device *bdget_disk(struct gendisk *disk, int partno);</code></pre>
<h2>Arguments</h2>
<p><i>disk</i></p>
<dl>
<dd>
<dd>gendisk of interest</dl>
<p> <i>partno</i></p>
<dl>
<dd>partition number</dl>
<h2>Description</h2>
<p>Find partition <i>partno</i> from <i>disk</i>, do <code>bdget</code> on it.</p>
<h2>Context</h2>
<p>Don&#8217;t care.</p>
<h2>Return</h2>
<p>Resulting block_device on success, NULL on failure.</p>
<h2>Copyright</h2>
