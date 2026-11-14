---
title: "ata_is_40wire(9)"
name: "ata_is_40wire"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_is_40wire/"
description: "ata_is_40wire – check drive side detection"
---

<p>ata_is_40wire &#8211; check drive side detection</p>
<h2>Synopsis</h2>
<pre><code>int ata_is_40wire(struct ata_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device</dl>
<h2>Description</h2>
<p>Perform drive side detection decoding, allowing for device vendors who can&#8217;t follow the documentation.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
