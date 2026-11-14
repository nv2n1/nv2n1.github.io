---
title: "w1_reset_bus(9)"
name: "w1_reset_bus"
section: "9"
letter: "w"
url: "/docs/linux/man/9-w1_reset_bus/"
description: "w1_reset_bus – Issues a reset bus sequence."
---

<p>w1_reset_bus &#8211; Issues a reset bus sequence.</p>
<h2>Synopsis</h2>
<pre><code>int w1_reset_bus(struct w1_master *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the master device</dl>
<h2>Return</h2>
<p>0=Device present, 1=No device present or error</p>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
