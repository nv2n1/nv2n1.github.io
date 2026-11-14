---
title: "scsi_check_sense(9)"
name: "scsi_check_sense"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_check_sense/"
description: "scsi_check_sense – Examine scsi cmd sense"
---

<p>scsi_check_sense &#8211; Examine scsi cmd sense</p>
<h2>Synopsis</h2>
<pre><code>int scsi_check_sense(struct scsi_cmnd *scmd);</code></pre>
<h2>Arguments</h2>
<p><i>scmd</i></p>
<dl>
<dd>
<dd>Cmd to have sense checked.</dl>
<h2>Description</h2>
<p>Return value: SUCCESS or FAILED or NEEDS_RETRY or ADD_TO_MLQUEUE</p>
<h2>Notes</h2>
<p>When a deferred error is detected the current command has not been executed and needs retrying.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
