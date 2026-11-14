---
title: "fc_vport_create(9)"
name: "fc_vport_create"
section: "9"
letter: "f"
url: "/docs/linux/man/9-fc_vport_create/"
description: "fc_vport_create – Admin App or LLDD requests creation of a vport"
---

<p>fc_vport_create &#8211; Admin App or LLDD requests creation of a vport</p>
<h2>Synopsis</h2>
<pre><code>struct fc_vport *fc_vport_create(struct Scsi_Host *shost, int channel, struct fc_vport_identifiers *ids);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>scsi host the virtual port is connected to.</dl>
<p> <i>channel</i></p>
<dl>
<dd>channel on shost port connected to.</dl>
<p> <i>ids</i></p>
<dl>
<dd>The world wide names, FC4 port roles, etc for the virtual port.</dl>
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
