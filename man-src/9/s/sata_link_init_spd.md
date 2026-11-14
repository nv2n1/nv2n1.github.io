---
title: "sata_link_init_spd(9)"
name: "sata_link_init_spd"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sata_link_init_spd/"
description: "sata_link_init_spd – Initialize link->sata_spd_limit"
---

<p>sata_link_init_spd &#8211; Initialize link-&gt;sata_spd_limit</p>
<h2>Synopsis</h2>
<pre><code>int sata_link_init_spd(struct ata_link *link);</code></pre>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>Link to configure sata_spd_limit for</dl>
<h2>Description</h2>
<p>Initialize <i>link</i>-&gt;[hw_]sata_spd_limit to the currently configured value. </p>
<p> LOCKING: Kernel thread context (may sleep).</p>
<h2>Return</h2>
<p>0 on success, -errno on failure.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
