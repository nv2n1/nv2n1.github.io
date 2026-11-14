---
title: "sata_link_hardreset(9)"
name: "sata_link_hardreset"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sata_link_hardreset/"
description: "sata_link_hardreset – reset link via SATA phy reset"
---

<p>sata_link_hardreset &#8211; reset link via SATA phy reset</p>
<h2>Synopsis</h2>
<pre><code>int sata_link_hardreset(struct ata_link *link, const unsigned long *timing, unsigned long deadline, bool *online, int (*check_ready)(struct ata_link *));</code></pre>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>link to reset</dl>
<p> <i>timing</i></p>
<dl>
<dd>timing parameters { interval, duration, timeout } in msec</dl>
<p> <i>deadline</i></p>
<dl>
<dd>deadline jiffies for the operation</dl>
<p> <i>online</i></p>
<dl>
<dd>optional out parameter indicating link onlineness</dl>
<p> <i>check_ready</i></p>
<dl>
<dd>optional callback to check link readiness</dl>
<h2>Description</h2>
<p>SATA phy-reset <i>link</i> using DET bits of SControl register. After hardreset, link readiness is waited upon using <code>ata_wait_ready</code> if <i>check_ready</i> is specified. LLDs are allowed to not specify <i>check_ready</i> and wait itself after this function returns. Device classification is LLD&#8217;s responsibility. </p>
<p> *<i>online</i> is set to one iff reset succeeded and <i>link</i> is online after reset. </p>
<p> LOCKING: Kernel thread context (may sleep)</p>
<h2>Return</h2>
<p>0 on success, -errno otherwise.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
