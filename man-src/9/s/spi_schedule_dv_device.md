---
title: "spi_schedule_dv_device(9)"
name: "spi_schedule_dv_device"
section: "9"
letter: "s"
url: "/docs/linux/man/9-spi_schedule_dv_device/"
description: "spi_schedule_dv_device – schedule domain validation to occur on the device"
---

<p>spi_schedule_dv_device &#8211; schedule domain validation to occur on the device</p>
<h2>Synopsis</h2>
<pre><code>void spi_schedule_dv_device(struct scsi_device *sdev);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>The device to validate</dl>
<h2>Description</h2>
<p>Identical to <code>spi_dv_device</code> above, except that the DV will be scheduled to occur in a workqueue later. All memory allocations are atomic, so may be called from any context including those holding SCSI locks.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
