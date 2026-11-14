---
title: "sas_end_device_alloc(9)"
name: "sas_end_device_alloc"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sas_end_device_alloc/"
description: "sas_end_device_alloc – allocate an rphy for an end device"
---

<p>sas_end_device_alloc &#8211; allocate an rphy for an end device</p>
<h2>Synopsis</h2>
<pre><code>struct sas_rphy *sas_end_device_alloc(struct sas_port *parent);</code></pre>
<h2>Arguments</h2>
<p><i>parent</i></p>
<dl>
<dd>
<dd>which port</dl>
<h2>Description</h2>
<p>Allocates an SAS remote PHY structure, connected to <i>parent</i>.</p>
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
