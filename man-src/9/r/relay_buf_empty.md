---
title: "relay_buf_empty(9)"
name: "relay_buf_empty"
section: "9"
letter: "r"
url: "/docs/linux/man/9-relay_buf_empty/"
---

relay_buf_empty - boolean, is the channel buffer empty?

<h2>Synopsis</h2>

<pre><code>int relay_buf_empty(struct rchan_buf *buf);</code></pre>

<h2>Arguments</h2>

<i>buf</i>
<dl><dd><dd>channel buffer</dl>

<h2>Description</h2>

Returns 1 if the buffer is empty, 0 otherwise.

<h2>Copyright</h2>


