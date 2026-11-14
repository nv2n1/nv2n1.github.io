---
title: "scsi_sequential_lun_scan(9)"
name: "scsi_sequential_lun_scan"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_sequential_lun_scan/"
description: "scsi_sequential_lun_scan – sequentially scan a SCSI target"
---

<p>scsi_sequential_lun_scan &#8211; sequentially scan a SCSI target</p>
<h2>Synopsis</h2>
<pre><code>void scsi_sequential_lun_scan(struct scsi_target *starget, int bflags, int scsi_level, enum scsi_scan_mode rescan);</code></pre>
<h2>Arguments</h2>
<p><i>starget</i></p>
<dl>
<dd>
<dd>pointer to target structure to scan</dl>
<p> <i>bflags</i></p>
<dl>
<dd>black/white list flag for LUN 0</dl>
<p> <i>scsi_level</i></p>
<dl>
<dd>Which version of the standard does this device adhere to</dl>
<p> <i>rescan</i></p>
<dl>
<dd>passed to <code>scsi_probe_add_lun</code></dl>
<h2>Description</h2>
<p>Generally, scan from LUN 1 (LUN 0 is assumed to already have been scanned) to some maximum lun until a LUN is found with no device attached. Use the bflags to figure out any oddities. </p>
<p> Modifies sdevscan-&gt;lun.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
