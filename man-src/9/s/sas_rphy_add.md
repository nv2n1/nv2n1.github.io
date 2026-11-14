---
title: "sas_rphy_add(9)"
name: "sas_rphy_add"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sas_rphy_add/"
description: "sas_rphy_add – add a SAS remote PHY to the device hierarchy"
---

<p>sas_rphy_add &#8211; add a SAS remote PHY to the device hierarchy</p>
<h2>Synopsis</h2>
<pre><code>int sas_rphy_add(struct sas_rphy *rphy);</code></pre>
<h2>Arguments</h2>
<p><i>rphy</i></p>
<dl>
<dd>
<dd>The remote PHY to be added</dl>
<h2>Description</h2>
<p>Publishes a SAS remote PHY to the rest of the system.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
