---
title: "get_bbt_block(9)"
name: "get_bbt_block"
section: "9"
letter: "g"
url: "/docs/linux/man/9-get_bbt_block/"
description: "get_bbt_block – Get the first valid eraseblock suitable to store a BBT"
---

<p>get_bbt_block &#8211; Get the first valid eraseblock suitable to store a BBT</p>
<h2>Synopsis</h2>
<pre><code>int get_bbt_block(struct nand_chip *this, struct nand_bbt_descr *td, struct nand_bbt_descr *md, int chip);</code></pre>
<h2>Arguments</h2>
<p><i>this</i></p>
<dl>
<dd>
<dd>the NAND device</dl>
<p> <i>td</i></p>
<dl>
<dd>the BBT description</dl>
<p> <i>md</i></p>
<dl>
<dd>the mirror BBT descriptor</dl>
<p> <i>chip</i></p>
<dl>
<dd>the CHIP selector</dl>
<h2>Description</h2>
<p>This functions returns a positive block number pointing a valid eraseblock suitable to store a BBT (i.e. in the range reserved for BBT), or -ENOSPC if all blocks are already used of marked bad. If td-&gt;pages[chip] was already pointing to a valid block we re-use it, otherwise we search for the next valid one.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
