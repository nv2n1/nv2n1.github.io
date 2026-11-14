---
title: "scsi_device_lookup_by_target(9)"
name: "scsi_device_lookup_by_target"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_device_lookup_by_target/"
description: "scsi_device_lookup_by_target – find a device given the target"
---

<p>scsi_device_lookup_by_target &#8211; find a device given the target</p>
<h2>Synopsis</h2>
<pre><code>struct scsi_device *scsi_device_lookup_by_target(struct scsi_target *starget, u64 lun);</code></pre>
<h2>Arguments</h2>
<p><i>starget</i></p>
<dl>
<dd>
<dd>SCSI target pointer</dl>
<p> <i>lun</i></p>
<dl>
<dd>SCSI Logical Unit Number</dl>
<h2>Description</h2>
<p>Looks up the scsi_device with the specified <i>lun</i> for a given <i>starget</i>. The returned scsi_device has an additional reference that needs to be released with scsi_device_put once you&#8217;re done with it.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
