---
title: "seq_write(9)"
name: "seq_write"
section: "9"
letter: "s"
url: "/docs/linux/man/9-seq_write/"
---

seq_write - write arbitrary data to buffer

<h2>Synopsis</h2>

<pre><code>int seq_write(struct seq_file *seq, const void *data, size_t len);</code></pre>

<h2>Arguments</h2>

<i>seq</i>
<dl><dd><dd>seq_file identifying the buffer to which data should be written</dl>
 

 <i>data</i>
<dl><dd>data address</dl>
 

 <i>len</i>
<dl><dd>number of bytes</dl>

<h2>Description</h2>

Return 0 on success, non-zero otherwise.

<h2>Copyright</h2>


