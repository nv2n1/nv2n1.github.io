---
title: "relay_file_read_end_pos(9)"
name: "relay_file_read_end_pos"
section: "9"
letter: "r"
url: "/docs/linux/man/9-relay_file_read_end_pos/"
---

relay_file_read_end_pos - return the new read position

<h2>Synopsis</h2>

<pre><code>size_t relay_file_read_end_pos(struct rchan_buf *buf, size_t read_pos, size_t count);</code></pre>

<h2>Arguments</h2>

<i>buf</i>
<dl><dd></dd><dd>relay channel buffer</dd></dl>
 

 <i>read_pos</i>
<dl><dd>file read position</dd></dl>
 

 <i>count</i>
<dl><dd>number of bytes to be read</dd></dl>

<h2>Copyright</h2>


