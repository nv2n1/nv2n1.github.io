---
title: "sas_port_delete(9)"
name: "sas_port_delete"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sas_port_delete/"
description: "sas_port_delete – remove SAS PORT"
---

<p>sas_port_delete &#8211; remove SAS PORT</p>
<h2>Synopsis</h2>
<pre><code>void sas_port_delete(struct sas_port *port);</code></pre>
<h2>Arguments</h2>
<p><i>port</i></p>
<dl>
<dd>
<dd>SAS PORT to remove</dl>
<h2>Description</h2>
<p>Removes the specified SAS PORT. If the SAS PORT has an associated phys, unlink them from the port as well.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
