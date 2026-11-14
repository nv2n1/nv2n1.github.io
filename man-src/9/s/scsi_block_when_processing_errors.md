---
title: "scsi_block_when_processing_errors(9)"
name: "scsi_block_when_processing_errors"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_block_when_processing_errors/"
description: "scsi_block_when_processing_errors – Prevent cmds from being queued."
---

<p>scsi_block_when_processing_errors &#8211; Prevent cmds from being queued.</p>
<h2>Synopsis</h2>
<pre><code>int scsi_block_when_processing_errors(struct scsi_device *sdev);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>Device on which we are performing recovery.</dl>
<h2>Description</h2>
<p>We block until the host is out of error recovery, and then check to see whether the host or the device is offline. </p>
<p> Return value: 0 when dev was taken offline by error recovery. 1 OK to proceed.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
