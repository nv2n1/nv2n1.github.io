---
title: "ata_host_alloc_pinfo(9)"
name: "ata_host_alloc_pinfo"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_host_alloc_pinfo/"
description: "ata_host_alloc_pinfo – alloc host and init with port_info array"
---

<p>ata_host_alloc_pinfo &#8211; alloc host and init with port_info array</p>
<h2>Synopsis</h2>
<pre><code>struct ata_host *ata_host_alloc_pinfo(struct device *dev, const struct ata_port_info *const *ppi, int n_ports);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>generic device this host is associated with</dl>
<p> <i>ppi</i></p>
<dl>
<dd>array of ATA port_info to initialize host with</dl>
<p> <i>n_ports</i></p>
<dl>
<dd>number of ATA ports attached to this host</dl>
<h2>Description</h2>
<p>Allocate ATA host and initialize with info from <i>ppi</i>. If NULL terminated, <i>ppi</i> may contain fewer entries than <i>n_ports</i>. The last entry will be used for the remaining ports.</p>
<h2>Return</h2>
<p>Allocate ATA host on success, NULL on failure. </p>
<p> LOCKING: Inherited from calling layer (may sleep).</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
