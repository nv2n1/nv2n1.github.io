---
title: "sas_phy_alloc(9)"
name: "sas_phy_alloc"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sas_phy_alloc/"
description: "sas_phy_alloc – allocates and initialize a SAS PHY structure"
---

<p>sas_phy_alloc &#8211; allocates and initialize a SAS PHY structure</p>
<h2>Synopsis</h2>
<pre><code>struct sas_phy *sas_phy_alloc(struct device *parent, int number);</code></pre>
<h2>Arguments</h2>
<p><i>parent</i></p>
<dl>
<dd>
<dd>Parent device</dl>
<p> <i>number</i></p>
<dl>
<dd>Phy index</dl>
<h2>Description</h2>
<p>Allocates an SAS PHY structure. It will be added in the device tree below the device specified by <i>parent</i>, which has to be either a Scsi_Host or sas_rphy.</p>
<h2>Return</h2>
<p>SAS PHY allocated or <code>NULL</code> if the allocation failed.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
