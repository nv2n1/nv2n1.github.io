---
title: "scsi_kmap_atomic_sg(9)"
name: "scsi_kmap_atomic_sg"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_kmap_atomic_sg/"
description: "scsi_kmap_atomic_sg – find and atomically map an sg-elemnt"
---

<p>scsi_kmap_atomic_sg &#8211; find and atomically map an sg-elemnt</p>
<h2>Synopsis</h2>
<pre><code>void *scsi_kmap_atomic_sg(struct scatterlist *sgl, int sg_count, size_t *offset, size_t *len);</code></pre>
<h2>Arguments</h2>
<p><i>sgl</i></p>
<dl>
<dd>
<dd>scatter-gather list</dl>
<p> <i>sg_count</i></p>
<dl>
<dd>number of segments in sg</dl>
<p> <i>offset</i></p>
<dl>
<dd>offset in bytes into sg, on return offset into the mapped area</dl>
<p> <i>len</i></p>
<dl>
<dd>bytes to map, on return number of bytes mapped</dl>
<h2>Description</h2>
<p>Returns virtual address of the start of the mapped page</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
