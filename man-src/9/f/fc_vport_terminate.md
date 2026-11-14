---
title: "fc_vport_terminate(9)"
name: "fc_vport_terminate"
section: "9"
letter: "f"
url: "/docs/linux/man/9-fc_vport_terminate/"
description: "fc_vport_terminate – Admin App or LLDD requests termination of a vport"
---

<p>fc_vport_terminate &#8211; Admin App or LLDD requests termination of a vport</p>
<h2>Synopsis</h2>
<pre><code>int fc_vport_terminate(struct fc_vport *vport);</code></pre>
<h2>Arguments</h2>
<p><i>vport</i></p>
<dl>
<dd>
<dd>fc_vport to be terminated</dl>
<h2>Description</h2>
<p>Calls the LLDD <code>vport_delete</code> function, then deallocates and removes the vport from the shost and object tree.</p>
<h2>Notes</h2>
<p>This routine assumes no locks are held on entry.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
