---
title: "ata_platform_remove_one(9)"
name: "ata_platform_remove_one"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_platform_remove_one/"
description: "ata_platform_remove_one – Platform layer callback for device removal"
---

<p>ata_platform_remove_one &#8211; Platform layer callback for device removal</p>
<h2>Synopsis</h2>
<pre><code>int ata_platform_remove_one(struct platform_device *pdev);</code></pre>
<h2>Arguments</h2>
<p><i>pdev</i></p>
<dl>
<dd>
<dd>Platform device that was removed</dl>
<h2>Description</h2>
<p>Platform layer indicates to libata via this hook that hot-unplug or module unload event has occurred. Detach all ports. Resource release is handled via devres. </p>
<p> LOCKING: Inherited from platform layer (may sleep).</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
