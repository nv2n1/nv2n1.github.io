---
title: "scsi_dma_unmap(9)"
name: "scsi_dma_unmap"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_dma_unmap/"
description: "scsi_dma_unmap – unmap command’s sg lists mapped by scsi_dma_map"
---

<p>scsi_dma_unmap &#8211; unmap command&#8217;s sg lists mapped by scsi_dma_map</p>
<h2>Synopsis</h2>
<pre><code>void scsi_dma_unmap(struct scsi_cmnd *cmd);</code></pre>
<h2>Arguments</h2>
<p><i>cmd</i></p>
<dl>
<dd>
<dd>scsi command</dl>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
