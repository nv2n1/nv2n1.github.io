---
title: "mark_bbt_block_bad(9)"
name: "mark_bbt_block_bad"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mark_bbt_block_bad/"
description: "mark_bbt_block_bad – Mark one of the block reserved for BBT bad"
---

<p>mark_bbt_block_bad &#8211; Mark one of the block reserved for BBT bad</p>
<h2>Synopsis</h2>
<pre><code>void mark_bbt_block_bad(struct nand_chip *this, struct nand_bbt_descr *td, int chip, int block);</code></pre>
<h2>Arguments</h2>
<p><i>this</i></p>
<dl>
<dd>
<dd>the NAND device</dl>
<p> <i>td</i></p>
<dl>
<dd>the BBT description</dl>
<p> <i>chip</i></p>
<dl>
<dd>the CHIP selector</dl>
<p> <i>block</i></p>
<dl>
<dd>the BBT block to mark</dl>
<h2>Description</h2>
<p>Blocks reserved for BBT can become bad. This functions is an helper to mark such blocks as bad. It takes care of updating the in-memory BBT, marking the block as bad using a bad block marker and invalidating the associated td-&gt;pages[] entry.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
