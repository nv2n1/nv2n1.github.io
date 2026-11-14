---
title: "w1_read_block(9)"
name: "w1_read_block"
section: "9"
letter: "w"
url: "/docs/linux/man/9-w1_read_block/"
description: "w1_read_block – Reads a series of bytes."
---

<p>w1_read_block &#8211; Reads a series of bytes.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u8 w1_read_block(struct w1_master&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>, u8&nbsp;<wbr>*&nbsp;<wbr></code><i>buf</i><code>, int&nbsp;<wbr></code><i>len</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the master device</dl>
<p> <i>buf</i></p>
<dl>
<dd>pointer to the buffer to fill</dl>
<p> <i>len</i></p>
<dl>
<dd>the number of bytes to read</dl>
<h2>Return</h2>
<p>the number of bytes read</p>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
