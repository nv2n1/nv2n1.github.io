---
title: "sata_link_scr_lpm(9)"
name: "sata_link_scr_lpm"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sata_link_scr_lpm/"
description: "sata_link_scr_lpm – manipulate SControl IPM and SPM fields"
---

<p>sata_link_scr_lpm &#8211; manipulate SControl IPM and SPM fields</p>
<h2>Synopsis</h2>
<pre><code>int sata_link_scr_lpm(struct ata_link *link, enum ata_lpm_policy policy, bool spm_wakeup);</code></pre>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>ATA link to manipulate SControl for</dl>
<p> <i>policy</i></p>
<dl>
<dd>LPM policy to configure</dl>
<p> <i>spm_wakeup</i></p>
<dl>
<dd>initiate LPM transition to active state</dl>
<h2>Description</h2>
<p>Manipulate the IPM field of the SControl register of <i>link</i> according to <i>policy</i>. If <i>policy</i> is ATA_LPM_MAX_POWER and <i>spm_wakeup</i> is <code>true</code>, the SPM field is manipulated to wake up the link. This function also clears PHYRDY_CHG before returning. </p>
<p> LOCKING: EH context.</p>
<h2>Return</h2>
<p>0 on success, -errno otherwise.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
