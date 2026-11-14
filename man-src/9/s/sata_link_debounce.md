---
title: "sata_link_debounce(9)"
name: "sata_link_debounce"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sata_link_debounce/"
description: "sata_link_debounce – debounce SATA phy status"
---

<p>sata_link_debounce &#8211; debounce SATA phy status</p>
<h2>Synopsis</h2>
<pre><code>int sata_link_debounce(struct ata_link *link, const unsigned long *params, unsigned long deadline);</code></pre>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>ATA link to debounce SATA phy status for</dl>
<p> <i>params</i></p>
<dl>
<dd>timing parameters { interval, duration, timeout } in msec</dl>
<p> <i>deadline</i></p>
<dl>
<dd>deadline jiffies for the operation</dl>
<h2>Description</h2>
<p>Make sure SStatus of <i>link</i> reaches stable state, determined by holding the same value where DET is not 1 for <i>duration</i> polled every <i>interval</i>, before <i>timeout</i>. Timeout constraints the beginning of the stable state. Because DET gets stuck at 1 on some controllers after hot unplugging, this functions waits until timeout then returns 0 if DET is stable at 1. </p>
<p> <i>timeout</i> is further limited by <i>deadline</i>. The sooner of the two is used. </p>
<p> LOCKING: Kernel thread context (may sleep)</p>
<h2>Return</h2>
<p>0 on success, -errno on failure.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
