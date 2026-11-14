---
title: "trace_block_touch_buffer(9)"
name: "trace_block_touch_buffer"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_block_touch_buffer/"
description: "trace_block_touch_buffer – mark a buffer accessed"
---

<p>trace_block_touch_buffer &#8211; mark a buffer accessed</p>
<h2>Synopsis</h2>
<pre><code>void trace_block_touch_buffer(struct buffer_head *bh);</code></pre>
<h2>Arguments</h2>
<p><i>bh</i></p>
<dl>
<dd>
<dd>buffer_head being touched</dl>
<h2>Description</h2>
<p>Called from <code>touch_buffer</code>.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
