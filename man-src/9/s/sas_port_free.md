---
title: "sas_port_free(9)"
name: "sas_port_free"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sas_port_free/"
description: "sas_port_free – free a SAS PORT"
---

<p>sas_port_free &#8211; free a SAS PORT</p>
<h2>Synopsis</h2>
<pre><code>void sas_port_free(struct sas_port *port);</code></pre>
<h2>Arguments</h2>
<p><i>port</i></p>
<dl>
<dd>
<dd>SAS PORT to free</dl>
<h2>Description</h2>
<p>Frees the specified SAS PORT.</p>
<h2>Note</h2>
<p>This function must only be called on a PORT that has not successfully been added using <code>sas_port_add</code>.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
