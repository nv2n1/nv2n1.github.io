---
title: "sas_tlr_supported(9)"
name: "sas_tlr_supported"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sas_tlr_supported/"
description: "sas_tlr_supported – checking TLR bit in vpd 0x90"
---

<p>sas_tlr_supported &#8211; checking TLR bit in vpd 0x90</p>
<h2>Synopsis</h2>
<pre><code>unsigned int sas_tlr_supported(struct scsi_device *sdev);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>scsi device struct</dl>
<h2>Description</h2>
<p>Check Transport Layer Retries are supported or not. If vpd page 0x90 is present, TRL is supported.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
