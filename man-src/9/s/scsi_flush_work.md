---
title: "scsi_flush_work(9)"
name: "scsi_flush_work"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_flush_work/"
description: "scsi_flush_work – Flush a Scsi_Host’s workqueue."
---

<p>scsi_flush_work &#8211; Flush a Scsi_Host&#8217;s workqueue.</p>
<h2>Synopsis</h2>
<pre><code>void scsi_flush_work(struct Scsi_Host *shost);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>Pointer to Scsi_Host.</dl>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
