---
title: "scsi_dma_map(9)"
name: "scsi_dma_map"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_dma_map/"
description: "scsi_dma_map – perform DMA mapping against command’s sg lists"
---

<p>scsi_dma_map &#8211; perform DMA mapping against command&#8217;s sg lists</p>
<h2>Synopsis</h2>
<pre><code>int scsi_dma_map(struct scsi_cmnd *cmd);</code></pre>
<h2>Arguments</h2>
<p><i>cmd</i></p>
<dl>
<dd>
<dd>scsi command</dl>
<h2>Description</h2>
<p>Returns the number of sg lists actually used, zero if the sg lists is NULL, or -ENOMEM if the mapping failed.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
