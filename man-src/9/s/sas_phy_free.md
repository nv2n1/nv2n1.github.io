---
title: "sas_phy_free(9)"
name: "sas_phy_free"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sas_phy_free/"
description: "sas_phy_free – free a SAS PHY"
---

<p>sas_phy_free &#8211; free a SAS PHY</p>
<h2>Synopsis</h2>
<pre><code>void sas_phy_free(struct sas_phy *phy);</code></pre>
<h2>Arguments</h2>
<p><i>phy</i></p>
<dl>
<dd>
<dd>SAS PHY to free</dl>
<h2>Description</h2>
<p>Frees the specified SAS PHY.</p>
<h2>Note</h2>
<p>This function must only be called on a PHY that has not successfully been added using <code>sas_phy_add</code>.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
