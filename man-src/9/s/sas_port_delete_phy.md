---
title: "sas_port_delete_phy(9)"
name: "sas_port_delete_phy"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sas_port_delete_phy/"
description: "sas_port_delete_phy – remove a phy from a port or wide port"
---

<p>sas_port_delete_phy &#8211; remove a phy from a port or wide port</p>
<h2>Synopsis</h2>
<pre><code>void sas_port_delete_phy(struct sas_port *port, struct sas_phy *phy);</code></pre>
<h2>Arguments</h2>
<p><i>port</i></p>
<dl>
<dd>
<dd>port to remove the phy from</dl>
<p> <i>phy</i></p>
<dl>
<dd>phy to remove</dl>
<h2>Description</h2>
<p>This operation is used for tearing down ports again. It must be done to every port or wide port before calling sas_port_delete.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
