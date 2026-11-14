---
title: "scsi_schedule_eh(9)"
name: "scsi_schedule_eh"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_schedule_eh/"
description: "scsi_schedule_eh – schedule EH for SCSI host"
---

<p>scsi_schedule_eh &#8211; schedule EH for SCSI host</p>
<h2>Synopsis</h2>
<pre><code>void scsi_schedule_eh(struct Scsi_Host *shost);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>SCSI host to invoke error handling on.</dl>
<h2>Description</h2>
<p>Schedule SCSI EH without scmd.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
