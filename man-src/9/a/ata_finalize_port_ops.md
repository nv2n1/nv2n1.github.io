---
title: "ata_finalize_port_ops(9)"
name: "ata_finalize_port_ops"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_finalize_port_ops/"
description: "ata_finalize_port_ops – finalize ata_port_operations"
---

<p>ata_finalize_port_ops &#8211; finalize ata_port_operations</p>
<h2>Synopsis</h2>
<pre><code>void ata_finalize_port_ops(struct ata_port_operations *ops);</code></pre>
<h2>Arguments</h2>
<p><i>ops</i></p>
<dl>
<dd>
<dd>ata_port_operations to finalize</dl>
<h2>Description</h2>
<p>An ata_port_operations can inherit from another ops and that ops can again inherit from another. This can go on as many times as necessary as long as there is no loop in the inheritance chain. </p>
<p> Ops tables are finalized when the host is started. NULL or unspecified entries are inherited from the closet ancestor which has the method and the entry is populated with it. After finalization, the ops table directly points to all the methods and -&gt;inherits is no longer necessary and cleared. </p>
<p> Using ATA_OP_NULL, inheriting ops can force a method to NULL. </p>
<p> LOCKING: None.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
