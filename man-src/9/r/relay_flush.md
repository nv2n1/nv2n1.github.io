---
title: "relay_flush(9)"
name: "relay_flush"
section: "9"
letter: "r"
url: "/docs/linux/man/9-relay_flush/"
---

relay_flush - close the channel

<h2>Synopsis</h2>

<pre><code>void relay_flush(struct rchan *chan);</code></pre>

<h2>Arguments</h2>

<i>chan</i>
<dl><dd><dd>the channel</dl>

<h2>Description</h2>

Flushes all channel buffers, i.e. forces buffer switch.

<h2>Copyright</h2>


