---
title: "scsi_host_alloc(9)"
name: "scsi_host_alloc"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_host_alloc/"
description: "scsi_host_alloc – register a scsi host adapter instance."
---

<p>scsi_host_alloc &#8211; register a scsi host adapter instance.</p>
<h2>Synopsis</h2>
<pre><code>struct Scsi_Host *scsi_host_alloc(struct scsi_host_template *sht, int privsize);</code></pre>
<h2>Arguments</h2>
<p><i>sht</i></p>
<dl>
<dd>
<dd>pointer to scsi host template</dl>
<p> <i>privsize</i></p>
<dl>
<dd>extra bytes to allocate for driver</dl>
<h2>Note</h2>
<p>Allocate a new Scsi_Host and perform basic initialization. The host is not published to the scsi midlayer until scsi_add_host is called. </p>
<p> Return value: Pointer to a new Scsi_Host</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
