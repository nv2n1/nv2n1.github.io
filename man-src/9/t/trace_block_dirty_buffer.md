---
title: "trace_block_dirty_buffer(9)"
name: "trace_block_dirty_buffer"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_block_dirty_buffer/"
description: "trace_block_dirty_buffer – mark a buffer dirty"
---

<p>trace_block_dirty_buffer &#8211; mark a buffer dirty</p>
<h2>Synopsis</h2>
<pre><code>void trace_block_dirty_buffer(struct buffer_head *bh);</code></pre>
<h2>Arguments</h2>
<p><i>bh</i></p>
<dl>
<dd>
<dd>buffer_head being dirtied</dl>
<h2>Description</h2>
<p>Called from <code>mark_buffer_dirty</code>.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
