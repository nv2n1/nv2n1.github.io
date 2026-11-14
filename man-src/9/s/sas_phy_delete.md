---
title: "sas_phy_delete(9)"
name: "sas_phy_delete"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sas_phy_delete/"
description: "sas_phy_delete – remove SAS PHY"
---

<p>sas_phy_delete &#8211; remove SAS PHY</p>
<h2>Synopsis</h2>
<pre><code>void sas_phy_delete(struct sas_phy *phy);</code></pre>
<h2>Arguments</h2>
<p><i>phy</i></p>
<dl>
<dd>
<dd>SAS PHY to remove</dl>
<h2>Description</h2>
<p>Removes the specified SAS PHY. If the SAS PHY has an associated remote PHY it is removed before.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
