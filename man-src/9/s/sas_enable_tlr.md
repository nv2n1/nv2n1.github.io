---
title: "sas_enable_tlr(9)"
name: "sas_enable_tlr"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sas_enable_tlr/"
description: "sas_enable_tlr – setting TLR flags"
---

<p>sas_enable_tlr &#8211; setting TLR flags</p>
<h2>Synopsis</h2>
<pre><code>void sas_enable_tlr(struct scsi_device *sdev);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>scsi device struct</dl>
<h2>Description</h2>
<p>Seting tlr_enabled flag 1.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
