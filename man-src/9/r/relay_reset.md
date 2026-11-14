---
title: "relay_reset(9)"
name: "relay_reset"
section: "9"
letter: "r"
url: "/docs/linux/man/9-relay_reset/"
---

relay_reset - reset the channel

<h2>Synopsis</h2>

<pre><code>void relay_reset(struct rchan *chan);</code></pre>

<h2>Arguments</h2>

<i>chan</i>
<dl><dd><dd>the channel</dl>

<h2>Description</h2>

This has the effect of erasing all data from all channel buffers and restarting the channel in its initial state. The buffers are not freed, so any mappings are still in effect. 

 NOTE. Care should be taken that the channel isn't actually being used by anything when this call is made.

<h2>Copyright</h2>


