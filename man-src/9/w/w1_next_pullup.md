---
title: "w1_next_pullup(9)"
name: "w1_next_pullup"
section: "9"
letter: "w"
url: "/docs/linux/man/9-w1_next_pullup/"
description: "w1_next_pullup – register for a strong pullup"
---

<p>w1_next_pullup &#8211; register for a strong pullup</p>
<h2>Synopsis</h2>
<pre><code>void w1_next_pullup(struct w1_master *dev, int delay);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the master device</dl>
<p> <i>delay</i></p>
<dl>
<dd>time in milliseconds</dl>
<h2>Description</h2>
<p>Put out a strong pull-up of the specified duration after the next write operation. Not all hardware supports strong pullups. Hardware that doesn&#8217;t support strong pullups will sleep for the given time after the write operation without a strong pullup. This is a one shot request for the next write, specifying zero will clear a previous request. The w1 master lock must be held.</p>
<h2>Return</h2>
<p>0=success, anything else=error</p>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
