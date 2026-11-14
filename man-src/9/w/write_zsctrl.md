---
title: "write_zsctrl(9)"
name: "write_zsctrl"
section: "9"
letter: "w"
url: "/docs/linux/man/9-write_zsctrl/"
description: "write_zsctrl – Write to a Z8530 control register"
---

<p>write_zsctrl &#8211; Write to a Z8530 control register</p>
<h2>Synopsis</h2>
<pre><code>void write_zsctrl(struct z8530_channel *c, u8 val);</code></pre>
<h2>Arguments</h2>
<p><i>c</i></p>
<dl>
<dd>
<dd>The Z8530 channel</dl>
<p> <i>val</i></p>
<dl>
<dd>Value to write</dl>
<h2>Description</h2>
<p>Write directly to the control register on the Z8530</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
