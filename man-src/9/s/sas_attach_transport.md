---
title: "sas_attach_transport(9)"
name: "sas_attach_transport"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sas_attach_transport/"
description: "sas_attach_transport – instantiate SAS transport template"
---

<p>sas_attach_transport &#8211; instantiate SAS transport template</p>
<h2>Synopsis</h2>
<pre><code>struct scsi_transport_template *sas_attach_transport(struct sas_function_template *ft);</code></pre>
<h2>Arguments</h2>
<p><i>ft</i></p>
<dl>
<dd>
<dd>SAS transport class function template</dl>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
