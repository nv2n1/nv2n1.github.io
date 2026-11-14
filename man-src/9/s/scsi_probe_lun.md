---
title: "scsi_probe_lun(9)"
name: "scsi_probe_lun"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_probe_lun/"
description: "scsi_probe_lun – probe a single LUN using a SCSI INQUIRY"
---

<p>scsi_probe_lun &#8211; probe a single LUN using a SCSI INQUIRY</p>
<h2>Synopsis</h2>
<pre><code>int scsi_probe_lun(struct scsi_device *sdev, unsigned char *inq_result, int result_len, int *bflags);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>scsi_device to probe</dl>
<p> <i>inq_result</i></p>
<dl>
<dd>area to store the INQUIRY result</dl>
<p> <i>result_len</i></p>
<dl>
<dd>len of inq_result</dl>
<p> <i>bflags</i></p>
<dl>
<dd>store any bflags found here</dl>
<h2>Description</h2>
<p>Probe the lun associated with <i>req</i> using a standard SCSI INQUIRY; </p>
<p> If the INQUIRY is successful, zero is returned and the INQUIRY data is in <i>inq_result</i>; the scsi_level and INQUIRY length are copied to the scsi_device any flags value is stored in *<i>bflags</i>.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
