---
title: "ata_wait_after_reset(9)"
name: "ata_wait_after_reset"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_wait_after_reset/"
description: "ata_wait_after_reset – wait for link to become ready after reset"
---

<p>ata_wait_after_reset &#8211; wait for link to become ready after reset</p>
<h2>Synopsis</h2>
<pre><code>int ata_wait_after_reset(struct ata_link *link, unsigned long deadline, int (*check_ready)(struct ata_link *link));</code></pre>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>link to be waited on</dl>
<p> <i>deadline</i></p>
<dl>
<dd>deadline jiffies for the operation</dl>
<p> <i>check_ready</i></p>
<dl>
<dd>callback to check link readiness</dl>
<h2>Description</h2>
<p>Wait for <i>link</i> to become ready after reset. </p>
<p> LOCKING: EH context.</p>
<h2>Return</h2>
<p>0 if <i>link</i> is ready before <i>deadline</i>; otherwise, -errno.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
