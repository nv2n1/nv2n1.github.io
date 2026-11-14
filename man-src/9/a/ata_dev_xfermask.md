---
title: "ata_dev_xfermask(9)"
name: "ata_dev_xfermask"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_dev_xfermask/"
description: "ata_dev_xfermask – Compute supported xfermask of the given device"
---

<p>ata_dev_xfermask &#8211; Compute supported xfermask of the given device</p>
<h2>Synopsis</h2>
<pre><code>void ata_dev_xfermask(struct ata_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Device to compute xfermask for</dl>
<h2>Description</h2>
<p>Compute supported xfermask of <i>dev</i> and store it in dev-&gt;*_mask. This function is responsible for applying all known limits including host controller limits, device blacklist, etc&#8230; </p>
<p> LOCKING: None.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
