---
title: "atapi_xlat(9)"
name: "atapi_xlat"
section: "9"
letter: "a"
url: "/docs/linux/man/9-atapi_xlat/"
description: "atapi_xlat – Initialize PACKET taskfile"
---

<p>atapi_xlat &#8211; Initialize PACKET taskfile</p>
<h2>Synopsis</h2>
<pre><code>unsigned int atapi_xlat(struct ata_queued_cmd *qc);</code></pre>
<h2>Arguments</h2>
<p><i>qc</i></p>
<dl>
<dd>
<dd>command structure to be initialized</dl>
<h2>Description</h2>
<p>LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Return</h2>
<p>Zero on success, non-zero on failure.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
