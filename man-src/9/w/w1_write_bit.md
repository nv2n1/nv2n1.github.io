---
title: "w1_write_bit(9)"
name: "w1_write_bit"
section: "9"
letter: "w"
url: "/docs/linux/man/9-w1_write_bit/"
description: "w1_write_bit – Generates a write-0 or write-1 cycle."
---

<p>w1_write_bit &#8211; Generates a write-0 or write-1 cycle.</p>
<h2>Synopsis</h2>
<pre><code>void w1_write_bit(struct w1_master *dev, int bit);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the master device</dl>
<p> <i>bit</i></p>
<dl>
<dd>bit to write</dl>
<h2>Description</h2>
<p>Only call if dev-&gt;bus_master-&gt;touch_bit is NULL</p>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
