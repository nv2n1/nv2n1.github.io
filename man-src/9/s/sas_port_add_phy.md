---
title: "sas_port_add_phy(9)"
name: "sas_port_add_phy"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sas_port_add_phy/"
description: "sas_port_add_phy – add another phy to a port to form a wide port"
---

<p>sas_port_add_phy &#8211; add another phy to a port to form a wide port</p>
<h2>Synopsis</h2>
<pre><code>void sas_port_add_phy(struct sas_port *port, struct sas_phy *phy);</code></pre>
<h2>Arguments</h2>
<p><i>port</i></p>
<dl>
<dd>
<dd>port to add the phy to</dl>
<p> <i>phy</i></p>
<dl>
<dd>phy to add</dl>
<h2>Description</h2>
<p>When a port is initially created, it is empty (has no phys). All ports must have at least one phy to operated, and all wide ports must have at least two. The current code makes no difference between ports and wide ports, but the only object that can be connected to a remote device is a port, so ports must be formed on all devices with phys if they&#8217;re connected to anything.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
