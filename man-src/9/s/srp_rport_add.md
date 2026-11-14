---
title: "srp_rport_add(9)"
name: "srp_rport_add"
section: "9"
letter: "s"
url: "/docs/linux/man/9-srp_rport_add/"
description: "srp_rport_add – add a SRP remote port to the device hierarchy"
---

<p>srp_rport_add &#8211; add a SRP remote port to the device hierarchy</p>
<h2>Synopsis</h2>
<pre><code>struct srp_rport *srp_rport_add(struct Scsi_Host *shost, struct srp_rport_identifiers *ids);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>scsi host the remote port is connected to.</dl>
<p> <i>ids</i></p>
<dl>
<dd>The port id for the remote port.</dl>
<h2>Description</h2>
<p>Publishes a port to the rest of the system.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
