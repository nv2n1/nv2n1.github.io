---
title: "ata_msleep(9)"
name: "ata_msleep"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_msleep/"
description: "ata_msleep – ATA EH owner aware msleep"
---

<p>ata_msleep &#8211; ATA EH owner aware msleep</p>
<h2>Synopsis</h2>
<pre><code>void ata_msleep(struct ata_port *ap, unsigned int msecs);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>ATA port to attribute the sleep to</dl>
<p> <i>msecs</i></p>
<dl>
<dd>duration to sleep in milliseconds</dl>
<h2>Description</h2>
<p>Sleeps <i>msecs</i>. If the current task is owner of <i>ap</i>&#8216;s EH, the ownership is released before going to sleep and reacquired after the sleep is complete. IOW, other ports sharing the <i>ap</i>-&gt;host will be allowed to own the EH while this task is sleeping. </p>
<p> LOCKING: Might sleep.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
