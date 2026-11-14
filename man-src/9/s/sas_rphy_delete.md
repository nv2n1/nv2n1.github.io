---
title: "sas_rphy_delete(9)"
name: "sas_rphy_delete"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sas_rphy_delete/"
description: "sas_rphy_delete – remove and free SAS remote PHY"
---

<p>sas_rphy_delete &#8211; remove and free SAS remote PHY</p>
<h2>Synopsis</h2>
<pre><code>void sas_rphy_delete(struct sas_rphy *rphy);</code></pre>
<h2>Arguments</h2>
<p><i>rphy</i></p>
<dl>
<dd>
<dd>SAS remote PHY to remove and free</dl>
<h2>Description</h2>
<p>Removes the specified SAS remote PHY and frees it.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
