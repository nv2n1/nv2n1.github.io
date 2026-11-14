---
title: "write_zsreg(9)"
name: "write_zsreg"
section: "9"
letter: "w"
url: "/docs/linux/man/9-write_zsreg/"
description: "write_zsreg – Write to a Z8530 channel register"
---

<p>write_zsreg &#8211; Write to a Z8530 channel register</p>
<h2>Synopsis</h2>
<pre><code>void write_zsreg(struct z8530_channel *c, u8 reg, u8 val);</code></pre>
<h2>Arguments</h2>
<p><i>c</i></p>
<dl>
<dd>
<dd>The Z8530 channel</dl>
<p> <i>reg</i></p>
<dl>
<dd>Register number</dl>
<p> <i>val</i></p>
<dl>
<dd>Value to write</dl>
<h2>Description</h2>
<p>Write a value to an indexed register. The caller must hold the lock to honour the irritating delay rules. We know about register 0 being fast to access. </p>
<p> Assumes c-&gt;lock is held.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
