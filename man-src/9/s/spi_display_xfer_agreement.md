---
title: "spi_display_xfer_agreement(9)"
name: "spi_display_xfer_agreement"
section: "9"
letter: "s"
url: "/docs/linux/man/9-spi_display_xfer_agreement/"
description: "spi_display_xfer_agreement – Print the current target transfer agreement"
---

<p>spi_display_xfer_agreement &#8211; Print the current target transfer agreement</p>
<h2>Synopsis</h2>
<pre><code>void spi_display_xfer_agreement(struct scsi_target *starget);</code></pre>
<h2>Arguments</h2>
<p><i>starget</i></p>
<dl>
<dd>
<dd>The target for which to display the agreement</dl>
<h2>Description</h2>
<p>Each SPI port is required to maintain a transfer agreement for each other port on the bus. This function prints a one-line summary of the current agreement; more detailed information is available in sysfs.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
