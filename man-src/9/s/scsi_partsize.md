---
title: "scsi_partsize(9)"
name: "scsi_partsize"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_partsize/"
description: "scsi_partsize – Parse cylinders/heads/sectors from PC partition table"
---

<p>scsi_partsize &#8211; Parse cylinders/heads/sectors from PC partition table</p>
<h2>Synopsis</h2>
<pre><code>int scsi_partsize(unsigned char *buf, unsigned long capacity, unsigned int *cyls, unsigned int *hds, unsigned int *secs);</code></pre>
<h2>Arguments</h2>
<p><i>buf</i></p>
<dl>
<dd>
<dd>partition table, see <code>scsi_bios_ptable</code></dl>
<p> <i>capacity</i></p>
<dl>
<dd>size of the disk in sectors</dl>
<p> <i>cyls</i></p>
<dl>
<dd>put cylinders here</dl>
<p> <i>hds</i></p>
<dl>
<dd>put heads here</dl>
<p> <i>secs</i></p>
<dl>
<dd>put sectors here</dl>
<h2>Description</h2>
<p>determine the BIOS mapping/geometry used to create the partition table, storing the results in *cyls, *hds, and *secs</p>
<h2>Return</h2>
<p>-1 on failure, 0 on success.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
