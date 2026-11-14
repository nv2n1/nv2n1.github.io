---
title: "w1_read_bit(9)"
name: "w1_read_bit"
section: "9"
letter: "w"
url: "/docs/linux/man/9-w1_read_bit/"
description: "w1_read_bit – Generates a write-1 cycle and samples the level."
---

<p>w1_read_bit &#8211; Generates a write-1 cycle and samples the level.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u8 w1_read_bit(struct w1_master&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the master device</dl>
<h2>Description</h2>
<p>Only call if dev-&gt;bus_master-&gt;touch_bit is NULL</p>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
