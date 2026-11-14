---
title: "scsi_add_lun(9)"
name: "scsi_add_lun"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_add_lun/"
description: "scsi_add_lun – allocate and fully initialze a scsi_device"
---

<p>scsi_add_lun &#8211; allocate and fully initialze a scsi_device</p>
<h2>Synopsis</h2>
<pre><code>int scsi_add_lun(struct scsi_device *sdev, unsigned char *inq_result, int *bflags, int async);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>holds information to be stored in the new scsi_device</dl>
<p> <i>inq_result</i></p>
<dl>
<dd>holds the result of a previous INQUIRY to the LUN</dl>
<p> <i>bflags</i></p>
<dl>
<dd>black/white list flag</dl>
<p> <i>async</i></p>
<dl>
<dd>1 if this device is being scanned asynchronously</dl>
<h2>Description</h2>
<p>Initialize the scsi_device <i>sdev</i>. Optionally set fields based on values in *<i>bflags</i>.</p>
<h2>Return</h2>
<p>SCSI_SCAN_NO_RESPONSE: could not allocate or setup a scsi_device SCSI_SCAN_LUN_PRESENT: a new scsi_device was allocated and initialized</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
