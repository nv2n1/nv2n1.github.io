---
title: "sata_down_spd_limit(9)"
name: "sata_down_spd_limit"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sata_down_spd_limit/"
description: "sata_down_spd_limit – adjust SATA spd limit downward"
---

<p>sata_down_spd_limit &#8211; adjust SATA spd limit downward</p>
<h2>Synopsis</h2>
<pre><code>int sata_down_spd_limit(struct ata_link *link, u32 spd_limit);</code></pre>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>Link to adjust SATA spd limit for</dl>
<p> <i>spd_limit</i></p>
<dl>
<dd>Additional limit</dl>
<h2>Description</h2>
<p>Adjust SATA spd limit of <i>link</i> downward. Note that this function only adjusts the limit. The change must be applied using <code>sata_set_spd</code>. </p>
<p> If <i>spd_limit</i> is non-zero, the speed is limited to equal to or lower than <i>spd_limit</i> if such speed is supported. If <i>spd_limit</i> is slower than any supported speed, only the lowest supported speed is allowed. </p>
<p> LOCKING: Inherited from caller.</p>
<h2>Return</h2>
<p>0 on success, negative errno on failure</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
