---
title: "scsi_get_vpd_page(9)"
name: "scsi_get_vpd_page"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_get_vpd_page/"
description: "scsi_get_vpd_page – Get Vital Product Data from a SCSI device"
---

<p>scsi_get_vpd_page &#8211; Get Vital Product Data from a SCSI device</p>
<h2>Synopsis</h2>
<pre><code>int scsi_get_vpd_page(struct scsi_device *sdev, u8 page, unsigned char *buf, int buf_len);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
</dd><dd>The device to ask</dd></dl>
<p> <i>page</i></p>
<dl>
<dd>Which Vital Product Data to return</dd></dl>
<p> <i>buf</i></p>
<dl>
<dd>where to store the VPD</dd></dl>
<p> <i>buf_len</i></p>
<dl>
<dd>number of bytes in the VPD buffer area</dd></dl>
<h2>Description</h2>
<p>SCSI devices may optionally supply Vital Product Data. Each &#8216;page&#8217; of VPD is defined in the appropriate SCSI document (eg SPC, SBC). If the device supports this VPD page, this routine returns a pointer to a buffer containing the data from that page. The caller is responsible for calling <code>kfree</code> on this pointer when it is no longer needed. If we cannot retrieve the VPD page this routine returns <code>NULL</code>.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dd></dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Copyright</h2>
