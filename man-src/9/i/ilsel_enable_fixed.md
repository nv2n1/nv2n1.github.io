---
title: "ilsel_enable_fixed(9)"
name: "ilsel_enable_fixed"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ilsel_enable_fixed/"
description: "ilsel_enable_fixed – Enable an ILSEL set at a fixed interrupt level"
---

<p>ilsel_enable_fixed &#8211; Enable an ILSEL set at a fixed interrupt level</p>
<h2>Synopsis</h2>
<pre><code>int ilsel_enable_fixed(ilsel_source_t set, unsigned int level);</code></pre>
<h2>Arguments</h2>
<p><i>set</i></p>
<dl>
<dd>
<dd>ILSEL source (see ilsel_source_t enum in include/asm-sh/ilsel.h).</dl>
<p> <i>level</i></p>
<dl>
<dd>Interrupt level (1 &#8211; 15)</dl>
<h2>Description</h2>
<p>Enables a given ILSEL source at a fixed interrupt level. Necessary both for level reservation as well as for aliased sources that only exist on special ILSEL#s. </p>
<p> Returns an IRQ number (as <code>ilsel_enable</code>).</p>
<h2>Author</h2>
<p><code>Paul Mundt</code> &lt;lethal [at] linux-sh.org&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
