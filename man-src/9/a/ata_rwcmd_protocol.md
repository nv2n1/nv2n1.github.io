---
title: "ata_rwcmd_protocol(9)"
name: "ata_rwcmd_protocol"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_rwcmd_protocol/"
description: "ata_rwcmd_protocol – set taskfile r/w commands and protocol"
---

<p>ata_rwcmd_protocol &#8211; set taskfile r/w commands and protocol</p>
<h2>Synopsis</h2>
<pre><code>int ata_rwcmd_protocol(struct ata_taskfile *tf, struct ata_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>tf</i></p>
<dl>
<dd>
<dd>command to examine and configure</dl>
<p> <i>dev</i></p>
<dl>
<dd>device tf belongs to</dl>
<h2>Description</h2>
<p>Examine the device configuration and tf-&gt;flags to calculate the proper read/write commands and protocol to use. </p>
<p> LOCKING: caller.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
