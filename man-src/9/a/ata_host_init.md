---
title: "ata_host_init(9)"
name: "ata_host_init"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_host_init/"
description: "ata_host_init – Initialize a host struct for sas (ipr, libsas)"
---

<p>ata_host_init &#8211; Initialize a host struct for sas (ipr, libsas)</p>
<h2>Synopsis</h2>
<pre><code>void ata_host_init(struct ata_host *host, struct device *dev, struct ata_port_operations *ops);</code></pre>
<h2>Arguments</h2>
<p><i>host</i></p>
<dl>
<dd>
<dd>host to initialize</dl>
<p> <i>dev</i></p>
<dl>
<dd>device host is attached to</dl>
<p> <i>ops</i></p>
<dl>
<dd>port_ops</dl>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
