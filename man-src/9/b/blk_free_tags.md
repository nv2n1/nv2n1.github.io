---
title: "blk_free_tags(9)"
name: "blk_free_tags"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_free_tags/"
---

blk_free_tags - release a given set of tag maintenance info

<h2>Synopsis</h2>

<pre><code>void blk_free_tags(struct blk_queue_tag *bqt);</code></pre>

<h2>Arguments</h2>

<i>bqt</i>
<dl><dd><dd>the tag map to free</dl>

<h2>Description</h2>

Drop the reference count on <i>bqt</i> and frees it when the last reference is dropped.

<h2>Copyright</h2>


