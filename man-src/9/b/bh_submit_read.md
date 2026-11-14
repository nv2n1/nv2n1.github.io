---
title: "bh_submit_read(9)"
name: "bh_submit_read"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bh_submit_read/"
---

bh_submit_read - Submit a locked buffer for reading

<h2>Synopsis</h2>

<pre><code>int bh_submit_read(struct buffer_head *bh);</code></pre>

<h2>Arguments</h2>

<i>bh</i>
<dl><dd><dd>struct buffer_head</dl>

<h2>Description</h2>

Returns zero on success and -EIO on error.

<h2>Copyright</h2>


