---
title: "sata_set_spd_needed(9)"
name: "sata_set_spd_needed"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sata_set_spd_needed/"
description: "sata_set_spd_needed – is SATA spd configuration needed"
---

<p>sata_set_spd_needed &#8211; is SATA spd configuration needed</p>
<h2>Synopsis</h2>
<pre><code>int sata_set_spd_needed(struct ata_link *link);</code></pre>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>Link in question</dl>
<h2>Description</h2>
<p>Test whether the spd limit in SControl matches <i>link</i>-&gt;sata_spd_limit. This function is used to determine whether hardreset is necessary to apply SATA spd configuration. </p>
<p> LOCKING: Inherited from caller.</p>
<h2>Return</h2>
<p>1 if SATA spd configuration is needed, 0 otherwise.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
