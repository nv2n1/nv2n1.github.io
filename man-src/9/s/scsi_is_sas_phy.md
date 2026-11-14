---
title: "scsi_is_sas_phy(9)"
name: "scsi_is_sas_phy"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_is_sas_phy/"
description: "scsi_is_sas_phy – check if a struct device represents a SAS PHY"
---

<p>scsi_is_sas_phy &#8211; check if a struct device represents a SAS PHY</p>
<h2>Synopsis</h2>
<pre><code>int scsi_is_sas_phy(const struct device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device to check</dl>
<h2>Return</h2>
<p><code>1</code> if the device represents a SAS PHY, <code>0</code> else</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
