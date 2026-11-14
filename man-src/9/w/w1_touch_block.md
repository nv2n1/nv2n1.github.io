---
title: "w1_touch_block(9)"
name: "w1_touch_block"
section: "9"
letter: "w"
url: "/docs/linux/man/9-w1_touch_block/"
description: "w1_touch_block – Touches a series of bytes."
---

<p>w1_touch_block &#8211; Touches a series of bytes.</p>
<h2>Synopsis</h2>
<pre><code>void w1_touch_block(struct w1_master *dev, u8 *buf, int len);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the master device</dl>
<p> <i>buf</i></p>
<dl>
<dd>pointer to the data to write</dl>
<p> <i>len</i></p>
<dl>
<dd>the number of bytes to write</dl>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
