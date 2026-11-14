---
title: "sas_port_add(9)"
name: "sas_port_add"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sas_port_add/"
description: "sas_port_add – add a SAS port to the device hierarchy"
---

<p>sas_port_add &#8211; add a SAS port to the device hierarchy</p>
<h2>Synopsis</h2>
<pre><code>int sas_port_add(struct sas_port *port);</code></pre>
<h2>Arguments</h2>
<p><i>port</i></p>
<dl>
<dd>
<dd>port to be added</dl>
<h2>Description</h2>
<p>publishes a port to the rest of the system</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
