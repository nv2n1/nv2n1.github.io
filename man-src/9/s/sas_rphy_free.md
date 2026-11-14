---
title: "sas_rphy_free(9)"
name: "sas_rphy_free"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sas_rphy_free/"
description: "sas_rphy_free – free a SAS remote PHY"
---

<p>sas_rphy_free &#8211; free a SAS remote PHY</p>
<h2>Synopsis</h2>
<pre><code>void sas_rphy_free(struct sas_rphy *rphy);</code></pre>
<h2>Arguments</h2>
<p><i>rphy</i></p>
<dl>
<dd>
<dd>SAS remote PHY to free</dl>
<h2>Description</h2>
<p>Frees the specified SAS remote PHY.</p>
<h2>Note</h2>
<p>This function must only be called on a remote PHY that has not successfully been added using <code>sas_rphy_add</code> (or has been <code>sas_rphy_remove</code>&#8216;d)</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
