---
title: "scsi_vpd_lun_id(9)"
name: "scsi_vpd_lun_id"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_vpd_lun_id/"
description: "scsi_vpd_lun_id – return a unique device identification"
---

<p>scsi_vpd_lun_id &#8211; return a unique device identification</p>
<h2>Synopsis</h2>
<pre><code>int scsi_vpd_lun_id(struct scsi_device *sdev, char *id, size_t id_len);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>SCSI device</dl>
<p> <i>id</i></p>
<dl>
<dd>buffer for the identification</dl>
<p> <i>id_len</i></p>
<dl>
<dd>length of the buffer</dl>
<h2>Description</h2>
<p>Copies a unique device identification into <i>id</i> based on the information in the VPD page 0x83 of the device. The string will be formatted as a SCSI name string. </p>
<p> Returns the length of the identification or error on failure. If the identifier is longer than the supplied buffer the actual identifier length is returned and the buffer is not zero-padded.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
