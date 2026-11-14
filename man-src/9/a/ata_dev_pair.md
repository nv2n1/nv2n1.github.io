---
title: "ata_dev_pair(9)"
name: "ata_dev_pair"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_dev_pair/"
description: "ata_dev_pair – return other device on cable"
---

<p>ata_dev_pair &#8211; return other device on cable</p>
<h2>Synopsis</h2>
<pre><code>struct ata_device *ata_dev_pair(struct ata_device *adev);</code></pre>
<h2>Arguments</h2>
<p><i>adev</i></p>
<dl>
<dd>
<dd>device</dl>
<h2>Description</h2>
<p>Obtain the other device on the same cable, or if none is present NULL is returned</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
