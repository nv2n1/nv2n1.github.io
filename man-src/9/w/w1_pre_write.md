---
title: "w1_pre_write(9)"
name: "w1_pre_write"
section: "9"
letter: "w"
url: "/docs/linux/man/9-w1_pre_write/"
description: "w1_pre_write – pre-write operations"
---

<p>w1_pre_write &#8211; pre-write operations</p>
<h2>Synopsis</h2>
<pre><code>void w1_pre_write(struct w1_master *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the master device</dl>
<h2>Description</h2>
<p>Pre-write operation, currently only supporting strong pullups. Program the hardware for a strong pullup, if one has been requested and the hardware supports it.</p>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
