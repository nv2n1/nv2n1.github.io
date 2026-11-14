---
title: "ata_msense_rw_recovery(9)"
name: "ata_msense_rw_recovery"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_msense_rw_recovery/"
description: "ata_msense_rw_recovery – Simulate MODE SENSE r/w error recovery page"
---

<p>ata_msense_rw_recovery &#8211; Simulate MODE SENSE r/w error recovery page</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_msense_rw_recovery(u8 *buf, bool changeable);</code></pre>
<h2>Arguments</h2>
<p><i>buf</i></p>
<dl>
<dd>
<dd>output buffer</dl>
<p> <i>changeable</i></p>
<dl>
<dd>whether changeable parameters are requested</dl>
<h2>Description</h2>
<p>Generate a generic MODE SENSE r/w error recovery page. </p>
<p> LOCKING: None.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
