---
title: "scsi_internal_device_block(9)"
name: "scsi_internal_device_block"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_internal_device_block/"
description: "scsi_internal_device_block – internal function to put a device temporarily into the SDEV_BLOCK state"
---

<p>scsi_internal_device_block &#8211; internal function to put a device temporarily into the SDEV_BLOCK state</p>
<h2>Synopsis</h2>
<pre><code>int scsi_internal_device_block(struct scsi_device *sdev);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>device to block</dl>
<h2>Description</h2>
<p>Block request made by scsi lld&#8217;s to temporarily stop all scsi commands on the specified device. Called from interrupt or normal process context. </p>
<p> Returns zero if successful or error if not</p>
<h2>Notes</h2>
<p>This routine transitions the device to the SDEV_BLOCK state (which must be a legal transition). When the device is in this state, all commands are deferred until the scsi lld reenables the device with scsi_device_unblock or device_block_tmo fires.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
