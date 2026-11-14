---
title: "write_zsdata(9)"
name: "write_zsdata"
section: "9"
letter: "w"
url: "/docs/linux/man/9-write_zsdata/"
description: "write_zsdata – Write to a Z8530 control register"
---

<p>write_zsdata &#8211; Write to a Z8530 control register</p>
<h2>Synopsis</h2>
<pre><code>void write_zsdata(struct z8530_channel *c, u8 val);</code></pre>
<h2>Arguments</h2>
<p><i>c</i></p>
<dl>
<dd>
<dd>The Z8530 channel</dl>
<p> <i>val</i></p>
<dl>
<dd>Value to write</dl>
<h2>Description</h2>
<p>Write directly to the data register on the Z8530</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
