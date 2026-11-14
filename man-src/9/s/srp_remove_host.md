---
title: "srp_remove_host(9)"
name: "srp_remove_host"
section: "9"
letter: "s"
url: "/docs/linux/man/9-srp_remove_host/"
description: "srp_remove_host – tear down a Scsi_Host’s SRP data structures"
---

<p>srp_remove_host &#8211; tear down a Scsi_Host&#8217;s SRP data structures</p>
<h2>Synopsis</h2>
<pre><code>void srp_remove_host(struct Scsi_Host *shost);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>Scsi Host that is torn down</dl>
<h2>Description</h2>
<p>Removes all SRP remote ports for a given Scsi_Host. Must be called just before scsi_remove_host for SRP HBAs.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
