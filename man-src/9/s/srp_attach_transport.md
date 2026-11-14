---
title: "srp_attach_transport(9)"
name: "srp_attach_transport"
section: "9"
letter: "s"
url: "/docs/linux/man/9-srp_attach_transport/"
description: "srp_attach_transport – instantiate SRP transport template"
---

<p>srp_attach_transport &#8211; instantiate SRP transport template</p>
<h2>Synopsis</h2>
<pre><code>struct scsi_transport_template *srp_attach_transport(struct srp_function_template *ft);</code></pre>
<h2>Arguments</h2>
<p><i>ft</i></p>
<dl>
<dd>
<dd>SRP transport class function template</dl>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
