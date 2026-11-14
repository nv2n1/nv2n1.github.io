---
title: "ata_dev_phys_link(9)"
name: "ata_dev_phys_link"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_dev_phys_link/"
description: "ata_dev_phys_link – find physical link for a device"
---

<p>ata_dev_phys_link &#8211; find physical link for a device</p>
<h2>Synopsis</h2>
<pre><code>struct ata_link *ata_dev_phys_link(struct ata_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>ATA device to look up physical link for</dl>
<h2>Description</h2>
<p>Look up physical link which <i>dev</i> is attached to. Note that this is different from <i>dev</i>-&gt;link only when <i>dev</i> is on slave link. For all other cases, it&#8217;s the same as <i>dev</i>-&gt;link. </p>
<p> LOCKING: Don&#8217;t care.</p>
<h2>Return</h2>
<p>Pointer to the found physical link.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
