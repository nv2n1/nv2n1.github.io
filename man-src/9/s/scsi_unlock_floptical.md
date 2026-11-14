---
title: "scsi_unlock_floptical(9)"
name: "scsi_unlock_floptical"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_unlock_floptical/"
description: "scsi_unlock_floptical – unlock device via a special MODE SENSE command"
---

<p>scsi_unlock_floptical &#8211; unlock device via a special MODE SENSE command</p>
<h2>Synopsis</h2>
<pre><code>void scsi_unlock_floptical(struct scsi_device *sdev, unsigned char *result);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>scsi device to send command to</dl>
<p> <i>result</i></p>
<dl>
<dd>area to store the result of the MODE SENSE</dl>
<h2>Description</h2>
<p>Send a vendor specific MODE SENSE (not a MODE SELECT) command. Called for BLIST_KEY devices.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
