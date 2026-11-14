---
title: "scsi_remove_single_device(9)"
name: "scsi_remove_single_device"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_remove_single_device/"
description: "scsi_remove_single_device – Respond to user request to remove a device"
---

<p>scsi_remove_single_device &#8211; Respond to user request to remove a device</p>
<h2>Synopsis</h2>
<pre><code>int scsi_remove_single_device(uint host, uint channel, uint id, uint lun);</code></pre>
<h2>Arguments</h2>
<p><i>host</i></p>
<dl>
<dd>
<dd>user-supplied decimal integer</dl>
<p> <i>channel</i></p>
<dl>
<dd>user-supplied decimal integer</dl>
<p> <i>id</i></p>
<dl>
<dd>user-supplied decimal integer</dl>
<p> <i>lun</i></p>
<dl>
<dd>user-supplied decimal integer</dl>
<h2>Description</h2>
<p>called by writing &#8220;scsi remove-single-device&#8221; to /proc/scsi/scsi. Does a <code>scsi_device_lookup</code> and <code>scsi_remove_device</code></p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
