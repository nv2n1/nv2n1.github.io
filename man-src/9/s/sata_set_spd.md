---
title: "sata_set_spd(9)"
name: "sata_set_spd"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sata_set_spd/"
description: "sata_set_spd – set SATA spd according to spd limit"
---

<p>sata_set_spd &#8211; set SATA spd according to spd limit</p>
<h2>Synopsis</h2>
<pre><code>int sata_set_spd(struct ata_link *link);</code></pre>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>Link to set SATA spd for</dl>
<h2>Description</h2>
<p>Set SATA spd of <i>link</i> according to sata_spd_limit. </p>
<p> LOCKING: Inherited from caller.</p>
<h2>Return</h2>
<p>0 if spd doesn&#8217;t need to be changed, 1 if spd has been changed. Negative errno if SCR registers are inaccessible.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
