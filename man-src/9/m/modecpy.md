---
title: "modecpy(9)"
name: "modecpy"
section: "9"
letter: "m"
url: "/docs/linux/man/9-modecpy/"
description: "modecpy – Prepare response for MODE SENSE"
---

<p>modecpy &#8211; Prepare response for MODE SENSE</p>
<h2>Synopsis</h2>
<pre><code>void modecpy(u8 *dest, const u8 *src, int n, bool changeable);</code></pre>
<h2>Arguments</h2>
<p><i>dest</i></p>
<dl>
<dd>
<dd>output buffer</dl>
<p> <i>src</i></p>
<dl>
<dd>data being copied</dl>
<p> <i>n</i></p>
<dl>
<dd>length of mode page</dl>
<p> <i>changeable</i></p>
<dl>
<dd>whether changeable parameters are requested</dl>
<h2>Description</h2>
<p>Generate a generic MODE SENSE page for either current or changeable parameters. </p>
<p> LOCKING: None.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
