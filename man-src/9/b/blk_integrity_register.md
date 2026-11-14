---
title: "blk_integrity_register(9)"
name: "blk_integrity_register"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_integrity_register/"
---

blk_integrity_register - Register a gendisk as being integrity-capable

<h2>Synopsis</h2>

<pre><code>void blk_integrity_register(struct gendisk *disk, struct blk_integrity *template);</code></pre>

<h2>Arguments</h2>

<i>disk</i>
<dl><dd><dd>struct gendisk pointer to make integrity-aware</dl>
 

 <i>template</i>
<dl><dd>block integrity profile to register</dl>

<h2>Description</h2>

When a device needs to advertise itself as being able to send/receive integrity metadata it must use this function to register the capability with the block layer. The template is a blk_integrity struct with values appropriate for the underlying hardware. See Documentation/block/data-integrity.txt.

<h2>Copyright</h2>


