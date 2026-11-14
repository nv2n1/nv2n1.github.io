---
title: "ata_down_xfermask_limit(9)"
name: "ata_down_xfermask_limit"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_down_xfermask_limit/"
description: "ata_down_xfermask_limit – adjust dev xfer masks downward"
---

<p>ata_down_xfermask_limit &#8211; adjust dev xfer masks downward</p>
<h2>Synopsis</h2>
<pre><code>int ata_down_xfermask_limit(struct ata_device *dev, unsigned int sel);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Device to adjust xfer masks</dl>
<p> <i>sel</i></p>
<dl>
<dd>ATA_DNXFER_* selector</dl>
<h2>Description</h2>
<p>Adjust xfer masks of <i>dev</i> downward. Note that this function does not apply the change. Invoking <code>ata_set_mode</code> afterwards will apply the limit. </p>
<p> LOCKING: Inherited from caller.</p>
<h2>Return</h2>
<p>0 on success, negative errno on failure</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
