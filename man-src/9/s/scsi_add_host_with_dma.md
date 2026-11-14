---
title: "scsi_add_host_with_dma(9)"
name: "scsi_add_host_with_dma"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_add_host_with_dma/"
description: "scsi_add_host_with_dma – add a scsi host with dma device"
---

<p>scsi_add_host_with_dma &#8211; add a scsi host with dma device</p>
<h2>Synopsis</h2>
<pre><code>int scsi_add_host_with_dma(struct Scsi_Host *shost, struct device *dev, struct device *dma_dev);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>scsi host pointer to add</dl>
<p> <i>dev</i></p>
<dl>
<dd>a struct device of type scsi class</dl>
<p> <i>dma_dev</i></p>
<dl>
<dd>dma device for the host</dl>
<h2>Note</h2>
<p>You rarely need to worry about this unless you&#8217;re in a virtualised host environments, so use the simpler <code>scsi_add_host</code> function instead. </p>
<p> Return value: 0 on success / != 0 for error</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
