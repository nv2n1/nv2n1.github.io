---
title: "scsi_alloc_sdev(9)"
name: "scsi_alloc_sdev"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_alloc_sdev/"
description: "scsi_alloc_sdev – allocate and setup a scsi_Device"
---

<p>scsi_alloc_sdev &#8211; allocate and setup a scsi_Device</p>
<h2>Synopsis</h2>
<pre><code>struct scsi_device *scsi_alloc_sdev(struct scsi_target *starget, u64 lun, void *hostdata);</code></pre>
<h2>Arguments</h2>
<p><i>starget</i></p>
<dl>
<dd>
<dd>which target to allocate a scsi_device for</dl>
<p> <i>lun</i></p>
<dl>
<dd>which lun</dl>
<p> <i>hostdata</i></p>
<dl>
<dd>usually NULL and set by -&gt;slave_alloc instead</dl>
<h2>Description</h2>
<p>Allocate, initialize for io, and return a pointer to a scsi_Device. Stores the <i>shost</i>, <i>channel</i>, <i>id</i>, and <i>lun</i> in the scsi_Device, and adds scsi_Device to the appropriate list. </p>
<p> Return value: scsi_Device pointer, or NULL on failure.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
