---
title: "block_invalidatepage(9)"
name: "block_invalidatepage"
section: "9"
letter: "b"
url: "/docs/linux/man/9-block_invalidatepage/"
description: "block_invalidatepage – invalidate part or all of a buffer-backed page"
---

<p>block_invalidatepage &#8211; invalidate part or all of a buffer-backed page</p>
<h2>Synopsis</h2>
<pre><code>void block_invalidatepage(struct page *page, unsigned int offset, unsigned int length);</code></pre>
<h2>Arguments</h2>
<p><i>page</i></p>
<dl>
<dd>
<dd>the page which is affected</dl>
<p> <i>offset</i></p>
<dl>
<dd>start of the range to invalidate</dl>
<p> <i>length</i></p>
<dl>
<dd>length of the range to invalidate</dl>
<h2>Description</h2>
<p><code>block_invalidatepage</code> is called when all or part of the page has become invalidated by a truncate operation. </p>
<p> <code>block_invalidatepage</code> does not have to release all buffers, but it must ensure that no dirty buffer is left outside <i>offset</i> and that no I/O is underway against any of the blocks which are outside the truncation point. Because the caller is about to free (and possibly reuse) those blocks on-disk.</p>
<h2>Copyright</h2>
