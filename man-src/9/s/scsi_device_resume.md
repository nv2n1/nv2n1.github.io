---
title: "scsi_device_resume(9)"
name: "scsi_device_resume"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_device_resume/"
description: "scsi_device_resume – Restart user issued commands to a quiesced device."
---

<p>scsi_device_resume &#8211; Restart user issued commands to a quiesced device.</p>
<h2>Synopsis</h2>
<pre><code>void scsi_device_resume(struct scsi_device *sdev);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>scsi device to resume.</dl>
<h2>Description</h2>
<p>Moves the device from quiesced back to running and restarts the queues. </p>
<p> Must be called with user context, may sleep.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
