---
title: "scsi_device_put(9)"
name: "scsi_device_put"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_device_put/"
description: "scsi_device_put – release a reference to a scsi_device"
---

<p>scsi_device_put &#8211; release a reference to a scsi_device</p>
<h2>Synopsis</h2>
<pre><code>void scsi_device_put(struct scsi_device *sdev);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>device to release a reference on.</dl>
<h2>Description</h2>
<p>Release a reference to the scsi_device and decrements the use count of the underlying LLDD module. The device is freed once the last user vanishes.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
