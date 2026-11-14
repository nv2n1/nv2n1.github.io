---
title: "maple_add_packet(9)"
name: "maple_add_packet"
section: "9"
letter: "m"
url: "/docs/linux/man/9-maple_add_packet/"
description: "maple_add_packet – add a single instruction to the maple bus queue"
---

<p>maple_add_packet &#8211; add a single instruction to the maple bus queue</p>
<h2>Synopsis</h2>
<pre><code>int maple_add_packet(struct maple_device *mdev, u32 function, u32 command, size_t length, void *data);</code></pre>
<h2>Arguments</h2>
<p><i>mdev</i></p>
<dl>
<dd>
<dd>maple device</dl>
<p> <i>function</i></p>
<dl>
<dd>function on device being queried</dl>
<p> <i>command</i></p>
<dl>
<dd>maple command to add</dl>
<p> <i>length</i></p>
<dl>
<dd>length of command string (in 32 bit words)</dl>
<p> <i>data</i></p>
<dl>
<dd>remainder of command string</dl>
<h2>Author</h2>
<p><code>Paul Mundt</code> &lt;lethal [at] linux-sh.org&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
