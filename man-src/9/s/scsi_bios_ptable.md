---
title: "scsi_bios_ptable(9)"
name: "scsi_bios_ptable"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_bios_ptable/"
description: "scsi_bios_ptable – Read PC partition table out of first sector of device."
---

<p>scsi_bios_ptable &#8211; Read PC partition table out of first sector of device.</p>
<h2>Synopsis</h2>
<pre><code>unsigned char *scsi_bios_ptable(struct block_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>from this device</dl>
<h2>Description</h2>
<p>Reads the first sector from the device and returns <code>0x42</code> bytes starting at offset <code>0x1be</code>.</p>
<h2>Return</h2>
<p>partition table in kmalloc(GFP_KERNEL) memory, or NULL on error.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
