---
title: "relay_file_read_start_pos(9)"
name: "relay_file_read_start_pos"
section: "9"
letter: "r"
url: "/docs/linux/man/9-relay_file_read_start_pos/"
---

relay_file_read_start_pos - find the first available byte to read

<h2>Synopsis</h2>

<pre><code>size_t relay_file_read_start_pos(size_t read_pos, struct rchan_buf *buf);</code></pre>

<h2>Arguments</h2>

<i>read_pos</i>
<dl><dd><dd>file read position</dl>
 

 <i>buf</i>
<dl><dd>relay channel buffer</dl>

<h2>Description</h2>

If the <i>read_pos</i> is in the middle of padding, return the position of the first actually available byte, otherwise return the original value.

<h2>Copyright</h2>


