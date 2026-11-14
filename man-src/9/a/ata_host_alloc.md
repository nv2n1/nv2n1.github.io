---
title: "ata_host_alloc(9)"
name: "ata_host_alloc"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_host_alloc/"
description: "ata_host_alloc – allocate and init basic ATA host resources"
---

<p>ata_host_alloc &#8211; allocate and init basic ATA host resources</p>
<h2>Synopsis</h2>
<pre><code>struct ata_host *ata_host_alloc(struct device *dev, int max_ports);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>generic device this host is associated with</dl>
<p> <i>max_ports</i></p>
<dl>
<dd>maximum number of ATA ports associated with this host</dl>
<h2>Description</h2>
<p>Allocate and initialize basic ATA host resources. LLD calls this function to allocate a host, initializes it fully and attaches it using <code>ata_host_register</code>. </p>
<p> <i>max_ports</i> ports are allocated and host-&gt;n_ports is initialized to <i>max_ports</i>. The caller is allowed to decrease host-&gt;n_ports before calling <code>ata_host_register</code>. The unused ports will be automatically freed on registration.</p>
<h2>Return</h2>
<p>Allocate ATA host on success, NULL on failure. </p>
<p> LOCKING: Inherited from calling layer (may sleep).</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
