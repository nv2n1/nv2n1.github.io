---
title: "scsi_device_supports_vpd(9)"
name: "scsi_device_supports_vpd"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_device_supports_vpd/"
description: "scsi_device_supports_vpd – test if a device supports VPD pages"
---

<p>scsi_device_supports_vpd &#8211; test if a device supports VPD pages</p>
<h2>Synopsis</h2>
<pre><code>int scsi_device_supports_vpd(struct scsi_device *sdev);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>the struct scsi_device to test</dl>
<h2>Description</h2>
<p>If the &#8216;try_vpd_pages&#8217; flag is set it takes precedence. Otherwise we will assume VPD pages are supported if the SCSI level is at least SPC-3 and &#8216;skip_vpd_pages&#8217; is not set.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
