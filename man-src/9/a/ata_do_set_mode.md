---
title: "ata_do_set_mode(9)"
name: "ata_do_set_mode"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_do_set_mode/"
description: "ata_do_set_mode – Program timings and issue SET FEATURES – XFER"
---

<p>ata_do_set_mode &#8211; Program timings and issue SET FEATURES &#8211; XFER</p>
<h2>Synopsis</h2>
<pre><code>int ata_do_set_mode(struct ata_link *link, struct ata_device **r_failed_dev);</code></pre>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>link on which timings will be programmed</dl>
<p> <i>r_failed_dev</i></p>
<dl>
<dd>out parameter for failed device</dl>
<h2>Description</h2>
<p>Standard implementation of the function used to tune and set ATA device disk transfer mode (PIO3, UDMA6, etc.). If <code>ata_dev_set_mode</code> fails, pointer to the failing device is returned in <i>r_failed_dev</i>. </p>
<p> LOCKING: PCI/etc. bus probe sem.</p>
<h2>Return</h2>
<p>0 on success, negative errno otherwise</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
