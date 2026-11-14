---
title: "filemap_flush(9)"
name: "filemap_flush"
section: "9"
letter: "f"
url: "/docs/linux/man/9-filemap_flush/"
---

filemap_flush - mostly a non-blocking flush

<h2>Synopsis</h2>

<pre><code>int filemap_flush(struct address_space *mapping);</code></pre>

<h2>Arguments</h2>

<i>mapping</i>
<dl><dd><dd>target address_space</dl>

<h2>Description</h2>

This is a mostly non-blocking flush. Not suitable for data-integrity purposes - I/O may not be started against all dirty pages.

<h2>Copyright</h2>


