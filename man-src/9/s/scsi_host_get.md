---
title: "scsi_host_get(9)"
name: "scsi_host_get"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_host_get/"
description: "scsi_host_get – inc a Scsi_Host ref count"
---

<p>scsi_host_get &#8211; inc a Scsi_Host ref count</p>
<h2>Synopsis</h2>
<pre><code>struct Scsi_Host *scsi_host_get(struct Scsi_Host *shost);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>Pointer to Scsi_Host to inc.</dl>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
