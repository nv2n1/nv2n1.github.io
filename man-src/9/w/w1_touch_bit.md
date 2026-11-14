---
title: "w1_touch_bit(9)"
name: "w1_touch_bit"
section: "9"
letter: "w"
url: "/docs/linux/man/9-w1_touch_bit/"
description: "w1_touch_bit – Generates a write-0 or write-1 cycle and samples the level."
---

<p>w1_touch_bit &#8211; Generates a write-0 or write-1 cycle and samples the level.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u8 w1_touch_bit(struct w1_master&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>, int&nbsp;<wbr></code><i>bit</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the master device</dl>
<p> <i>bit</i></p>
<dl>
<dd>0 &#8211; write a 0, 1 &#8211; write a 0 read the level</dl>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
