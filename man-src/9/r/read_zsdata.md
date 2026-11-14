---
title: "read_zsdata(9)"
name: "read_zsdata"
section: "9"
letter: "r"
url: "/docs/linux/man/9-read_zsdata/"
description: "read_zsdata – Read the data port of a Z8530 channel"
---

<p>read_zsdata &#8211; Read the data port of a Z8530 channel</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u8 read_zsdata(struct z8530_channel&nbsp;<wbr>*&nbsp;<wbr></code><i>c</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>c</i></p>
<dl>
<dd>
<dd>The Z8530 channel to read the data port from</dl>
<h2>Description</h2>
<p>The data port provides fast access to some things. We still have all the 5uS delays to worry about.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
