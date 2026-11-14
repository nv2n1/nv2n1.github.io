---
title: "scsi_device_lookup(9)"
name: "scsi_device_lookup"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_device_lookup/"
description: "scsi_device_lookup – find a device given the host"
---

<p>scsi_device_lookup &#8211; find a device given the host</p>
<h2>Synopsis</h2>
<pre><code>struct scsi_device *scsi_device_lookup(struct Scsi_Host *shost, uint channel, uint id, u64 lun);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>SCSI host pointer</dl>
<p> <i>channel</i></p>
<dl>
<dd>SCSI channel (zero if only one channel)</dl>
<p> <i>id</i></p>
<dl>
<dd>SCSI target number (physical unit number)</dl>
<p> <i>lun</i></p>
<dl>
<dd>SCSI Logical Unit Number</dl>
<h2>Description</h2>
<p>Looks up the scsi_device with the specified <i>channel</i>, <i>id</i>, <i>lun</i> for a given host. The returned scsi_device has an additional reference that needs to be released with scsi_device_put once you&#8217;re done with it.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
