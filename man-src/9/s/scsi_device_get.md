---
title: "scsi_device_get(9)"
name: "scsi_device_get"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_device_get/"
description: "scsi_device_get – get an additional reference to a scsi_device"
---

<p>scsi_device_get &#8211; get an additional reference to a scsi_device</p>
<h2>Synopsis</h2>
<pre><code>int scsi_device_get(struct scsi_device *sdev);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>device to get a reference to</dl>
<h2>Description</h2>
<p>Gets a reference to the scsi_device and increments the use count of the underlying LLDD module. You must hold host_lock of the parent Scsi_Host or already have a reference when calling this. </p>
<p> This will fail if a device is deleted or cancelled, or when the LLD module is in the process of being unloaded.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
