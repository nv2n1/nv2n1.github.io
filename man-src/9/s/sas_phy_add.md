---
title: "sas_phy_add(9)"
name: "sas_phy_add"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sas_phy_add/"
description: "sas_phy_add – add a SAS PHY to the device hierarchy"
---

<p>sas_phy_add &#8211; add a SAS PHY to the device hierarchy</p>
<h2>Synopsis</h2>
<pre><code>int sas_phy_add(struct sas_phy *phy);</code></pre>
<h2>Arguments</h2>
<p><i>phy</i></p>
<dl>
<dd>
<dd>The PHY to be added</dl>
<h2>Description</h2>
<p>Publishes a SAS PHY to the rest of the system.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
