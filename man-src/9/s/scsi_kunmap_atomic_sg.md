---
title: "scsi_kunmap_atomic_sg(9)"
name: "scsi_kunmap_atomic_sg"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_kunmap_atomic_sg/"
description: "scsi_kunmap_atomic_sg – atomically unmap a virtual address, previously mapped with scsi_kmap_atomic_sg"
---

<p>scsi_kunmap_atomic_sg &#8211; atomically unmap a virtual address, previously mapped with scsi_kmap_atomic_sg</p>
<h2>Synopsis</h2>
<pre><code>void scsi_kunmap_atomic_sg(void *virt);</code></pre>
<h2>Arguments</h2>
<p><i>virt</i></p>
<dl>
<dd>
<dd>virtual address to be unmapped</dl>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
