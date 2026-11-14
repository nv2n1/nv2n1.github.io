---
title: "relay_close_buf(9)"
name: "relay_close_buf"
section: "9"
letter: "r"
url: "/docs/linux/man/9-relay_close_buf/"
---

relay_close_buf - close a channel buffer

<h2>Synopsis</h2>

<pre><code>void relay_close_buf(struct rchan_buf *buf);</code></pre>

<h2>Arguments</h2>

<i>buf</i>
<dl><dd><dd>channel buffer</dl>

<h2>Description</h2>

Marks the buffer finalized and restores the default callbacks. The channel buffer and channel buffer data structure are then freed automatically when the last reference is given up.

<h2>Copyright</h2>


