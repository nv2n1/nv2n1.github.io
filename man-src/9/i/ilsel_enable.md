---
title: "ilsel_enable(9)"
name: "ilsel_enable"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ilsel_enable/"
description: "ilsel_enable – Enable an ILSEL set."
---

<p>ilsel_enable &#8211; Enable an ILSEL set.</p>
<h2>Synopsis</h2>
<pre><code>int ilsel_enable(ilsel_source_t set);</code></pre>
<h2>Arguments</h2>
<p><i>set</i></p>
<dl>
<dd>
<dd>ILSEL source (see ilsel_source_t enum in include/asm-sh/ilsel.h).</dl>
<h2>Description</h2>
<p>Enables a given non-aliased ILSEL source (&lt;= ILSEL_KEY) at the highest available interrupt level. Callers should take care to order callsites noting descending interrupt levels. Aliasing FPGA and external board IRQs need to use <code>ilsel_enable_fixed</code>. </p>
<p> The return value is an IRQ number that can later be taken down with <code>ilsel_disable</code>.</p>
<h2>Author</h2>
<p><code>Paul Mundt</code> &lt;lethal [at] linux-sh.org&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
