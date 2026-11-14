---
title: "scsi_probe_and_add_lun(9)"
name: "scsi_probe_and_add_lun"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_probe_and_add_lun/"
description: "scsi_probe_and_add_lun – probe a LUN, if a LUN is found add it"
---

<p>scsi_probe_and_add_lun &#8211; probe a LUN, if a LUN is found add it</p>
<h2>Synopsis</h2>
<pre><code>int scsi_probe_and_add_lun(struct scsi_target *starget, u64 lun, int *bflagsp, struct scsi_device **sdevp, enum scsi_scan_mode rescan, void *hostdata);</code></pre>
<h2>Arguments</h2>
<p><i>starget</i></p>
<dl>
<dd>
<dd>pointer to target device structure</dl>
<p> <i>lun</i></p>
<dl>
<dd>LUN of target device</dl>
<p> <i>bflagsp</i></p>
<dl>
<dd>store bflags here if not NULL</dl>
<p> <i>sdevp</i></p>
<dl>
<dd>probe the LUN corresponding to this scsi_device</dl>
<p> <i>rescan</i></p>
<dl>
<dd>if not equal to SCSI_SCAN_INITIAL skip some code only needed on first scan</dl>
<p> <i>hostdata</i></p>
<dl>
<dd>passed to <code>scsi_alloc_sdev</code></dl>
<h2>Description</h2>
<p>Call scsi_probe_lun, if a LUN with an attached device is found, allocate and set it up by calling scsi_add_lun.</p>
<h2>Return</h2>
<p>SCSI_SCAN_NO_RESPONSE: could not allocate or setup a scsi_device SCSI_SCAN_TARGET_PRESENT: target responded, but no device is attached at the LUN SCSI_SCAN_LUN_PRESENT: a new scsi_device was allocated and initialized</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
