---
title: "ata_host_start(9)"
name: "ata_host_start"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_host_start/"
description: "ata_host_start – start and freeze ports of an ATA host"
---

<p>ata_host_start &#8211; start and freeze ports of an ATA host</p>
<h2>Synopsis</h2>
<pre><code>int ata_host_start(struct ata_host *host);</code></pre>
<h2>Arguments</h2>
<p><i>host</i></p>
<dl>
<dd>
<dd>ATA host to start ports for</dl>
<h2>Description</h2>
<p>Start and then freeze ports of <i>host</i>. Started status is recorded in host-&gt;flags, so this function can be called multiple times. Ports are guaranteed to get started only once. If host-&gt;ops isn&#8217;t initialized yet, its set to the first non-dummy port ops. </p>
<p> LOCKING: Inherited from calling layer (may sleep).</p>
<h2>Return</h2>
<p>0 if all ports are started successfully, -errno otherwise.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
