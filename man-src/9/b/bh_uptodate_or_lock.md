---
title: "bh_uptodate_or_lock(9)"
name: "bh_uptodate_or_lock"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bh_uptodate_or_lock/"
---

bh_uptodate_or_lock - Test whether the buffer is uptodate

<h2>Synopsis</h2>

<pre><code>int bh_uptodate_or_lock(struct buffer_head *bh);</code></pre>

<h2>Arguments</h2>

<i>bh</i>
<dl><dd><dd>struct buffer_head</dl>

<h2>Description</h2>

Return true if the buffer is up-to-date and false, with the buffer locked, if not.

<h2>Copyright</h2>


